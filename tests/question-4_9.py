test = {
  'name': 'question 4.9',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(A) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(A, [[0, 12, -1], [-1, -1, -1], [11, 5, 5]])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(b) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(b, [-2, 1, 7])
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
          >>> type(c) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(c, [5., -6., 18.])
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
          >>> type(multiply) == types.FunctionType # You were asked to put your code in a function called multiply
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
      'setup': 'import types; import inspect; param = inspect.signature(multiply).parameters',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> np.allclose(multiply(ain, bin), bout)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': """
import numpy as np
ain = np.array([[1,1],[0,1]])
bin = np.array([1,1])
bout = np.array([2,1])
""",
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
