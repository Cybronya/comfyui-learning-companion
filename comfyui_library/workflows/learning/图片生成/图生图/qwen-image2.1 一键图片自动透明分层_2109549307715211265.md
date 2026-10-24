---
key: 图片生成/图生图/qwen-image2.1 一键图片自动透明分层_2109549307715211265.json
name: qwen-image2.1 一键图片自动透明分层_2109549307715211265
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image2.1 一键图片自动透明分层_2109549307715211265.json
hash: e6502a3b25c73b07
coverage: 0.722222
learned_at: 2026-10-23 11:42:55
nodes: [CLIPLoader, KSampler, EmptyLatentImage, PrimitiveStringMultiline, UNETLoader, LoadImage, PrimitiveStringMultiline, ShowText|pysssss, VAELoader, VAEDecode, SaveImage, RHLLMChatNode, PrimitiveStringMultiline, ShowText|pysssss, easy promptLine, ResolutionSelector, QwenPERewriteT8, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "normal", "seed": 579567489072353, "steps": 25, "width": 1024}
---

# 图片生成/图生图/qwen-image2.1 一键图片自动透明分层_2109549307715211265.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image2.1 一键图片自动透明分层_2109549307715211265.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `CLIPLoader`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `LoadImage`
- `PrimitiveStringMultiline`
- `ShowText|pysssss`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `RHLLMChatNode`
- `PrimitiveStringMultiline`
- `ShowText|pysssss`
- `easy promptLine`
- `ResolutionSelector`
- `QwenPERewriteT8`
- `TextEncodeQwenImage21`

## 关键参数

- `seed` = `579567489072353`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **72%**（13/18）

**有卡**：`CLIPLoader`、`KSampler`、`EmptyLatentImage`、`UNETLoader`、`LoadImage`、`VAELoader`、`VAEDecode`、`SaveImage`、`RHLLMChatNode`、`easy promptLine`、`ResolutionSelector`、`QwenPERewriteT8`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
