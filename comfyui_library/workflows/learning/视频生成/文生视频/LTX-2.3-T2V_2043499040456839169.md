---
key: 视频生成/文生视频/LTX-2.3-T2V_2043499040456839169.json
name: LTX-2.3-T2V_2043499040456839169
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3-T2V_2043499040456839169.json
hash: 951e384b66e4778a
coverage: 0.767857
learned_at: 2026-10-11 19:49:36
nodes: [CFGGuider, CLIPTextEncode, LTXVConcatAVLatent, SamplerCustomAdvanced, GetImageSize, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVLatentUpsampler, Reroute, Reroute, EmptyLTXVLatentVideo, RandomNoise, LTXVAudioVAEDecode, Reroute, Reroute, Reroute, LTXVEmptyLatentAudio, RandomNoise, LTXVCropGuides, Reroute, LTXVSeparateAVLatent, LTXVAudioVAEDecode, Reroute, LTXVConditioning, PrimitiveInt, CM_IntToFloat, Reroute, ImpactExecutionOrderController, Reroute, ManualSigmas, KSamplerSelect, KSamplerSelect, PrimitiveInt, ImageScaleBy, LTXVScheduler, CFGGuider, MarkdownNote, MarkdownNote, CLIPTextEncode, EmptyImage, VAEDecodeTiled, VAEDecodeTiled, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LatentUpscaleModelLoader, LoraLoaderModelOnly, CheckpointLoaderSimple, UnetLoaderGGUF, VAELoader, LTXVAudioVAELoader, VAELoaderKJ, DualCLIPLoader, LTXAVTextEncoderLoader, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX-2.3-T2V_2043499040456839169.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3-T2V_2043499040456839169.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（56 个）：
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `GetImageSize`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `Reroute`
- `Reroute`
- `EmptyLTXVLatentVideo`
- `RandomNoise`
- `LTXVAudioVAEDecode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVEmptyLatentAudio` ★核心
- `RandomNoise`
- `LTXVCropGuides`
- `Reroute`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `Reroute`
- `LTXVConditioning`
- `PrimitiveInt`
- `CM_IntToFloat`
- `Reroute`
- `ImpactExecutionOrderController`
- `Reroute`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `PrimitiveInt`
- `ImageScaleBy`
- `LTXVScheduler`
- `CFGGuider`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `EmptyImage`
- `VAEDecodeTiled` ★核心
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `UnetLoaderGGUF` ★核心
- `VAELoader`
- `LTXVAudioVAELoader`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LTXAVTextEncoderLoader`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **77%**（43/56）

**有卡**：`CFGGuider`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`GetImageSize`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`EmptyLTXVLatentVideo`、`RandomNoise`、`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`LTXVConditioning`、`CM_IntToFloat`、`ImpactExecutionOrderController`、`ManualSigmas`、`KSamplerSelect`、`ImageScaleBy`、`LTXVScheduler`、`EmptyImage`、`VAEDecodeTiled`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`CheckpointLoaderSimple`、`UnetLoaderGGUF`、`VAELoader`、`LTXVAudioVAELoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXAVTextEncoderLoader`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
