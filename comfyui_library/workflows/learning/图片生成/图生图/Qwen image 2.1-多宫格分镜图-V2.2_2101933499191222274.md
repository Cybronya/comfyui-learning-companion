---
key: 图片生成/图生图/Qwen image 2.1-多宫格分镜图-V2.2_2101933499191222274.json
name: Qwen image 2.1-多宫格分镜图-V2.2_2101933499191222274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1-多宫格分镜图-V2.2_2101933499191222274.json
hash: dfce843629e7bbf4
coverage: 0.84375
learned_at: 2026-10-10 20:48:08
nodes: [QwenImage21Cache, TextEncodeQwenImage21, ComfySwitchNode, KSampler, EmptyLatentImage, VAELoader, LoadImage, LoadImage, UNETLoader, CLIPLoader, UNETLoader, CLIPLoader, VAEDecode, ResolutionSelector, SaveImage, CLIPLoader, ZNGB_ImageBatchMulti, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, TextGenerateLTX2Prompt, StringConcatenate, RHLLMChatNode, PrimitiveStringMultiline, PrimitiveStringMultiline, easy showAnything, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1043280988992203, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen image 2.1-多宫格分镜图-V2.2_2101933499191222274.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1-多宫格分镜图-V2.2_2101933499191222274.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `ResolutionSelector`
- `SaveImage`
- `CLIPLoader`
- `ZNGB_ImageBatchMulti`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextGenerateLTX2Prompt`
- `StringConcatenate`
- `RHLLMChatNode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `easy showAnything`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `1043280988992203`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（27/32）

**有卡**：`QwenImage21Cache`、`TextEncodeQwenImage21`、`KSampler`、`EmptyLatentImage`、`VAELoader`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAEDecode`、`ResolutionSelector`、`SaveImage`、`ZNGB_ImageBatchMulti`、`TextGenerateLTX2Prompt`、`StringConcatenate`、`RHLLMChatNode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
