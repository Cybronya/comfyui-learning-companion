---
key: 图片生成/反推提示词/Qwen Image 2.1 PE提示词强化（T8节点版）_2102224088881258498.json
name: Qwen Image 2.1 PE提示词强化（T8节点版）_2102224088881258498
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen Image 2.1 PE提示词强化（T8节点版）_2102224088881258498.json
hash: dc5fbecbcc121e3a
coverage: 0.823529
learned_at: 2026-10-26 01:45:50
nodes: [PreviewAny, PreviewAny, QwenPECanvasT8, PreviewAny, ShellAgentPluginOutputText, QwenPERewriteT8, LoadImage, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/反推提示词/Qwen Image 2.1 PE提示词强化（T8节点版）_2102224088881258498.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen Image 2.1 PE提示词强化（T8节点版）_2102224088881258498.json`

## 结构

**生成流程**：Output → Other

**节点**（17 个）：
- `PreviewAny`
- `PreviewAny`
- `QwenPECanvasT8`
- `PreviewAny`
- `ShellAgentPluginOutputText`
- `QwenPERewriteT8`
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

## 知识

覆盖率 **82%**（14/17）

**有卡**：`QwenPECanvasT8`、`ShellAgentPluginOutputText`、`QwenPERewriteT8`、`LoadImage`、`SaveImage`

**用到的条目**：SaveImage、LoadImage、ShellAgentPluginOutputText、QwenPERewriteT8、QwenPECanvasT8、sd15-t2i-basic、sd15-t2i-lora、sd1_5_text2image_sampler_clip_checkpoint
