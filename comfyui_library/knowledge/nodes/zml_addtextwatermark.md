# ZML_AddTextWatermark

## 节点类型

`ZML_AddTextWatermark`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `文本:STRING`（1 次）
- `字体:COMBO`（1 次）
- `字体大小:INT`（1 次）
- `颜色:STRING`（1 次）
- `不透明度:FLOAT`（1 次）
- `书写方向:COMBO`（1 次）
- `位置:COMBO`（1 次）
- `水平边距:INT`（1 次）
- `垂直边距:INT`（1 次）

## 输出

- `图像:IMAGE`（1 次）
- `Help:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ZML_水印", "Default", 48, "#000000", 0.7, "横排", "左上", 20, 20, 10, 10, 1, "#FFFFFF", -30, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
