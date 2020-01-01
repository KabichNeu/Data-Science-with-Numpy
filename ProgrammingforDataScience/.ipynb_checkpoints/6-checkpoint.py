{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = np.arange(25).reshape(5,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 0  1  2  3  4]\n",
      " [ 5  6  7  8  9]\n",
      " [10 11 12 13 14]\n",
      " [15 16 17 18 19]\n",
      " [20 21 22 23 24]]\n"
     ]
    }
   ],
   "source": [
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[11 12 13 14 15 16 17 18 19 20 21 22 23 24]\n"
     ]
    }
   ],
   "source": [
    "print(x[x>10])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5]\n",
      "[1 2 3 4]\n",
      "[1 2 3 4 5 6 7 8 9]\n"
     ]
    }
   ],
   "source": [
    "x = np.array([1,2,3,4,5])\n",
    "y = np.array([6,7,8,9,5])\n",
    "\n",
    "print(np.intersect1d(x,y))\n",
    "print(np.setdiff1d(x,y))\n",
    "print(np.union1d(x,y))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5]\n"
     ]
    }
   ],
   "source": [
    "print(np.sort(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5]\n"
     ]
    }
   ],
   "source": [
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5]\n"
     ]
    }
   ],
   "source": [
    "print(np.sort(np.unique(x)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 9  8  3  6  3]\n",
      " [ 5  3  8  8  7]\n",
      " [ 6  1 10  5  1]\n",
      " [ 7 10  1  2  4]\n",
      " [ 3  4  4  7  4]]\n"
     ]
    }
   ],
   "source": [
    "x = np.random.randint(1,11,size = (5,5))\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 3  1  1  2  1]\n",
      " [ 5  3  3  5  3]\n",
      " [ 6  4  4  6  4]\n",
      " [ 7  8  8  7  4]\n",
      " [ 9 10 10  8  7]]\n"
     ]
    }
   ],
   "source": [
    "print(np.sort(x,axis=0))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 3  3  6  8  9]\n",
      " [ 3  5  7  8  8]\n",
      " [ 1  1  5  6 10]\n",
      " [ 1  2  4  7 10]\n",
      " [ 3  4  4  4  7]]\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "print(print(np.sort(x,axis=1)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
