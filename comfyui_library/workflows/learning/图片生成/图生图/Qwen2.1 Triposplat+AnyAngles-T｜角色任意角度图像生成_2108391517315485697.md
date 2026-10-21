---
key: 图片生成/图生图/Qwen2.1 Triposplat+AnyAngles-T｜角色任意角度图像生成_2108391517315485697.json
name: Qwen2.1 Triposplat+AnyAngles-T｜角色任意角度图像生成_2108391517315485697
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1 Triposplat+AnyAngles-T｜角色任意角度图像生成_2108391517315485697.json
hash: e864ccd50a05d6f8
coverage: 0.731959
learned_at: 2026-10-21 00:43:35
nodes: [TripoSplatConditioning, TripoSplatSamplingPreview, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, TextEncodeQwenImage21, QwenImage21Cache, EmptyLatentImage, KSampler, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetImageSize, SetNode, VAEDecodeTripoSplat, InvertMask, SetNode, RemoveBackground, JoinImageWithAlpha, InvertMask, KSampler, CLIPVisionLoader, VAELoader, VAELoader, UNETLoader, UNETLoader, VAELoader, CLIPLoader, CLIPLoader, LoraLoaderModelOnly, SetNode, LoadBackgroundRemovalModel, TripoSplatPreprocessImage, ComfySwitchNode, GetNode, PreviewImage, ComfySwitchNode, LoadImage, VAEDecode, RenderMesh, SplatToMesh, PreviewImage, GetNode, GetNode, SplatToFile3D, CreateCameraInfo, PreviewGaussianSplat, SaveImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen2.1 Triposplat+AnyAngles-T｜角色任意角度图像生成_2108391517315485697.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1 Triposplat+AnyAngles-T｜角色任意角度图像生成_2108391517315485697.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（97 个）：
- `TripoSplatConditioning`
- `TripoSplatSamplingPreview`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetImageSize`
- `SetNode`
- `VAEDecodeTripoSplat` ★核心
- `InvertMask`
- `SetNode`
- `RemoveBackground`
- `JoinImageWithAlpha`
- `InvertMask`
- `KSampler` ★核心
- `CLIPVisionLoader`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LoadBackgroundRemovalModel`
- `TripoSplatPreprocessImage`
- `ComfySwitchNode`
- `GetNode`
- `PreviewImage`
- `ComfySwitchNode`
- `LoadImage`
- `VAEDecode` ★核心
- `RenderMesh`
- `SplatToMesh`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `SplatToFile3D`
- `CreateCameraInfo`
- `PreviewGaussianSplat`
- `SaveImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **73%**（71/97）

**有卡**：`TripoSplatConditioning`、`TripoSplatSamplingPreview`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`EmptyLatentImage`、`KSampler`、`GetImageSize`、`VAEDecodeTripoSplat`、`InvertMask`、`RemoveBackground`、`JoinImageWithAlpha`、`CLIPVisionLoader`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`LoadBackgroundRemovalModel`、`TripoSplatPreprocessImage`、`LoadImage`、`VAEDecode`、`RenderMesh`、`SplatToMesh`、`SplatToFile3D`、`CreateCameraInfo`、`PreviewGaussianSplat`、`SaveImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
