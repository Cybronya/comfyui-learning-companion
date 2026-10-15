# NanguangTextToImage

## 节点类型

`NanguangTextToImage`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `文本内容:STRING`（1 次）
- `字体文件:COMBO`（1 次）
- `图像宽度:INT`（1 次）
- `图像高度:INT`（1 次）
- `字体大小:INT`（1 次）
- `文字颜色:STRING`（1 次）
- `背景颜色:STRING`（1 次）
- `边距:INT`（1 次）
- `行间距:INT`（1 次）
- `文件名前缀:STRING`（1 次）

## 输出

- `图像:IMAGE`（1 次）
- `保存路径:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["南光AI\n文本转图像", "华文中宋.ttf", 1280, 1920, 32, "000000", "FFF4D5", 60, 6, "南光AI文本", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
