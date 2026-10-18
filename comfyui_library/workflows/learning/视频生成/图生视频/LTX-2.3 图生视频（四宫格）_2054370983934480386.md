---
key: 视频生成/图生视频/LTX-2.3 图生视频（四宫格）_2054370983934480386.json
name: LTX-2.3 图生视频（四宫格）_2054370983934480386.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3 图生视频（四宫格）_2054370983934480386.json
hash: 7b44ac2005172c85
coverage: 0.6
learned_at: 2026-10-15 22:37:46
nodes: [SetNode, GetNode, GetNode, CFGGuider, KSamplerSelect, LTXVLatentUpsampler, GetNode, GetNode, GetNode, ManualSigmas, LTXVImgToVideoConditionOnly, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, RandomNoise, ManualSigmas, GetNode, FloatConstant, GetNode, GetNode, ImageResizeKJv2, ImageResizeKJv2, GetNode, CR Float To Integer, LatentUpscaleModelLoader, LoraLoaderModelOnly, CheckpointLoaderSimple, LTXVAudioVAELoader, SetNode, SetNode, SetNode, SetNode, JoinStrings, Text Multiline, Text Multiline, Qwen3_VQA, easy showAnything, ImageResizeKJv2, ImageResizeKJv2, PrimitiveFloat, INTConstant, SimpleMath+, SetNode, LTXVConditioning, GetNode, LTXVConcatAVLatent, ComfyMathExpression, GetNode, GetNode, VAEDecodeTiled, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, VHS_VideoCombine, LTXAVTextEncoderLoader, CLIPTextEncode, CLIPTextEncode, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVImgToVideoInplaceKJ, LTXVEmptyLatentAudio, ImageScaleBy, GuHaiAutoImageSplit, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, PreviewImage, LoadImage, TTResolutionSelector, LTXVSeparateAVLatent, SamplerCustomAdvanced, CFGGuider, KSamplerSelect, RandomNoise, GetNode, LTXVConcatAVLatent]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX-2.3 图生视频（四宫格）_2054370983934480386.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2054370983934480386.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（85 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `LTXVImgToVideoConditionOnly`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `RandomNoise`
- `ManualSigmas`
- `GetNode`
- `FloatConstant`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `GetNode`
- `CR Float To Integer`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `JoinStrings`
- `Text Multiline`
- `Text Multiline`
- `Qwen3_VQA`
- `easy showAnything`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `PrimitiveFloat`
- `INTConstant`
- `SimpleMath+`
- `SetNode`
- `LTXVConditioning`
- `GetNode`
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplaceKJ`
- `LTXVEmptyLatentAudio` ★核心
- `ImageScaleBy`
- `GuHaiAutoImageSplit`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `LoadImage`
- `TTResolutionSelector`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `GetNode`
- `LTXVConcatAVLatent`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **60%**（51/85）

**有卡**：`CFGGuider`、`KSamplerSelect`、`LTXVLatentUpsampler`、`ManualSigmas`、`LTXVImgToVideoConditionOnly`、`EmptyLTXVLatentVideo`、`RandomNoise`、`FloatConstant`、`ImageResizeKJv2`、`CR Float To Integer`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`JoinStrings`、`Text Multiline`、`Qwen3_VQA`、`INTConstant`、`SimpleMath+`、`LTXVConditioning`、`LTXVConcatAVLatent`、`ComfyMathExpression`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVImgToVideoInplaceKJ`、`LTXVEmptyLatentAudio`、`ImageScaleBy`、`GuHaiAutoImageSplit`、`ImageFromBatch+`、`LoadImage`、`TTResolutionSelector`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
