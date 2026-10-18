---
key: 视频生成/图生视频/LTX2.3-transition-lora-丝滑转场-首尾帧视频-自动提示词_2037153504921391105.json
name: LTX2.3-transition-lora-丝滑转场-首尾帧视频-自动提示词_2037153504921391105.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-transition-lora-丝滑转场-首尾帧视频-自动提示词_2037153504921391105.json
hash: cb6a30923a30b41e
coverage: 0.915254
learned_at: 2026-10-15 22:35:55
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, Reroute, SamplerCustomAdvanced, LTXVSeparateAVLatent, PrimitiveBoolean, ComfyMathExpression, EmptyLTXVLatentVideo, ResizeImageMaskNode, ResizeImagesByLongerEdge, ImageResizeKJv2, ResizeImagesByLongerEdge, LTXVPreprocess, LTXVPreprocess, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, LTXVLatentUpsampler, CreateVideo, ManualSigmas, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVImgToVideoInplace, CFGGuider, KSamplerSelect, LTXVCropGuides, ComfyMathExpression, PrimitiveStringMultiline, Int, Int, SimpleMath+, Int, JWFloat, UNETLoader, LTXVAddGuideMulti, JjkText, RH_LLMAPI_Pro_Node, LoadImage, CustomAddLabel, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVEmptyLatentAudio, ComfyMathExpression, VHS_VideoCombine, VHS_VideoCombine, LatentUpscaleModelLoader, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, LoraLoaderModelOnly, MarkdownNote, MarkdownNote, ShowText, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3-transition-lora-丝滑转场-首尾帧视频-自动提示词_2037153504921391105.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037153504921391105.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（59 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `PrimitiveBoolean`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVLatentUpsampler` ★核心
- `CreateVideo`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVCropGuides`
- `ComfyMathExpression`
- `PrimitiveStringMultiline`
- `Int`
- `Int`
- `SimpleMath+`
- `Int`
- `JWFloat`
- `UNETLoader` ★核心
- `LTXVAddGuideMulti`
- `JjkText`
- `RH_LLMAPI_Pro_Node`
- `LoadImage`
- `CustomAddLabel`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `ShowText`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（54/59）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`PrimitiveBoolean`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`ImageResizeKJv2`、`LTXVPreprocess`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVLatentUpsampler`、`CreateVideo`、`LTXVImgToVideoInplace`、`LTXVCropGuides`、`Int`、`SimpleMath+`、`JWFloat`、`UNETLoader`、`LTXVAddGuideMulti`、`RH_LLMAPI_Pro_Node`、`LoadImage`、`CustomAddLabel`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`VHS_VideoCombine`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`LoraLoaderModelOnly`、`ShowText`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
