---
key: 视频生成/图生视频/LTX2.3+文生视频+图生视频(二合一工作流)_2031341493738283009.json
name: LTX2.3+文生视频+图生视频(二合一工作流)_2031341493738283009.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3+文生视频+图生视频(二合一工作流)_2031341493738283009.json
hash: 6b44350e9f0ac3b4
coverage: 0.459677
learned_at: 2026-10-15 22:35:30
nodes: [LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVConcatAVLatent, LTXVEmptyLatentAudio, SimpleCalculatorKJ, LTXVImgToVideoInplace, LTXVLatentUpsampler, KSamplerSelect, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SamplerCustom, LatentUpscaleModelLoader, DualCLIPLoader, VAELoader, VAELoaderKJ, SetNode, SetNode, SetNode, LTXVConditioning, ManualSigmas, CLIPTextEncode, TextInput_, SamplerCustom, LoraLoaderModelOnly, UNETLoader, SetNode, SetNode, JDC_ResizeFactor, GetImageSize, SetNode, SetNode, GetNode, SimpleCalculatorKJ, SetNode, SetNode, LTXVPreprocess, ResizeImagesByLongerEdge, ShowText|pysssss, JoinStrings, LTXVSeparateAVLatent, LoadImage, ImageResizeKJv2, GetNode, TextInput_, GetNode, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, SetNode, PathchSageAttentionKJ, LTXVChunkFeedForward, SetNode, GetNode, GetNode, MarkdownNote, LoadImage, PrimitiveFloat, RH_LLMAPI_NODE, SetNode, GetNode, LTXVScheduler, VAEDecodeTiled, PlaySound|pysssss, PlaySound|pysssss, PlaySound|pysssss, GetNode, SetNode, GetNode, LTXVScheduler, ManualSigmas, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, LTX2SamplingPreviewOverride, GetNode, SetNode, KSamplerSelect, GetNode, GetNode, LTX2SamplingPreviewOverride, GetNode, GetNode, GetNode, SetNode, PrimitiveBoolean, CLIPTextEncode, AnySwitch, GetNode, easy showAnything, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), SetNode, SetNode, GetNode, LTX2_NAG, SetNode, TextInput_, VHS_VideoCombine, INTConstant, Seed (rgthree), INTConstant, INTConstant]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 121}
---

# 视频生成/图生视频/LTX2.3+文生视频+图生视频(二合一工作流)_2031341493738283009.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031341493738283009.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（124 个）：
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `SimpleCalculatorKJ`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SamplerCustom` ★核心
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVConditioning`
- `ManualSigmas`
- `CLIPTextEncode` ★核心
- `TextInput_`
- `SamplerCustom` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `JDC_ResizeFactor`
- `GetImageSize`
- `SetNode`
- `SetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `SetNode`
- `SetNode`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `ShowText|pysssss`
- `JoinStrings`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ImageResizeKJv2`
- `GetNode`
- `TextInput_`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `SetNode`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `SetNode`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `LoadImage`
- `PrimitiveFloat`
- `RH_LLMAPI_NODE`
- `SetNode`
- `GetNode`
- `LTXVScheduler`
- `VAEDecodeTiled` ★核心
- `PlaySound|pysssss`
- `PlaySound|pysssss`
- `PlaySound|pysssss`
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVScheduler`
- `ManualSigmas`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `AnySwitch`
- `GetNode`
- `easy showAnything`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTX2_NAG`
- `SetNode`
- `TextInput_`
- `VHS_VideoCombine`
- `INTConstant`
- `Seed (rgthree)`
- `INTConstant`
- `INTConstant`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **46%**（57/124）

**有卡**：`LTXVImgToVideoInplace`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`SimpleCalculatorKJ`、`LTXVLatentUpsampler`、`KSamplerSelect`、`SamplerCustom`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`LTXVConditioning`、`ManualSigmas`、`CLIPTextEncode`、`TextInput_`、`LoraLoaderModelOnly`、`UNETLoader`、`JDC_ResizeFactor`、`GetImageSize`、`LTXVPreprocess`、`ResizeImagesByLongerEdge`、`JoinStrings`、`LoadImage`、`ImageResizeKJv2`、`LTXVAudioVAEDecode`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`RH_LLMAPI_NODE`、`LTXVScheduler`、`VAEDecodeTiled`、`PlaySound|pysssss`、`LTX2SamplingPreviewOverride`、`PrimitiveBoolean`、`AnySwitch`、`LTX2_NAG`、`VHS_VideoCombine`、`INTConstant`、`Seed (rgthree)`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVLatentUpsampler
