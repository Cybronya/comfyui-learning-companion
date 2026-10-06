# SeaArtAppendPrompt

## 节点类型

`SeaArtAppendPrompt`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `charactor_prompt:STRING`（8 次）
- `prompt:STRING`（8 次）

## 输出

- `STRING:STRING`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "在繁华的街上,商店门牌上写着\"快手很牛\"的中文字"]`（5 次）
- `["", "城堡里，正凝望着窗外的星空,墙上写着\"快手很牛\"中文字"]`（1 次）
- `["", "穿过森林，越过山丘，来到了一片神秘的花园"]`（1 次）
- `["", "月光洒在宁静的湖面上，银色的波光粼粼"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
