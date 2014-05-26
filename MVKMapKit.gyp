{
  'target_defaults': {
    'default_configuration': 'Release',
    'type': 'executable',
    'mac_bundle': 1,
    'xcode_settings': {
      'SDKROOT': 'iphoneos',
      'SUPPORTED_PLATFORMS':['iphonesimulator','iphoneos'],
      'ARCHS': [ 'armv7', 'armv7s', 'arm64', 'i386' ]
    },
    'configurations': {
      'Debug': {
        'xcode_settings': {
          'CODE_SIGN_IDENTITY': 'iPhone Developer',
        }
      },
      'Release': {
        'xcode_settings': {
          'CODE_SIGN_IDENTITY': 'iPhone Distribution',
        }
      }
    },
  },
  'targets': [
    {
        'target_name': 'Resources',
        'product_name': 'MVKMapKit',
        'product_extension': 'bundle',
        'mac_bundle_resources': [
          '<!@(find MVKMapKit/Resources -type f)'
        ],
    },
    {
        'target_name': 'Sample App',
        'product_name': 'Sample App',
        'sources': [
            './MVKMapKit/main.m',
            './MVKMapKit/MVKAppDelegate.h',
            './MVKMapKit/MVKAppDelegate.m',
            './MVKMapKit/MVKViewController.h',
            './MVKMapKit/MVKViewController.m',
            './MVKMapKit/MVKMapView.h',
            './MVKMapKit/MVKMapView.mm',
            '../../common/foundation_request.h',
            '../../common/foundation_request.mm',
        ],
        'product_extension': 'app',
        'mac_bundle_resources': [
          '<(PRODUCT_DIR)/MVKMapKit.bundle'
        ],
        'link_settings': {
          'libraries': [
            '$(SDKROOT)/System/Library/Frameworks/CoreGraphics.framework',
            '$(SDKROOT)/System/Library/Frameworks/CoreLocation.framework',
            '$(SDKROOT)/System/Library/Frameworks/GLKit.framework',
            '$(SDKROOT)/System/Library/Frameworks/OpenGLES.framework',
            '$(SDKROOT)/System/Library/Frameworks/UIKit.framework'
          ],
        },
        'xcode_settings': {
          'INFOPLIST_FILE': 'MVKMapKit/MVKMapKit-Info.plist',
          'CLANG_CXX_LIBRARY': 'libc++',
          'CLANG_CXX_LANGUAGE_STANDARD':'c++11',
          'IPHONEOS_DEPLOYMENT_TARGET':'7.0',
          'TARGETED_DEVICE_FAMILY': '1,2',
          'GCC_VERSION': 'com.apple.compilers.llvm.clang.1_0',
          'CLANG_ENABLE_OBJC_ARC': 'YES'
        },
        'dependencies': [
            '../../llmr.gyp:llmr-ios',
            'Resources'
        ]
    }
  ]
}