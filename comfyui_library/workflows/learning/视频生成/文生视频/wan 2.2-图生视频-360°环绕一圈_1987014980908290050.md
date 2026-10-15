---
key: 视频生成/文生视频/wan 2.2-图生视频-360°环绕一圈_1987014980908290050.json
name: wan 2.2-图生视频-360°环绕一圈_1987014980908290050
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan 2.2-图生视频-360°环绕一圈_1987014980908290050.json
hash: 9cf7f9e3eb8d9827
coverage: 1
learned_at: 2026-10-15 22:47:34
nodes: [PathchSageAttentionKJ, LoraLoaderModelOnly, ModelSamplingSD3, Seed Generator, ImpactInt, KSamplerAdvanced, LayerUtility: PurgeVRAM, CLIPTextEncode, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, ModelSamplingSD3, KSamplerAdvanced, SimpleMath+, CLIPTextEncode, VHS_VideoCombine, UNETLoader, LayerUtility: PurgeVRAM, CLIPLoader, VAELoader, UNETLoader, SaveImage, LoadImage, WanImageToVideo, ImpactInt, CR Text, LayerUtility: ImageScaleByAspectRatio V2, Int]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "randomize"}
---

# 视频生成/文生视频/wan 2.2-图生视频-360°环绕一圈_1987014980908290050.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan 2.2-图生视频-360°环绕一圈_1987014980908290050.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `Seed Generator`
- `ImpactInt`
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `SaveImage`
- `LoadImage`
- `WanImageToVideo`
- `ImpactInt`
- `CR Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`Seed Generator`、`ImpactInt`、`KSamplerAdvanced`、`LayerUtility: PurgeVRAM`、`CLIPTextEncode`、`VAEDecode`、`SimpleMath+`、`VHS_VideoCombine`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImage`、`LoadImage`、`WanImageToVideo`、`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
