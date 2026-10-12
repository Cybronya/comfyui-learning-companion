# ToonCrafterInterpolation

## 节点类型

`ToonCrafterInterpolation`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:DCMODEL`（2 次）
- `clip_vision:CLIP_VISION`（2 次）
- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `images:IMAGE`（2 次）
- `optional_latents:LATENT`（2 次）
- `controlnet:DC_CONTROL`（1 次）

## 输出

- `samples:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[20, 7, 1, 16, 848912075889866, "randomize", 30, "fp16", 1, 0, 1000]`（1 次）
- `[20, 7, 1, 16, 1101314196604391, "randomize", 10, "auto", 1, 0, 1000]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
