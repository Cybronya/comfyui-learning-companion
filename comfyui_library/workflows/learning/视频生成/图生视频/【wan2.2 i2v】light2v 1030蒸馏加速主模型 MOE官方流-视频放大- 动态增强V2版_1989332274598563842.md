---
key: 视频生成/图生视频/【wan2.2 i2v】light2v 1030蒸馏加速主模型 MOE官方流-视频放大- 动态增强V2版_1989332274598563842.json
name: 【wan2.2 i2v】light2v 1030蒸馏加速主模型 MOE官方流-视频放大- 动态增强V2版_1989332274598563842.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1989332274598563842.json
hash: f7c4591f0ea2328c
coverage: 0.825
learned_at: 2026-10-15 22:33:06
nodes: [wanBlockSwap, ModelSamplingSD3, ModelSamplingSD3, VAELoader, PathchSageAttentionKJ, PathchSageAttentionKJ, SimpleMath+, KSamplerAdvanced, CLIPLoader, GetNode, SetNode, Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), CLIPTextEncode, KSamplerAdvanced, VAEDecode, GetNode, wanBlockSwap, SetNode, MarkdownNote, UNETLoader, CLIPTextEncode, LoraLoaderModelOnly, UNETLoader, ImpactInt, ImpactInt, LoadImage, CR Text, CR Upscale Image, RIFE VFI, easy cleanGpuUsed, VHS_VideoCombine, GetNode, ImageResizeKJv2, LoadImage, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, ImageConcatMulti, SetNode, PainterI2V]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "beta", "sampler_name": 1, "scheduler": "dpmpp_2m_sde", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/【wan2.2 i2v】light2v 1030蒸馏加速主模型 MOE官方流-视频放大- 动态增强V2版_1989332274598563842.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1989332274598563842.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（40 个）：
- `wanBlockSwap`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAELoader`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `GetNode`
- `SetNode`
- `Fast Bypasser (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `wanBlockSwap`
- `SetNode`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ImpactInt`
- `ImpactInt`
- `LoadImage`
- `CR Text`
- `CR Upscale Image`
- `RIFE VFI`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageConcatMulti`
- `SetNode`
- `PainterI2V`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `dpmpp_2m_sde`
- `denoise` = `beta`

## 知识

覆盖率 **82%**（33/40）

**有卡**：`wanBlockSwap`、`ModelSamplingSD3`、`VAELoader`、`PathchSageAttentionKJ`、`SimpleMath+`、`KSamplerAdvanced`、`CLIPLoader`、`Fast Bypasser (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`CLIPTextEncode`、`VAEDecode`、`UNETLoader`、`LoraLoaderModelOnly`、`ImpactInt`、`LoadImage`、`CR Text`、`CR Upscale Image`、`RIFE VFI`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcatMulti`、`PainterI2V`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
