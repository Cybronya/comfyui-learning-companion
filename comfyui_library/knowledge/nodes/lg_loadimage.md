# LG_LoadImage

## 节点类型

`LG_LoadImage`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:COMBO`（3 次）
- `keep_alpha:BOOLEAN`（3 次）
- `upload:IMAGEUPLOAD`（3 次）

## 输出

- `IMAGE:IMAGE`（3 次）
- `MASK:MASK`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["8d4c706163e19054e9a64cd88777d0ebcb1d6b5ddbeba32e391d812446465995.png", false, "image"]`（1 次）
- `["78f076c0cf35583c5047514d173b2ea56c155082a017f975627f39554d5e017b.webp", false, "image"]`（1 次）
- `["e4a1d2f87f56c7941bd206b26f164c0c56d9a99b410a4e2429ad09713ddc2948.webp", false, "image"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
