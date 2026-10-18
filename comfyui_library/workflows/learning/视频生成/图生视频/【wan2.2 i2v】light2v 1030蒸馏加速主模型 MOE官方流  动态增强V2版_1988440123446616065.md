---
key: 视频生成/图生视频/【wan2.2 i2v】light2v 1030蒸馏加速主模型 MOE官方流  动态增强V2版_1988440123446616065.json
name: 【wan2.2 i2v】light2v 1030蒸馏加速主模型 MOE官方流  动态增强V2版_1988440123446616065.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【wan2.2 i2v】light2v 1030蒸馏加速主模型 MOE官方流  动态增强V2版_1988440123446616065.json
hash: 60d4bfc0a8ea4868
coverage: 0.818182
learned_at: 2026-10-15 22:33:02
nodes: [wanBlockSwap, ModelSamplingSD3, ModelSamplingSD3, VAELoader, PathchSageAttentionKJ, PathchSageAttentionKJ, SimpleMath+, MarkdownNote, KSamplerAdvanced, CLIPLoader, GetNode, SetNode, Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, KSamplerAdvanced, VAEDecode, GetNode, wanBlockSwap, SetNode, WanImageToVideo, MarkdownNote, UNETLoader, PainterI2V, CLIPTextEncode, LoadImage, VHS_VideoCombine, LoraLoaderModelOnly, UNETLoader, ImpactInt, ImpactInt, CR Text]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "beta", "sampler_name": 1, "scheduler": "dpmpp_2m_sde", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/【wan2.2 i2v】light2v 1030蒸馏加速主模型 MOE官方流  动态增强V2版_1988440123446616065.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1988440123446616065.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（33 个）：
- `wanBlockSwap`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAELoader`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `MarkdownNote`
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `GetNode`
- `SetNode`
- `Fast Bypasser (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `wanBlockSwap`
- `SetNode`
- `WanImageToVideo`
- `MarkdownNote`
- `UNETLoader` ★核心
- `PainterI2V`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ImpactInt`
- `ImpactInt`
- `CR Text`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `dpmpp_2m_sde`
- `denoise` = `beta`

## 知识

覆盖率 **82%**（27/33）

**有卡**：`wanBlockSwap`、`ModelSamplingSD3`、`VAELoader`、`PathchSageAttentionKJ`、`SimpleMath+`、`KSamplerAdvanced`、`CLIPLoader`、`Fast Bypasser (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`WanImageToVideo`、`UNETLoader`、`PainterI2V`、`LoadImage`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`ImpactInt`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
