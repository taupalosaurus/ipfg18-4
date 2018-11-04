test = {
  'name': 'question 4.10',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(A33) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(A33, [[0.,  12.,  -1.], [ -1.,  -1.,  -1.], [11.,  5.,  5.]])
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
          >>> type(f_cubic) == types.FunctionType
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(param) # wrong number of argument
          1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'setup': 'import types, inspect; param = inspect.signature(f_cubic).parameters',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> type(A33_vec) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(A33_vec, f_A33)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': """
import numpy as np
f_A33 = np.array([[ 1.00000000e+00,  1.95478650e+06, -3.67879441e-01],
                  [-3.67879441e-01, -3.67879441e-01, -3.67879441e-01],
                  [ 6.59947559e+05,  8.68065796e+02,  8.68065796e+02]])
""",
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> type(A33_f) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(A33_f, f_A33)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': """
import numpy as np
f_A33 = np.array([[ 1.00000000e+00,  1.95478650e+06, -3.67879441e-01],
                  [-3.67879441e-01, -3.67879441e-01, -3.67879441e-01],
                  [ 6.59947559e+05,  8.68065796e+02,  8.68065796e+02]])
""",
      'teardown': '',
      'type': 'doctest'
    }
  ]
}