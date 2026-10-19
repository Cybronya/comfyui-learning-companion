---
key: 数字人/数字人/LTX2.5 - CQ Enhancer lora video 视频高清修复放大工具-小宣喧-RH_2100842998178340866.json
name: LTX2.5 - CQ Enhancer lora video 视频高清修复放大工具-小宣喧-RH_2100842998178340866
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.5 - CQ Enhancer lora video 视频高清修复放大工具-小宣喧-RH_2100842998178340866.json
hash: b3d4c03879387462
coverage: 0.921053
learned_at: 2026-10-19 00:19:10
nodes: [Reroute, CLIPTextEncode, VAELoaderKJ, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, CM_FloatToInt, EmptyLTXVLatentVideo, KSamplerSelect, LTXVSeparateAVLatent, LTXVCropGuides, SamplerCustomAdvanced, RandomNoise, GetImageSize, LTXVImgToVideoConditionOnly, LTXVEmptyLatentAudio, LTXAddVideoICLoRAGuide, CFGGuider, LTXVConcatAVLatent, VAELoaderKJ, LTXVConditioning, LTXVAudioVAEEncode, FL_Switch, ManualSigmas, CLIPLoader, LoraLoaderModelOnly, Note, PathchSageAttentionKJ, LTXVAudioVAEDecode, VAEDecode, LG_Color_Match_V2, VHS_VideoInfo, ResizeImageMaskNode, ResizeImageMaskNode, ImpactInt, VHS_LoadVideo, Reroute, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 数字人/数字人/LTX2.5 - CQ Enhancer lora video 视频高清修复放大工具-小宣喧-RH_2100842998178340866.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.5 - CQ Enhancer lora video 视频高清修复放大工具-小宣喧-RH_2100842998178340866.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（38 个）：
- `Reroute`
- `CLIPTextEncode` ★核心
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CM_FloatToInt`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `GetImageSize`
- `LTXVImgToVideoConditionOnly`
- `LTXVEmptyLatentAudio` ★核心
- `LTXAddVideoICLoRAGuide`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `VAELoaderKJ`
- `LTXVConditioning`
- `LTXVAudioVAEEncode` ★核心
- `FL_Switch`
- `ManualSigmas`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `PathchSageAttentionKJ`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `LG_Color_Match_V2`
- `VHS_VideoInfo`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `ImpactInt`
- `VHS_LoadVideo`
- `Reroute`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（35/38）

**有卡**：`CLIPTextEncode`、`VAELoaderKJ`、`UNETLoader`、`LoraLoaderModelOnly`、`CM_FloatToInt`、`EmptyLTXVLatentVideo`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`RandomNoise`、`GetImageSize`、`LTXVImgToVideoConditionOnly`、`LTXVEmptyLatentAudio`、`LTXAddVideoICLoRAGuide`、`CFGGuider`、`LTXVConcatAVLatent`、`LTXVConditioning`、`LTXVAudioVAEEncode`、`FL_Switch`、`ManualSigmas`、`CLIPLoader`、`PathchSageAttentionKJ`、`LTXVAudioVAEDecode`、`VAEDecode`、`LG_Color_Match_V2`、`VHS_VideoInfo`、`ResizeImageMaskNode`、`ImpactInt`、`VHS_LoadVideo`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
