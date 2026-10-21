---
key: 图片生成/文生图/万象AI真人短剧专用文_图生视频工作流（LTX2.3自动提示词优化版10秒）自动横屏竖屏_2037526578241998850.json
name: 万象AI真人短剧专用文_图生视频工作流（LTX2.3自动提示词优化版10秒）自动横屏竖屏_2037526578241998850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/万象AI真人短剧专用文_图生视频工作流（LTX2.3自动提示词优化版10秒）自动横屏竖屏_2037526578241998850.json
hash: cc64e79de98eb5c6
coverage: 0.851852
learned_at: 2026-10-21 02:58:23
nodes: [LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, KSamplerSelect, Reroute, LTXVImgToVideoInplace, LTXVAudioVAEDecode, CLIPTextEncode, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, ComfyMathExpression, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, LTXVAudioVAELoader, CFGGuider, LTXVConditioning, ResizeImageMaskNode, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LatentUpscaleModelLoader, RandomNoise, RandomNoise, LTXAVTextEncoderLoader, ManualSigmas, CLIPTextEncode, PrimitiveInt, CreateVideo, ResizeImagesByLongerEdge, LTXVPreprocess, PrimitiveBoolean, RH_LLMAPI_Pro_Node, MarkdownNote, PrimitiveInt, PrimitiveStringMultiline, CheckpointLoaderSimple, LoraLoaderModelOnly, PrimitiveStringMultiline, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, CR Text, CR Text, easy showAnything, CR Text, SaveVideo, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 图片生成/文生图/万象AI真人短剧专用文_图生视频工作流（LTX2.3自动提示词优化版10秒）自动横屏竖屏_2037526578241998850.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/万象AI真人短剧专用文_图生视频工作流（LTX2.3自动提示词优化版10秒）自动横屏竖屏_2037526578241998850.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVImgToVideoInplace`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `ComfyMathExpression`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVAudioVAELoader`
- `CFGGuider`
- `LTXVConditioning`
- `ResizeImageMaskNode`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `RandomNoise`
- `LTXAVTextEncoderLoader`
- `ManualSigmas`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `CreateVideo`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `PrimitiveBoolean`
- `RH_LLMAPI_Pro_Node`
- `MarkdownNote`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `CR Text`
- `easy showAnything`
- `CR Text`
- `SaveVideo`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **85%**（46/54）

**有卡**：`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`ComfyMathExpression`、`LTXVAudioVAELoader`、`LTXVConditioning`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`LatentUpscaleModelLoader`、`RandomNoise`、`LTXAVTextEncoderLoader`、`CreateVideo`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`PrimitiveBoolean`、`RH_LLMAPI_Pro_Node`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Text`、`SaveVideo`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
