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
    "x = np.array([1,2,3,4,5])"
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
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "x[3]=20"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 1  2  3 20  5]\n"
     ]
    }
   ],
   "source": [
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = np.arange(1,10).reshape(3,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3]\n",
      " [4 5 6]\n",
      " [7 8 9]]\n"
     ]
    }
   ],
   "source": [
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
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
    "x = np.array([1,2,3,4,5])\n",
    "print(x)\n",
    "x= np.delete(x,[0,4])"
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
      "[2 3 4]\n"
     ]
    }
   ],
   "source": [
    "print(x)"
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
      "[[1 2 3]\n",
      " [4 5 6]\n",
      " [7 8 9]]\n",
      "\n",
      " [[4 5 6]\n",
      " [7 8 9]]\n",
      "\n",
      " [[2]\n",
      " [5]\n",
      " [8]]\n"
     ]
    }
   ],
   "source": [
    "y = np.arange(1,10).reshape(3,3)\n",
    "print(y)\n",
    "\n",
    "w = np.delete(y,0,axis=0)\n",
    "print('\\n',w)\n",
    "\n",
    "v = np.delete(y,[0,2],axis=1)\n",
    "print('\\n',v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = np.array([1,2,3,4])"
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
      "[1 2 3 4 7 8]\n"
     ]
    }
   ],
   "source": [
    "x = np.append(x,[7,8])\n",
    "print(x)"
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
      "[[1 2 3]\n",
      " [4 5 6]\n",
      " [7 8 9]]\n"
     ]
    }
   ],
   "source": [
    "x=np.arange(1,10).reshape(3,3)\n",
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
      "[[ 1  2  3]\n",
      " [ 4  5  6]\n",
      " [ 7  8  9]\n",
      " [10 11 12]]\n"
     ]
    }
   ],
   "source": [
    "w = np.append(x,[[10,11,12]],axis=0)\n",
    "print(w)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "#axis=1 ->represents column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 3 4 5 6 7 8 9]\n"
     ]
    }
   ],
   "source": [
    "x = np.insert(x,2,[3,4])\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3]\n",
      " [7 8 9]]\n"
     ]
    }
   ],
   "source": [
    "y = np.array([[1,2,3],[7,8,9]])\n",
    "print(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "w=np.insert(y,1,[4,5,6],axis = 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3]\n",
      " [4 5 6]\n",
      " [7 8 9]]\n"
     ]
    }
   ],
   "source": [
    "print(w)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 3 4 5 6 7 8 9]\n"
     ]
    }
   ],
   "source": [
    "x = np.insert(w,2,[3,4])\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 5 2 3]\n",
      " [4 5 5 6]\n",
      " [7 5 8 9]]\n"
     ]
    }
   ],
   "source": [
    "v = np.insert(w,1,5,axis = 1)\n",
    "print(v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "#z = np.vstack((x,y)) vertically stacking x on top of y "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
