# TE_prompt_text

## 节点类型

`TE_prompt_text`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `text:STRING`（1 次）
- `reference_labels:STRING`（1 次）

## 输出

- `text:STRING`（1 次）
- `H3参考素材:TE_H3_REFERENCES`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["两人一起走在喧闹的古代集市中，<Picture 2> 人物说：我们去吃点东西吧。<Picture 1> 人物说：好啊，我记得前面有家包子铺。", "", "两人一起走在喧闹的古代集市中，<Picture 2> 人物说：我们去吃点东西吧。`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
