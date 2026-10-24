# EasySizeSimpleImage

## 节点类型

`EasySizeSimpleImage`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 13 个 workflow 中。

## 输入

- `图像:IMAGE`（15 次）
- `遮罩:MASK`（15 次）
- `SD1.5:COMBO`（15 次）
- `SDXL:COMBO`（15 次）
- `FLUX:COMBO`（15 次）
- `WAN:COMBO`（15 次）
- `QWEN:COMBO`（15 次）
- `裁剪方式:COMBO`（15 次）
- `缩放算法:COMBO`（15 次）
- `启用边长缩放:BOOLEAN`（15 次）

## 输出

- `图像:IMAGE`（15 次）
- `遮罩:MASK`（15 次）
- `宽:INT`（15 次）
- `高:INT`（15 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["关", "关", "关", "关", "关", "中心裁剪", "lanczos", true, "最长边", 1280]`（7 次）
- `["关", "关", "关", "关", "关", "中心裁剪", "lanczos", true, "最长边", 1024]`（5 次）
- `["关", "关", "关", "关", "关", "中心裁剪", "lanczos", true, "最短边", 1024]`（2 次）
- `["关", "关", "关", "关", "关", "中心裁剪", "lanczos", true, "最长边", 2048]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
