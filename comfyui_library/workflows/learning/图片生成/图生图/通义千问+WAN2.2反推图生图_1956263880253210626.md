---
key: 图片生成/图生图/通义千问+WAN2.2反推图生图_1956263880253210626.json
name: 通义千问+WAN2.2反推图生图_1956263880253210626
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/通义千问+WAN2.2反推图生图_1956263880253210626.json
hash: 7db08b19ecc5dea9
coverage: 0.869565
learned_at: 2026-10-23 13:30:34
nodes: [UNETLoader, ConditioningZeroOut, ShowText|pysssss, CLIPLoader, ModelSamplingAuraFlow, PreviewImage, Image Comparer (rgthree), UNETLoader, CLIPTextEncode, VAEEncode, SaveImage, easy cleanGpuUsed, LoraLoaderModelOnly, VAELoader, ImageConcatMulti, RandomNoise, SplitSigmas, SamplerCustomAdvanced, DisableNoise, SamplerCustomAdvanced, ModelSamplingSD3, KSamplerSelect, CLIPTextEncode, Image Comparer (rgthree), RH_Captioner, WanVideoNAG, CFGGuider, PreviewImage, CLIPLoader, CLIPTextEncode, CLIPTextEncode, PreviewImage, UpscaleModelLoader, SDXLPromptStyler, VAELoader, KSampler, CLIPTextEncode, EmptyLatentImage, VAEDecode, UltimateSDUpscale, RH_Captioner, easy cleanGpuUsed, VAEDecode, easy cleanGpuUsed, LoadImage, BasicScheduler]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 976354092755445, "steps": 30, "width": 768}
---

# 图片生成/图生图/通义千问+WAN2.2反推图生图_1956263880253210626.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/通义千问+WAN2.2反推图生图_1956263880253210626.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `ShowText|pysssss`
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `SaveImage`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `ImageConcatMulti`
- `RandomNoise`
- `SplitSigmas`
- `SamplerCustomAdvanced` ★核心
- `DisableNoise`
- `SamplerCustomAdvanced` ★核心
- `ModelSamplingSD3`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `RH_Captioner`
- `WanVideoNAG`
- `CFGGuider`
- `PreviewImage`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `UpscaleModelLoader`
- `SDXLPromptStyler`
- `VAELoader`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `UltimateSDUpscale`
- `RH_Captioner`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `LoadImage`
- `BasicScheduler`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `976354092755445`
- `steps` = `30`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（40/46）

**有卡**：`UNETLoader`、`ConditioningZeroOut`、`CLIPLoader`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`VAEEncode`、`SaveImage`、`easy cleanGpuUsed`、`LoraLoaderModelOnly`、`VAELoader`、`ImageConcatMulti`、`RandomNoise`、`SplitSigmas`、`SamplerCustomAdvanced`、`DisableNoise`、`ModelSamplingSD3`、`KSamplerSelect`、`RH_Captioner`、`WanVideoNAG`、`CFGGuider`、`UpscaleModelLoader`、`SDXLPromptStyler`、`KSampler`、`EmptyLatentImage`、`VAEDecode`、`UltimateSDUpscale`、`LoadImage`、`BasicScheduler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
