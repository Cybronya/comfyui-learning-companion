---
key: 视频生成/图生视频/wan2.2图生视频美女跳舞6步极速版预置多段背景音乐随机_1952322555396984834.json
name: wan2.2图生视频美女跳舞6步极速版预置多段背景音乐随机_1952322555396984834.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2图生视频美女跳舞6步极速版预置多段背景音乐随机_1952322555396984834.json
hash: a1d2b5efaa596868
coverage: 1
learned_at: 2026-10-15 22:31:01
nodes: [UNETLoader, UNETLoader, CLIPLoader, VAELoader, Random Number, LayerUtility: PurgeVRAM, PathchSageAttentionKJ, CLIPTextEncode, WanImageToVideo, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, LayerUtility: PurgeVRAM, VAEDecode, JWInteger, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, CR Text, LoadImage, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, LoadAudio, LoadAudio, LoadAudio, LoadAudio, LoadAudio, LoadAudio, LoadAudio, InversionDemoLazyIndexSwitch]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2图生视频美女跳舞6步极速版预置多段背景音乐随机_1952322555396984834.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952322555396984834.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（33 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Random Number`
- `LayerUtility: PurgeVRAM`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `JWInteger`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text`
- `LoadImage`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `InversionDemoLazyIndexSwitch`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（33/33）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`Random Number`、`LayerUtility: PurgeVRAM`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`WanImageToVideo`、`ModelSamplingSD3`、`VAEDecode`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Text`、`LoadImage`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`LoadAudio`、`InversionDemoLazyIndexSwitch`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
