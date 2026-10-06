# DualCLIPLoader

## 节点类型

`DualCLIPLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 9 个 workflow 中。

## 输入

- `clip_name1:COMBO`（13 次）
- `clip_name2:COMBO`（13 次）
- `type:COMBO`（13 次）
- `device:COMBO`（13 次）

## 输出

- `CLIP:CLIP`（13 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["t5xxl_fp8_e4m3fn.safetensors", "clip_l.safetensors", "flux", "default"]`（7 次）
- `["clip_l.safetensors", "t5xxl_fp16.safetensors", "flux", "default"]`（6 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
