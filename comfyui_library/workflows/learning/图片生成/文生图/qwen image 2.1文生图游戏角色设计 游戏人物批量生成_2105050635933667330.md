---
key: 图片生成/文生图/qwen image 2.1文生图游戏角色设计 游戏人物批量生成_2105050635933667330.json
name: qwen image 2.1文生图游戏角色设计 游戏人物批量生成_2105050635933667330
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen image 2.1文生图游戏角色设计 游戏人物批量生成_2105050635933667330.json
hash: 03f80ecf333a65af
coverage: 0.84127
learned_at: 2026-10-07 02:21:29
nodes: [QwenImage21Cache, CLIPLoader, SamplerCustomAdvanced, KSamplerSelect, BasicGuider, VAELoader, ReferenceLatent, CLIPLoader, VAEDecode, VAEEncode, UNETLoader, TextGenerateLTX2Prompt, KSampler, RandomNoise, SaveImage, VAEDecode, PreviewImage, PreviewImage, CLIPTextEncode, VAELoader, BasicScheduler, ResolutionSelector, easy positive, Seed (rgthree), easy showAnything, CLIPLoader, TextEncodeQwenImage21, EmptyLatentImage, ImageScaleToTotalPixelsX, UNETLoader, ColorMatchV2, VOSR2ModelLoader, VOSR2Upscale, PreviewImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [easy positive, Seed (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/qwen image 2.1文生图游戏角色设计 游戏人物批量生成_2105050635933667330.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen image 2.1文生图游戏角色设计 游戏人物批量生成_2105050635933667330.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
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
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（53/63）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicGuider`、`VAELoader`、`ReferenceLatent`、`VAEDecode`、`VAEEncode`、`UNETLoader`、`TextGenerateLTX2Prompt`、`KSampler`、`RandomNoise`、`SaveImage`、`CLIPTextEncode`、`BasicScheduler`、`ResolutionSelector`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`ImageScaleToTotalPixelsX`、`ColorMatchV2`、`VOSR2ModelLoader`、`VOSR2Upscale`、`LoraLoaderModelOnly`、`solarL_SaveImagesToZip`

**缺卡**（2）：`easy positive`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
