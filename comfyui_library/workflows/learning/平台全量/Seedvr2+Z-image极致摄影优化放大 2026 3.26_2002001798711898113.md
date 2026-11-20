---
key: 平台全量/Seedvr2+Z-image极致摄影优化放大 2026 3.26_2002001798711898113.json
name: Seedvr2+Z-image极致摄影优化放大 2026 3.26_2002001798711898113
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Seedvr2+Z-image极致摄影优化放大 2026 3.26_2002001798711898113.json
hash: 60b247591ef59d16
coverage: 0.74359
learned_at: 2026-11-14 01:00:35
nodes: [CLIPTextEncode, VAEDecodeTiled, ImageListToImageBatch, TTP_Image_Assy, ConditioningZeroOut, Image Comparer (rgthree), LoadImage, ImpactImageBatchToImageList, VAELoader, VAEEncode, UNETLoader, CLIPLoader, TTP_Image_Tile_Batch, TTP_Tile_image_size, ImageScaleToTotalPixels, SeedVR2LoadVAEModel, ImageScaleToTotalPixels, LoadImage, Image Comparer (rgthree), LoadImage, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, LoadImage, LoadImage, Note, Note, Note, LoadImage, LoadImage, ImageUpscaleWithModel, Note, SaveImage, Image Comparer (rgthree), LoraLoaderModelOnly, MarkdownNote, UpscaleModelLoader, Fast Groups Bypasser (rgthree), KSampler, Note]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 986724212385935, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 平台全量/Seedvr2+Z-image极致摄影优化放大 2026 3.26_2002001798711898113.json

> 来源文件 `comfyui_library/workflows/平台全量/Seedvr2+Z-image极致摄影优化放大 2026 3.26_2002001798711898113.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `CLIPTextEncode` ★核心
- `VAEDecodeTiled` ★核心
- `ImageListToImageBatch`
- `TTP_Image_Assy`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `LoadImage`
- `ImpactImageBatchToImageList`
- `VAELoader`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `ImageScaleToTotalPixels`
- `SeedVR2LoadVAEModel`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `LoadImage`
- `LoadImage`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `ImageUpscaleWithModel`
- `Note`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `UpscaleModelLoader`
- `Fast Groups Bypasser (rgthree)`
- `KSampler` ★核心
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `986724212385935`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **74%**（29/39）

**有卡**：`CLIPTextEncode`、`VAEDecodeTiled`、`ImageListToImageBatch`、`TTP_Image_Assy`、`ConditioningZeroOut`、`LoadImage`、`ImpactImageBatchToImageList`、`VAELoader`、`VAEEncode`、`UNETLoader`、`CLIPLoader`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`ImageScaleToTotalPixels`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`ImageUpscaleWithModel`、`SaveImage`、`LoraLoaderModelOnly`、`UpscaleModelLoader`、`KSampler`

**用到的条目**：KSampler、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
