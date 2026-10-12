---
key: 视频生成/图生视频/【图生视频】WAN2.2_I2V_light2v蒸馏加速_动态增强_2031291982454202370.json
name: 【图生视频】WAN2.2_I2V_light2v蒸馏加速_动态增强_2031291982454202370
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【图生视频】WAN2.2_I2V_light2v蒸馏加速_动态增强_2031291982454202370.json
hash: f848b2778f29621e
coverage: 0.450704
learned_at: 2026-10-13 01:36:55
nodes: [CLIPTextEncode, CLIPTextEncode, GetNode, SetNode, SetNode, Mute / Bypass Repeater (rgthree), wanBlockSwap, UNETLoader, PathchSageAttentionKJ, ModelSamplingSD3, SetNode, UNETLoader, LoraLoaderModelOnly, wanBlockSwap, PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, Fast Bypasser (rgthree), GetNode, easy float, easy float, GetNode, GetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, SetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, GetNode, SetNode, SetNode, SeedVR2VideoUpscaler, ImageScaleBy, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, ImageResizeKJv2, WujiCleaner, Anything Everywhere, PainterI2V, FilmGrain, MarkdownNote, easy cleanGpuUsed, ImageConcatMulti, easy boolean, ImpactInt, easy float, ImpactInt, SimpleMath+, ImpactSwitch, PrimitiveNode, ImpactConditionalBranch, GetNode, LoadImage, CR Text, VHS_VideoCombine, VAEDecode, SetNode, GetNode, SetNode, GetNode, Fast Groups Bypasser (rgthree), Image Input Switch, SetNode, ImpactSwitch, PrimitiveNode, FlashVSRNode, IFRNet VFI, RIFE VFI, FILM VFI]
patterns: []
missing: [CR Text, FILM VFI, Fast Bypasser (rgthree), IFRNet VFI, Image Input Switch, LayerUtility: ImageScaleByAspectRatio V2, Mute / Bypass Repeater (rgthree), RIFE VFI, SimpleMath+, easy boolean, easy cleanGpuUsed, easy float, easy float, easy float]
parameters: {"cfg": 4, "denoise": "beta", "sampler_name": 1, "scheduler": "dpmpp_2m_sde", "seed": "enable", "steps": "fixed"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `FILM VFI` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `IFRNet VFI` 知识库中没有该节点类型的任何知识, 次要节点 `Image Input Switch` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识]
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

覆盖率 **45%**（32/71）

**有卡**：`CLIPTextEncode`、`wanBlockSwap`、`UNETLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`CLIPLoader`、`LoadImage`、`VAELoader`、`KSamplerAdvanced`、`SeedVR2VideoUpscaler`、`ImageScaleBy`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`ImageResizeKJv2`、`WujiCleaner`、`PainterI2V`、`FilmGrain`、`ImageConcatMulti`、`ImpactInt`、`ImpactConditionalBranch`、`VHS_VideoCombine`、`VAEDecode`、`FlashVSRNode`

**缺卡**（14）：`CR Text`、`FILM VFI`、`Fast Bypasser (rgthree)`、`IFRNet VFI`、`Image Input Switch`、`LayerUtility: ImageScaleByAspectRatio V2`、`Mute / Bypass Repeater (rgthree)`、`RIFE VFI`、`SimpleMath+`、`easy boolean`、`easy cleanGpuUsed`、`easy float`、`easy float`、`easy float`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `FILM VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `IFRNet VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `Image Input Switch` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
