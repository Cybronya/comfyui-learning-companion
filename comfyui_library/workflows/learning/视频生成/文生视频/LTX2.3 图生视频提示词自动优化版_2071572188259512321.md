---
key: 视频生成/文生视频/LTX2.3 图生视频提示词自动优化版_2071572188259512321.json
name: LTX2.3 图生视频提示词自动优化版_2071572188259512321
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 图生视频提示词自动优化版_2071572188259512321.json
hash: 45d74901d9ca2c61
coverage: 0.95
learned_at: 2026-10-15 22:44:59
nodes: [RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, KSamplerSelect, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVAudioVAEDecode, LTXVConditioning, LTXVConcatAVLatent, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LatentUpscaleModelLoader, CLIPTextEncode, CFGGuider, RandomNoise, PathchSageAttentionKJ, ManualSigmas, ResizeImagesByLongerEdge, LTXVPreprocess, VAEDecode, LTXVAudioVAEDecode, easy imageSize, ImageConcanate, EmptyImage, easy mathInt, CLIPTextEncode, VAEDecode, GetImageSize, ImageResizeKJv2, ImageResizeKJv2, easy ifElse, easy compare, ImageScaleBy, easy imageSize, easy ifElse, ImageResizeKJv2, ImageResizeKJv2, easy promptConcat, SimpleMath+, CR Text, Dapao_LlamaChat, LoadImage, easy int, VHS_VideoCombine, Note, easy positive, CR Text, LoraLoaderModelOnly, UNETLoader, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 361}
---

# 视频生成/文生视频/LTX2.3 图生视频提示词自动优化版_2071572188259512321.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 图生视频提示词自动优化版_2071572188259512321.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（60 个）：
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `KSamplerSelect` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `RandomNoise`
- `PathchSageAttentionKJ`
- `ManualSigmas`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `easy imageSize`
- `ImageConcanate`
- `EmptyImage`
- `easy mathInt`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `GetImageSize`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `easy ifElse`
- `easy compare`
- `ImageScaleBy`
- `easy imageSize`
- `easy ifElse`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `easy promptConcat`
- `SimpleMath+`
- `CR Text`
- `Dapao_LlamaChat`
- `LoadImage`
- `easy int`
- `VHS_VideoCombine`
- `Note`
- `easy positive`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`

## 关键参数

- `width` = `361`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（57/60）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`VAEDecode`、`easy imageSize`、`ImageConcanate`、`EmptyImage`、`easy mathInt`、`GetImageSize`、`ImageResizeKJv2`、`easy compare`、`ImageScaleBy`、`easy promptConcat`、`SimpleMath+`、`CR Text`、`Dapao_LlamaChat`、`LoadImage`、`easy int`、`VHS_VideoCombine`、`easy positive`、`LoraLoaderModelOnly`、`UNETLoader`、`DualCLIPLoader`、`VAELoaderKJ`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
