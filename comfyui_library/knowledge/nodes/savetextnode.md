# SaveTextNode

## 节点类型

`SaveTextNode`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `text:STRING`（2 次）
- `file_path:STRING`（2 次）
- `filename:STRING`（2 次）
- `extension:COMBO`（2 次）
- `exist_mode:COMBO`（2 次）
- `text_prefix:STRING`（2 次）

## 输出

- `保存信息:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", "ComfyUI", "txt", "换行追加", ""]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
