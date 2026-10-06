# Qwen3VL_Chat

## 节点类型

`Qwen3VL_Chat`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `🖼️ 图像1:IMAGE`（4 次）
- `🖼️ 图像2:IMAGE`（4 次）
- `🖼️ 图像3:IMAGE`（4 次）
- `🖼️ 图像4:IMAGE`（4 次）
- `🎯 Qwen3VL额外选项:QWEN3VL_EXTRA_OPTIONS`（4 次）
- `🤖 模型选择:COMBO`（4 次）
- `⚙️ 量化级别:COMBO`（4 次）
- `🧠 注意力模式:COMBO`（4 次）
- `🖼️ 最大长边:INT`（4 次）
- `💬 用户输入:STRING`（4 次）

## 输出

- `AI回复:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Qwen3-VL-4B-Instruct", "None (FP16)", "SDPA", 768, "", "你是一个专业、友好且乐于助人的AI助手。", 0.7, 0.9, 1024, 42, "固定", false, false,`（3 次）
- `["Qwen3-VL-8B-Instruct", "None (FP16)", "SDPA", 768, "你好，请介绍一下你自己。", "你是一个专业、友好且乐于助人的AI助手。", 0.7, 0.9, 1024, -1, "随机", f`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
