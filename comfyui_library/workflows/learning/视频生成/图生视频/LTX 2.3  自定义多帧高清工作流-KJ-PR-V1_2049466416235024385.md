---
key: 视频生成/图生视频/LTX 2.3  自定义多帧高清工作流-KJ-PR-V1_2049466416235024385.json
name: LTX 2.3  自定义多帧高清工作流-KJ-PR-V1_2049466416235024385.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2049466416235024385.json
hash: 6861bb512c2a2127
coverage: 0.519231
learned_at: 2026-10-15 22:37:14
nodes: [SetNode, SetNode, VAELoaderKJ, VAELoaderKJ, SimpleMath+, GetNode, MarkdownNote, LTXVAudioVAEDecode, DualCLIPLoader, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, GetNode, VHS_VideoCombine, GetNode, GetNode, KSamplerSelect, BasicScheduler, VHS_VideoCombine, GetNode, SimpleMath+, VAEDecode, SetNode, SimpleCalculatorKJ, SetNode, SetNode, INTConstant, GetNode, GetNode, GetNode, SetNode, LTXVAudioVAEDecode, Label (rgthree), Label (rgthree), ManualSigmas, LTXVLatentUpsampler, CFGGuider, SamplerCustomAdvanced, LTXVConcatAVLatent, SetNode, DiffusionModelLoaderKJ, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, SimpleMath+, SetNode, GetNode, GetNode, GetNode, VAEDecodeTiled, VAEDecode, GetNode, Label (rgthree), Label (rgthree), BasicScheduler, KSamplerSelect, GetNode, SetNode, GetNode, LTXVEmptyLatentAudio, SetNode, GetNode, ManualSigmas, GetNode, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXSequencer, LTXVConditioning, CLIPTextEncode, RandomNoise, GetNode, GetNode, GetNode, LTX2SamplingPreviewOverride, CFGGuider, SamplerCustomAdvanced, SetNode, LatentUpscaleModelLoader, INTConstant, INTConstant, INTConstant, PromptRelayEncodeTimeline, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), MultiImageLoader, LTXSequencer, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 121}
---

# 视频生成/图生视频/LTX 2.3  自定义多帧高清工作流-KJ-PR-V1_2049466416235024385.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2049466416235024385.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（104 个）：
- `SetNode`
- `SetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `SimpleMath+`
- `GetNode`
- `MarkdownNote`
- `LTXVAudioVAEDecode` ★核心
- `DualCLIPLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VHS_VideoCombine`
- `GetNode`
- `SimpleMath+`
- `VAEDecode` ★核心
- `SetNode`
- `SimpleCalculatorKJ`
- `SetNode`
- `SetNode`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `Label (rgthree)`
- `Label (rgthree)`
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `DiffusionModelLoaderKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `SetNode`
- `GetNode`
- `ManualSigmas`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXSequencer`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `LatentUpscaleModelLoader`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `PromptRelayEncodeTimeline`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `MultiImageLoader`
- `LTXSequencer`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **52%**（54/104）

**有卡**：`VAELoaderKJ`、`SimpleMath+`、`LTXVAudioVAEDecode`、`DualCLIPLoader`、`LTXVSeparateAVLatent`、`VHS_VideoCombine`、`KSamplerSelect`、`BasicScheduler`、`VAEDecode`、`SimpleCalculatorKJ`、`INTConstant`、`Label (rgthree)`、`ManualSigmas`、`LTXVLatentUpsampler`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`DiffusionModelLoaderKJ`、`VAEDecodeTiled`、`LTXVEmptyLatentAudio`、`LTXSequencer`、`LTXVConditioning`、`CLIPTextEncode`、`RandomNoise`、`LTX2SamplingPreviewOverride`、`LatentUpscaleModelLoader`、`PromptRelayEncodeTimeline`、`LoraLoaderModelOnly`、`MultiImageLoader`、`EmptyLTXVLatentVideo`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
