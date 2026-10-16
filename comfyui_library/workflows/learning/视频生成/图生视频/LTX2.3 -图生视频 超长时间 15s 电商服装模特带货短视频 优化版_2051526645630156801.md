---
key: 视频生成/图生视频/LTX2.3 -图生视频 超长时间 15s 电商服装模特带货短视频 优化版_2051526645630156801.json
name: LTX2.3 -图生视频 超长时间 15s 电商服装模特带货短视频 优化版_2051526645630156801.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2051526645630156801.json
hash: c8962efef846a5fb
coverage: 0.915254
learned_at: 2026-10-15 22:37:22
nodes: [CFGGuider, KSamplerSelect, KSamplerSelect, VAELoaderKJ, LTXVConcatAVLatent, SamplerCustomAdvanced, CFGGuider, DualCLIPLoader, PathchSageAttentionKJ, LTXVImgToVideoInplace, LTXVLatentUpsampler, ManualSigmas, LTXVConcatAVLatent, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, LTXVImgToVideoInplace, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, easy mathInt, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LTXVAudioVAEDecode, RandomNoise, RandomNoise, easy imageSize, ResizeImagesByLongerEdge, VAEDecode, easy imageSize, VAELoaderKJ, ImageScaleBy, LTXVSeparateAVLatent, EmptyImage, LTXVCropGuides, UNETLoader, LoraLoaderModelOnly, ImageConcanate, easy ifElse, VAEDecode, ImageResizeKJv2, ImageResizeKJv2, easy ifElse, LTXVPreprocess, PreviewImage, ImageResizeKJv2, ImageResizeKJv2, Note, SamplerCustomAdvanced, GetImageSize, easy compare, easy promptConcat, easy showAnything, AILab_QwenVL, ManualSigmas, VHS_VideoCombine, VHS_VideoCombine, LoadImage, easy positive]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 361}
---

# 视频生成/图生视频/LTX2.3 -图生视频 超长时间 15s 电商服装模特带货短视频 优化版_2051526645630156801.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2051526645630156801.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `VAELoaderKJ`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `DualCLIPLoader`
- `PathchSageAttentionKJ`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode` ★核心
- `easy mathInt`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LTXVAudioVAEDecode` ★核心
- `RandomNoise`
- `RandomNoise`
- `easy imageSize`
- `ResizeImagesByLongerEdge`
- `VAEDecode` ★核心
- `easy imageSize`
- `VAELoaderKJ`
- `ImageScaleBy`
- `LTXVSeparateAVLatent`
- `EmptyImage`
- `LTXVCropGuides`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageConcanate`
- `easy ifElse`
- `VAEDecode` ★核心
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `easy ifElse`
- `LTXVPreprocess`
- `PreviewImage`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `Note`
- `SamplerCustomAdvanced` ★核心
- `GetImageSize`
- `easy compare`
- `easy promptConcat`
- `easy showAnything`
- `AILab_QwenVL`
- `ManualSigmas`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `easy positive`

## 关键参数

- `width` = `361`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（54/59）

**有卡**：`CFGGuider`、`KSamplerSelect`、`VAELoaderKJ`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`DualCLIPLoader`、`PathchSageAttentionKJ`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`ManualSigmas`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`easy mathInt`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`RandomNoise`、`easy imageSize`、`ResizeImagesByLongerEdge`、`VAEDecode`、`ImageScaleBy`、`EmptyImage`、`LTXVCropGuides`、`UNETLoader`、`LoraLoaderModelOnly`、`ImageConcanate`、`ImageResizeKJv2`、`LTXVPreprocess`、`GetImageSize`、`easy compare`、`easy promptConcat`、`AILab_QwenVL`、`VHS_VideoCombine`、`LoadImage`、`easy positive`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
