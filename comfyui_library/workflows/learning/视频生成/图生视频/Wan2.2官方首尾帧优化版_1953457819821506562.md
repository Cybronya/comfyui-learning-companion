---
key: 视频生成/图生视频/Wan2.2官方首尾帧优化版_1953457819821506562.json
name: Wan2.2官方首尾帧优化版_1953457819821506562.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2官方首尾帧优化版_1953457819821506562.json
hash: 973a82422436ea52
coverage: 0.75
learned_at: 2026-10-15 22:31:05
nodes: [JWInteger, PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, SetNode, VAELoader, GetNode, ModelSamplingSD3, SetNode, PathchSageAttentionKJ, SetNode, LoraLoaderModelOnly, UNETLoader, SetNode, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, UNETLoader, LoraLoaderModelOnly, Note, ImpactSwitch, LoadImage, GetNode, VAEDecode, ImageConcanate, ImageConcanate, CLIPTextEncode, RH_LLMAPI_NODE, ImageConcanate, KSamplerAdvanced, KSamplerAdvanced, ImageResizeKJ, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, GetNode, GetNode, CLIPVisionEncode, CLIPTextEncode, Note, LoadImage, CR Text, MathExpression|pysssss, VHS_VideoCombine, VHS_VideoCombine, WanFirstLastFrameToVideo, CLIPVisionEncode, WanVideoNAG, easy showAnything, JWInteger]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2官方首尾帧优化版_1953457819821506562.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1953457819821506562.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（48 个）：
- `JWInteger`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `GetNode`
- `ModelSamplingSD3`
- `SetNode`
- `PathchSageAttentionKJ`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `ImpactSwitch`
- `LoadImage`
- `GetNode`
- `VAEDecode` ★核心
- `ImageConcanate`
- `ImageConcanate`
- `CLIPTextEncode` ★核心
- `RH_LLMAPI_NODE`
- `ImageConcanate`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ImageResizeKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `Note`
- `LoadImage`
- `CR Text`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `CLIPVisionEncode`
- `WanVideoNAG`
- `easy showAnything`
- `JWInteger`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **75%**（36/48）

**有卡**：`JWInteger`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`LayerUtility: PurgeVRAM V2`、`LoadImage`、`VAEDecode`、`ImageConcanate`、`CLIPTextEncode`、`RH_LLMAPI_NODE`、`KSamplerAdvanced`、`ImageResizeKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionLoader`、`CLIPVisionEncode`、`CR Text`、`MathExpression|pysssss`、`VHS_VideoCombine`、`WanFirstLastFrameToVideo`、`WanVideoNAG`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
