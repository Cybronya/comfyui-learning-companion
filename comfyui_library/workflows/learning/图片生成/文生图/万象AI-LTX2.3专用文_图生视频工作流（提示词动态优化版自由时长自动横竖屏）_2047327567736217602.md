---
key: 图片生成/文生图/万象AI-LTX2.3专用文_图生视频工作流（提示词动态优化版自由时长自动横竖屏）_2047327567736217602.json
name: 万象AI-LTX2.3专用文_图生视频工作流（提示词动态优化版自由时长自动横竖屏）_2047327567736217602
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/万象AI-LTX2.3专用文_图生视频工作流（提示词动态优化版自由时长自动横竖屏）_2047327567736217602.json
hash: a06681b0e8ebae93
coverage: 0.84127
learned_at: 2026-10-21 02:58:22
nodes: [LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, LTXVLatentUpsampler, LTXVImgToVideoInplace, KSamplerSelect, Reroute, LTXVImgToVideoInplace, LTXVAudioVAEDecode, LTXVEmptyLatentAudio, VAEDecodeTiled, ComfyMathExpression, ComfyMathExpression, CFGGuider, ResizeImageMaskNode, LTXVConcatAVLatent, EmptyLTXVLatentVideo, RandomNoise, RandomNoise, ManualSigmas, ComfyMathExpression, LTXVCropGuides, SamplerCustomAdvanced, LTXVSeparateAVLatent, LoadImage, LoadAudio, GetAudioDurationFromAudio, Int, PrimitiveInt, easy showAnything, easy promptReplace, MathExpression|pysssss, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, MarkdownNote, RH_LLMAPI_NODE, PrimitiveBoolean, PrimitiveStringMultiline, PrimitiveInt, CR Integer To String, ResizeImagesByLongerEdge, LTXVPreprocess, CR Text, easy showAnything, LatentUpscaleModelLoader, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LoraLoaderModelOnly, CheckpointLoaderSimple, LoraLoaderModelOnly, PrimitiveStringMultiline, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, SamplerCustomAdvanced, LTXVSeparateAVLatent, CreateVideo, SaveVideo, CR Text, CR Text, PrimitiveInt, RH_LLMAPI_Pro_Node]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 图片生成/文生图/万象AI-LTX2.3专用文_图生视频工作流（提示词动态优化版自由时长自动横竖屏）_2047327567736217602.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/万象AI-LTX2.3专用文_图生视频工作流（提示词动态优化版自由时长自动横竖屏）_2047327567736217602.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVImgToVideoInplace`
- `LTXVAudioVAEDecode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `VAEDecodeTiled` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `CFGGuider`
- `ResizeImageMaskNode`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `RandomNoise`
- `RandomNoise`
- `ManualSigmas`
- `ComfyMathExpression`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoadAudio`
- `GetAudioDurationFromAudio`
- `Int`
- `PrimitiveInt`
- `easy showAnything`
- `easy promptReplace`
- `MathExpression|pysssss`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MarkdownNote`
- `RH_LLMAPI_NODE`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `CR Integer To String`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `CR Text`
- `easy showAnything`
- `LatentUpscaleModelLoader`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `SaveVideo`
- `CR Text`
- `CR Text`
- `PrimitiveInt`
- `RH_LLMAPI_Pro_Node`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **84%**（53/63）

**有卡**：`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`VAEDecodeTiled`、`ComfyMathExpression`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`RandomNoise`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LoadImage`、`LoadAudio`、`GetAudioDurationFromAudio`、`Int`、`easy promptReplace`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`RH_LLMAPI_NODE`、`PrimitiveBoolean`、`CR Integer To String`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`CR Text`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`LTXVConditioning`、`CreateVideo`、`SaveVideo`、`RH_LLMAPI_Pro_Node`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
