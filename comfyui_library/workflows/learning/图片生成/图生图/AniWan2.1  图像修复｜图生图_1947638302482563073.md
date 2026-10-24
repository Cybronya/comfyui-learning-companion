---
key: 图片生成/图生图/AniWan2.1  图像修复｜图生图_1947638302482563073.json
name: AniWan2.1  图像修复｜图生图_1947638302482563073
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/AniWan2.1  图像修复｜图生图_1947638302482563073.json
hash: 93e2d6fc8bb2efd6
coverage: 0.944444
learned_at: 2026-10-23 10:51:05
nodes: [ImageSharpen, EsesImageEffectBloom, PreviewImage, VAEEncode, VAELoader, CLIPLoader, ModelSamplingSD3, BetterFilmGrain, ImageConcanate, LoraLoaderModelOnly, UNETLoader, CLIPTextEncode, CLIPTextEncode, VAEDecode, KSampler, LoraLoaderModelOnly, LoadImage, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.25000000000000006, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 262997824898883, "steps": 10}
---

# 图片生成/图生图/AniWan2.1  图像修复｜图生图_1947638302482563073.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/AniWan2.1  图像修复｜图生图_1947638302482563073.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `ImageSharpen`
- `EsesImageEffectBloom`
- `PreviewImage`
- `VAEEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `ModelSamplingSD3`
- `BetterFilmGrain`
- `ImageConcanate`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `262997824898883`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.25000000000000006`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`ImageSharpen`、`EsesImageEffectBloom`、`VAEEncode`、`VAELoader`、`CLIPLoader`、`ModelSamplingSD3`、`BetterFilmGrain`、`ImageConcanate`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
