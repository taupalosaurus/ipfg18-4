test = {
  'name': 'question 4.2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(t_array)==np.ndarray 
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(t_array, array_42_ref)
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': """
import numpy as np
array_42_ref = [3., 3.04959014, 3.09838668, 3.14642654, 3.19374388, 3.24037035, 3.28633535, 3.33166625, 3.3763886, 3.42052628, 3.46410162]
""",
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
