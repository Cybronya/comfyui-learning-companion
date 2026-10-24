---
key: 图片生成/图生图/国风人物变美工作流-ZImage+Kook大佬瑶光lora+Kook如梦似幻lora_2053095520524091394.json
name: 国风人物变美工作流-ZImage+Kook大佬瑶光lora+Kook如梦似幻lora_2053095520524091394
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/国风人物变美工作流-ZImage+Kook大佬瑶光lora+Kook如梦似幻lora_2053095520524091394.json
hash: 9d9080c8fe6c64d1
coverage: 0.942857
learned_at: 2026-10-23 12:37:52
nodes: [CLIPTextEncode, FastFilmGrain, LayerColor: BrightnessContrastV2, Fast Groups Bypasser (rgthree), UNETLoader, LoraLoaderModelOnly, VAELoader, VAEDecode, ImageScaleToTotalPixels, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, CLIPLoader, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, SaveImage, CR Text, CR Text, CR Text, SaveImage, VAEEncode, MuyeTextEditOutput, Image Comparer (rgthree), LoadImage, KSampler]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.7500000000000001, "sampler_name": "res_2m_ode", "scheduler": "kl_optimal", "seed": 95981260513846, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/国风人物变美工作流-ZImage+Kook大佬瑶光lora+Kook如梦似幻lora_2053095520524091394.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/国风人物变美工作流-ZImage+Kook大佬瑶光lora+Kook如梦似幻lora_2053095520524091394.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
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
- `LoraLoaderModelOnly` ★核心
- `CR Text`
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
- `SaveImage`
- `VAEEncode` ★核心
- `MuyeTextEditOutput`
- `Image Comparer (rgthree)`
- `LoadImage`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `95981260513846`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2m_ode`
- `scheduler` = `kl_optimal`
- `denoise` = `0.7500000000000001`

## 知识

覆盖率 **94%**（33/35）

**有卡**：`CLIPTextEncode`、`FastFilmGrain`、`LayerColor: BrightnessContrastV2`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`VAEDecode`、`ImageScaleToTotalPixels`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`CLIPLoader`、`CR Text`、`SaveImage`、`VAEEncode`、`MuyeTextEditOutput`、`LoadImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、SaveImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
