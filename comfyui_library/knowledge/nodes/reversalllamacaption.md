# ReversalLlamaCaption

## 节点类型

`ReversalLlamaCaption`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `🖼️图像1:IMAGE`（1 次）
- `🖼️图像2:IMAGE`（1 次）
- `🖼️图像3:IMAGE`（1 次）
- `🖼️图像4:IMAGE`（1 次）
- `🖼️图像5:IMAGE`（1 次）
- `🖼️图像6:IMAGE`（1 次）
- `🖼️图像7:IMAGE`（1 次）
- `🖼️图像8:IMAGE`（1 次）
- `🎞️视频帧批次:IMAGE`（1 次）
- `🎛️反推额外选项:REVERSAL_CAPTION_OPTIONS`（1 次）

## 输出

- `反推文本:STRING`（1 次）
- `完整对话历史:STRING`（1 次）
- `使用的种子:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Qwen3.6-35B-A3B-Abliterated-Heretic-Q6_K.gguf", "Qwen3.5 / Qwen3.6｜图像+视频帧｜apache-2.0", "mmproj-Qwen3.6-35B-A3B-Uncenso`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
