# HYPIRAdvancedRestoration

## 节点类型

`HYPIRAdvancedRestoration`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `prompt:STRING`（2 次）
- `upscale_factor:INT`（2 次）
- `seed:INT`（2 次）
- `model_name:COMBO`（2 次）
- `base_model_path:COMBO`（2 次）
- `model_t:INT`（2 次）
- `coeff_t:INT`（2 次）
- `lora_rank:INT`（2 次）
- `patch_size:INT`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）
- `STRING:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["high quality, detailed", 1, 793262013523130, "randomize", "HYPIR_sd2", "stable-diffusion-2-1-base", 200, 100, 256, 512`（1 次）
- `["high quality, detailed", 2, 672886096902386, "randomize", "HYPIR_sd2", "stable-diffusion-2-1-base", 200, 120, 256, 256`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
