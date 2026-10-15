# ZML_LoadImage

## 节点类型

`ZML_LoadImage`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:COMBO`（1 次）
- `正规化:COMBO`（1 次）
- `读取文本块:COMBO`（1 次）
- `输出透明:COMBO`（1 次）
- `upload:IMAGEUPLOAD`（1 次）

## 输出

- `图像:IMAGE`（1 次）
- `文本块:STRING`（1 次）
- `Name:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["undefined", "正规", "禁用", "启用", "image"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
