# ZML_LimitImageAspect

## 节点类型

`ZML_LimitImageAspect`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `图像:IMAGE`（5 次）
- `目标比例:COMBO`（5 次）
- `模式:COMBO`（5 次）
- `限制分辨率:BOOLEAN`（5 次）

## 输出

- `处理后图像:IMAGE`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["1：1", "裁剪", true]`（3 次）
- `["1：1", "填充白", true]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
