# StringOutputList

## 节点类型

`StringOutputList`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输出

- `value:*`（4 次）
- `index:INT`（4 次）
- `count:INT`（4 次）
- `inspect_combo:COMBO`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["\\n", "simple\nsgm_uniform"]`（1 次）
- `["\\n", "euler\neuler_ancestral"]`（1 次）
- `["\\n", "a watercolor painting of a woman in an extravagant red dress riding a white horse\na watercolor painting of a w`（1 次）
- `["\\n", "\nfedor_bypass.safetensors\nkrea2_darkbrush.safetensors\nkrea2_depth_lrzjason.safetensors\nkrea2_dotmatrix.safe`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
