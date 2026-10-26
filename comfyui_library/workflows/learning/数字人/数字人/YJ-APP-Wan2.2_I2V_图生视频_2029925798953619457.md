---
key: 数字人/数字人/YJ-APP-Wan2.2_I2V_图生视频_2029925798953619457.json
name: YJ-APP-Wan2.2_I2V_图生视频_2029925798953619457
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/YJ-APP-Wan2.2_I2V_图生视频_2029925798953619457.json
hash: 335be493a835e333
coverage: 0.492958
learned_at: 2026-10-26 01:58:13
nodes: [Note, KSamplerAdvanced, Note, GetNode, GetNode, VAELoader, CLIPLoader, SetNode, GetNode, SetNode, CLIPVisionEncode, CLIPVisionLoader, SetNode, SetNode, SetNode, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, LayerUtility: PurgeVRAM, VAEDecode, GetNode, SetNode, KSamplerAdvanced, Note, SetNode, Note, SetNode, LoraLoaderModelOnly, PathchSageAttentionKJ, SetNode, ModelSamplingSD3, ModelSamplingSD3, VHS_VideoCombine, PathchSageAttentionKJ, Note, JWInteger, JWInteger, Note, Note, SetNode, SimpleMath+, JWInteger, SetNode, SetNode, SetNode, ImageResizeKJv2, Fast Groups Bypasser (rgthree), Text, LoraLoaderModelOnly, LoraLoaderModelOnly, Switch, Switch, UNETLoader, UNETLoader, UNETLoader, UNETLoader, Int, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, WanImageToVideo, GetNode, GetNode, GetNode, Float, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 数字人/数字人/YJ-APP-Wan2.2_I2V_图生视频_2029925798953619457.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/YJ-APP-Wan2.2_I2V_图生视频_2029925798953619457.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（71 个）：
- `Note`
- `KSamplerAdvanced` ★核心
- `Note`
- `GetNode`
- `GetNode`
- `VAELoader`
- `CLIPLoader`
- `SetNode`
- `GetNode`
- `SetNode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `Note`
- `SetNode`
- `Note`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `SetNode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `PathchSageAttentionKJ`
- `Note`
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`
- `SetNode`
- `SimpleMath+`
- `JWInteger`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `Fast Groups Bypasser (rgthree)`
- `Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Switch`
- `Switch`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Int`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `WanImageToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `Float`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **49%**（35/71）

**有卡**：`KSamplerAdvanced`、`VAELoader`、`CLIPLoader`、`CLIPVisionEncode`、`CLIPVisionLoader`、`CLIPTextEncode`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VHS_VideoCombine`、`JWInteger`、`SimpleMath+`、`ImageResizeKJv2`、`Text`、`Switch`、`UNETLoader`、`Int`、`LoadImage`、`WanImageToVideo`、`Float`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
