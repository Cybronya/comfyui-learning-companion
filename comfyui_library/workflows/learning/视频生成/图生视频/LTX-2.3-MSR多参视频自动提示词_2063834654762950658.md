---
key: 视频生成/图生视频/LTX-2.3-MSR多参视频自动提示词_2063834654762950658.json
name: LTX-2.3-MSR多参视频自动提示词_2063834654762950658.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2063834654762950658.json
hash: bbc300759456e668
coverage: 0.453488
learned_at: 2026-10-15 22:39:18
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SimpleCalculatorKJ, GetNode, SetNode, SetNode, SetNode, GetNode, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, PathchSageAttentionKJ, LTXVChunkFeedForward, LTX2AttentionTunerPatch, SetNode, GetNode, INTConstant, SetNode, SetNode, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, GetNode, SetNode, GetNode, GetNode, SamplerCustomAdvanced, ComfySwitchNode, GetNode, LTX2_NAG, RandomNoise, ManualSigmas, GetNode, RMBG, LatentUpscaleModelLoader, VAELoader, VAELoaderKJ, VAELoader, LoraLoaderModelOnly, GetNode, ComfyMathExpression, SetNode, ComfySwitchNode, ComfySwitchNode, LTXVEmptyLatentAudio, SamplerCustomAdvanced, UNETLoader, SetNode, LTXVAudioVAEDecode, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, KSamplerSelect, SeedGenerator, VAEDecode, GetNode, GetNode, SetNode, SetNode, LTXVConcatAVLatent, Reroute, Reroute, Reroute, PrimitiveFloat, DualCLIPLoader, ImageBatchMulti, LTXVAudioVAEDecode, Reroute, Reroute, Reroute, GetNode, SetNode, LTXVSeparateAVLatent, GetNode, GetNode, ComfySwitchNode, VAEDecode, GetNode, GetNode, GetNode, ComfySwitchNode, GetNode, LTXVCropGuides, GetNode, GetNode, ImageBatchMulti, SetNode, GetNode, LTXVCropGuides, KSamplerSelect, RandomNoise, CFGGuider, LTXVAddGuidesFromBatch, LoadImage, LoadImage, CreateVideo, INTConstant, INTConstant, LTXVConditioning, RH_LLMAPI_NODE, TTP_text_mix, CLIPTextEncode, CLIPTextEncode, TextInput_, VHS_VideoCombine, ModelSamplingSD3, BasicScheduler, ManualSigmas, LTXVAddGuidesFromBatch, ImageResizeKJv2, ImageResizeKJv2, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, CFGGuider, SetNode, LTXVLatentUpsampler, LTXAddVideoICLoRAGuide, ManualSigmas, LTXVAddGuideMulti, LTX2SamplingPreviewOverride, PrimitiveBoolean, ImageResizeKJv2, GetImageSizeAndCount, SetNode, SetNode, GetNode, LiconMSR, RMBG, LTXAddVideoICLoRAGuide, EmptyLTXVLatentVideo, LTXVAddGuideMulti, LoadImage, TextInput_, VHS_VideoCombine, PreviewAny, SaveVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 145}
---

# 视频生成/图生视频/LTX-2.3-MSR多参视频自动提示词_2063834654762950658.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2063834654762950658.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（172 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `LTX2AttentionTunerPatch`
- `SetNode`
- `GetNode`
- `INTConstant`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
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
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `ComfySwitchNode`
- `GetNode`
- `LTX2_NAG`
- `RandomNoise`
- `ManualSigmas`
- `GetNode`
- `RMBG`
- `LatentUpscaleModelLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `SeedGenerator`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `Reroute`
- `Reroute`
- `Reroute`
- `PrimitiveFloat`
- `DualCLIPLoader`
- `ImageBatchMulti`
- `LTXVAudioVAEDecode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `GetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `GetNode`
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `ImageBatchMulti`
- `SetNode`
- `GetNode`
- `LTXVCropGuides`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `LTXVAddGuidesFromBatch`
- `LoadImage`
- `LoadImage`
- `CreateVideo`
- `INTConstant`
- `INTConstant`
- `LTXVConditioning`
- `RH_LLMAPI_NODE`
- `TTP_text_mix`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `TextInput_`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `BasicScheduler`
- `ManualSigmas`
- `LTXVAddGuidesFromBatch`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `CFGGuider`
- `SetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXAddVideoICLoRAGuide`
- `ManualSigmas`
- `LTXVAddGuideMulti`
- `LTX2SamplingPreviewOverride`
- `PrimitiveBoolean`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `GetNode`
- `LiconMSR`
- `RMBG`
- `LTXAddVideoICLoRAGuide`
- `EmptyLTXVLatentVideo`
- `LTXVAddGuideMulti`
- `LoadImage`
- `TextInput_`
- `VHS_VideoCombine`
- `PreviewAny`
- `SaveVideo`

## 关键参数

- `width` = `145`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **45%**（78/172）

**有卡**：`SimpleCalculatorKJ`、`ComfyMathExpression`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`LTX2AttentionTunerPatch`、`INTConstant`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTX2_NAG`、`RandomNoise`、`ManualSigmas`、`RMBG`、`LatentUpscaleModelLoader`、`VAELoader`、`VAELoaderKJ`、`LoraLoaderModelOnly`、`LTXVEmptyLatentAudio`、`UNETLoader`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`KSamplerSelect`、`SeedGenerator`、`VAEDecode`、`DualCLIPLoader`、`ImageBatchMulti`、`LTXVCropGuides`、`CFGGuider`、`LTXVAddGuidesFromBatch`、`LoadImage`、`CreateVideo`、`LTXVConditioning`、`RH_LLMAPI_NODE`、`TTP_text_mix`、`CLIPTextEncode`、`TextInput_`、`VHS_VideoCombine`、`ModelSamplingSD3`、`BasicScheduler`、`ImageResizeKJv2`、`LTXICLoRALoaderModelOnly`、`LTXVLatentUpsampler`、`LTXAddVideoICLoRAGuide`、`LTXVAddGuideMulti`、`LTX2SamplingPreviewOverride`、`PrimitiveBoolean`、`GetImageSizeAndCount`、`LiconMSR`、`EmptyLTXVLatentVideo`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
