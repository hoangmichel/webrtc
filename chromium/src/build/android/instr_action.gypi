# Copyright 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# This file is meant to be included into an action to provide a rule that
# instruments either java class files, or jars.

{
  'variables': {
    'instr_type%': 'jar',
    'input_path%': '',
    'output_path%': '',
    'stamp_path%': '',
    'extra_instr_args': [
      '--coverage-file=<(_target_name).em',
      '--sources-file=<(_target_name)_sources.txt',
    ],
    'emma_jar': '<(android_sdk_root)/tools/lib/emma.jar',
    'conditions': [
      ['emma_instrument != 0', {
        'extra_instr_args': [
          '--sources=<(java_in_dir)/src >(additional_src_dirs) >(generated_src_dirs)',
          '--src-root=<(webrtc_depot_dir)',
          '--emma-jar=<(emma_jar)',
          '--filter-string=<(emma_filter)',
        ],
        'conditions': [
          ['instr_type == "jar"', {
            'instr_action': 'instrument_jar',
          }, {
            'instr_action': 'instrument_classes',
          }]
        ],
      }, {
        'instr_action': 'copy',
        'extra_instr_args': [],
      }]
    ]
  },
  'inputs': [
    '<(webrtc_depot_dir)/build/android/gyp/emma_instr.py',
    '<(webrtc_depot_dir)/build/android/gyp/util/build_utils.py',
    '<(webrtc_depot_dir)/build/android/pylib/utils/command_option_parser.py',
  ],
  'action': [
    'python', '<(webrtc_depot_dir)/build/android/gyp/emma_instr.py',
    '<(instr_action)',
    '--input-path=<(input_path)',
    '--output-path=<(output_path)',
    '--stamp=<(stamp_path)',
    '<@(extra_instr_args)',
  ]
}
