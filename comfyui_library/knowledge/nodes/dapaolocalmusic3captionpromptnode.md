# DapaoLocalMusic3CaptionPromptNode

## 节点类型

`DapaoLocalMusic3CaptionPromptNode`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `🔗 外部音乐需求:STRING`（1 次）
- `🔗 外部歌词:STRING`（1 次）
- `🤖本地模型文件:COMBO`（1 次）
- `🔌本地对话处理器:COMBO`（1 次）
- `🖼️本地mmproj文件:COMBO`（1 次）
- `📐本地上下文长度:INT`（1 次）
- `💾本地显存限制(GB):FLOAT`（1 次）
- `🔢图像最小token:INT`（1 次）
- `🔢图像最大token:INT`（1 次）
- `🧠本地思考模式:BOOLEAN`（1 次）

## 输出

- `🎼 音乐描述:STRING`（1 次）
- `📝 歌词:STRING`（1 次）
- `🌐 全局音乐信息:STRING`（1 次）
- `🎙️ 人声细节:STRING`（1 次）
- `🧱 编曲结构:STRING`（1 次）
- `📑 音乐结构分析:STRING`（1 次）
- `📄 语言模型完整响应:STRING`（1 次）
- `ℹ️ 处理信息:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Qwen3.5-27B-heretic.Q8_0.gguf", "Qwen3.5", "Qwen3.5-27B-heretic.mmproj-f16.gguf", 8192, -1, 256, 1344, false, "关闭", "温`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
