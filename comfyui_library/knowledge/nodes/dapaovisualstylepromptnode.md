# DapaoVisualStylePromptNode

## 节点类型

`DapaoVisualStylePromptNode`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `🖼️ 用户参考图1:IMAGE`（1 次）
- `🖼️ 用户参考图2:IMAGE`（1 次）
- `🖼️ 用户参考图3:IMAGE`（1 次）
- `🖼️ 用户参考图4:IMAGE`（1 次）
- `🖼️ 用户参考图5:IMAGE`（1 次）
- `🖼️ 用户参考图6:IMAGE`（1 次）
- `🖼️ 用户参考图7:IMAGE`（1 次）
- `🖼️ 用户参考图8:IMAGE`（1 次）
- `🖼️ 用户参考图9:IMAGE`（1 次）
- `🔑 API密钥:STRING`（1 次）

## 输出

- `🎨 最终图像提示词:STRING`（1 次）
- `🇨🇳 中文提示词:STRING`（1 次）
- `🇬🇧 英文提示词:STRING`（1 次）
- `🧬 Creative Spec视觉规范:STRING`（1 次）
- `🔎 检索参考报告:STRING`（1 次）
- `🃏 使用风格卡:STRING`（1 次）
- `ℹ️ 最终处理信息:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "gemini-3.7-flash", "", "自动判断", "", false, 2, "自动选择", "", "自动判断", "", "自动", "通用图像模型", "英文（推荐）", true, "自动识别", "", "`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
