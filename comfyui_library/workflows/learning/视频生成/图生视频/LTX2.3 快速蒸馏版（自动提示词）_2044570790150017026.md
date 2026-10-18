---
key: 视频生成/图生视频/LTX2.3 快速蒸馏版（自动提示词）_2044570790150017026.json
name: LTX2.3 快速蒸馏版（自动提示词）_2044570790150017026.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 快速蒸馏版（自动提示词）_2044570790150017026.json
hash: 462a4b25b2ccf938
coverage: 0.578431
learned_at: 2026-10-15 22:36:38
nodes: [GetNode, GetNode, SimpleCalculatorKJ, GetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SamplerCustomAdvanced, LTXVEmptyLatentAudio, GetNode, GetNode, GetNode, LTX2_NAG, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, LTXVImgToVideoInplace, GetNode, GetNode, ResizeImagesByLongerEdge, GetNode, SetNode, SetNode, GetNode, GetNode, LTXVSeparateAVLatent, GetNode, RandomNoise, SamplerCustomAdvanced, CFGGuider, KSamplerSelect, SetNode, GetNode, RandomNoise, KSamplerSelect, SetNode, ImageScaleBy, SetNode, LTXVPreprocess, ResizeImagesByLongerEdge, GetImageSize, LTXVPreprocess, LTXVConditioning, EmptyLTXVLatentVideo, LTXVSeparateAVLatent, GetNode, Seed (rgthree), SetNode, SimpleCalculatorKJ, SetNode, SetNode, GetNode, GetNode, CFGGuider, LTXVScheduler, CLIPTextEncode, LTXVLatentUpsampler, LatentUpscaleModelLoader, INTConstant, INTConstant, LTX2SamplingPreviewOverride, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVConcatAVLatent, ManualSigmas, ManualSigmas, LoraLoaderModelOnly, ManualSigmas, VHS_VideoCombine, INTConstant, RH_LLMAPI_Pro_Node, CR Text, GetNode, VAELoader, VAELoaderKJ, ConcatTextOfUtils, PrimitiveFloat, CLIPTextEncode, LTXVImgToVideoConditionOnly, SetNode, VAELoader, DualCLIPLoader, LatentUpscaleModelLoader, LoraLoaderModelOnly, UNETLoader, ImageResizeKJv2, LoadImage, CR Text, LoadImage, CR Prompt Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 快速蒸馏版（自动提示词）_2044570790150017026.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044570790150017026.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（102 个）：
- `GetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTX2_NAG`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `GetNode`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SetNode`
- `GetNode`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `SetNode`
- `ImageScaleBy`
- `SetNode`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `GetImageSize`
- `LTXVPreprocess`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVSeparateAVLatent`
- `GetNode`
- `Seed (rgthree)`
- `SetNode`
- `SimpleCalculatorKJ`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `LTXVScheduler`
- `CLIPTextEncode` ★核心
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `INTConstant`
- `INTConstant`
- `LTX2SamplingPreviewOverride`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `ManualSigmas`
- `LoraLoaderModelOnly` ★核心
- `ManualSigmas`
- `VHS_VideoCombine`
- `INTConstant`
- `RH_LLMAPI_Pro_Node`
- `CR Text`
- `GetNode`
- `VAELoader`
- `VAELoaderKJ`
- `ConcatTextOfUtils`
- `PrimitiveFloat`
- `CLIPTextEncode` ★核心
- `LTXVImgToVideoConditionOnly`
- `SetNode`
- `VAELoader`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ImageResizeKJv2`
- `LoadImage`
- `CR Text`
- `LoadImage`
- `CR Prompt Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **58%**（59/102）

**有卡**：`SimpleCalculatorKJ`、`ImageResizeKJv2`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`LTX2_NAG`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplace`、`ResizeImagesByLongerEdge`、`LTXVSeparateAVLatent`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`ImageScaleBy`、`LTXVPreprocess`、`GetImageSize`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`Seed (rgthree)`、`LTXVScheduler`、`CLIPTextEncode`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`INTConstant`、`LTX2SamplingPreviewOverride`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`ManualSigmas`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`RH_LLMAPI_Pro_Node`、`CR Text`、`VAELoader`、`VAELoaderKJ`、`ConcatTextOfUtils`、`LTXVImgToVideoConditionOnly`、`DualCLIPLoader`、`UNETLoader`、`LoadImage`、`CR Prompt Text`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
