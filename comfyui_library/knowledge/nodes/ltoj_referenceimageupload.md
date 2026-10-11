# LtoJ_ReferenceImageUpload

## 节点类型

`LtoJ_ReferenceImageUpload`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:COMBO`（9 次）
- `enabled:BOOLEAN`（9 次）
- `upload:IMAGEUPLOAD`（9 次）

## 输出

- `参考图与启用状态:LTOJ_H3_REFERENCE_ITEM`（9 次）
- `图像:IMAGE`（9 次）
- `遮罩:MASK`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["example.png", false, "image"]`（9 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
