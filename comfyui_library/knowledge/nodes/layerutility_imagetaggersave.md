# LayerUtility: ImageTaggerSave

## 节点类型

`LayerUtility: ImageTaggerSave`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `tag_text:STRING`（1 次）
- `custom_path:STRING`（1 次）
- `filename_prefix:STRING`（1 次）
- `timestamp:COMBO`（1 次）
- `format:COMBO`（1 次）
- `quality:INT`（1 次）
- `preview:BOOLEAN`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "krea2moyou", "None", "jpg", 100, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
