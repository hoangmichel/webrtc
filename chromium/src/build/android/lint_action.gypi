# Copyright 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# This file is meant to be included into an action to provide a rule to
# run lint on java/class files.

{
  'action_name': 'lint_<(_target_name)',
  'message': 'Linting <(_target_name)',
  'variables': {
    'conditions': [
      ['chromium_code != 0 and android_lint != 0 and never_lint == 0', {
        'is_enabled': '--enable',
      }, {
        'is_enabled': '',
      }]
    ],
    'android_manifest_path%': '<(peeracle_webrtc_root)/build/android/AndroidManifest.xml',
    'resource_dir%': '<(peeracle_webrtc_root)/build/android/ant/empty/res',
  },
  'inputs': [
    '<(peeracle_webrtc_root)/build/android/gyp/util/build_utils.py',
    '<(peeracle_webrtc_root)/build/android/gyp/lint.py',
    '<(peeracle_webrtc_root)/build/android/lint/suppressions.xml',
    '<(lint_jar_path)',
  ],
  'action': [
    'python', '<(peeracle_webrtc_root)/build/android/gyp/lint.py',
    '--lint-path=<(android_sdk_root)/tools/lint',
    '--config-path=<(peeracle_webrtc_root)/build/android/lint/suppressions.xml',
    '--processed-config-path=<(config_path)',
    '--manifest-path=<(android_manifest_path)',
    '--result-path=<(result_path)',
    '--resource-dir=<(resource_dir)',
    '--product-dir=<(PRODUCT_DIR)',
    '--src-dirs=>(src_dirs)',
    '--jar-path=<(lint_jar_path)',
    '--stamp=<(stamp_path)',
    '<(is_enabled)',
  ],
}
