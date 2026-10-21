---
key: 图片生成/文生图/ZImage+Kook大佬瑶光lora+Kook如梦似幻lora_2059586906224156674.json
name: ZImage+Kook大佬瑶光lora+Kook如梦似幻lora_2059586906224156674
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ZImage+Kook大佬瑶光lora+Kook如梦似幻lora_2059586906224156674.json
hash: 3540604ca40a993e
coverage: 0.941176
learned_at: 2026-10-19 23:03:03
nodes: [CLIPTextEncode, FastFilmGrain, LayerColor: BrightnessContrastV2, Fast Groups Bypasser (rgthree), UNETLoader, LoraLoaderModelOnly, VAELoader, VAEDecode, ImageScaleToTotalPixels, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, CLIPLoader, CLIPTextEncode, LoraLoaderModelOnly, KSampler, LoraLoaderModelOnly, EmptyLatentImage, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, SaveImage, CR Text, CR Text, CR Text, Image Comparer (rgthree), SaveImage, CR Text, MuyeTextEditOutput]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "res_2m_ode", "scheduler": "kl_optimal", "seed": 749364866774997, "steps": 8, "width": 1920}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/ZImage+Kook大佬瑶光lora+Kook如梦似幻lora_2059586906224156674.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ZImage+Kook大佬瑶光lora+Kook如梦似幻lora_2059586906224156674.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `CLIPTextEncode` ★核心
- `FastFilmGrain`
- `LayerColor: BrightnessContrastV2`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `SaveImage`
- `CR Text`
- `CR Text`
- `CR Text`
- `Image Comparer (rgthree)`
- `SaveImage`
- `CR Text`
- `MuyeTextEditOutput`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `749364866774997`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2m_ode`
- `scheduler` = `kl_optimal`
- `denoise` = `1`
- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（32/34）

**有卡**：`CLIPTextEncode`、`FastFilmGrain`、`LayerColor: BrightnessContrastV2`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`VAEDecode`、`ImageScaleToTotalPixels`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`CLIPLoader`、`KSampler`、`EmptyLatentImage`、`CR Text`、`SaveImage`、`MuyeTextEditOutput`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、SaveImage、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
