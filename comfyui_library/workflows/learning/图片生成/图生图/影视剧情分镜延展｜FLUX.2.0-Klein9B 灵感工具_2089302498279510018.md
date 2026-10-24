---
key: 图片生成/图生图/影视剧情分镜延展｜FLUX.2.0-Klein9B 灵感工具_2089302498279510018.json
name: 影视剧情分镜延展｜FLUX.2.0-Klein9B 灵感工具_2089302498279510018
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/影视剧情分镜延展｜FLUX.2.0-Klein9B 灵感工具_2089302498279510018.json
hash: 4570047113ba543a
coverage: 0.898305
learned_at: 2026-10-23 12:51:47
nodes: [Anything Everywhere3, CLIPLoader, VAELoader, UNETLoader, easy getNode, SaveImage, CLIPTextEncode, ReferenceLatent, ReferenceLatent, CLIPTextEncode, easy promptLine, VAEEncode, SamplerCustomAdvanced, CFGGuider, RandomNoise, KSamplerSelect, VAEDecode, easy setNode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, Text Multiline, JWStringConcat, Qwen3_VQA, INTConstant, INTConstant, LoadImage, CR Prompt Text, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/影视剧情分镜延展｜FLUX.2.0-Klein9B 灵感工具_2089302498279510018.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/影视剧情分镜延展｜FLUX.2.0-Klein9B 灵感工具_2089302498279510018.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `Anything Everywhere3`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `easy getNode`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `easy promptLine`
- `VAEEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `easy setNode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `Text Multiline`
- `JWStringConcat`
- `Qwen3_VQA`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `CR Prompt Text`
- `孤海注释`
- `孤海注释`
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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image、image_to_image

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

覆盖率 **90%**（53/59）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`easy getNode`、`SaveImage`、`CLIPTextEncode`、`ReferenceLatent`、`easy promptLine`、`VAEEncode`、`SamplerCustomAdvanced`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`VAEDecode`、`easy setNode`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`GetImageSize`、`LayerUtility: ImageScaleByAspectRatio V2`、`Text Multiline`、`JWStringConcat`、`Qwen3_VQA`、`INTConstant`、`LoadImage`、`CR Prompt Text`、`LoraLoaderModelOnly`、`KSampler`、`solarL_SaveImagesToZip`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
