---
key: 图片生成/文生图/ernie-image-turbo+zimage-turbo_双采样人像去油去拟合感_2044777572101267457.json
name: ernie-image-turbo+zimage-turbo_双采样人像去油去拟合感_2044777572101267457
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ernie-image-turbo+zimage-turbo_双采样人像去油去拟合感_2044777572101267457.json
hash: b25f8fbde00d2930
coverage: 0.645833
learned_at: 2026-10-21 02:56:45
nodes: [StringReplace, Fast Groups Bypasser (rgthree), Note, CLIPLoader, PrimitiveBoolean, TextGenerate, MarkdownNote, CLIPTextEncode, ConditioningZeroOut, CLIPTextEncode, ShowText|pysssss, ComfySwitchNode, CLIPTextEncode, SetNode, VAELoader, CLIPLoader, GetNode, SaveImage, Reroute (rgthree), PrimitiveStringMultiline, VAELoader, CLIPLoader, SetNode, VAEDecode, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, GetNode, GetNode, VAEEncode, Int, TTResolutionSelector, EmptyFlux2LatentImage, Reroute, Reroute, Reroute, Seed (rgthree), Int, AddLabel, Image Comparer (rgthree), AddLabel, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, PreviewImage, UNETLoader, ModelSamplingAuraFlow, LoraLoaderModelOnly, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "ddim_uniform", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/文生图/ernie-image-turbo+zimage-turbo_双采样人像去油去拟合感_2044777572101267457.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ernie-image-turbo+zimage-turbo_双采样人像去油去拟合感_2044777572101267457.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `StringReplace`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `CLIPLoader`
- `PrimitiveBoolean`
- `TextGenerate`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `ComfySwitchNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `VAELoader`
- `CLIPLoader`
- `GetNode`
- `SaveImage`
- `Reroute (rgthree)`
- `PrimitiveStringMultiline`
- `VAELoader`
- `CLIPLoader`
- `SetNode`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `Int`
- `TTResolutionSelector`
- `EmptyFlux2LatentImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `Seed (rgthree)`
- `Int`
- `AddLabel`
- `Image Comparer (rgthree)`
- `AddLabel`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `ddim_uniform`

## 知识

覆盖率 **65%**（31/48）

**有卡**：`StringReplace`、`CLIPLoader`、`PrimitiveBoolean`、`TextGenerate`、`CLIPTextEncode`、`ConditioningZeroOut`、`VAELoader`、`SaveImage`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`VAEEncode`、`Int`、`TTResolutionSelector`、`EmptyFlux2LatentImage`、`Seed (rgthree)`、`AddLabel`、`KSamplerAdvanced`、`UNETLoader`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、KSamplerAdvanced
