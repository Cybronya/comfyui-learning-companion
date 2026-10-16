---
key: 视频生成/图生视频/LTX2.3 三阶段采样（分辨率除4三采）_2036795915394093058.json
name: LTX2.3 三阶段采样（分辨率除4三采）_2036795915394093058.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2036795915394093058.json
hash: 71fca279eb87a7e1
coverage: 0.864865
learned_at: 2026-10-15 22:35:53
nodes: [CFGGuider, KSamplerSelect, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVEmptyLatentAudio, easy showAnything, easy showAnything, SimpleMath+, easy cleanGpuUsed, easy clearCacheAll, CFGGuider, LTXVSeparateAVLatent, VHS_PruneOutputs, RandomNoise, VHS_PruneOutputs, LTXVLatentUpsampler, PrimitiveFloat, VHS_PruneOutputs, VHS_PruneOutputs, LayerUtility: PurgeVRAM V2, easy cleanGpuUsed, easy clearCacheAll, LayerUtility: PurgeVRAM V2, easy cleanGpuUsed, easy clearCacheAll, easy cleanGpuUsed, easy clearCacheAll, LTXVSeparateAVLatent, easy cleanGpuUsed, easy clearCacheAll, LayerUtility: PurgeVRAM V2, easy cleanGpuUsed, easy clearCacheAll, LayerUtility: PurgeVRAM V2, CFGGuider, LTXVSeparateAVLatent, ManualSigmas, PrimitiveBoolean, SamplerCustomAdvanced, LTXVImgToVideoConditionOnly, VAEDecodeTiled, ManualSigmas, PrimitiveInt, KSamplerSelect, RandomNoise, VAEDecodeTiled, LTXVImgToVideoConditionOnly, LTXVAudioVAEDecode, LTXVAudioVAEDecode, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVImgToVideoConditionOnly, CLIPTextEncode, PrimitiveInt, PrimitiveFloat, SimpleMath+, ComfyMathExpression, LoadImage, easy showAnything, EmptyLTXVLatentVideo, LTXVLatentUpsampler, VHS_PruneOutputs, VHS_PruneOutputs, LTXVChunkFeedForward, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVEnhanceAVideoKJ, PathchSageAttentionKJ, LTXVConcatAVLatent, LoraLoaderModelOnly, LTX2_NAG, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, ManualSigmas, Reroute, LTXVEnhanceAVideoKJ, SimpleMath+, VHS_VideoCombine, VHS_VideoCombine, Note, KSamplerSelect, KSamplerSelect, LTXVEnhanceAVideoKJ, PreviewImage, LTXVConditioning, RandomNoise, CFGNorm, CreateVideo, VHS_VideoCombine, SaveVideo, easy seed, LTXVConcatAVLatent, LTXVConcatAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LTXVPreprocess, LTXVPreprocess, CheckpointLoaderSimple, LoraLoaderModelOnly, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, LTXVAudioVAELoader, PrimitiveInt, Note, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, LoraLoaderModelOnly, CLIPTextEncode, LoraLoaderModelOnly, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 三阶段采样（分辨率除4三采）_2036795915394093058.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2036795915394093058.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（111 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `easy showAnything`
- `easy showAnything`
- `SimpleMath+`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `VHS_PruneOutputs`
- `RandomNoise`
- `VHS_PruneOutputs`
- `LTXVLatentUpsampler` ★核心
- `PrimitiveFloat`
- `VHS_PruneOutputs`
- `VHS_PruneOutputs`
- `LayerUtility: PurgeVRAM V2`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `LayerUtility: PurgeVRAM V2`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `LTXVSeparateAVLatent`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `LayerUtility: PurgeVRAM V2`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `LayerUtility: PurgeVRAM V2`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `PrimitiveBoolean`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoConditionOnly`
- `VAEDecodeTiled` ★核心
- `ManualSigmas`
- `PrimitiveInt`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `VAEDecodeTiled` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXVAudioVAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVImgToVideoConditionOnly`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `PrimitiveFloat`
- `SimpleMath+`
- `ComfyMathExpression`
- `LoadImage`
- `easy showAnything`
- `EmptyLTXVLatentVideo`
- `LTXVLatentUpsampler` ★核心
- `VHS_PruneOutputs`
- `VHS_PruneOutputs`
- `LTXVChunkFeedForward`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVEnhanceAVideoKJ`
- `PathchSageAttentionKJ`
- `LTXVConcatAVLatent`
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `ManualSigmas`
- `Reroute`
- `LTXVEnhanceAVideoKJ`
- `SimpleMath+`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Note`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `LTXVEnhanceAVideoKJ`
- `PreviewImage`
- `LTXVConditioning`
- `RandomNoise`
- `CFGNorm`
- `CreateVideo`
- `VHS_VideoCombine`
- `SaveVideo`
- `easy seed`
- `LTXVConcatAVLatent`
- `LTXVConcatAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `LTXVAudioVAELoader`
- `PrimitiveInt`
- `Note`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **86%**（96/111）

**有卡**：`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`SimpleMath+`、`easy cleanGpuUsed`、`easy clearCacheAll`、`LTXVSeparateAVLatent`、`VHS_PruneOutputs`、`RandomNoise`、`LTXVLatentUpsampler`、`LayerUtility: PurgeVRAM V2`、`ManualSigmas`、`PrimitiveBoolean`、`LTXVImgToVideoConditionOnly`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`ComfyMathExpression`、`LoadImage`、`EmptyLTXVLatentVideo`、`LTXVChunkFeedForward`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`LTXVEnhanceAVideoKJ`、`PathchSageAttentionKJ`、`LTXVConcatAVLatent`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`LTXVConditioning`、`CFGNorm`、`CreateVideo`、`SaveVideo`、`easy seed`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVPreprocess`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`LTXVAudioVAELoader`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、CFGNorm、KSamplerSelect、SamplerCustomAdvanced
