---
key: 视频生成/文生视频/LTX 2.3 文生视频 + 图生视频 （超清）_2031725601656152066.json
name: LTX 2.3 文生视频 + 图生视频 （超清）_2031725601656152066
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.3 文生视频 + 图生视频 （超清）_2031725601656152066.json
hash: 5d9a05f19da80f62
coverage: 0.461538
learned_at: 2026-10-15 22:44:33
nodes: [LTXVAudioVAEDecode, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVConcatAVLatent, KSamplerSelect, ResizeImagesByLongerEdge, EmptyLTXVLatentVideo, LTXVConcatAVLatent, LTXVEmptyLatentAudio, SimpleCalculatorKJ, LTXVImgToVideoInplace, LTXVLatentUpsampler, KSamplerSelect, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, VAEDecodeTiled, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, LTXVPreprocess, SetNode, SetNode, SetNode, GetNode, SetNode, LTX2SamplingPreviewOverride, SamplerCustom, LTX2SamplingPreviewOverride, SamplerCustom, SetNode, PrimitiveBoolean, VHS_VideoCombine, Seed (rgthree), LatentUpscaleModelLoader, DualCLIPLoader, VAELoader, VAELoaderKJ, GetImageSize, ImageResizeKJv2, SetNode, SetNode, JDC_ResizeFactor, GetNode, Fast Groups Bypasser (rgthree), CLIPTextEncode, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, LTXVChunkFeedForward, PathchSageAttentionKJ, TextInput_, UNETLoader, SetNode, SetNode, LTX2_NAG, GetNode, LTXVConditioning, LTXVScheduler, LTXVScheduler, ManualSigmas, ManualSigmas, GetNode, GetNode, JoinStrings, RH_LLMAPI_NODE, SetNode, CLIPTextEncode, TextInput_, INTConstant, SimpleCalculatorKJ, SetNode, SetNode, SetNode, PrimitiveFloat, GetNode, TextInput_, LoadImage, INTConstant, INTConstant, Text Multiline, ShowText|pysssss, Label (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 121}
---

# 视频生成/文生视频/LTX 2.3 文生视频 + 图生视频 （超清）_2031725601656152066.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.3 文生视频 + 图生视频 （超清）_2031725601656152066.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（117 个）：
- `LTXVAudioVAEDecode` ★核心
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ResizeImagesByLongerEdge`
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
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
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
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVPreprocess`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `LTX2SamplingPreviewOverride`
- `SamplerCustom` ★核心
- `LTX2SamplingPreviewOverride`
- `SamplerCustom` ★核心
- `SetNode`
- `PrimitiveBoolean`
- `VHS_VideoCombine`
- `Seed (rgthree)`
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `GetImageSize`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `JDC_ResizeFactor`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `TextInput_`
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `LTX2_NAG`
- `GetNode`
- `LTXVConditioning`
- `LTXVScheduler`
- `LTXVScheduler`
- `ManualSigmas`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `JoinStrings`
- `RH_LLMAPI_NODE`
- `SetNode`
- `CLIPTextEncode` ★核心
- `TextInput_`
- `INTConstant`
- `SimpleCalculatorKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `GetNode`
- `TextInput_`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `Text Multiline`
- `ShowText|pysssss`
- `Label (rgthree)`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **46%**（54/117）

**有卡**：`LTXVAudioVAEDecode`、`LTXVImgToVideoInplace`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ResizeImagesByLongerEdge`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`SimpleCalculatorKJ`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVPreprocess`、`LTX2SamplingPreviewOverride`、`SamplerCustom`、`PrimitiveBoolean`、`VHS_VideoCombine`、`Seed (rgthree)`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`GetImageSize`、`ImageResizeKJv2`、`JDC_ResizeFactor`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`TextInput_`、`UNETLoader`、`LTX2_NAG`、`LTXVConditioning`、`LTXVScheduler`、`ManualSigmas`、`JoinStrings`、`RH_LLMAPI_NODE`、`INTConstant`、`LoadImage`、`Text Multiline`、`Label (rgthree)`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVLatentUpsampler
