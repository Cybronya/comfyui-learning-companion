# workflow>h3采样

## 节点类型

`workflow>h3采样`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `H3 Context:MINIMAX_H3_CONTEXT`（1 次）
- `noise_seed:INT`（1 次）
- `lora_name:COMBO`（1 次）
- `strength:FLOAT`（1 次）
- `low_vram:BOOLEAN`（1 次）
- `scheduler:COMBO`（1 次）
- `steps:INT`（1 次）
- `denoise:FLOAT`（1 次）

## 输出

- `FPS:FLOAT`（1 次）
- `驱动音频:AUDIO`（1 次）
- `IMAGE:IMAGE`（1 次）
- `AUDIO:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, "fixed", "minimax_h3_turbo_v4_step600_ema.safetensors", 1, false, "simple", 4, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
