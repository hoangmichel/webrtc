
{
  'action_name': 'findbugs_<(_target_name)',
  'message': 'Running findbugs on <(_target_name)',
  'variables': {
  },
  'inputs': [
    '<(webrtc_depot_dir)/build/android/findbugs_diff.py',
    '<(webrtc_depot_dir)/build/android/findbugs_filter/findbugs_exclude.xml',
    '<(webrtc_depot_dir)/build/android/pylib/utils/findbugs.py',
    '<(findbugs_target_jar_path)',
  ],
  'outputs': [
    '<(stamp_path)',
  ],
  'action': [
    'python', '<(webrtc_depot_dir)/build/android/findbugs_diff.py',
    '--auxclasspath-gyp', '>(auxclasspath)',
    '--stamp', '<(stamp_path)',
    '<(findbugs_target_jar_path)',
  ],
}
