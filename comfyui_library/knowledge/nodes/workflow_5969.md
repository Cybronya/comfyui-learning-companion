# workflow>高清放大处理

## 节点类型

`workflow>高清放大处理`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `LoRA:PEFTLORA`（1 次）
- `图像:IMAGE`（1 次）
- `text1:STRING`（1 次）
- `text2:STRING`（1 次）
- `text3:STRING`（1 次）
- `text4:STRING`（1 次）
- `text5:STRING`（1 次）
- `model_name:COMBO`（1 次）
- `UpscaleModelLoader model_name:COMBO`（1 次）
- `model:COMBO`（1 次）

## 输出

- `图像:IMAGE`（1 次）
- `Florence2Run 图像:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- `json数据:JSON`（1 次）
- `batch_size:INT`（1 次）
- `宽度:INT`（1 次）
- `高度:INT`（1 次）
- `image_urls:STRING`（1 次）
- `Florence2Run 25 图像:IMAGE`（1 次）
- `Florence2Run 遮罩:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["4xFaceUpLDAT.pth", "4x-ClearRealityV1.pth", "Florence-2-Flux-Large", "fp16", "sdpa", false, "z_image_turbo_bf16.safete`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
