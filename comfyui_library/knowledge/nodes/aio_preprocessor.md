# AIO_Preprocessor

## 节点类型

`AIO_Preprocessor`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 13 个 workflow 中。

## 输入

- `image:IMAGE`（16 次）
- `preprocessor:COMBO`（16 次）
- `resolution:INT`（16 次）

## 输出

- `IMAGE:IMAGE`（16 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["DWPreprocessor", 512]`（3 次）
- `["DWPreprocessor", 1024]`（3 次）
- `["DepthAnythingV2Preprocessor", 1024]`（3 次）
- `["CannyEdgePreprocessor", 1024]`（3 次）
- `["DepthAnythingV2Preprocessor", 1472]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
