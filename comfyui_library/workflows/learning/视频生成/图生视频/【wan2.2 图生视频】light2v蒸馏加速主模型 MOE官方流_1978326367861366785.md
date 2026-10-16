---
key: 视频生成/图生视频/【wan2.2 图生视频】light2v蒸馏加速主模型 MOE官方流_1978326367861366785.json
name: 【wan2.2 图生视频】light2v蒸馏加速主模型 MOE官方流_1978326367861366785.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1978326367861366785.json
hash: f1ef4904c46afef0
coverage: 0.861111
learned_at: 2026-10-15 22:32:18
nodes: [wanBlockSwap, ModelSamplingSD3, ModelSamplingSD3, VAELoader, wanBlockSwap, PathchSageAttentionKJ, PathchSageAttentionKJ, ImpactInt, WanImageToVideo, SimpleMath+, LayerUtility: ImageScaleByAspectRatio V2, MarkdownNote, KSamplerAdvanced, CLIPLoader, GetNode, SetNode, SetNode, Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), CLIPTextEncode, CLIPTextEncode, GetNode, UNETLoader, UNETLoader, LoraLoaderModelOnly, KSamplerAdvanced, ImpactInt, LoadImage, CR Text, VHS_VideoCombine, VAEDecode, RIFE VFI, Mute / Bypass Repeater (rgthree), Fast Bypasser (rgthree), VHS_VideoCombine, Seed (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "beta", "sampler_name": 1, "scheduler": "dpmpp_2m_sde", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/【wan2.2 图生视频】light2v蒸馏加速主模型 MOE官方流_1978326367861366785.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1978326367861366785.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（36 个）：
- `wanBlockSwap`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAELoader`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ImpactInt`
- `WanImageToVideo`
- `SimpleMath+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MarkdownNote`
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `GetNode`
- `SetNode`
- `SetNode`
- `Fast Bypasser (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `ImpactInt`
- `LoadImage`
- `CR Text`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `RIFE VFI`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Bypasser (rgthree)`
- `VHS_VideoCombine`
- `Seed (rgthree)`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `dpmpp_2m_sde`
- `denoise` = `beta`

## 知识

覆盖率 **86%**（31/36）

**有卡**：`wanBlockSwap`、`ModelSamplingSD3`、`VAELoader`、`PathchSageAttentionKJ`、`ImpactInt`、`WanImageToVideo`、`SimpleMath+`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSamplerAdvanced`、`CLIPLoader`、`Fast Bypasser (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`CLIPTextEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`CR Text`、`VHS_VideoCombine`、`VAEDecode`、`RIFE VFI`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
