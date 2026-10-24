---
key: 图片生成/图生图/Qwen image 2.1图片编辑-2_2112555622364438530.json
name: Qwen image 2.1图片编辑-2_2112555622364438530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图片编辑-2_2112555622364438530.json
hash: 0ff3c3d3a8732f60
coverage: 0.72
learned_at: 2026-10-23 11:14:02
nodes: [PathchSageAttentionKJ, CLIPLoader, VAELoader, VAEDecode, Any Switch (rgthree), SaveImage, UNETLoader, QwenImage21Cache, ShowText|pysssss, QwenPERewriteT8, LoadImage, LoadImage, MarkdownNote, CR Prompt Text, TextEncodeQwenImage21, EmptyLatentImage, PrimitiveString, StringToInt, StringToInt, PrimitiveString, KSampler, StringToInt, PrimitiveString, StringToInt, PrimitiveString]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 845250527012946, "steps": 40, "width": 16}
---

# 图片生成/图生图/Qwen image 2.1图片编辑-2_2112555622364438530.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图片编辑-2_2112555622364438530.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（25 个）：
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `Any Switch (rgthree)`
- `SaveImage`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `ShowText|pysssss`
- `QwenPERewriteT8`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `CR Prompt Text`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `PrimitiveString`
- `StringToInt`
- `StringToInt`
- `PrimitiveString`
- `KSampler` ★核心
- `StringToInt`
- `PrimitiveString`
- `StringToInt`
- `PrimitiveString`

## 关键参数

- `width` = `16`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `845250527012946`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **72%**（18/25）

**有卡**：`PathchSageAttentionKJ`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`SaveImage`、`UNETLoader`、`QwenImage21Cache`、`QwenPERewriteT8`、`LoadImage`、`CR Prompt Text`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`StringToInt`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
