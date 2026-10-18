# RunningHub_VoxCPM_MultiSpeaker_ListReference

## 节点类型

`RunningHub_VoxCPM_MultiSpeaker_ListReference`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:VOXCPM_MODEL`（1 次）
- `audio_1:AUDIO`（1 次）
- `audio_2:AUDIO`（1 次）
- `script:STRING`（1 次）
- `speaker_controls:STRING`（1 次）
- `cfg_value:FLOAT`（1 次）
- `inference_steps:INT`（1 次）
- `seed:INT`（1 次）
- `normalize_text:BOOLEAN`（1 次）
- `denoise_reference:BOOLEAN`（1 次）

## 输出

- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["[spk1]我是思考者 THIN-K，我会在行动前把各种可能性过一遍：最优解、最坏结果、备用方案全都在脑子里跑过。所以你看起来像在犹豫，但其实是在提高成功率。\n[spk2]我是行者 GOGO，灵感一来，立刻行动。今天健身、明天创业、后`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
