# ReActorSaveFaceModel

## 节点类型

`ReActorSaveFaceModel`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `face_model:FACE_MODEL`（2 次）
- `save_mode:BOOLEAN`（1 次）
- `face_model_name:STRING`（1 次）
- `select_face_index:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, "mix-1", 0]`（1 次）
- `[true, "face_test", 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
