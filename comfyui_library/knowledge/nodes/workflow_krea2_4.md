# workflow>Krea2 4视图

## 节点类型

`workflow>Krea2 4视图`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `IMAGE:IMAGE`（1 次）
- `image_b:IMAGE`（1 次）
- `negative (leave empty) image_b:IMAGE`（1 次）
- `source_latent_b:LATENT`（1 次）
- `ref_boost_mask:MASK`（1 次）
- `source_image_b:IMAGE`（1 次）
- `clip_name:COMBO`（1 次）
- `type:COMBO`（1 次）
- `device:COMBO`（1 次）
- `width:INT`（1 次）

## 输出

- `图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["qwen3vl_4b_fp8_scaled.safetensors", "krea2", "default", 1536, 1024, 1, "qwen_image_HDR_vae_fp32_comfy.safetensors", "k`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
