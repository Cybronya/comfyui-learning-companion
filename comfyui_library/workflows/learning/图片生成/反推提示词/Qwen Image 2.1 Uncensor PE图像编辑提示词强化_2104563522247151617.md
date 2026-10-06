---
key: 图片生成/反推提示词/Qwen Image 2.1 Uncensor PE图像编辑提示词强化_2104563522247151617.json
name: Qwen Image 2.1 Uncensor PE图像编辑提示词强化_2104563522247151617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen Image 2.1 Uncensor PE图像编辑提示词强化_2104563522247151617.json
hash: 3125302d1230258a
coverage: 0.647059
learned_at: 2026-10-06 21:36:10
nodes: [PreviewAny, PreviewAny, LoadImage, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, QwenPERewriteT8, QwenPECanvasT8, PreviewAny, ShellAgentPluginOutputText]
patterns: []
missing: [QwenPECanvasT8, QwenPERewriteT8, PreviewAny, PreviewAny, PreviewAny, ShellAgentPluginOutputText]
discoveries: [次要节点 `QwenPECanvasT8` 知识库中没有该节点类型的任何知识, 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `ShellAgentPluginOutputText` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 图片生成/反推提示词/Qwen Image 2.1 Uncensor PE图像编辑提示词强化_2104563522247151617.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen Image 2.1 Uncensor PE图像编辑提示词强化_2104563522247151617.json`

## 结构

**生成流程**：Output → Other

**节点**（17 个）：
- `PreviewAny`
- `PreviewAny`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `QwenPERewriteT8`
- `QwenPECanvasT8`
- `PreviewAny`
- `ShellAgentPluginOutputText`

## 知识

覆盖率 **65%**（11/17）

**有卡**：`LoadImage`、`SaveImage`

**缺卡**（6）：`QwenPECanvasT8`、`QwenPERewriteT8`、`PreviewAny`、`PreviewAny`、`PreviewAny`、`ShellAgentPluginOutputText`

**用到的条目**：SaveImage、LoadImage、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 次要节点 `QwenPECanvasT8` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `ShellAgentPluginOutputText` 仅有 SaveImage 的通用知识，没有该节点自己的说明
