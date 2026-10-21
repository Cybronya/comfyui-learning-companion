---
key: 图片生成/文生图/AA--缓存加速Zimage-base-MeanCache5种加速模式对比_2019746684867190785.json
name: AA--缓存加速Zimage-base-MeanCache5种加速模式对比_2019746684867190785
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/AA--缓存加速Zimage-base-MeanCache5种加速模式对比_2019746684867190785.json
hash: 0c47e55464fa9b6d
coverage: 0.971014
learned_at: 2026-10-19 22:29:32
nodes: [CLIPLoader, CLIPTextEncode, VAELoader, ModelSamplingAuraFlow, KSampler, CLIPTextEncode, MarkdownNote, Note, CLIPLoader, CLIPTextEncode, VAELoader, UNETLoader, KSampler, CLIPTextEncode, ModelSamplingAuraFlow, CLIPLoader, CLIPTextEncode, VAELoader, UNETLoader, ModelSamplingAuraFlow, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, ModelSamplingAuraFlow, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, VAELoader, ModelSamplingAuraFlow, KSampler, CLIPTextEncode, MeanCache_ZImage, MeanCache_ZImage, MeanCache_ZImage, MeanCache_ZImage, AddLabel, LayerUtility: PurgeVRAM, SaveImage, VAEDecode, VAEDecode, SaveImage, VAEDecode, VAEDecode, LayerUtility: PurgeVRAM, AddLabel, AddLabel, AddLabel, SaveImage, VAEDecode, ImageConcatMulti, LayerUtility: PurgeVRAM, EmptySD3LatentImage, EmptySD3LatentImage, EmptySD3LatentImage, EmptySD3LatentImage, EmptySD3LatentImage, MeanCache_ZImage, UNETLoader, VAELoader, UNETLoader, UNETLoader, SaveImage, SaveImage, LayerUtility: PurgeVRAM, AddLabel, SaveImage, LayerUtility: PurgeVRAM]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 1041512707229443, "steps": 50}
---

# 图片生成/文生图/AA--缓存加速Zimage-base-MeanCache5种加速模式对比_2019746684867190785.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/AA--缓存加速Zimage-base-MeanCache5种加速模式对比_2019746684867190785.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `Note`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `MeanCache_ZImage`
- `MeanCache_ZImage`
- `MeanCache_ZImage`
- `MeanCache_ZImage`
- `AddLabel`
- `LayerUtility: PurgeVRAM`
- `SaveImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `SaveImage`
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `LayerUtility: PurgeVRAM`
- `EmptySD3LatentImage`
- `EmptySD3LatentImage`
- `EmptySD3LatentImage`
- `EmptySD3LatentImage`
- `EmptySD3LatentImage`
- `MeanCache_ZImage`
- `UNETLoader` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `SaveImage`
- `LayerUtility: PurgeVRAM`
- `AddLabel`
- `SaveImage`
- `LayerUtility: PurgeVRAM`

## 关键参数

- `seed` = `1041512707229443`
- `steps` = `50`
- `cfg` = `4`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **97%**（67/69）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`ModelSamplingAuraFlow`、`KSampler`、`UNETLoader`、`MeanCache_ZImage`、`AddLabel`、`LayerUtility: PurgeVRAM`、`SaveImage`、`VAEDecode`、`ImageConcatMulti`、`EmptySD3LatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、SaveImage、EmptySD3LatentImage
