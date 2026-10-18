---
key: 视频生成/图生视频/Qwen_Image_2.1人物姿势编辑迁移｜图片处理姿势随心改_2107277724539768834.json
name: Qwen_Image_2.1人物姿势编辑迁移｜图片处理姿势随心改_2107277724539768834
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1人物姿势编辑迁移｜图片处理姿势随心改_2107277724539768834.json
hash: 3a409e566566a0d7
coverage: 0.8375
learned_at: 2026-10-17 22:18:54
nodes: [UNETLoader, VAELoader, EmptyLatentImage, VAEDecode, ComfySwitchNode, QwenImage21Cache, CLIPLoader, easy showAnything, SaveImageAdvanced, Hina.PoseEditor3D, AnyLineArtPreprocessor_aux, LoadDepthPro, LoadImage, DepthPro, MetricDepthToRelative, DWPreprocessor, LoadImage, Fast Groups Bypasser (rgthree), ImageResizeKJv2, TTResolutionSelector, PreviewImage, PreviewImage, PreviewImage, TextEncodeQwenImage21, PreviewImage, PreviewImage, PreviewImage, PreviewImage, MuyeTextEditOutput, TextGenerate, BatchImagesNode, ResolutionSelector, KSampler, CR Prompt Text, CLIPLoader, SaveImage, easy cleanGpuUsed, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Qwen_Image_2.1人物姿势编辑迁移｜图片处理姿势随心改_2107277724539768834.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1人物姿势编辑迁移｜图片处理姿势随心改_2107277724539768834.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（80 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `CLIPLoader`
- `easy showAnything`
- `SaveImageAdvanced`
- `Hina.PoseEditor3D`
- `AnyLineArtPreprocessor_aux`
- `LoadDepthPro`
- `LoadImage`
- `DepthPro`
- `MetricDepthToRelative`
- `DWPreprocessor`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `TTResolutionSelector`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `TextEncodeQwenImage21`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `MuyeTextEditOutput`
- `TextGenerate`
- `BatchImagesNode`
- `ResolutionSelector`
- `KSampler` ★核心
- `CR Prompt Text`
- `CLIPLoader`
- `SaveImage`
- `easy cleanGpuUsed`
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
- `EmptyImage`
- `PreviewImage`

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

覆盖率 **84%**（67/80）

**有卡**：`UNETLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`QwenImage21Cache`、`CLIPLoader`、`SaveImageAdvanced`、`Hina.PoseEditor3D`、`AnyLineArtPreprocessor_aux`、`LoadDepthPro`、`LoadImage`、`DepthPro`、`MetricDepthToRelative`、`DWPreprocessor`、`ImageResizeKJv2`、`TTResolutionSelector`、`TextEncodeQwenImage21`、`MuyeTextEditOutput`、`TextGenerate`、`BatchImagesNode`、`ResolutionSelector`、`KSampler`、`CR Prompt Text`、`SaveImage`、`easy cleanGpuUsed`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
