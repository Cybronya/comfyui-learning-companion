---
key: 视频生成/图生视频/wan2.2_14B_自动提示词优化_图生视频-加速版-KJ模型_1950557926803099649.json
name: wan2.2_14B_自动提示词优化_图生视频-加速版-KJ模型_1950557926803099649.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950557926803099649.json
hash: 79b76d967c449380
coverage: 0.857143
learned_at: 2026-10-15 22:30:55
nodes: [CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, WanImageToVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, easy ifElse, TextBox, MarkdownNote, PrimitiveBoolean, TextBox, MarkdownNote, ImpactSwitch, TextBox, RH_Translator, CLIPTextEncode, TextBox, CR Text Replace, easy showAnything, CR Text Concatenate, RH_Captioner, LayerUtility: PurgeVRAM, easy showAnything, LoadImage, Text, SimpleMath+, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, VAELoader, VAEDecode, CreateVideo, ImpactInt, KSamplerAdvanced, KSamplerAdvanced, TextBox, SaveVideo, ImpactInt, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2_14B_自动提示词优化_图生视频-加速版-KJ模型_1950557926803099649.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950557926803099649.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `WanImageToVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `easy ifElse`
- `TextBox`
- `MarkdownNote`
- `PrimitiveBoolean`
- `TextBox`
- `MarkdownNote`
- `ImpactSwitch`
- `TextBox`
- `RH_Translator`
- `CLIPTextEncode` ★核心
- `TextBox`
- `CR Text Replace`
- `easy showAnything`
- `CR Text Concatenate`
- `RH_Captioner`
- `LayerUtility: PurgeVRAM`
- `easy showAnything`
- `LoadImage`
- `Text`
- `SimpleMath+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `CreateVideo`
- `ImpactInt`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `TextBox`
- `SaveVideo`
- `ImpactInt`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **86%**（36/42）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`WanImageToVideo`、`LoraLoaderModelOnly`、`UNETLoader`、`TextBox`、`PrimitiveBoolean`、`RH_Translator`、`CR Text Replace`、`CR Text Concatenate`、`RH_Captioner`、`LayerUtility: PurgeVRAM`、`LoadImage`、`Text`、`SimpleMath+`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`CreateVideo`、`ImpactInt`、`KSamplerAdvanced`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
