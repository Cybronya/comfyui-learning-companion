# workflow/WanVideo Model Loader

## 节点类型

`workflow/WanVideo Model Loader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:WANCLIP`（1 次）
- `image:IMAGE`（1 次）
- `samples:LATENT`（1 次）

## 输出

- `image_embeds:WANVIDIMAGE_EMBEDS`（1 次）
- `images:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Wan2_1_VAE_bf16.safetensors", "bf16", 512, 512, 81, true, true, 272, 272, 144, 128]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
