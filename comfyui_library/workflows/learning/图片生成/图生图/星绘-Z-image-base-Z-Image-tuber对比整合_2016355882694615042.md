---
key: 图片生成/图生图/星绘-Z-image-base-Z-Image-tuber对比整合_2016355882694615042.json
name: 星绘-Z-image-base-Z-Image-tuber对比整合_2016355882694615042
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/星绘-Z-image-base-Z-Image-tuber对比整合_2016355882694615042.json
hash: d275a5defc5a2e68
coverage: 1
learned_at: 2026-10-23 13:04:51
nodes: [VAELoader, CLIPLoader, UNETLoader, ModelSamplingAuraFlow, CLIPTextEncode, EmptySD3LatentImage, KSampler, VAEDecode, UNETLoader, ModelSamplingAuraFlow, VAELoader, CLIPLoader, LayerUtility: ImageReel, CLIPTextEncode, CLIPTextEncode, KSampler, VAEDecode, INTConstant, INTConstant, LayerUtility: ImageReelComposit, CLIPTextEncode, CR Text, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 128001005470511, "steps": 25}
---

# 图片生成/图生图/星绘-Z-image-base-Z-Image-tuber对比整合_2016355882694615042.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/星绘-Z-image-base-Z-Image-tuber对比整合_2016355882694615042.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `VAELoader`
- `CLIPLoader`
- `LayerUtility: ImageReel`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `INTConstant`
- `INTConstant`
- `LayerUtility: ImageReelComposit`
- `CLIPTextEncode` ★核心
- `CR Text`
- `SaveImage`

## 关键参数

- `seed` = `128001005470511`
- `steps` = `25`
- `cfg` = `3`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`EmptySD3LatentImage`、`KSampler`、`VAEDecode`、`LayerUtility: ImageReel`、`INTConstant`、`LayerUtility: ImageReelComposit`、`CR Text`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、SaveImage、EmptySD3LatentImage
