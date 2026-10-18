---
key: 视频生成/图生视频/Wan2.2 图生视频(MOE官方流)｜Light2v 加速版_2104706846383759362.json
name: Wan2.2 图生视频(MOE官方流)｜Light2v 加速版_2104706846383759362
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 图生视频(MOE官方流)｜Light2v 加速版_2104706846383759362.json
hash: cff553b1ef4b83a5
coverage: 0.837838
learned_at: 2026-10-17 22:19:10
nodes: [RIFE VFI, Mute / Bypass Repeater (rgthree), UNETLoader, GetNode, wanBlockSwap, PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, SetNode, GetNode, wanBlockSwap, PathchSageAttentionKJ, ModelSamplingSD3, VAELoader, SetNode, LoraLoaderModelOnly, UNETLoader, VAEDecode, SimpleMath+, WanImageToVideo, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, Fast Bypasser (rgthree), VHS_VideoCombine, Mute / Bypass Repeater (rgthree), Fast Bypasser (rgthree), CLIPTextEncode, Seed (rgthree), LayerUtility: ImageScaleByAspectRatio V2, 孤海注释, ImpactInt, 孤海注释, LoadImage, CR Text, ImpactInt, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "beta", "sampler_name": 1, "scheduler": "dpmpp_2m_sde", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 图生视频(MOE官方流)｜Light2v 加速版_2104706846383759362.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan2.2 图生视频(MOE官方流)｜Light2v 加速版_2104706846383759362.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（37 个）：
- `RIFE VFI`
- `Mute / Bypass Repeater (rgthree)`
- `UNETLoader` ★核心
- `GetNode`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPLoader`
- `SetNode`
- `GetNode`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAELoader`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SimpleMath+`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Fast Bypasser (rgthree)`
- `VHS_VideoCombine`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `孤海注释`
- `ImpactInt`
- `孤海注释`
- `LoadImage`
- `CR Text`
- `ImpactInt`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `dpmpp_2m_sde`
- `denoise` = `beta`

## 知识

覆盖率 **84%**（31/37）

**有卡**：`RIFE VFI`、`Mute / Bypass Repeater (rgthree)`、`UNETLoader`、`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`VAEDecode`、`SimpleMath+`、`WanImageToVideo`、`CLIPTextEncode`、`KSamplerAdvanced`、`Fast Bypasser (rgthree)`、`VHS_VideoCombine`、`Seed (rgthree)`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImpactInt`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
