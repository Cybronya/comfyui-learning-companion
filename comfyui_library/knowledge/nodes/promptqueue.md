# PromptQueue

## 节点类型

`PromptQueue`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `prompts:STRING`（1 次）
- `prompts_json:STRING`（1 次）
- `index:INT`（1 次）

## 输出

- `prompt:STRING`（1 次）
- `index:INT`（1 次）
- `total:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["[\"3d风格, 极致画质, 8k超清, BJDDARK1，一位黑发少女，身着红白相间的洛丽塔风格圣诞女仆装，裙摆蓬松，白色长筒袜，头戴红色绒球发饰，脚穿红色高跟鞋，站立于中式廊桥之上，背景为传统彩绘木结构廊道，远处可见水面与建筑，阳光`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
