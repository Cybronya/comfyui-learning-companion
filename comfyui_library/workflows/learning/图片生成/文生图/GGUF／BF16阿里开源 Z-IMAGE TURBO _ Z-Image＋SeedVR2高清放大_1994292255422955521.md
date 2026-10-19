---
key: 图片生成/文生图/GGUF／BF16阿里开源 Z-IMAGE TURBO _ Z-Image＋SeedVR2高清放大_1994292255422955521.json
name: GGUF／BF16阿里开源 Z-IMAGE TURBO _ Z-Image＋SeedVR2高清放大_1994292255422955521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/GGUF／BF16阿里开源 Z-IMAGE TURBO _ Z-Image＋SeedVR2高清放大_1994292255422955521.json
hash: ff9fa05b00fd3e20
coverage: 0.818182
learned_at: 2026-10-19 21:32:35
nodes: [KSampler, CLIPTextEncode, CLIPTextEncode, SaveImage, EmptySD3LatentImage, PrimitiveNode, PrimitiveNode, PrimitiveNode, Text Multiline, VAELoader, CLIPLoader, Power Lora Loader (rgthree), UNETLoader, CR Model Input Switch, UnetLoaderGGUF, ImageScaleBy, SaveImage, SeedVR2VideoUpscaler, Image Comparer (rgthree), VAEDecode, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 372695476089856, "steps": 10}
---

# 图片生成/文生图/GGUF／BF16阿里开源 Z-IMAGE TURBO _ Z-Image＋SeedVR2高清放大_1994292255422955521.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/GGUF／BF16阿里开源 Z-IMAGE TURBO _ Z-Image＋SeedVR2高清放大_1994292255422955521.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `EmptySD3LatentImage`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `Text Multiline`
- `VAELoader`
- `CLIPLoader`
- `Power Lora Loader (rgthree)`
- `UNETLoader` ★核心
- `CR Model Input Switch`
- `UnetLoaderGGUF` ★核心
- `ImageScaleBy`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`

## 关键参数

- `seed` = `372695476089856`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（18/22）

**有卡**：`KSampler`、`CLIPTextEncode`、`SaveImage`、`EmptySD3LatentImage`、`Text Multiline`、`VAELoader`、`CLIPLoader`、`Power Lora Loader (rgthree)`、`UNETLoader`、`CR Model Input Switch`、`UnetLoaderGGUF`、`ImageScaleBy`、`SeedVR2VideoUpscaler`、`VAEDecode`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel
