# workflow>真实照片处理

## 节点类型

`workflow>真实照片处理`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `LayerMask: PersonMaskUltra V2 images:IMAGE`（1 次）
- `图像_kps:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- `InpaintModelConditioning pixels:IMAGE`（1 次）
- `InpaintModelConditioning mask:MASK`（1 次）
- `library:COMBO`（1 次）
- `provider:COMBO`（1 次）
- `InstantIDFaceAnalysis provider:COMBO`（1 次）
- `InstantID文件:COMBO`（1 次）

## 输出

- `X:INT`（1 次）
- `Y:INT`（1 次）
- `宽度:INT`（1 次）
- `高度:INT`（1 次）
- `图像:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- `VAEDecode 图像:IMAGE`（1 次）
- `image_urls:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["insightface", "CUDA", "CUDA", "ip-adapter.bin", "instantid/diffusion_pytorch_model.safetensors", "juggernautXL_v9Rdpho`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
