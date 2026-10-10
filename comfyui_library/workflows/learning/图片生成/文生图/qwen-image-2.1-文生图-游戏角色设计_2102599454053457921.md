---
key: qwen-image-2.1-文生图-游戏角色设计_2102599454053457921.json
name: qwen-image-2.1-文生图-游戏角色设计_2102599454053457921
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image-2.1-文生图-游戏角色设计_2102599454053457921.json
hash: 30df76452dd36c50
coverage: 0.823529
learned_at: 2026-10-10 20:59:24
nodes: [QwenImage21Cache, CLIPLoader, SamplerCustomAdvanced, KSamplerSelect, BasicGuider, VAELoader, ReferenceLatent, CLIPLoader, VAEDecode, VAEEncode, UNETLoader, TextGenerateLTX2Prompt, KSampler, RandomNoise, SaveImage, VAEDecode, PreviewImage, PreviewImage, CLIPTextEncode, VAELoader, BasicScheduler, ResolutionSelector, easy positive, Seed (rgthree), easy showAnything, CLIPLoader, TextEncodeQwenImage21, EmptyLatentImage, ImageScaleToTotalPixelsX, UNETLoader, ColorMatchV2, VOSR2ModelLoader, VOSR2Upscale, PreviewImage]
patterns: [text_to_image]
missing: [easy positive, Seed (rgthree)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 486426918943366, "steps": 25, "width": 1024}
discoveries: [次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# qwen-image-2.1-文生图-游戏角色设计_2102599454053457921.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image-2.1-文生图-游戏角色设计_2102599454053457921.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `QwenImage21Cache`
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `VAELoader`
- `ReferenceLatent`
- `CLIPLoader`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `TextGenerateLTX2Prompt`
- `KSampler` ★核心
- `RandomNoise`
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `BasicScheduler`
- `ResolutionSelector`
- `easy positive`
- `Seed (rgthree)`
- `easy showAnything`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ImageScaleToTotalPixelsX`
- `UNETLoader` ★核心
- `ColorMatchV2`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `486426918943366`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（28/34）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicGuider`、`VAELoader`、`ReferenceLatent`、`VAEDecode`、`VAEEncode`、`UNETLoader`、`TextGenerateLTX2Prompt`、`KSampler`、`RandomNoise`、`SaveImage`、`CLIPTextEncode`、`BasicScheduler`、`ResolutionSelector`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`ImageScaleToTotalPixelsX`、`ColorMatchV2`、`VOSR2ModelLoader`、`VOSR2Upscale`

**缺卡**（2）：`easy positive`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 学习发现

- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
