# Eden_Save_Param_Dict

## 节点类型

`Eden_Save_Param_Dict`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `value_1:*`（8 次）
- `value_2:*`（8 次）
- `value_3:*`（8 次）
- `value_4:*`（8 次）
- `value_5:*`（8 次）
- `value_6:*`（8 次）
- `value_7:*`（8 次）
- `value_8:*`（8 次）
- `value_9:*`（8 次）
- `value_10:*`（8 次）

## 输出

- `saved_path:STRING`（8 次）
- `json_string:STRING`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["params.json", "scores", "bboxs", "masks", "image_urls", "param5", "param6", "param7", "param8", "param9", "param10"]`（8 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
