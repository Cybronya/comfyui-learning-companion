---
key: 视频生成/图生视频/Wan2.2 电影级画面图生视频_1950023437323517954.json
name: Wan2.2 电影级画面图生视频_1950023437323517954.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950023437323517954.json
hash: 25aea7a203ce8594
coverage: 0.933333
learned_at: 2026-10-15 22:30:51
nodes: [JWInteger, JWInteger, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, KSamplerAdvanced, ModelSamplingSD3, WanImageToVideo, CLIPLoader, VAELoader, VAELoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, PathchSageAttentionKJ, CR Text Replace, RH_Captioner, TextBox, UNETLoader, CLIPTextEncode, CLIPTextEncode, TextBox, TextBox, CR Text Concatenate, LayerUtility: PurgeVRAM, TextBox, TextBox, Primitive integer [Crystools], SimpleMath+, Primitive integer [Crystools], PrimitiveBoolean, KSamplerAdvanced, ImageResizeKJ, VAEDecode, VHS_VideoCombine, RHHiddenNodes, ImageResizeKJ, VHS_VideoCombine, easy ifElse, easy showAnything, TextBox, ImpactSwitch, LoadImage, TextBox]
patterns: []
missing: []
parameters: {"cfg": 7, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 电影级画面图生视频_1950023437323517954.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950023437323517954.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（45 个）：
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
- `ImageResizeKJ`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `RHHiddenNodes`
- `ImageResizeKJ`
- `VHS_VideoCombine`
- `easy ifElse`
- `easy showAnything`
- `TextBox`
- `ImpactSwitch`
- `LoadImage`
- `TextBox`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `7`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **93%**（42/45）

**有卡**：`JWInteger`、`LayerUtility: PurgeVRAM`、`KSamplerAdvanced`、`ModelSamplingSD3`、`WanImageToVideo`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`PathchSageAttentionKJ`、`CR Text Replace`、`RH_Captioner`、`TextBox`、`CLIPTextEncode`、`CR Text Concatenate`、`Primitive integer [Crystools]`、`SimpleMath+`、`PrimitiveBoolean`、`ImageResizeKJ`、`VAEDecode`、`VHS_VideoCombine`、`RHHiddenNodes`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
