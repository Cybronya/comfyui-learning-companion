# RunningHub_VoxCPM_MultiSpeaker

## 节点类型

`RunningHub_VoxCPM_MultiSpeaker`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:VOXCPM_MODEL`（3 次）
- `audio_1:AUDIO`（3 次）
- `audio_2:AUDIO`（3 次）
- `audio_3:AUDIO`（3 次）
- `audio_4:AUDIO`（3 次）
- `audio_5:AUDIO`（3 次）
- `script:STRING`（3 次）
- `cfg_value:FLOAT`（3 次）
- `inference_steps:INT`（3 次）
- `seed:INT`（3 次）

## 输出

- `audio:AUDIO`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 2, 10, 1111132265002331, "randomize", "四川话", "成年女性，东北话", "", "", "旁白音，成熟男性", false, false, 4096, true]`（1 次）
- `["", 2, 10, 897615007377742, "randomize", "压低声量，成熟男性", "成年女性，东北话", "", "", "旁白音，成熟男性", false, false, 4096, true]`（1 次）
- `["", 2, 10, 509918152758564, "randomize", "四川话", "成年女性，东北话", "", "", "旁白音，成熟男性", false, false, 4096, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
