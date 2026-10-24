# CLIPSeg

## 节点类型

`CLIPSeg`

## 分类

Conditioning

## 作用

CLIP/条件相关节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `image:IMAGE`（6 次）
- `text:STRING`（2 次）
- `blur:FLOAT`（2 次）
- `threshold:FLOAT`（2 次）
- `dilation_factor:INT`（2 次）

## 输出

- `Mask:MASK`（6 次）
- `Heatmap Mask:IMAGE`（6 次）
- `BW Mask:IMAGE`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["face,head", 7, 0.4, 10]`（2 次）
- `["girl face", 5.800000000000001, 0.4, 4]`（1 次）
- `["hair", 7, 0.4, 4]`（1 次）
- `["face,head", 8, 0.4, 5]`（1 次）
- `["fece", 5.6000000000000005, 0.3500000000000001, 4]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
