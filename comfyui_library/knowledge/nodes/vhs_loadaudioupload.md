# VHS_LoadAudioUpload

## 节点类型

`VHS_LoadAudioUpload`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `audio:STRING`（6 次）
- `start_time:FLOAT`（6 次）
- `duration:FLOAT`（6 次）

## 输出

- `audio:AUDIO`（6 次）
- `audio_length_seconds:FLOAT`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `{"audio": "None", "choose audio to upload": "image", "duration": 0, "start_time": 0}`（3 次）
- `{"audio": "0029ac860f04be2b6e84a44475cd003a98fda7d6794325f56e6c4bf962d05ea3.mp4", "choose audio to upload": "image", "du`（1 次）
- `{"audio": "10s.MP3", "choose audio to upload": "image", "duration": 5.000000000000001, "start_time": 4.7}`（1 次）
- `{"audio": "06d16104cbf732b85679781b81a4246c.mp4", "choose audio to upload": "image", "duration": 0, "start_time": 0}`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
