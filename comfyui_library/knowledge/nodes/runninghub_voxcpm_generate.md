# RunningHub_VoxCPM_Generate

## 节点类型

`RunningHub_VoxCPM_Generate`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:VOXCPM_MODEL`（3 次）
- `reference_audio:AUDIO`（3 次）
- `control_instruction:STRING`（3 次）
- `text:STRING`（3 次）
- `cfg_value:FLOAT`（3 次）
- `inference_steps:INT`（3 次）
- `seed:INT`（3 次）
- `ultimate_clone:BOOLEAN`（3 次）
- `reference_audio_text:STRING`（3 次）
- `normalize_text:BOOLEAN`（3 次）

## 输出

- `audio:AUDIO`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["声音洪亮 语气急促", "T8那个瓜娃子，一天到黑只晓得搞视频，耳都不耳你一下。", 2, 10, 460719784844134, "randomize", false, "", false, false, 4096, true]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
