# LTXLoraStackAV

## 节点类型

`LTXLoraStackAV`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `num_loras:INT`（2 次）
- `lora_1:COMBO`（2 次）
- `strength_1:FLOAT`（2 次）
- `audio_weight_1:FLOAT`（2 次）
- `video_weight_1:FLOAT`（2 次）
- `lora_2:COMBO`（2 次）
- `strength_2:FLOAT`（2 次）
- `audio_weight_2:FLOAT`（2 次）
- `video_weight_2:FLOAT`（2 次）

## 输出

- `MODEL:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2, "None", 1, 1, 0.5, "ltx-2.3-22b-distilled-lora-1.1_rank72_energy.safetensors", 1, 1, 0.3799999999999999, "None", 1, `（1 次）
- `[1, "ltx-2.3-22b-distilled-lora-1.1_rank72_energy.safetensors", 1, 1, 0.6799999999999997, "None", 1, 1, 1, "None", 1, 1,`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
