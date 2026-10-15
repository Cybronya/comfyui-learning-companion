---
key: 视频生成/图生视频/Wan2.2-高速版-直出720p -自动提示词_1949982975842803713.json
name: Wan2.2-高速版-直出720p -自动提示词_1949982975842803713
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-高速版-直出720p -自动提示词_1949982975842803713.json
hash: 42e7e9a91e260ef6
coverage: 0.914894
learned_at: 2026-10-15 22:42:57
nodes: [JWInteger, JWInteger, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, KSamplerAdvanced, ModelSamplingSD3, WanImageToVideo, CLIPLoader, VAELoader, VAELoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, PathchSageAttentionKJ, CR Text Replace, RH_Captioner, TextBox, UNETLoader, CLIPTextEncode, CLIPTextEncode, TextBox, TextBox, CR Text Concatenate, LayerUtility: PurgeVRAM, TextBox, TextBox, Primitive integer [Crystools], SimpleMath+, Primitive integer [Crystools], PrimitiveBoolean, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, RHHiddenNodes, easy ifElse, TextBox, TextBox, ImageResizeKJ, ImageResizeKJ, VHS_VideoCombine, LoadImage, MarkdownNote, easy showAnything, LoadImage, ImpactSwitch]
patterns: []
missing: []
parameters: {"cfg": 7, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2-高速版-直出720p -自动提示词_1949982975842803713.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan2.2-高速版-直出720p -自动提示词_1949982975842803713.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（47 个）：
- `JWInteger`
- `JWInteger`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `WanImageToVideo`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `CR Text Replace`
- `RH_Captioner`
- `TextBox`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `TextBox`
- `TextBox`
- `CR Text Concatenate`
- `LayerUtility: PurgeVRAM`
- `TextBox`
- `TextBox`
- `Primitive integer [Crystools]`
- `SimpleMath+`
- `Primitive integer [Crystools]`
- `PrimitiveBoolean`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `RHHiddenNodes`
- `easy ifElse`
- `TextBox`
- `TextBox`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `VHS_VideoCombine`
- `LoadImage`
- `MarkdownNote`
- `easy showAnything`
- `LoadImage`
- `ImpactSwitch`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `7`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（43/47）

**有卡**：`JWInteger`、`LayerUtility: PurgeVRAM`、`KSamplerAdvanced`、`ModelSamplingSD3`、`WanImageToVideo`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`PathchSageAttentionKJ`、`CR Text Replace`、`RH_Captioner`、`TextBox`、`CLIPTextEncode`、`CR Text Concatenate`、`Primitive integer [Crystools]`、`SimpleMath+`、`PrimitiveBoolean`、`VAEDecode`、`VHS_VideoCombine`、`RHHiddenNodes`、`ImageResizeKJ`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
