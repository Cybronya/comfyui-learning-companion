---
key: 图片生成/文生图/Qwen Image 2.1 PE 文生图（优化版）_2102388624821153793.json
name: Qwen Image 2.1 PE 文生图（优化版）_2102388624821153793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 PE 文生图（优化版）_2102388624821153793.json
hash: 424ec775d6950799
coverage: 0.714286
learned_at: 2026-10-20 01:50:51
nodes: [TextEncodeQwenImage21, KSampler, VAEDecode, PreviewAny, PreviewAny, PreviewAny, CLIPLoader, UNETLoader, VAELoader, QwenPECanvasT8, MarkdownNote, QwenPERewriteT8, QwenImage21Cache, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 459135892154888, "steps": 25}
---

# 图片生成/文生图/Qwen Image 2.1 PE 文生图（优化版）_2102388624821153793.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 PE 文生图（优化版）_2102388624821153793.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewAny`
- `PreviewAny`
- `PreviewAny`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `QwenPECanvasT8`
- `MarkdownNote`
- `QwenPERewriteT8`
- `QwenImage21Cache`
- `SaveImage`

## 关键参数

- `seed` = `459135892154888`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（10/14）

**有卡**：`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`QwenPECanvasT8`、`QwenPERewriteT8`、`QwenImage21Cache`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、QwenImage21Cache、UNETLoader、SaveImage
