# LoadImageReturnFilename

## 节点类型

`LoadImageReturnFilename`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:COMBO`（18 次）
- `upload:IMAGEUPLOAD`（18 次）

## 输出

- `image:IMAGE`（18 次）
- `mask:MASK`（18 次）
- `filename:STRING`（18 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["826a630ecad8dfcd63400da03972b775a2cd482de638956d1148a62f18205239.png", "image"]`（6 次）
- `["d86e78156191523b05e636c2fa83303264667617a8d317b2722b4e6255d8a658.png", "image"]`（2 次）
- `["d96c4dcd125a16e3c41ab09772ba9413cffdd254707fe34c1682da0989a31a88.png", "image"]`（1 次）
- `["296d2d51bd3e609e4d39225ac4c6dc99c7b6b0b86ecc2d09e0495be8da28922a.png", "image"]`（1 次）
- `["f3892f1526c08976cda0f9475d52c343c5f4bacf77efa16e6fec5401327ea8b4.png", "image"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
