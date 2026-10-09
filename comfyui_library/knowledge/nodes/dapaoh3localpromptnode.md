# DapaoH3LocalPromptNode

## 节点类型

`DapaoH3LocalPromptNode`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `🧩 H3素材标记:DAPAO_H3_REFERENCES`（1 次）
- `🔗 外部文本输入:STRING`（1 次）
- `🎬 首帧图:IMAGE`（1 次）
- `🏁 尾帧图:IMAGE`（1 次）
- `🖼️ 参考图1:IMAGE`（1 次）
- `🖼️ 参考图2:IMAGE`（1 次）
- `🖼️ 参考图3:IMAGE`（1 次）
- `🖼️ 参考图4:IMAGE`（1 次）
- `🖼️ 参考图5:IMAGE`（1 次）
- `🖼️ 参考图6:IMAGE`（1 次）

## 输出

- `🎬 H3最终提示词:STRING`（1 次）
- `🎛️ 识别模式:STRING`（1 次）
- `📑 素材与制作分析:STRING`（1 次）
- `📄 LLM完整响应:STRING`（1 次）
- `ℹ️ 处理信息:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive-Q8_K_P.gguf", "Qwen3.5", "mmproj-Qwen3.6-35B-A3B-Uncensored-HauhauCS-Ag`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
