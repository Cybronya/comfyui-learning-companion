---
key: 图片生成/反推提示词/Qwen Image 2.1 Uncensor PE图像编辑提示词强化_2104563522247151617.json
name: Qwen Image 2.1 Uncensor PE图像编辑提示词强化_2104563522247151617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen Image 2.1 Uncensor PE图像编辑提示词强化_2104563522247151617.json
hash: 3125302d1230258a
coverage: 0.764706
learned_at: 2026-10-06 22:26:26
nodes: [PreviewAny, PreviewAny, LoadImage, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, QwenPERewriteT8, QwenPECanvasT8, PreviewAny, ShellAgentPluginOutputText]
patterns: []
missing: [QwenPECanvasT8]
discoveries: [次要节点 `QwenPECanvasT8` 知识库中没有该节点类型的任何知识]
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

覆盖率 **76%**（13/17）

**有卡**：`LoadImage`、`SaveImage`、`QwenPERewriteT8`、`ShellAgentPluginOutputText`

**缺卡**（1）：`QwenPECanvasT8`

**用到的条目**：SaveImage、LoadImage、ShellAgentPluginOutputText、QwenPERewriteT8、sd15-t2i-basic、sd15-t2i-lora、Text、CS_Preview_Any

## 学习发现

- 次要节点 `QwenPECanvasT8` 知识库中没有该节点类型的任何知识
