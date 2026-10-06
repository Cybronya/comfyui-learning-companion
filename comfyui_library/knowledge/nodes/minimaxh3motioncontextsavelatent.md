# MiniMaxH3MotionContextSaveLatent

## 节点类型

`MiniMaxH3MotionContextSaveLatent`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `latent:LATENT`（4 次）
- `filename_prefix:STRING`（4 次）
- `clip_index:INT`（4 次）

## 输出

- `latent_path:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["h3_context/clip", 1]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
