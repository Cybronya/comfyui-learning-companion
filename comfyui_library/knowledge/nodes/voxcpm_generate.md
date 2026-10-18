# VoxCPM_Generate

## 节点类型

`VoxCPM_Generate`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:VOXCPM_MODEL`（2 次）
- `reference_audio:AUDIO`（2 次）
- `control_instruction:STRING`（2 次）
- `text:STRING`（2 次）
- `cfg_value:FLOAT`（2 次）
- `inference_steps:INT`（2 次）
- `seed:INT`（2 次）
- `ultimate_clone:BOOLEAN`（2 次）
- `reference_audio_text:STRING`（2 次）
- `normalize_text:BOOLEAN`（2 次）

## 输出

- `audio:AUDIO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["粤语，", "努力唔一定会即刻见效果，但坚持落去，一定有收获", 2, 10, 567407752357854, "randomize", false, "", false, false]`（1 次）
- `["", "", 2.7, 50, 299926936992814, "randomize", false, "", false, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
