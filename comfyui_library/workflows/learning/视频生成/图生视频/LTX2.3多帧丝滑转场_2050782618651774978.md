---
key: 视频生成/图生视频/LTX2.3多帧丝滑转场_2050782618651774978.json
name: LTX2.3多帧丝滑转场_2050782618651774978.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3多帧丝滑转场_2050782618651774978.json
hash: a27fcdf65a8f2646
coverage: 0.567568
learned_at: 2026-10-15 22:37:19
nodes: [GetNode, GetNode, SimpleCalculatorKJ, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SamplerCustomAdvanced, LTXVEmptyLatentAudio, GetNode, GetNode, GetNode, LTX2_NAG, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, LTXVImgToVideoInplace, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, LTXVLatentUpsampler, LTXVSeparateAVLatent, CFGGuider, GetNode, SamplerCustomAdvanced, CFGGuider, KSamplerSelect, SetNode, GetNode, GetNode, RandomNoise, KSamplerSelect, ManualSigmas, LTXVScheduler, SetNode, VAELoader, VAELoaderKJ, VAELoader, LatentUpscaleModelLoader, ImageResizeKJv2, SetNode, LTXVConcatAVLatent, LTXVConditioning, EmptyLTXVLatentVideo, LTX2SamplingPreviewOverride, LatentUpscaleModelLoader, LTXVSeparateAVLatent, GetNode, ManualSigmas, ManualSigmas, LTXVAudioVAEDecode, SetNode, SetNode, UNETLoader, DualCLIPLoader, RandomNoise, ImageScaleBy, GetImageSize, ResizeImagesByLongerEdge, ImageResizeKJv2, SetNode, ImageResizeKJv2, ResizeImagesByLongerEdge, GetNode, ResizeImagesByLongerEdge, LTXVPreprocess, LTXVPreprocess, LTXVPreprocess, INTConstant, INTConstant, MathExpression|pysssss, GetNode, SetNode, SimpleCalculatorKJ, INTConstant, CLIPTextEncode, GetNode, PrimitiveFloat, Seed (rgthree), CLIPTextEncode, LoadImage, TTP_text_mix, SeedGenerator, LoadImage, LoadImage, TextInput_, VHS_VideoCombine, GetNode, CreateVideo, GetNode, VAEDecodeTiled, SaveVideo, LoraLoaderModelOnly, LTXVImgToVideoInplaceKJ]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3多帧丝滑转场_2050782618651774978.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2050782618651774978.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（111 个）：
- `GetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `GetNode`
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
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVScheduler`
- `SetNode`
- `VAELoader`
- `VAELoaderKJ`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `ImageResizeKJv2`
- `SetNode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTX2SamplingPreviewOverride`
- `LatentUpscaleModelLoader`
- `LTXVSeparateAVLatent`
- `GetNode`
- `ManualSigmas`
- `ManualSigmas`
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `SetNode`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `RandomNoise`
- `ImageScaleBy`
- `GetImageSize`
- `ResizeImagesByLongerEdge`
- `ImageResizeKJv2`
- `SetNode`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `INTConstant`
- `INTConstant`
- `MathExpression|pysssss`
- `GetNode`
- `SetNode`
- `SimpleCalculatorKJ`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `GetNode`
- `PrimitiveFloat`
- `Seed (rgthree)`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `TTP_text_mix`
- `SeedGenerator`
- `LoadImage`
- `LoadImage`
- `TextInput_`
- `VHS_VideoCombine`
- `GetNode`
- `CreateVideo`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `SaveVideo`
- `LoraLoaderModelOnly` ★核心
- `LTXVImgToVideoInplaceKJ`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **57%**（63/111）

**有卡**：`SimpleCalculatorKJ`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`LTX2_NAG`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`ManualSigmas`、`LTXVScheduler`、`VAELoader`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`ImageResizeKJv2`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTX2SamplingPreviewOverride`、`LTXVAudioVAEDecode`、`UNETLoader`、`DualCLIPLoader`、`ImageScaleBy`、`GetImageSize`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`INTConstant`、`MathExpression|pysssss`、`CLIPTextEncode`、`Seed (rgthree)`、`LoadImage`、`TTP_text_mix`、`SeedGenerator`、`TextInput_`、`VHS_VideoCombine`、`CreateVideo`、`VAEDecodeTiled`、`SaveVideo`、`LoraLoaderModelOnly`、`LTXVImgToVideoInplaceKJ`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
