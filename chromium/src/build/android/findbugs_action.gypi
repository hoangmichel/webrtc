
{
  'action_name': 'findbugs_<(_target_name)',
  'message': 'Running findbugs on <(_target_name)',
  'variables': {
  },
  'inputs': [
    '<(peeracle_webrtc_root)/build/android/findbugs_diff.py',
    '<(peeracle_webrtc_root)/build/android/findbugs_filter/findbugs_exclude.xml',
    '<(peeracle_webrtc_root)/build/android/pylib/utils/findbugs.py',
    '<(findbugs_target_jar_path)',
  ],
  'outputs': [
    '<(stamp_path)',
  ],
  'action': [
    'python', '<(peeracle_webrtc_root)/build/android/findbugs_diff.py',
    '--auxclasspath-gyp', '>(auxclasspath)',
    '--stamp', '<(stamp_path)',
    '<(findbugs_target_jar_path)',
  ],
}
