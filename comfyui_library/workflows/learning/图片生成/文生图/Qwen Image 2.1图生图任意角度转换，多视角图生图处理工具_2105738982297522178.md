---
key: 图片生成/文生图/Qwen Image 2.1图生图任意角度转换，多视角图生图处理工具_2105738982297522178.json
name: Qwen Image 2.1图生图任意角度转换，多视角图生图处理工具_2105738982297522178
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1图生图任意角度转换，多视角图生图处理工具_2105738982297522178.json
hash: 6e02fa72cbbfe795
coverage: 0.677966
learned_at: 2026-10-06 21:48:18
nodes: [LoadBackgroundRemovalModel, RemoveBackground, InvertMask, TripoSplatPreprocessImage, PreviewImage, UNETLoader, CLIPVisionLoader, VAELoader, VAELoader, TripoSplatConditioning, KSampler, VAEDecodeTripoSplat, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, QwenImage21Cache, KSampler, VAEDecode, ComfySwitchNode, SaveImage, CreateCameraInfo, LoraLoaderModelOnly, RenderSplat, GetImageSize, ImageScaleToMaxDimension, LoadImage, SaveImage, ImageConcanate, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [CreateCameraInfo, ImageConcanate, ImageScaleToMaxDimension, InvertMask, LoadBackgroundRemovalModel, RemoveBackground, RenderSplat, TripoSplatPreprocessImage, VAEDecodeTripoSplat, CLIPVisionLoader, GetImageSize, TripoSplatConditioning, solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CreateCameraInfo` 知识库中没有该节点类型的任何知识, 次要节点 `ImageConcanate` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToMaxDimension` 知识库中没有该节点类型的任何知识, 次要节点 `InvertMask` 知识库中没有该节点类型的任何知识, 次要节点 `LoadBackgroundRemovalModel` 知识库中没有该节点类型的任何知识, 次要节点 `RemoveBackground` 知识库中没有该节点类型的任何知识, 次要节点 `RenderSplat` 知识库中没有该节点类型的任何知识, 次要节点 `TripoSplatPreprocessImage` 知识库中没有该节点类型的任何知识, 核心节点 `VAEDecodeTripoSplat` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `CLIPVisionLoader` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `GetImageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `TripoSplatConditioning` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1图生图任意角度转换，多视角图生图处理工具_2105738982297522178.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1图生图任意角度转换，多视角图生图处理工具_2105738982297522178.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（59 个）：
- `LoadBackgroundRemovalModel`
- `RemoveBackground`
- `InvertMask`
- `TripoSplatPreprocessImage`
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPVisionLoader`
- `VAELoader`
- `VAELoader`
- `TripoSplatConditioning`
- `KSampler` ★核心
- `VAEDecodeTripoSplat` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `SaveImage`
- `CreateCameraInfo`
- `LoraLoaderModelOnly` ★核心
- `RenderSplat`
- `GetImageSize`
- `ImageScaleToMaxDimension`
- `LoadImage`
- `SaveImage`
- `ImageConcanate`
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

**识别到的模式**：text_to_image

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

覆盖率 **68%**（40/59）

**有卡**：`UNETLoader`、`VAELoader`、`KSampler`、`CLIPLoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`VAEDecode`、`SaveImage`、`LoraLoaderModelOnly`、`LoadImage`、`EmptyLatentImage`、`CLIPTextEncode`

**缺卡**（13）：`CreateCameraInfo`、`ImageConcanate`、`ImageScaleToMaxDimension`、`InvertMask`、`LoadBackgroundRemovalModel`、`RemoveBackground`、`RenderSplat`、`TripoSplatPreprocessImage`、`VAEDecodeTripoSplat`、`CLIPVisionLoader`、`GetImageSize`、`TripoSplatConditioning`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CreateCameraInfo` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageConcanate` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToMaxDimension` 知识库中没有该节点类型的任何知识
- 次要节点 `InvertMask` 知识库中没有该节点类型的任何知识
- 次要节点 `LoadBackgroundRemovalModel` 知识库中没有该节点类型的任何知识
- 次要节点 `RemoveBackground` 知识库中没有该节点类型的任何知识
- 次要节点 `RenderSplat` 知识库中没有该节点类型的任何知识
- 次要节点 `TripoSplatPreprocessImage` 知识库中没有该节点类型的任何知识
- 核心节点 `VAEDecodeTripoSplat` 仅有 VAE 的通用知识，没有该节点自己的说明
- 次要节点 `CLIPVisionLoader` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `GetImageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `TripoSplatConditioning` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
