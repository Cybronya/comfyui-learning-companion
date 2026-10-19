---
key: 图片生成/文生图/killer Qwen image出图+Contronet+反推+4K修复v2.0_1999339009170079745.json
name: killer Qwen image出图+Contronet+反推+4K修复v2.0_1999339009170079745
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/killer Qwen image出图+Contronet+反推+4K修复v2.0_1999339009170079745.json
hash: 0035a20fc9eed048
coverage: 0.844444
learned_at: 2026-10-19 21:47:18
nodes: [VAELoader, PreviewImage, SetUnionControlNetType, AIO_Preprocessor, ImageScaleToTotalPixels, ControlNetLoader, ControlNetApplyAdvanced, CLIPLoader, UNETLoader, VAELoader, VAEDecode, ModelSamplingAuraFlow, CLIPLoader, KSampler, EmptySD3LatentImage, SaveImage, LoraLoaderModelOnly, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, CLIPTextEncode, MiniCPM_VQA, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptySD3LatentImage, ShowText|pysssss, KSampler, LoadImage, CLIPTextEncode, ModelSamplingAuraFlow, SaveImage, LoraLoaderModelOnly, Note, Note, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, Image Comparer (rgthree), PreviewImage, LoadImage, Note, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 2.5, "controlnet_strength": 0.6, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 802806432467323, "steps": 20}
---

# 图片生成/文生图/killer Qwen image出图+Contronet+反推+4K修复v2.0_1999339009170079745.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/killer Qwen image出图+Contronet+反推+4K修复v2.0_1999339009170079745.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `VAELoader`
- `PreviewImage`
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `ImageScaleToTotalPixels`
- `ControlNetLoader`
- `ControlNetApplyAdvanced` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `MiniCPM_VQA`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptySD3LatentImage`
- `ShowText|pysssss`
- `KSampler` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `LoadImage`
- `Note`
- `CLIPTextEncode` ★核心

## 关键参数

- `controlnet_strength` = `0.6`
- `seed` = `802806432467323`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **84%**（38/45）

**有卡**：`VAELoader`、`SetUnionControlNetType`、`AIO_Preprocessor`、`ImageScaleToTotalPixels`、`ControlNetLoader`、`ControlNetApplyAdvanced`、`CLIPLoader`、`UNETLoader`、`VAEDecode`、`ModelSamplingAuraFlow`、`KSampler`、`EmptySD3LatentImage`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`MiniCPM_VQA`、`LoadImage`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
