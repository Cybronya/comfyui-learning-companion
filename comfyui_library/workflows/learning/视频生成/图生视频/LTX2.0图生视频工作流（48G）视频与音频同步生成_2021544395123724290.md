---
key: 视频生成/图生视频/LTX2.0图生视频工作流（48G）视频与音频同步生成_2021544395123724290.json
name: LTX2.0图生视频工作流（48G）视频与音频同步生成_2021544395123724290.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2021544395123724290.json
hash: 0f8889f83474aeb8
coverage: 0.910714
learned_at: 2026-10-15 22:35:09
nodes: [KSamplerSelect, LTXVScheduler, KSamplerSelect, ManualSigmas, LatentUpscaleModelLoader, LTXVCropGuides, CFGGuider, LTXVEmptyLatentAudio, CLIPTextEncode, RandomNoise, SamplerCustomAdvanced, LTXVLatentUpsampler, ImageScaleBy, GetImageSize, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, CFGGuider, ResizeImagesByLongerEdge, LTXVPreprocess, LoraLoaderModelOnly, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVConcatAVLatent, MarkdownNote, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, EmptyImage, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecode, LTXVAudioVAEDecode, RandomNoise, CLIPTextEncode, ImageResizeKJv2, PrimitiveInt, GetImageSize, DF_Int_to_Float, LayerUtility: ImageScaleByAspectRatio V2, Int, LTXVSeparateAVLatent, VAEDecode, LTXVAudioVAEDecode, LTXVConditioning, SetNode, MathExpression|pysssss, Int, GetNode, VHS_VideoCombine, VHS_VideoCombine, Int, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.0图生视频工作流（48G）视频与音频同步生成_2021544395123724290.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2021544395123724290.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（56 个）：
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LatentUpscaleModelLoader`
- `LTXVCropGuides`
- `CFGGuider`
- `LTXVEmptyLatentAudio` ★核心
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `ImageScaleBy`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LoraLoaderModelOnly` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVConcatAVLatent`
- `MarkdownNote`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `EmptyImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `PrimitiveInt`
- `GetImageSize`
- `DF_Int_to_Float`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `SetNode`
- `MathExpression|pysssss`
- `Int`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Int`
- `LoadImage`
- `CR Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **91%**（51/56）

**有卡**：`KSamplerSelect`、`LTXVScheduler`、`ManualSigmas`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`CFGGuider`、`LTXVEmptyLatentAudio`、`CLIPTextEncode`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`ImageScaleBy`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LoraLoaderModelOnly`、`LTXVConcatAVLatent`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`EmptyImage`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVAudioVAEDecode`、`ImageResizeKJv2`、`DF_Int_to_Float`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`LTXVConditioning`、`MathExpression|pysssss`、`VHS_VideoCombine`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
