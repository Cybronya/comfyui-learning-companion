---
key: 图片生成/图生图/YJ-FAST-wan2.2-分镜视频-grand-tmp2-step2_2038262525682257922.json
name: YJ-FAST-wan2.2-分镜视频-grand-tmp2-step2_2038262525682257922
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/YJ-FAST-wan2.2-分镜视频-grand-tmp2-step2_2038262525682257922.json
hash: a1b53bae75d4aa98
coverage: 0.492754
learned_at: 2026-10-23 11:28:50
nodes: [Note, KSamplerAdvanced, VAELoader, CLIPLoader, SetNode, GetNode, SetNode, CLIPVisionEncode, CLIPVisionLoader, SetNode, GetNode, GetNode, GetNode, LayerUtility: PurgeVRAM, VAEDecode, GetNode, SetNode, KSamplerAdvanced, SetNode, Note, Note, GetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree), Note, GetNode, GetNode, GetNode, Note, SetNode, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, GetNode, GetNode, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, GetNode, LayerUtility: PurgeVRAM V2, Switch, SetNode, CR Prompt Text, CR Prompt Text, UNETLoader, UNETLoader, LoraLoaderModelOnly, SetNode, LoraLoaderModelOnly, CR Prompt Text, SetNode, CLIPTextEncode, SetNode, CLIPTextEncode, GetNode, VHS_VideoCombine, LoadImage, SetNode, SetNode, SetNode, ImageResizeKJv2, PrimitiveInt, CR Prompt Text, RIFE VFI, VHS_VideoCombine, JWInteger, JWInteger, JWInteger]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/YJ-FAST-wan2.2-分镜视频-grand-tmp2-step2_2038262525682257922.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/YJ-FAST-wan2.2-分镜视频-grand-tmp2-step2_2038262525682257922.json`

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
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `GetNode`
- `GetNode`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `GetNode`
- `LayerUtility: PurgeVRAM V2`
- `Switch`
- `SetNode`
- `CR Prompt Text`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `PrimitiveInt`
- `CR Prompt Text`
- `RIFE VFI`
- `VHS_VideoCombine`
- `JWInteger`
- `JWInteger`
- `JWInteger`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **49%**（34/69）

**有卡**：`KSamplerAdvanced`、`VAELoader`、`CLIPLoader`、`CLIPVisionEncode`、`CLIPVisionLoader`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`LayerUtility: PurgeVRAM V2`、`Switch`、`CR Prompt Text`、`UNETLoader`、`CLIPTextEncode`、`VHS_VideoCombine`、`LoadImage`、`ImageResizeKJv2`、`RIFE VFI`、`JWInteger`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
