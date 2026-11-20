# workflow/edit

## 节点类型

`workflow/edit`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `get_image_size:IMAGE`（1 次）
- `images:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `ImageResizeKJ image:IMAGE`（1 次）
- `ImageResizeKJ get_image_size:IMAGE`（1 次）
- `width_input:INT`（1 次）
- `height_input:INT`（1 次）
- `ImageResizeKJ width_input:INT`（1 次）
- `ImageResizeKJ height_input:INT`（1 次）

## 输出

- `height:INT`（1 次）
- `IMAGE:IMAGE`（1 次）
- `ImageConcanate IMAGE:IMAGE`（1 次）
- `VAEDecode IMAGE:IMAGE`（1 次）
- `ImageCrop IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["flux1-fill-dev.safetensors", "fp8_e4m3fn", "clip_l.safetensors", "sd3/t5xxl_fp8_e4m3fn.safetensors", "flux", "default"`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
