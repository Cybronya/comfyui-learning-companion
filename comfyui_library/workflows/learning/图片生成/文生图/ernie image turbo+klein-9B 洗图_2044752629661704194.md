---
key: 图片生成/文生图/ernie image turbo+klein-9B 洗图_2044752629661704194.json
name: ernie image turbo+klein-9B 洗图_2044752629661704194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ernie image turbo+klein-9B 洗图_2044752629661704194.json
hash: a221498a82317a3f
coverage: 0.909091
learned_at: 2026-10-21 02:56:43
nodes: [CLIPTextEncode, ConditioningZeroOut, ComfySwitchNode, CLIPLoader, PrimitiveStringMultiline, StringReplace, TextGenerate, UNETLoader, VAELoader, ConditioningZeroOut, CLIPLoader, VAELoader, PrimitiveBoolean, UNETLoader, KSamplerAdvanced, CLIPTextEncode, KSamplerAdvanced, ImageConcanate, Seed (rgthree), easy int, Fast Groups Bypasser (rgthree), easy int, SaveImage, VAEDecode, LayerUtility: PurgeVRAM V2, VAEEncode, EmptyFlux2LatentImage, AddLabel, AddLabel, SaveImage, LayerUtility: PurgeVRAM V2, SaveImage, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/文生图/ernie image turbo+klein-9B 洗图_2044752629661704194.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ernie image turbo+klein-9B 洗图_2044752629661704194.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ComfySwitchNode`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `StringReplace`
- `TextGenerate`
- `UNETLoader` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `CLIPLoader`
- `VAELoader`
- `PrimitiveBoolean`
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `ImageConcanate`
- `Seed (rgthree)`
- `easy int`
- `Fast Groups Bypasser (rgthree)`
- `easy int`
- `SaveImage`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VAEEncode` ★核心
- `EmptyFlux2LatentImage`
- `AddLabel`
- `AddLabel`
- `SaveImage`
- `LayerUtility: PurgeVRAM V2`
- `SaveImage`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`CLIPTextEncode`、`ConditioningZeroOut`、`CLIPLoader`、`StringReplace`、`TextGenerate`、`UNETLoader`、`VAELoader`、`PrimitiveBoolean`、`KSamplerAdvanced`、`ImageConcanate`、`Seed (rgthree)`、`easy int`、`SaveImage`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`VAEEncode`、`EmptyFlux2LatentImage`、`AddLabel`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、KSamplerAdvanced、Seed (rgthree)
