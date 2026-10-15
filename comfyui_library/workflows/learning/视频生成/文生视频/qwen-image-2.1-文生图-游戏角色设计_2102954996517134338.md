---
key: 视频生成/文生视频/qwen-image-2.1-文生图-游戏角色设计_2102954996517134338.json
name: qwen-image-2.1-文生图-游戏角色设计_2102954996517134338
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/qwen-image-2.1-文生图-游戏角色设计_2102954996517134338.json
hash: ae5ed20ada502170
coverage: 0.861111
learned_at: 2026-10-15 22:47:30
nodes: [QwenImage21Cache, CLIPLoader, SamplerCustomAdvanced, KSamplerSelect, BasicGuider, VAELoader, ReferenceLatent, UNETLoader, VAELoader, CLIPLoader, VAEDecode, VAEEncode, UNETLoader, VOSR2ModelLoader, BasicScheduler, TextEncodeQwenImage21, ImageScaleToTotalPixelsX, TextGenerateLTX2Prompt, KSampler, RandomNoise, ResolutionSelector, SaveImage, VOSR2Upscale, VAEDecode, ColorMatchV2, PreviewImage, PreviewImage, PreviewImage, CLIPLoader, easy showAnything, CLIPTextEncode, Seed (rgthree), easy positive, EmptyLatentImage, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 335670621579502, "steps": 25, "width": 1024}
---

# 视频生成/文生视频/qwen-image-2.1-文生图-游戏角色设计_2102954996517134338.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/qwen-image-2.1-文生图-游戏角色设计_2102954996517134338.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `QwenImage21Cache`
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `VAELoader`
- `ReferenceLatent`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `VOSR2ModelLoader`
- `BasicScheduler`
- `TextEncodeQwenImage21`
- `ImageScaleToTotalPixelsX`
- `TextGenerateLTX2Prompt`
- `KSampler` ★核心
- `RandomNoise`
- `ResolutionSelector`
- `SaveImage`
- `VOSR2Upscale`
- `VAEDecode` ★核心
- `ColorMatchV2`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `CLIPLoader`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
- `easy positive`
- `EmptyLatentImage` ★核心
- `EmptyImage`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `335670621579502`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（31/36）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicGuider`、`VAELoader`、`ReferenceLatent`、`UNETLoader`、`VAEDecode`、`VAEEncode`、`VOSR2ModelLoader`、`BasicScheduler`、`TextEncodeQwenImage21`、`ImageScaleToTotalPixelsX`、`TextGenerateLTX2Prompt`、`KSampler`、`RandomNoise`、`ResolutionSelector`、`SaveImage`、`VOSR2Upscale`、`ColorMatchV2`、`CLIPTextEncode`、`Seed (rgthree)`、`easy positive`、`EmptyLatentImage`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector
