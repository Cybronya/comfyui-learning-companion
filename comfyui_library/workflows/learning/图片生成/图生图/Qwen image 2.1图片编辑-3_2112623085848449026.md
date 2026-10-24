---
key: 图片生成/图生图/Qwen image 2.1图片编辑-3_2112623085848449026.json
name: Qwen image 2.1图片编辑-3_2112623085848449026
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图片编辑-3_2112623085848449026.json
hash: f6ab74af510e07f8
coverage: 0.730769
learned_at: 2026-10-23 11:14:03
nodes: [PathchSageAttentionKJ, CLIPLoader, VAELoader, VAEDecode, Any Switch (rgthree), SaveImage, UNETLoader, QwenImage21Cache, ShowText|pysssss, QwenPERewriteT8, MarkdownNote, TextEncodeQwenImage21, EmptyLatentImage, StringToInt, StringToInt, PrimitiveString, KSampler, StringToInt, PrimitiveString, LoadImage, LoadImage, LoadImage, PrimitiveString, CR Prompt Text, StringToInt, PrimitiveString]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 698887996065466, "steps": 40, "width": 16}
---

# 图片生成/图生图/Qwen image 2.1图片编辑-3_2112623085848449026.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图片编辑-3_2112623085848449026.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（26 个）：
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
- `MarkdownNote`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `StringToInt`
- `StringToInt`
- `PrimitiveString`
- `KSampler` ★核心
- `StringToInt`
- `PrimitiveString`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveString`
- `CR Prompt Text`
- `StringToInt`
- `PrimitiveString`

## 关键参数

- `width` = `16`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `698887996065466`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（19/26）

**有卡**：`PathchSageAttentionKJ`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`SaveImage`、`UNETLoader`、`QwenImage21Cache`、`QwenPERewriteT8`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`StringToInt`、`KSampler`、`LoadImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
