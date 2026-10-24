# DapaoRHBatchLLMPromptNode

## 节点类型

`DapaoRHBatchLLMPromptNode`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `🖼️ A组图像:IMAGE`（1 次）
- `🖼️ B组图像:IMAGE`（1 次）
- `🖼️ C组图像:IMAGE`（1 次）
- `🖼️ D组图像:IMAGE`（1 次）
- `🔑 API密钥:STRING`（1 次）
- `🤖 模型ID:COMBO`（1 次）
- `🎯 系统角色:STRING`（1 次）
- `🧾 元指令:STRING`（1 次）
- `📂 A组文件夹:STRING`（1 次）
- `📂 B组文件夹:STRING`（1 次）

## 输出

- `📝 提示词列表:STRING`（1 次）
- `📄 完整响应:STRING`（1 次）
- `ℹ️ 处理信息:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["d05e790a457a4f42981f1d67f7fb162f", "google/gemini-3.5-flash", "", "你是一位精通电商3D服装视觉规范与图像重绘（Image-to-Image）提示词工程的专家。你的任务是`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
