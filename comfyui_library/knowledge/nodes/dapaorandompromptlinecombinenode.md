# DapaoRandomPromptLineCombineNode

## 节点类型

`DapaoRandomPromptLineCombineNode`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `🧰 字符串预处理:COMBO`（2 次）
- `🔢 提取行数:INT`（2 次）
- `🎲 随机种子:INT`（2 次）
- `📝 提示词行1:STRING`（2 次）
- `📝 提示词行2:STRING`（2 次）
- `📝 提示词行3:STRING`（2 次）
- `📝 提示词行4:STRING`（2 次）
- `📝 提示词行5:STRING`（2 次）
- `📝 提示词行6:STRING`（2 次）
- `📝 提示词行7:STRING`（2 次）

## 输出

- `📝 提示词:STRING`（2 次）
- `🔢 字数:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["不改变", 4, 0, "", "", "", "", "", "", "", "", "", ""]`（1 次）
- `["不改变", 1, 0, "", "", "", "", "", "", "", "", "", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
