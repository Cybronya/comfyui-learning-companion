---
key: 视频生成/图生视频/LTX2.3首尾帧生视频（KJ流）_2044379140505214978.json
name: LTX2.3首尾帧生视频（KJ流）_2044379140505214978.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3首尾帧生视频（KJ流）_2044379140505214978.json
hash: 03830798ce7632f8
coverage: 0.989362
learned_at: 2026-10-15 22:36:37
nodes: [LatentUpscaleModelLoader, easy setNode, easy setNode, easy getNode, easy getNode, ImageResizeKJv2, easy setNode, easy setNode, easy setNode, easy int, easy int, easy float, easy setNode, easy setNode, EmptyLTXVLatentVideo, easy setNode, easy getNode, easy setNode, CFGGuider, LTXVConcatAVLatent, KSamplerSelect, SamplerCustomAdvanced, easy getNode, easy getNode, CFGGuider, easy getNode, easy getNode, easy setNode, easy getNode, SamplerCustomAdvanced, RandomNoise, easy getNode, LTXVConditioning, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy setNode, easy setNode, easy setNode, easy getNode, easy getNode, LTXVLatentUpsampler, LTXVCropGuides, VAEDecodeTiled, VAEDecodeTiled, KSamplerSelect, LTXVPreprocess, ManualSigmas, easy getNode, easy getNode, VHS_VideoCombine, CLIPTextEncode, RandomNoise, LTXVConcatAVLatent, LTX2_NAG, ImageResizeKJv2, LTXVScheduler, MarkdownNote, easy setNode, easy int, easy setNode, LTXVPreprocess, easy setNode, easy getNode, MathExpression|pysssss, MathExpression|pysssss, LTXVEmptyLatentAudio, CR Float To Integer, easy getNode, easy getNode, easy getNode, easy setNode, CLIPTextEncode, LTXVSeparateAVLatent, easy getNode, easy getNode, LTXVSeparateAVLatent, easy getNode, LTXVAudioVAEDecode, VHS_VideoCombine, MathExpression|pysssss, LTXVAudioVAEDecode, easy getNode, easy setNode, LoadImage, LoadImage, LoraLoaderModelOnly, DiffusionModelLoaderKJ, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, LTXVImgToVideoInplaceKJ]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3首尾帧生视频（KJ流）_2044379140505214978.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044379140505214978.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（94 个）：
- `LatentUpscaleModelLoader`
- `easy setNode`
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `ImageResizeKJv2`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `easy int`
- `easy int`
- `easy float`
- `easy setNode`
- `easy setNode`
- `EmptyLTXVLatentVideo`
- `easy setNode`
- `easy getNode`
- `easy setNode`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `easy getNode`
- `easy getNode`
- `CFGGuider`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `easy getNode`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `easy getNode`
- `LTXVConditioning`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `VAEDecodeTiled` ★核心
- `VAEDecodeTiled` ★核心
- `KSamplerSelect` ★核心
- `LTXVPreprocess`
- `ManualSigmas`
- `easy getNode`
- `easy getNode`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `LTXVConcatAVLatent`
- `LTX2_NAG`
- `ImageResizeKJv2`
- `LTXVScheduler`
- `MarkdownNote`
- `easy setNode`
- `easy int`
- `easy setNode`
- `LTXVPreprocess`
- `easy setNode`
- `easy getNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `LTXVEmptyLatentAudio` ★核心
- `CR Float To Integer`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `CLIPTextEncode` ★核心
- `LTXVSeparateAVLatent`
- `easy getNode`
- `easy getNode`
- `LTXVSeparateAVLatent`
- `easy getNode`
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `LTXVAudioVAEDecode` ★核心
- `easy getNode`
- `easy setNode`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelLoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LTXVImgToVideoInplaceKJ`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **99%**（93/94）

**有卡**：`LatentUpscaleModelLoader`、`easy setNode`、`easy getNode`、`ImageResizeKJv2`、`easy int`、`easy float`、`EmptyLTXVLatentVideo`、`CFGGuider`、`LTXVConcatAVLatent`、`KSamplerSelect`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVConditioning`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`VAEDecodeTiled`、`LTXVPreprocess`、`ManualSigmas`、`VHS_VideoCombine`、`CLIPTextEncode`、`LTX2_NAG`、`LTXVScheduler`、`MathExpression|pysssss`、`LTXVEmptyLatentAudio`、`CR Float To Integer`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LoadImage`、`LoraLoaderModelOnly`、`DiffusionModelLoaderKJ`、`DualCLIPLoader`、`VAELoaderKJ`、`LTXVImgToVideoInplaceKJ`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
