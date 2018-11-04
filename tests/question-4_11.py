test = {
  'name': 'question 4.11',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(M1) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(M1, [[0, 12, -1], [-1, -1, -1], [11, 5, 5]])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(M2) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(M2, [[-2, 1, 7], [3, 0, 6], [2, 3, 5]])
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': 'import numpy as np',
      'teardown': '',
      'type': 'doctest'

    },
    {
      'cases': [
        {
          'code': r"""
          >>> type(M3) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(M3, [[ 34, -3, 67], [-3, -4, -18], [3, 26, 132]])
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': 'import numpy as np',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> type(multiply_mat) == types.FunctionType # You were asked to put your code in a function called multiply_mat
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(param) # wrong number of argument
          2
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': """
import types; 
import inspect; 
param = inspect.signature(multiply_mat).parameters
""",
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> np.allclose(multiply_mat(ain1, ain2), aout)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': """
import numpy as np
ain1 = np.array([[1,1],[0,1]])
ain2 = np.array([[1,0],[1,1]])
aout = np.array([[2,1],[1,1]])
""",
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

