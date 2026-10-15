---
key: 视频生成/文生视频/ltx-2.3文生视频单阶段双轨_2030335561520648193.json
name: ltx-2.3文生视频单阶段双轨_2030335561520648193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx-2.3文生视频单阶段双轨_2030335561520648193.json
hash: 951da2e44fdbc77c
coverage: 0.952381
learned_at: 2026-10-15 22:47:22
nodes: [LTXVAudioVAEDecode, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVImgToVideoConditionOnly, LTXVEmptyLatentAudio, LTXVConditioning, LTXVPreprocess, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, SamplerCustomAdvanced, CM_FloatToInt, KSamplerSelect, CFGGuider, RandomNoise, LoraLoaderModelOnly, LoadImage, VAELoader, PrimitiveBoolean, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoaderKJ, DualCLIPLoader, UnetLoaderGGUF, PrimitiveFloat, VHS_VideoCombine, EmptyLTXVLatentVideo, CLIPTextEncode, ResizeImageMaskNode, CLIPTextEncode, PrimitiveInt, GuiderParameters, MultimodalGuider, ClownSampler_Beta, LTXVScheduler, RandomNoise, LTXVConcatAVLatent, UNETLoader, GuiderParameters, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/ltx-2.3文生视频单阶段双轨_2030335561520648193.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx-2.3文生视频单阶段双轨_2030335561520648193.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（42 个）：
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `LTXVPreprocess`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CM_FloatToInt`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `VAELoader`
- `PrimitiveBoolean`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `DualCLIPLoader`
- `UnetLoaderGGUF` ★核心
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `EmptyLTXVLatentVideo`
- `CLIPTextEncode` ★核心
- `ResizeImageMaskNode`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `GuiderParameters`
- `MultimodalGuider`
- `ClownSampler_Beta` ★核心
- `LTXVScheduler`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `UNETLoader` ★核心
- `GuiderParameters`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（40/42）

**有卡**：`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`LTXVImgToVideoConditionOnly`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`LTXVPreprocess`、`ManualSigmas`、`SamplerCustomAdvanced`、`CM_FloatToInt`、`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`LoraLoaderModelOnly`、`LoadImage`、`VAELoader`、`PrimitiveBoolean`、`VAELoaderKJ`、`DualCLIPLoader`、`UnetLoaderGGUF`、`VHS_VideoCombine`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`ResizeImageMaskNode`、`GuiderParameters`、`MultimodalGuider`、`ClownSampler_Beta`、`LTXVScheduler`、`LTXVConcatAVLatent`、`UNETLoader`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
