---
key: 图片生成/文生图/一致性9宫格文生图+Qwen2.5自动反推提示词+平替Nano_2000228200649289729.json
name: 一致性9宫格文生图+Qwen2.5自动反推提示词+平替Nano_2000228200649289729
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/一致性9宫格文生图+Qwen2.5自动反推提示词+平替Nano_2000228200649289729.json
hash: 55d96cc5bc82b887
coverage: 0.822222
learned_at: 2026-10-19 21:47:28
nodes: [SamplerCustomAdvanced, RandomNoise, FluxGuidance, EmptyLatentImage, BasicScheduler, KSamplerSelect, BasicGuider, VAELoader, CR Prompt Text, ShowText|pysssss, Note, PathchSageAttentionKJ, ModelSamplingSD3, Anything Everywhere, CLIPTextEncode, VAEDecode, VAEDecode, ConstrainImage|pysssss, Image Comparer (rgthree), KSampler, LoadImage, Qwen2.5VL, DualCLIPLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, Joy_caption_two, VAEEncode, CLIPTextEncode, CLIPLoader, VAELoader, Joy_caption_two_load, Anything Everywhere3, Lora Loader Stack (rgthree), CLIPTextEncode, SaveImage, CR Text Concatenate, PreviewAny, Text Multiline, RH_Translator, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.45, "height": 1536, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 903785502369369, "steps": 20, "width": 1024}
---

# 图片生成/文生图/一致性9宫格文生图+Qwen2.5自动反推提示词+平替Nano_2000228200649289729.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/一致性9宫格文生图+Qwen2.5自动反推提示词+平替Nano_2000228200649289729.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `FluxGuidance`
- `EmptyLatentImage` ★核心
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `VAELoader`
- `CR Prompt Text`
- `ShowText|pysssss`
- `Note`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `Anything Everywhere`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ConstrainImage|pysssss`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `LoadImage`
- `Qwen2.5VL`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `Joy_caption_two`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Joy_caption_two_load`
- `Anything Everywhere3`
- `Lora Loader Stack (rgthree)`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `CR Text Concatenate`
- `PreviewAny`
- `Text Multiline`
- `RH_Translator`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `903785502369369`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `0.45`

## 知识

覆盖率 **82%**（37/45）

**有卡**：`SamplerCustomAdvanced`、`RandomNoise`、`FluxGuidance`、`EmptyLatentImage`、`BasicScheduler`、`KSamplerSelect`、`BasicGuider`、`VAELoader`、`CR Prompt Text`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAEDecode`、`ConstrainImage|pysssss`、`KSampler`、`LoadImage`、`Qwen2.5VL`、`DualCLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`Joy_caption_two`、`VAEEncode`、`CLIPLoader`、`Joy_caption_two_load`、`Lora Loader Stack (rgthree)`、`SaveImage`、`CR Text Concatenate`、`Text Multiline`、`RH_Translator`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage
