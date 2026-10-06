---
key: 图片生成/反推提示词/Qwen Image 2.1 Uncensor PE图像编辑提示词强化_2104563522247151617.json
name: Qwen Image 2.1 Uncensor PE图像编辑提示词强化_2104563522247151617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen Image 2.1 Uncensor PE图像编辑提示词强化_2104563522247151617.json
hash: 3125302d1230258a
coverage: 0.823529
learned_at: 2026-10-07 02:40:58
nodes: [PreviewAny, PreviewAny, LoadImage, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, QwenPERewriteT8, QwenPECanvasT8, PreviewAny, ShellAgentPluginOutputText]
patterns: []
missing: []
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

覆盖率 **82%**（14/17）

**有卡**：`LoadImage`、`SaveImage`、`QwenPERewriteT8`、`QwenPECanvasT8`、`ShellAgentPluginOutputText`

**用到的条目**：SaveImage、LoadImage、ShellAgentPluginOutputText、QwenPERewriteT8、QwenPECanvasT8、sd15-t2i-basic、sd15-t2i-lora、Text
