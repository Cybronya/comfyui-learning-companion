# PowerPaintCLIPLoader

## 节点类型

`PowerPaintCLIPLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 11 个 workflow 中。

## 输入

- `base:COMBO`（1 次）
- `powerpaint:COMBO`（1 次）

## 输出

- `clip:CLIP`（11 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["clip_l.safetensors", "powerpaint/pytorch_model.bin"]`（6 次）
- `["clip-vit-large-patch14/model.safetensors", "JunhaoZhuang.PowerPaint-v2-1/pytorch_model.bin"]`（2 次）
- `["runwayml.stable-diffusion-v1-5/model.fp16.safetensors", "JunhaoZhuang.PowerPaint-v2-1/pytorch_model.bin"]`（1 次）
- `["clip_l.safetensors", "JunhaoZhuang.PowerPaint-v2-1/pytorch_model.bin"]`（1 次）
- `["runwayml.stable-diffusion-v1-5/model.fp16.safetensors", "powerpaint/pytorch_model.bin"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
