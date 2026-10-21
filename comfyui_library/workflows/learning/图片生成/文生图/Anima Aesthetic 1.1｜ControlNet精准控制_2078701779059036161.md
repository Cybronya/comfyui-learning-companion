---
key: 图片生成/文生图/Anima Aesthetic 1.1｜ControlNet精准控制_2078701779059036161.json
name: Anima Aesthetic 1.1｜ControlNet精准控制_2078701779059036161
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima Aesthetic 1.1｜ControlNet精准控制_2078701779059036161.json
hash: 068bcfe216be4023
coverage: 0.875
learned_at: 2026-10-20 00:18:44
nodes: [Note, LoraLoaderModelOnly, CLIPLoader, Text, CLIPTextEncode, CLIPTextEncode, FluxResolutionNode, EmptyLatentImage, LoadImage, ImageScale, AIO_Preprocessor, ClownsharKSampler_Beta, LatentUpscaleBy, ClownsharKSampler_Beta, VAEDecode, PreviewImage, SaveImage, Text, PreviewImage, AnimaLLLiteApply, XB_UNetNameBroadcaster, NAGuidance, LoraLoaderModelOnly, UNETLoader, VAELoader, VAEDecode, PreviewImage, SaveImage, VAEDecode, KSampler, LatentUpscaleBy, KSampler]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 2.88, "denoise": 0.5500000000000002, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 646485429179378, "steps": 30, "width": 512}
---

# 图片生成/文生图/Anima Aesthetic 1.1｜ControlNet精准控制_2078701779059036161.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima Aesthetic 1.1｜ControlNet精准控制_2078701779059036161.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `Note`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `Text`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `FluxResolutionNode`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `ImageScale`
- `AIO_Preprocessor`
- `ClownsharKSampler_Beta` ★核心
- `LatentUpscaleBy`
- `ClownsharKSampler_Beta` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `Text`
- `PreviewImage`
- `AnimaLLLiteApply`
- `XB_UNetNameBroadcaster`
- `NAGuidance`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LatentUpscaleBy`
- `KSampler` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `646485429179378`
- `steps` = `30`
- `cfg` = `2.88`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.5500000000000002`

## 知识

覆盖率 **88%**（28/32）

**有卡**：`LoraLoaderModelOnly`、`CLIPLoader`、`Text`、`CLIPTextEncode`、`FluxResolutionNode`、`EmptyLatentImage`、`LoadImage`、`ImageScale`、`AIO_Preprocessor`、`ClownsharKSampler_Beta`、`LatentUpscaleBy`、`VAEDecode`、`SaveImage`、`AnimaLLLiteApply`、`XB_UNetNameBroadcaster`、`NAGuidance`、`UNETLoader`、`VAELoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage
