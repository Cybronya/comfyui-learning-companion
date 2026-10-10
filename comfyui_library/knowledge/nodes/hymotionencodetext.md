# HYMotionEncodeText

## 节点类型

`HYMotionEncodeText`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `llm:HYMOTION_LLM`（4 次）
- `text:STRING`（4 次）

## 输出

- `conditioning:HYMOTION_COND`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[""]`（2 次）
- `["The person leaped repeatedly, then rolled forward and drew the sword\n"]`（1 次）
- `["The player received the ball with his back near the baseline, dribbled and backed down his defender twice. Suddenly, h`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
