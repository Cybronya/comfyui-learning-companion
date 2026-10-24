# LoadImageNode

## 节点类型

`LoadImageNode`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image_file:COMBO`（1 次）
- `upload:IMAGEUPLOAD`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `image_path:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["2ecd99c369e8dd926ae532c01408d038fa972ce4831ce16140aa5f4a30ff5f9d.jpg", "image"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
