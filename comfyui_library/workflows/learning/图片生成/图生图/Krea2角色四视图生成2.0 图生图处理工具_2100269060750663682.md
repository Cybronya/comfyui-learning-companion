---
key: 图片生成/图生图/Krea2角色四视图生成2.0 图生图处理工具_2100269060750663682.json
name: Krea2角色四视图生成2.0 图生图处理工具_2100269060750663682
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Krea2角色四视图生成2.0 图生图处理工具_2100269060750663682.json
hash: 8ffdac4bed6331ad
coverage: 0.869565
learned_at: 2026-10-21 00:41:21
nodes: [LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, CLIPLoader, Krea2EditGroundedEncode, KSampler, VAELoader, kkPadImageToCanvas, LoraLoaderModelOnly, UNETLoader, Krea2OstrisEditModelPatch, FluxKontextMultiReferenceLatentMethod, VAEEncode, FluxKontextMultiReferenceLatentMethod, PreviewImage, LoadImage, VAEDecode, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Krea2角色四视图生成2.0 图生图处理工具_2100269060750663682.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Krea2角色四视图生成2.0 图生图处理工具_2100269060750663682.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `CLIPLoader`
- `Krea2EditGroundedEncode`
- `KSampler` ★核心
- `VAELoader`
- `kkPadImageToCanvas`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `Krea2OstrisEditModelPatch`
- `FluxKontextMultiReferenceLatentMethod`
- `VAEEncode` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `PreviewImage`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（40/46）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`Krea2EditGroundedEncode`、`KSampler`、`VAELoader`、`kkPadImageToCanvas`、`LoraLoaderModelOnly`、`UNETLoader`、`Krea2OstrisEditModelPatch`、`FluxKontextMultiReferenceLatentMethod`、`VAEEncode`、`LoadImage`、`VAEDecode`、`SaveImage`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
