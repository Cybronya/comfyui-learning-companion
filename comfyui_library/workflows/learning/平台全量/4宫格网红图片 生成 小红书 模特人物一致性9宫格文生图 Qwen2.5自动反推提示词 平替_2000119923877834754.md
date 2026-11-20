---
key: 平台全量/4宫格网红图片 生成 小红书 模特人物一致性9宫格文生图 Qwen2.5自动反推提示词 平替_2000119923877834754.json
name: 4宫格网红图片 生成 小红书 模特人物一致性9宫格文生图 Qwen2.5自动反推提示词 平替_2000119923877834754
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/4宫格网红图片 生成 小红书 模特人物一致性9宫格文生图 Qwen2.5自动反推提示词 平替_2000119923877834754.json
hash: f6c82dc94dcc0a95
coverage: 0.818182
learned_at: 2026-11-14 00:13:26
nodes: [SamplerCustomAdvanced, RandomNoise, FluxGuidance, EmptyLatentImage, BasicScheduler, KSamplerSelect, BasicGuider, VAELoader, CR Prompt Text, Fast Groups Bypasser (rgthree), ShowText|pysssss, Fast Groups Bypasser (rgthree), Note, PathchSageAttentionKJ, ModelSamplingSD3, Anything Everywhere, CLIPTextEncode, VAEDecode, VAEDecode, ConstrainImage|pysssss, Image Comparer (rgthree), KSampler, LoadImage, Qwen2.5VL, DualCLIPLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, Joy_caption_two, VAEEncode, CLIPTextEncode, CLIPLoader, VAELoader, Joy_caption_two_load, Anything Everywhere3, Lora Loader Stack (rgthree), CLIPTextEncode, SaveImage, CR Text Concatenate, PreviewAny, Text Multiline, RH_Translator]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.45, "height": 1536, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 769995727230874, "steps": 20, "width": 1024}
---

# 平台全量/4宫格网红图片 生成 小红书 模特人物一致性9宫格文生图 Qwen2.5自动反推提示词 平替_2000119923877834754.json

> 来源文件 `comfyui_library/workflows/平台全量/4宫格网红图片 生成 小红书 模特人物一致性9宫格文生图 Qwen2.5自动反推提示词 平替_2000119923877834754.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `FluxGuidance`
- `EmptyLatentImage` ★核心
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `VAELoader`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `ShowText|pysssss`
- `Fast Groups Bypasser (rgthree)`
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

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `769995727230874`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `0.45`

## 知识

覆盖率 **82%**（36/44）

**有卡**：`SamplerCustomAdvanced`、`RandomNoise`、`FluxGuidance`、`EmptyLatentImage`、`BasicScheduler`、`KSamplerSelect`、`BasicGuider`、`VAELoader`、`CR Prompt Text`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAEDecode`、`ConstrainImage|pysssss`、`KSampler`、`LoadImage`、`Qwen2.5VL`、`DualCLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`Joy_caption_two`、`VAEEncode`、`CLIPLoader`、`Joy_caption_two_load`、`Lora Loader Stack (rgthree)`、`SaveImage`、`CR Text Concatenate`、`Text Multiline`、`RH_Translator`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、EmptyLatentImage
