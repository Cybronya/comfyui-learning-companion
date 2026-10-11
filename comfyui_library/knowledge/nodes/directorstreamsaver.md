# DirectorStreamSaver

## 节点类型

`DirectorStreamSaver`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `video:IMAGE`（3 次）
- `audio:*`（3 次）
- `idx_current:INT`（3 次）
- `idx_total:INT`（3 次）
- `filename_prefix:STRING`（3 次）
- `fps:INT`（3 次）

## 输出

- `Manifest_Path:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["scene", 20]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
