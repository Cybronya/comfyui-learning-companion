---
key: 视频生成/图生视频/LTX2.3-首尾帧超级转场（transition）_2037157386359672834.json
name: LTX2.3-首尾帧超级转场（transition）_2037157386359672834.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2037157386359672834.json
hash: c8329a1f3002127c
coverage: 0.90566
learned_at: 2026-10-15 22:35:55
nodes: [SamplerCustomAdvanced, ResizeImagesByLongerEdge, LoadImage, LatentUpscaleModelLoader, VAELoaderKJ, DualCLIPLoader, UNETLoader, CLIPTextEncode, LTXVPreprocess, LTXVPreprocess, Text, CLIPTextEncode, RandomNoise, LoadImage, LTXVAudioVAEDecode, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, ResizeImagesByLongerEdge, ImageResizeKJv2, ManualSigmas, LTXVConcatAVLatent, CFGGuider, KSamplerSelect, PrimitiveInt, LTXVEmptyLatentAudio, ImageResizeKJv2, ComfyMathExpression, PrimitiveInt, VAELoaderKJ, LoraLoaderModelOnly, KSamplerSelect, LTXVSeparateAVLatent, Text, RH_LLMAPI_Pro_Node, LTXVCropGuides, LTXVSeparateAVLatent, VAEDecodeTiled, SamplerCustomAdvanced, PrimitiveInt, SimpleMath+, LTXVConditioning, CreateVideo, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVConcatAVLatent, ManualSigmas, RandomNoise, CFGGuider, EmptyLTXVLatentVideo, SaveVideo, LTXVAddGuideMulti, ShowText|pysssss]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3-首尾帧超级转场（transition）_2037157386359672834.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037157386359672834.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `SamplerCustomAdvanced` ★核心
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `LatentUpscaleModelLoader`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `LTXVPreprocess`
- `Text`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `LoadImage`
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ResizeImagesByLongerEdge`
- `ImageResizeKJv2`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `PrimitiveInt`
- `LTXVEmptyLatentAudio` ★核心
- `ImageResizeKJv2`
- `ComfyMathExpression`
- `PrimitiveInt`
- `VAELoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `Text`
- `RH_LLMAPI_Pro_Node`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `SamplerCustomAdvanced` ★核心
- `PrimitiveInt`
- `SimpleMath+`
- `LTXVConditioning`
- `CreateVideo`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `RandomNoise`
- `CFGGuider`
- `EmptyLTXVLatentVideo`
- `SaveVideo`
- `LTXVAddGuideMulti`
- `ShowText|pysssss`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（48/53）

**有卡**：`SamplerCustomAdvanced`、`ResizeImagesByLongerEdge`、`LoadImage`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`LTXVPreprocess`、`Text`、`RandomNoise`、`LTXVAudioVAEDecode`、`ComfyMathExpression`、`ImageResizeKJv2`、`ManualSigmas`、`LTXVConcatAVLatent`、`CFGGuider`、`KSamplerSelect`、`LTXVEmptyLatentAudio`、`LoraLoaderModelOnly`、`LTXVSeparateAVLatent`、`RH_LLMAPI_Pro_Node`、`LTXVCropGuides`、`VAEDecodeTiled`、`SimpleMath+`、`LTXVConditioning`、`CreateVideo`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`EmptyLTXVLatentVideo`、`SaveVideo`、`LTXVAddGuideMulti`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
