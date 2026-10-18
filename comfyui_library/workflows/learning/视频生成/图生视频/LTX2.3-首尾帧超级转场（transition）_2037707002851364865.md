---
key: 视频生成/图生视频/LTX2.3-首尾帧超级转场（transition）_2037707002851364865.json
name: LTX2.3-首尾帧超级转场（transition）_2037707002851364865.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-首尾帧超级转场（transition）_2037707002851364865.json
hash: 83fb55390a25df4a
coverage: 0.943396
learned_at: 2026-10-15 22:35:58
nodes: [SamplerCustomAdvanced, LTXVSeparateAVLatent, CreateVideo, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVAudioVAEDecode, ComfyMathExpression, ImageResizeKJv2, ImageResizeKJv2, PrimitiveInt, SimpleMath+, PrimitiveInt, LatentUpscaleModelLoader, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, RH_LLMAPI_Pro_Node, ShowText|pysssss, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, LTXVPreprocess, LTXVPreprocess, ManualSigmas, Text, LTXVCropGuides, CLIPTextEncode, LTXVImgToVideoInplace, RandomNoise, CFGGuider, KSamplerSelect, LTXVConcatAVLatent, LTXVConditioning, CFGGuider, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVAddGuideMulti, SaveVideo, LoadImage, Text, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, LoadImage, ResizeImagesByLongerEdge, ImageSizeInfo, ComfyMathExpression, ComfyMathExpression]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3-首尾帧超级转场（transition）_2037707002851364865.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037707002851364865.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVAudioVAEDecode` ★核心
- `ComfyMathExpression`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `PrimitiveInt`
- `SimpleMath+`
- `PrimitiveInt`
- `LatentUpscaleModelLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `RH_LLMAPI_Pro_Node`
- `ShowText|pysssss`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `LTXVPreprocess`
- `ManualSigmas`
- `Text`
- `LTXVCropGuides`
- `CLIPTextEncode` ★核心
- `LTXVImgToVideoInplace`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVAddGuideMulti`
- `SaveVideo`
- `LoadImage`
- `Text`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `ResizeImagesByLongerEdge`
- `ImageSizeInfo`
- `ComfyMathExpression`
- `ComfyMathExpression`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（50/53）

**有卡**：`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`CreateVideo`、`RandomNoise`、`VAEDecodeTiled`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`ComfyMathExpression`、`ImageResizeKJv2`、`SimpleMath+`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`RH_LLMAPI_Pro_Node`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`LTXVPreprocess`、`ManualSigmas`、`Text`、`LTXVCropGuides`、`LTXVImgToVideoInplace`、`CFGGuider`、`KSamplerSelect`、`LTXVConcatAVLatent`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVAddGuideMulti`、`SaveVideo`、`LoadImage`、`ResizeImagesByLongerEdge`、`ImageSizeInfo`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
