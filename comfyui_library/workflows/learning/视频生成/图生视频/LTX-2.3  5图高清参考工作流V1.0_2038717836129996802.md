---
key: 视频生成/图生视频/LTX-2.3  5图高清参考工作流V1.0_2038717836129996802.json
name: LTX-2.3  5图高清参考工作流V1.0_2038717836129996802.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3  5图高清参考工作流V1.0_2038717836129996802.json
hash: 16730770201943c3
coverage: 0.902778
learned_at: 2026-10-15 22:36:04
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, Reroute, SamplerCustomAdvanced, LTXVSeparateAVLatent, LatentUpscaleModelLoader, KSamplerSelect, LTXVSeparateAVLatent, LTXVConditioning, LTXVLatentUpsampler, VAELoaderKJ, DualCLIPLoader, PrimitiveBoolean, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, VAELoaderKJ, EmptyLTXVLatentVideo, ResizeImageMaskNode, PrimitiveInt, PrimitiveInt, ResizeImagesByLongerEdge, ImageResizeKJv2, ResizeImagesByLongerEdge, ManualSigmas, LTXVEmptyLatentAudio, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, ResizeImagesByLongerEdge, ImageResizeKJv2, CFGGuider, LTXVImgToVideoInplace, CLIPTextEncode, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, ImageResizeKJv2, ComfyMathExpression, CLIPTextEncode, PrimitiveInt, LTXVPreprocess, LTXVPreprocess, PrimitiveStringMultiline, UNETLoader, LoraLoaderModelOnly, LTXVImgToVideoInplaceKJ, SaveVideo, LTXVPreprocess, LTXVPreprocess, ImageResizeKJv2, LTXVPreprocess, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, RH_LLMAPI_Pro_Node, LTXVConcatAVLatent, PreviewAny, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX-2.3  5图高清参考工作流V1.0_2038717836129996802.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2038717836129996802.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConditioning`
- `LTXVLatentUpsampler` ★核心
- `VAELoaderKJ`
- `DualCLIPLoader`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `VAELoaderKJ`
- `EmptyLTXVLatentVideo`
- `ResizeImageMaskNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `ResizeImagesByLongerEdge`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `ManualSigmas`
- `LTXVEmptyLatentAudio` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `ResizeImagesByLongerEdge`
- `ImageResizeKJv2`
- `CFGGuider`
- `LTXVImgToVideoInplace`
- `CLIPTextEncode` ★核心
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `ImageResizeKJv2`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVImgToVideoInplaceKJ`
- `SaveVideo`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `RH_LLMAPI_Pro_Node`
- `LTXVConcatAVLatent`
- `PreviewAny`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（65/72）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`LTXVConditioning`、`LTXVLatentUpsampler`、`VAELoaderKJ`、`DualCLIPLoader`、`PrimitiveBoolean`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`ImageResizeKJv2`、`LTXVEmptyLatentAudio`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`LTXVImgToVideoInplace`、`CLIPTextEncode`、`LTXVPreprocess`、`UNETLoader`、`LoraLoaderModelOnly`、`LTXVImgToVideoInplaceKJ`、`SaveVideo`、`LoadImage`、`RH_LLMAPI_Pro_Node`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
