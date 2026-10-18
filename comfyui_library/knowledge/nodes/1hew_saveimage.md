# 1hew_SaveImage

## 节点类型

`1hew_SaveImage`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `filename:STRING`（2 次）
- `auto_increment:BOOLEAN`（2 次）
- `save_output:BOOLEAN`（2 次）
- `save_metadata:BOOLEAN`（2 次）

## 输出

- `file_path:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["image/ComfyUI", true, true, true]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
