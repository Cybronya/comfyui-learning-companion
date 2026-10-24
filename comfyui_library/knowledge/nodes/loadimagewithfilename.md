# LoadImageWithFilename

## 节点类型

`LoadImageWithFilename`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:COMBO`（5 次）
- `upload:IMAGEUPLOAD`（5 次）

## 输出

- `IMAGE:IMAGE`（5 次）
- `STRING:STRING`（5 次）
- `MASK:MASK`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["842538092e8ef06cce474f31545622b218cf846e95c8fe4431c8eb0f854be03e.jpg", "image"]`（4 次）
- `["f67aafd56396094531b036f0df223ecaed9a83b620f7899a3aa03aed38d2e479.png", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
