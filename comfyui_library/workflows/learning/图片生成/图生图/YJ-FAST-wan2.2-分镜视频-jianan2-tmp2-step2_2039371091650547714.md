---
key: 图片生成/图生图/YJ-FAST-wan2.2-分镜视频-jianan2-tmp2-step2_2039371091650547714.json
name: YJ-FAST-wan2.2-分镜视频-jianan2-tmp2-step2_2039371091650547714
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/YJ-FAST-wan2.2-分镜视频-jianan2-tmp2-step2_2039371091650547714.json
hash: 669383c738e12018
coverage: 0.492754
learned_at: 2026-10-23 11:28:51
nodes: [Note, KSamplerAdvanced, VAELoader, CLIPLoader, SetNode, GetNode, SetNode, CLIPVisionEncode, CLIPVisionLoader, SetNode, SetNode, GetNode, GetNode, GetNode, LayerUtility: PurgeVRAM, VAEDecode, GetNode, SetNode, KSamplerAdvanced, SetNode, Note, Note, GetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree), GetNode, GetNode, GetNode, Note, SetNode, LoraLoaderModelOnly, PathchSageAttentionKJ, SetNode, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, GetNode, GetNode, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, GetNode, LayerUtility: PurgeVRAM V2, Switch, SetNode, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, SetNode, CLIPTextEncode, GetNode, CR Prompt Text, CR Prompt Text, CR Prompt Text, LoadImage, SetNode, SetNode, SetNode, ImageResizeKJv2, PrimitiveInt, VHS_VideoCombine, UNETLoader, UNETLoader, CR Prompt Text, JWInteger, JWInteger, JWInteger, VHS_VideoCombine, RIFE VFI]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/YJ-FAST-wan2.2-分镜视频-jianan2-tmp2-step2_2039371091650547714.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/YJ-FAST-wan2.2-分镜视频-jianan2-tmp2-step2_2039371091650547714.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（69 个）：
- `Note`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `CLIPLoader`
- `SetNode`
- `GetNode`
- `SetNode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `SetNode`
- `Note`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `SetNode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `GetNode`
- `LayerUtility: PurgeVRAM V2`
- `Switch`
- `SetNode`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CR Prompt Text`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`
- `RIFE VFI`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **49%**（34/69）

**有卡**：`KSamplerAdvanced`、`VAELoader`、`CLIPLoader`、`CLIPVisionEncode`、`CLIPVisionLoader`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPTextEncode`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`LayerUtility: PurgeVRAM V2`、`Switch`、`CR Prompt Text`、`LoadImage`、`ImageResizeKJv2`、`VHS_VideoCombine`、`UNETLoader`、`JWInteger`、`RIFE VFI`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
