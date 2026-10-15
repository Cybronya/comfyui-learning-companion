---
key: 图片生成/文生图/FLUX 1.D_基础文生图-优化速度_1907284499745366017.json
name: FLUX 1.D_基础文生图-优化速度_1907284499745366017
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX 1.D_基础文生图-优化速度_1907284499745366017.json
hash: 3a716a60c503e213
coverage: 0.944444
learned_at: 2026-10-15 22:26:16
nodes: [BasicGuider, FluxGuidance, SamplerCustomAdvanced, RandomNoise, VAELoader, EmptyLatentImage, Text Multiline, SiliconflowLLM, easy showAnything, ArtGallery_Zho, easy seed, easy promptConcat, KSamplerSelect, BasicScheduler, SaveImage, Node Collector (rgthree), Node Combiner (rgthree), easy showAnything, Text Multiline, DifferentialDiffusion, Fast Bypasser (rgthree), easy seed, ChinesePrompt_Mix, Int, Int, LoraLoader, CFGZeroStarAndInit, VAEDecode, easy cleanGpuUsed, CLIPTextEncode, DualCLIPLoader, UNETLoader, CFGZeroStarAndInit, ApplyFBCacheOnModel, Text Multiline, Text Multiline]
patterns: [lora]
missing: []
parameters: {"batch_size": 3, "height": 512, "lora_name": "F.1-Ghibli Characters-吉卜力动漫人物_F.1-吉卜力人物-V1.0.safetensors", "strength_clip": 1, "strength_model": 1.0000000000000002, "width": 512}
---

# 图片生成/文生图/FLUX 1.D_基础文生图-优化速度_1907284499745366017.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX 1.D_基础文生图-优化速度_1907284499745366017.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（36 个）：
- `BasicGuider`
- `FluxGuidance`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `Text Multiline`
- `SiliconflowLLM`
- `easy showAnything`
- `ArtGallery_Zho`
- `easy seed`
- `easy promptConcat`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SaveImage`
- `Node Collector (rgthree)`
- `Node Combiner (rgthree)`
- `easy showAnything`
- `Text Multiline`
- `DifferentialDiffusion`
- `Fast Bypasser (rgthree)`
- `easy seed`
- `ChinesePrompt_Mix`
- `Int`
- `Int`
- `LoraLoader` ★核心
- `CFGZeroStarAndInit`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `CFGZeroStarAndInit`
- `ApplyFBCacheOnModel`
- `Text Multiline`
- `Text Multiline`

**识别到的模式**：lora

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `3`
- `lora_name` = `F.1-Ghibli Characters-吉卜力动漫人物_F.1-吉卜力人物-V1.0.safetensors`
- `strength_model` = `1.0000000000000002`
- `strength_clip` = `1`

## 知识

覆盖率 **94%**（34/36）

**有卡**：`BasicGuider`、`FluxGuidance`、`SamplerCustomAdvanced`、`RandomNoise`、`VAELoader`、`EmptyLatentImage`、`Text Multiline`、`SiliconflowLLM`、`ArtGallery_Zho`、`easy seed`、`easy promptConcat`、`KSamplerSelect`、`BasicScheduler`、`SaveImage`、`Node Collector (rgthree)`、`Node Combiner (rgthree)`、`DifferentialDiffusion`、`Fast Bypasser (rgthree)`、`ChinesePrompt_Mix`、`Int`、`LoraLoader`、`CFGZeroStarAndInit`、`VAEDecode`、`easy cleanGpuUsed`、`CLIPTextEncode`、`DualCLIPLoader`、`UNETLoader`、`ApplyFBCacheOnModel`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
