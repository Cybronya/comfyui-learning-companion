---
key: 视频生成/文生视频/ltx-2.3文生视频蒸馏二阶段放大_2030336856772059137.json
name: ltx-2.3文生视频蒸馏二阶段放大_2030336856772059137
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx-2.3文生视频蒸馏二阶段放大_2030336856772059137.json
hash: b963d7c8dad4ccca
coverage: 0.95
learned_at: 2026-10-15 22:47:22
nodes: [LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXVImgToVideoConditionOnly, LTXVConditioning, KSamplerSelect, SamplerCustomAdvanced, CFGGuider, LTXVPreprocess, RandomNoise, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, RandomNoise, ManualSigmas, ManualSigmas, LTXVConcatAVLatent, LTXVImgToVideoConditionOnly, LTXVSeparateAVLatent, LTXVSeparateAVLatent, LTXVLatentUpsampler, UnetLoaderGGUF, LatentUpscaleModelLoader, ResizeImageMaskNode, LoraLoaderModelOnly, CM_FloatToInt, VAEDecodeTiled, VHS_VideoCombine, PrimitiveBoolean, VAELoader, VAELoaderKJ, LoraLoaderModelOnly, LTXVAudioVAEDecode, UNETLoader, DualCLIPLoader, PrimitiveFloat, EmptyLTXVLatentVideo, LoadImage, CLIPTextEncode, PrimitiveInt, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/ltx-2.3文生视频蒸馏二阶段放大_2030336856772059137.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx-2.3文生视频蒸馏二阶段放大_2030336856772059137.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（40 个）：
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTXVImgToVideoConditionOnly`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `LTXVPreprocess`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `ManualSigmas`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoConditionOnly`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `UnetLoaderGGUF` ★核心
- `LatentUpscaleModelLoader`
- `ResizeImageMaskNode`
- `LoraLoaderModelOnly` ★核心
- `CM_FloatToInt`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `PrimitiveBoolean`
- `VAELoader`
- `VAELoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAEDecode` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `PrimitiveFloat`
- `EmptyLTXVLatentVideo`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `CLIPTextEncode` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`LTXVImgToVideoConditionOnly`、`LTXVConditioning`、`KSamplerSelect`、`SamplerCustomAdvanced`、`CFGGuider`、`LTXVPreprocess`、`RandomNoise`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`UnetLoaderGGUF`、`LatentUpscaleModelLoader`、`ResizeImageMaskNode`、`LoraLoaderModelOnly`、`CM_FloatToInt`、`VAEDecodeTiled`、`VHS_VideoCombine`、`PrimitiveBoolean`、`VAELoader`、`VAELoaderKJ`、`LTXVAudioVAEDecode`、`UNETLoader`、`DualCLIPLoader`、`EmptyLTXVLatentVideo`、`LoadImage`、`CLIPTextEncode`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
