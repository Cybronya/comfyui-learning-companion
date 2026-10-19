# DapaoEcommercePromptGenerator

## 节点类型

`DapaoEcommercePromptGenerator`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `🖼️ 参考图1:IMAGE`（1 次）
- `🖼️ 参考图2:IMAGE`（1 次）
- `🖼️ 参考图3:IMAGE`（1 次）
- `🖼️ 参考图4:IMAGE`（1 次）
- `🌐 API地址:STRING`（1 次）
- `🔑 API密钥:STRING`（1 次）
- `🤖 模型名称:STRING`（1 次）
- `⚡ 全自动随机优化:BOOLEAN`（1 次）
- `✨ 随机优化（增强文字排版）:BOOLEAN`（1 次）
- `🛍️ 产品类型:STRING`（1 次）

## 输出

- `📜 提示词列表:STRING`（1 次）
- `🐞 调试信息:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["https://ai.t8star.cn/v1/chat/completions", "", "gemini-3-pro-preview", false, true, "牛角包", "外酥里嫩，唇齿留香", "科技感", "生活方式交互`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
