# StringFunction|pysssss

## 节点类型

`StringFunction|pysssss`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 9 个 workflow 中。

## 输入

- `action:COMBO`（9 次）
- `tidy_tags:COMBO`（9 次）
- `text_a:STRING`（9 次）
- `text_b:STRING`（9 次）
- `text_c:STRING`（9 次）

## 输出

- `STRING:STRING`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["replace", "no", "", "/(?:[\\s\\S]*?<\\/think>\\s*)|(?:[\\s\\S]*?\"rewritten_prompt\"\\s*:\\s*\"([\\s\\S]*?)\"\\s*,\\s*`（3 次）
- `["replace", "no", "", "/^[\\s\\S]*?<\\/think>\\s*/", ""]`（2 次）
- `["append", "yes", "", "", ""]`（2 次）
- `["append", "yes", "", "", "", "参考图片的人物和场景，帮我生成不同运镜和角度，不同的视角和景别，保持人物一致性不变, 分镜数量： 6"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
