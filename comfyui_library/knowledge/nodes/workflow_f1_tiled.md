# workflow/F1.tiled

## 节点类型

`workflow/F1.tiled`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `get_image_size:IMAGE`（1 次）
- `width_input:INT`（1 次）
- `height_input:INT`（1 次）

## 输出

- `width:INT`（1 次）
- `height:INT`（1 次）
- `denoised_output:LATENT`（1 次）
- `RECONSTRUCTED_IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ae.sft", "euler", 26115234363799, "randomize", "flux1-dev.sft", "fp8_e4m3fn", "t5xxl_fp8_e4m3fn.safetensors", "clip_l.`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
