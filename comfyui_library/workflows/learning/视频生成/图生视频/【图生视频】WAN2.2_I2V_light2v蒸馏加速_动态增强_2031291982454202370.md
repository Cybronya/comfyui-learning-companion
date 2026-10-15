---
key: 视频生成/图生视频/【图生视频】WAN2.2_I2V_light2v蒸馏加速_动态增强_2031291982454202370.json
name: 【图生视频】WAN2.2_I2V_light2v蒸馏加速_动态增强_2031291982454202370
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【图生视频】WAN2.2_I2V_light2v蒸馏加速_动态增强_2031291982454202370.json
hash: f848b2778f29621e
coverage: 0.647887
learned_at: 2026-10-15 22:43:00
nodes: [CLIPTextEncode, CLIPTextEncode, GetNode, SetNode, SetNode, Mute / Bypass Repeater (rgthree), wanBlockSwap, UNETLoader, PathchSageAttentionKJ, ModelSamplingSD3, SetNode, UNETLoader, LoraLoaderModelOnly, wanBlockSwap, PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, Fast Bypasser (rgthree), GetNode, easy float, easy float, GetNode, GetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, SetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, GetNode, SetNode, SetNode, SeedVR2VideoUpscaler, ImageScaleBy, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, ImageResizeKJv2, WujiCleaner, Anything Everywhere, PainterI2V, FilmGrain, MarkdownNote, easy cleanGpuUsed, ImageConcatMulti, easy boolean, ImpactInt, easy float, ImpactInt, SimpleMath+, ImpactSwitch, PrimitiveNode, ImpactConditionalBranch, GetNode, LoadImage, CR Text, VHS_VideoCombine, VAEDecode, SetNode, GetNode, SetNode, GetNode, Fast Groups Bypasser (rgthree), Image Input Switch, SetNode, ImpactSwitch, PrimitiveNode, FlashVSRNode, IFRNet VFI, RIFE VFI, FILM VFI]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "beta", "sampler_name": 1, "scheduler": "dpmpp_2m_sde", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/【图生视频】WAN2.2_I2V_light2v蒸馏加速_动态增强_2031291982454202370.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/【图生视频】WAN2.2_I2V_light2v蒸馏加速_动态增强_2031291982454202370.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（71 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `Mute / Bypass Repeater (rgthree)`
- `wanBlockSwap`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `SetNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPLoader`
- `Fast Bypasser (rgthree)`
- `GetNode`
- `easy float`
- `easy float`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `SetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `SeedVR2VideoUpscaler`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `ImageResizeKJv2`
- `WujiCleaner`
- `Anything Everywhere`
- `PainterI2V`
- `FilmGrain`
- `MarkdownNote`
- `easy cleanGpuUsed`
- `ImageConcatMulti`
- `easy boolean`
- `ImpactInt`
- `easy float`
- `ImpactInt`
- `SimpleMath+`
- `ImpactSwitch`
- `PrimitiveNode`
- `ImpactConditionalBranch`
- `GetNode`
- `LoadImage`
- `CR Text`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `Image Input Switch`
- `SetNode`
- `ImpactSwitch`
- `PrimitiveNode`
- `FlashVSRNode`
- `IFRNet VFI`
- `RIFE VFI`
- `FILM VFI`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `dpmpp_2m_sde`
- `denoise` = `beta`

## 知识

覆盖率 **65%**（46/71）

**有卡**：`CLIPTextEncode`、`Mute / Bypass Repeater (rgthree)`、`wanBlockSwap`、`UNETLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`CLIPLoader`、`Fast Bypasser (rgthree)`、`easy float`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`KSamplerAdvanced`、`SeedVR2VideoUpscaler`、`ImageScaleBy`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`ImageResizeKJv2`、`WujiCleaner`、`PainterI2V`、`FilmGrain`、`easy cleanGpuUsed`、`ImageConcatMulti`、`easy boolean`、`ImpactInt`、`SimpleMath+`、`ImpactConditionalBranch`、`CR Text`、`VHS_VideoCombine`、`VAEDecode`、`Image Input Switch`、`FlashVSRNode`、`IFRNet VFI`、`RIFE VFI`、`FILM VFI`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
