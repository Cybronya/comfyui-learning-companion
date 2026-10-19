# ImageLoaderPlus

## 节点类型

`ImageLoaderPlus`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:COMBO`（1 次）
- `upload:IMAGEUPLOAD`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `MASK:MASK`（1 次）
- `PATH:PATH`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["pasted/fd1d9a2a73cb8702466ca697b2e188e9afc56b148eb2b50f706ca4473fadd3ee.png", "image"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
