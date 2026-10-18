---
key: 视频生成/图生视频/LTX-2.3 MSR多主体参考视频生成V1_2063462550611779585.json
name: LTX-2.3 MSR多主体参考视频生成V1_2063462550611779585.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3 MSR多主体参考视频生成V1_2063462550611779585.json
hash: 4bf1c217db69bc91
coverage: 0.446429
learned_at: 2026-10-15 22:39:13
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SimpleCalculatorKJ, GetNode, SetNode, SetNode, SetNode, GetNode, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, RMBG, SetNode, SetNode, GetNode, GetNode, PathchSageAttentionKJ, LTXVChunkFeedForward, LTX2AttentionTunerPatch, SetNode, GetNode, INTConstant, SetNode, SetNode, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVLatentUpsampler, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, GetNode, SetNode, ManualSigmas, GetNode, GetNode, SamplerCustomAdvanced, ComfySwitchNode, GetNode, LTX2_NAG, RandomNoise, PrimitiveBoolean, ManualSigmas, GetNode, RMBG, ImageResizeKJv2, LatentUpscaleModelLoader, VAELoader, VAELoaderKJ, VAELoader, LoraLoaderModelOnly, ImageResizeKJv2, ImageResizeKJv2, EmptyLTXVLatentVideo, GetNode, ComfyMathExpression, SetNode, SetNode, SetNode, ComfySwitchNode, ComfySwitchNode, LTXVEmptyLatentAudio, SamplerCustomAdvanced, LoadImage, LoadImage, UNETLoader, SetNode, LTXVAudioVAEDecode, LTXVSeparateAVLatent, GetNode, GetNode, INTConstant, INTConstant, LoadImage, GetNode, KSamplerSelect, SeedGenerator, VAEDecode, GetNode, LTXAddVideoICLoRAGuide, GetNode, SetNode, SetNode, LTXVConcatAVLatent, Reroute, Reroute, Reroute, CFGGuider, PrimitiveFloat, DualCLIPLoader, GetNode, GetImageSizeAndCount, ImageBatchMulti, LTXVAudioVAEDecode, BasicScheduler, Reroute, Reroute, Reroute, GetNode, SetNode, LTXVSeparateAVLatent, GetNode, GetNode, ComfySwitchNode, VAEDecode, GetNode, GetNode, GetNode, ComfySwitchNode, GetNode, LTXVCropGuides, GetNode, GetNode, SaveVideo, CreateVideo, VHS_VideoCombine, ImageBatchMulti, SetNode, LTXVAddGuideMulti, LiconMSR, VHS_VideoCombine, ModelSamplingSD3, LTXAddVideoICLoRAGuide, GetNode, LTXVCropGuides, KSamplerSelect, RandomNoise, CFGGuider, LTXVAddGuidesFromBatch, LTXVAddGuideMulti, LTX2SamplingPreviewOverride, CLIPTextEncode, LTXVConditioning, CLIPTextEncode, TextInput_, ManualSigmas, LTXVAddGuidesFromBatch, LoraLoaderModelOnly, SetNode, LTXICLoRALoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 145}
---

# 视频生成/图生视频/LTX-2.3 MSR多主体参考视频生成V1_2063462550611779585.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2063462550611779585.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（168 个）：
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
- `RMBG`
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
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `SetNode`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `ComfySwitchNode`
- `GetNode`
- `LTX2_NAG`
- `RandomNoise`
- `PrimitiveBoolean`
- `ManualSigmas`
- `GetNode`
- `RMBG`
- `ImageResizeKJv2`
- `LatentUpscaleModelLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `SetNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `GetNode`
- `KSamplerSelect` ★核心
- `SeedGenerator`
- `VAEDecode` ★核心
- `GetNode`
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `SetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `Reroute`
- `Reroute`
- `Reroute`
- `CFGGuider`
- `PrimitiveFloat`
- `DualCLIPLoader`
- `GetNode`
- `GetImageSizeAndCount`
- `ImageBatchMulti`
- `LTXVAudioVAEDecode` ★核心
- `BasicScheduler`
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
- `SaveVideo`
- `CreateVideo`
- `VHS_VideoCombine`
- `ImageBatchMulti`
- `SetNode`
- `LTXVAddGuideMulti`
- `LiconMSR`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `LTXVCropGuides`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `LTXVAddGuidesFromBatch`
- `LTXVAddGuideMulti`
- `LTX2SamplingPreviewOverride`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `TextInput_`
- `ManualSigmas`
- `LTXVAddGuidesFromBatch`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LTXICLoRALoaderModelOnly` ★核心

## 关键参数

- `width` = `145`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **45%**（75/168）

**有卡**：`SimpleCalculatorKJ`、`ComfyMathExpression`、`RMBG`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`LTX2AttentionTunerPatch`、`INTConstant`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTX2_NAG`、`RandomNoise`、`PrimitiveBoolean`、`ImageResizeKJv2`、`LatentUpscaleModelLoader`、`VAELoader`、`VAELoaderKJ`、`LoraLoaderModelOnly`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LoadImage`、`UNETLoader`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`KSamplerSelect`、`SeedGenerator`、`VAEDecode`、`LTXAddVideoICLoRAGuide`、`CFGGuider`、`DualCLIPLoader`、`GetImageSizeAndCount`、`ImageBatchMulti`、`BasicScheduler`、`LTXVCropGuides`、`SaveVideo`、`CreateVideo`、`VHS_VideoCombine`、`LTXVAddGuideMulti`、`LiconMSR`、`ModelSamplingSD3`、`LTXVAddGuidesFromBatch`、`LTX2SamplingPreviewOverride`、`CLIPTextEncode`、`LTXVConditioning`、`TextInput_`、`LTXICLoRALoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
