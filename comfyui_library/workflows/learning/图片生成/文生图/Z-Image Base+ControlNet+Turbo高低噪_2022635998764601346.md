---
key: 图片生成/文生图/Z-Image Base+ControlNet+Turbo高低噪_2022635998764601346.json
name: Z-Image Base+ControlNet+Turbo高低噪_2022635998764601346
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image Base+ControlNet+Turbo高低噪_2022635998764601346.json
hash: 5e8014f1d7525f00
coverage: 0.909091
learned_at: 2026-10-19 22:29:57
nodes: [LoadImage, DetailDaemonSamplerNode, SamplerEulerAncestral, CLIPTextEncode, CLIPTextEncode, RandomNoise, DetailDaemonSamplerNode, CLIPLoader, VAELoader, VAEDecode, ImageScaleBy, VAEEncode, SamplerCustomAdvanced, VAEDecode, LoraLoaderModelOnly, ModelPatchLoader, ModelSamplingAuraFlow, VAELoader, SamplerEulerAncestral, UNETLoader, SamplerCustomAdvanced, EmptyLatentImage, CLIPTextEncode, UNETLoader, VAEDecode, CLIPLoader, CLIPTextEncode, RandomNoise, ModelSamplingAuraFlow, CFGGuider, image_scale_pixel_v2, easy int, ZImageFunControlnet, SplitSigmas, AIO_Preprocessor, PrimitiveStringMultiline, SamplerCustomAdvanced, CFGGuider, BasicScheduler, BasicScheduler, PreviewImage, PreviewImage, SaveImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 472, "width": 512}
---

# 图片生成/文生图/Z-Image Base+ControlNet+Turbo高低噪_2022635998764601346.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image Base+ControlNet+Turbo高低噪_2022635998764601346.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `LoadImage`
- `DetailDaemonSamplerNode` ★核心
- `SamplerEulerAncestral` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `DetailDaemonSamplerNode` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `VAEEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `VAELoader`
- `SamplerEulerAncestral` ★核心
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `ModelSamplingAuraFlow`
- `CFGGuider`
- `image_scale_pixel_v2`
- `easy int`
- `ZImageFunControlnet`
- `SplitSigmas`
- `AIO_Preprocessor`
- `PrimitiveStringMultiline`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `BasicScheduler`
- `BasicScheduler`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`

## 关键参数

- `width` = `512`
- `height` = `472`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（40/44）

**有卡**：`LoadImage`、`DetailDaemonSamplerNode`、`SamplerEulerAncestral`、`CLIPTextEncode`、`RandomNoise`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`ImageScaleBy`、`VAEEncode`、`SamplerCustomAdvanced`、`LoraLoaderModelOnly`、`ModelPatchLoader`、`ModelSamplingAuraFlow`、`UNETLoader`、`EmptyLatentImage`、`CFGGuider`、`image_scale_pixel_v2`、`easy int`、`ZImageFunControlnet`、`SplitSigmas`、`AIO_Preprocessor`、`BasicScheduler`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader
