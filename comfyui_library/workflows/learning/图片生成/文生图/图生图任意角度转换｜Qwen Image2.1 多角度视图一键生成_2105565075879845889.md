---
key: 图片生成/文生图/图生图任意角度转换｜Qwen Image2.1 多角度视图一键生成_2105565075879845889.json
name: 图生图任意角度转换｜Qwen Image2.1 多角度视图一键生成_2105565075879845889
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/图生图任意角度转换｜Qwen Image2.1 多角度视图一键生成_2105565075879845889.json
hash: ea9a620c99e40994
coverage: 0.917808
learned_at: 2026-10-10 20:59:41
nodes: [LoadBackgroundRemovalModel, RemoveBackground, InvertMask, TripoSplatPreprocessImage, PreviewImage, UNETLoader, CLIPVisionLoader, VAELoader, VAELoader, TripoSplatConditioning, KSampler, VAEDecodeTripoSplat, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, QwenImage21Cache, KSampler, VAEDecode, ComfySwitchNode, SaveImage, CreateCameraInfo, LoraLoaderModelOnly, RenderSplat, GetImageSize, ImageScaleToMaxDimension, LoadImage, SaveImage, ImageConcanate, SaveImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/图生图任意角度转换｜Qwen Image2.1 多角度视图一键生成_2105565075879845889.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/图生图任意角度转换｜Qwen Image2.1 多角度视图一键生成_2105565075879845889.json`

## 结构

**节点**（73 个）：
- `LoadBackgroundRemovalModel`
- `RemoveBackground`
- `InvertMask`
- `TripoSplatPreprocessImage`
- `PreviewImage`
- `UNETLoader`
- `CLIPVisionLoader`
- `VAELoader`
- `VAELoader`
- `TripoSplatConditioning`
- `KSampler`
- `VAEDecodeTripoSplat`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `KSampler`
- `VAEDecode`
- `ComfySwitchNode`
- `SaveImage`
- `CreateCameraInfo`
- `LoraLoaderModelOnly`
- `RenderSplat`
- `GetImageSize`
- `ImageScaleToMaxDimension`
- `LoadImage`
- `SaveImage`
- `ImageConcanate`
- `SaveImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `VAELoader`
- `EmptyLatentImage`
- `KSampler`
- `VAEDecode`
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4.5`
- `denoise` = `1`
- `height` = `80`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `seed` = `598626327129635`
- `steps` = `4`
- `width` = `80`

## 知识

覆盖率 **92%**（67/73）

**有卡**：`LoadBackgroundRemovalModel`、`RemoveBackground`、`InvertMask`、`TripoSplatPreprocessImage`、`PreviewImage`、`UNETLoader`、`CLIPVisionLoader`、`VAELoader`、`TripoSplatConditioning`、`KSampler`、`VAEDecodeTripoSplat`、`CLIPLoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`VAEDecode`、`ComfySwitchNode`、`SaveImage`、`CreateCameraInfo`、`LoraLoaderModelOnly`、`RenderSplat`、`GetImageSize`、`ImageScaleToMaxDimension`、`LoadImage`、`ImageConcanate`、`孤海注释`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`JjkText`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
