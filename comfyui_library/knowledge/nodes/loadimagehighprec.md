# LoadImageHighPrec

## 节点类型

`LoadImageHighPrec`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:COMBO`（2 次）
- `upload:IMAGEUPLOAD`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）
- `MASK:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["d1c0953fde27656d4e898b56e1b37123665f33159e0105525e9660fdb59faa9c.jpg", "image"]`（1 次）
- `["f2f8a3ecc88c83ff860d86abe9977a09d5b8a3d6649a62641ab8c7a2a5855ec2.jpg", "image"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
