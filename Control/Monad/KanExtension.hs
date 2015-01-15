-----------------------------------------------------------------------------
-- |
-- Module      :  Control.Monad.KanExtension
-- Copyright   :  (C) 2008 Edward Kmett
-- License     :  BSD-style (see the file LICENSE)
--
-- Maintainer  :  Edward Kmett <ekmett@gmail.com>
-- Stability   :  experimental
-- Portability :  non-portable (rank-2 polymorphism)
--
-- Left and right Kan extensions, expressed as higher order functors
--
-- Included is the 'monad generated by a functor' @Ran f f@
----------------------------------------------------------------------------
module Control.Monad.KanExtension 
	( rep, abs
	, FreeLike(..) -- , improve
	) where

import Prelude hiding (abs)
import Control.Functor.Composition
import Control.Functor.Extras
import Control.Functor.Pointed ()
import Control.Functor.HigherOrder
import Control.Comonad
import Control.Monad.Cont

rep :: Monad m => m a -> Ran m m a
rep m = Ran (m >>=)

abs :: Monad m => Ran m m a -> m a 
abs a = runRan a return

class (Functor f, Monad m) => FreeLike f m where
	wrap :: f (m a) -> m a

instance FreeLike f m => FreeLike f (Ran m m) where
	wrap t = Ran (wrap . flip fmap t . flip runRan)

instance Functor f => FreeLike f (Free f) where
	wrap = inFree

improve :: Functor f => (forall a. FreeLike f m -> m a) -> Free f a
improve = abs

-- | Left Kan Extension
data Lan g h a = forall b. Lan (g b -> a) (h b)

toLan :: (Composition o, Functor f) => (h :~> (f `o` g)) -> Lan g h :~> f
toLan s (Lan f v) = fmap f . decompose $ s v

fromLan :: Composition o => (Lan g h :~> f) -> h :~> (f `o` g)
fromLan s = compose . s . Lan id

instance Functor g => HFunctor (Lan g) where
	ffmap f (Lan g h) = Lan (f . g) h
	hfmap f (Lan g h) = Lan g (f h)

instance Functor (Lan f g) where
	fmap f (Lan g h) = Lan (f . g) h

instance Copointed (Lan f f) where
	extract (Lan f a) = f a

instance Comonad (Lan f f) where
	duplicate (Lan f ws) = Lan (Lan f) ws

coabs :: Comonad w => w a -> Lan w w a
coabs = Lan extract 

corep :: Comonad w => Lan w w a -> w a 
corep (Lan f c) = extend f c

class (Functor f, Comonad w) => Cocheap f w where 
	unwrap :: w a -> f (w a)

-- instance Functor f => CofreeLike f (Cofree f) where
--	unwrap = outCofree 

instance Cocheap f w => Cocheap f (Lan w w) where
	unwrap (Lan f c) = fmap (Lan f) (unwrap c)

--  unwrap = snd

-- coimprove :: Functor f => Cofree f a -> (forall a. Cocheap f w => w a)
-- coimprove = coabs

-- * Limits and Colimits of Functors
-- type Lim = Ran VoidF 
-- type Colim = Lan VoidF
