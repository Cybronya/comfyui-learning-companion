---
key: 图片生成/文生图/killer Z image出图+Contronet+Minicpmv4.5反推+4K放大v1.0_2002006378497622017.json
name: killer Z image出图+Contronet+Minicpmv4.5反推+4K放大v1.0_2002006378497622017
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/killer Z image出图+Contronet+Minicpmv4.5反推+4K放大v1.0_2002006378497622017.json
hash: f5630a631a825b48
coverage: 0.822222
learned_at: 2026-10-19 21:47:18
nodes: [VAELoader, CLIPLoader, UNETLoader, VAELoader, VAEDecode, ModelSamplingAuraFlow, CLIPLoader, KSampler, EmptySD3LatentImage, SaveImage, LoraLoaderModelOnly, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, MiniCPM_VQA, LoadImage, EmptySD3LatentImage, ShowText|pysssss, CLIPTextEncode, Note, Note, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, Image Comparer (rgthree), PreviewImage, LoadImage, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, SaveImage, CLIPTextEncode, LoraLoaderModelOnly, QwenImageDiffsynthControlnet, AIO_Preprocessor, ModelPatchLoader, PreviewImage, PreviewImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, ModelSamplingAuraFlow, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "dpmpp_2m_sde", "scheduler": "sgm_uniform", "seed": 74115011394364, "steps": 10}
---

# 图片生成/文生图/killer Z image出图+Contronet+Minicpmv4.5反推+4K放大v1.0_2002006378497622017.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/killer Z image出图+Contronet+Minicpmv4.5反推+4K放大v1.0_2002006378497622017.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `VAELoader`
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
- `MiniCPM_VQA`
- `LoadImage`
- `EmptySD3LatentImage`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `LoadImage`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `QwenImageDiffsynthControlnet`
- `AIO_Preprocessor`
- `ModelPatchLoader`
- `PreviewImage`
- `PreviewImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `74115011394364`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **82%**（37/45）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`VAEDecode`、`ModelSamplingAuraFlow`、`KSampler`、`EmptySD3LatentImage`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`MiniCPM_VQA`、`LoadImage`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`QwenImageDiffsynthControlnet`、`AIO_Preprocessor`、`ModelPatchLoader`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
