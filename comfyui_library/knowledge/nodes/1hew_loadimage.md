# 1hew_LoadImage

## 节点类型

`1hew_LoadImage`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `get_image_size:IMAGE`（1 次）
- `file:STRING`（1 次）
- `index:INT`（1 次）
- `include_subdir:BOOLEAN`（1 次）
- `all:BOOLEAN`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `filename:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["/data/ComfyUI/personal/input/1hew_uploads_images/1783859713291488597/e69ce3e9-cc7f-407c-8ef2-c7744f8075b7.png", 0, tru`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
