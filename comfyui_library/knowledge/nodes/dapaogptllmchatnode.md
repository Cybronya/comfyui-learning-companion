# DapaoGPTLLMChatNode

## 节点类型

`DapaoGPTLLMChatNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `🖼️ 图像1:IMAGE`（3 次）
- `🖼️ 图像2:IMAGE`（3 次）
- `🖼️ 图像3:IMAGE`（3 次）
- `🖼️ 图像4:IMAGE`（3 次）
- `🖼️ 图像5:IMAGE`（3 次）
- `🖼️ 图像6:IMAGE`（3 次）
- `🖼️ 图像7:IMAGE`（3 次）
- `🖼️ 图像8:IMAGE`（3 次）
- `🔑 API密钥:STRING`（3 次）
- `🤖 模型:COMBO`（3 次）

## 输出

- `💭 AI回复:STRING`（3 次）
- `📄 完整响应:STRING`（3 次）
- `ℹ️ 处理信息:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "gemini-3.7-flash", "你是“人物多视图提示词生成器”。你的任务是将用户的简短描述、参考图片及修改要求，转化为一份可直接用于图像生成的完整提示词。\n\n你的交付物是图像生成提示词，不是人物分析报告，也不是实际生`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
