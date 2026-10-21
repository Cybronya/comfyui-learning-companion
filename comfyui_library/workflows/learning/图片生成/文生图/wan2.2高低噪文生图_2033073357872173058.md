---
key: 图片生成/文生图/wan2.2高低噪文生图_2033073357872173058.json
name: wan2.2高低噪文生图_2033073357872173058
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2高低噪文生图_2033073357872173058.json
hash: 790ae8f1000dcb37
coverage: 0.869565
learned_at: 2026-10-21 02:57:40
nodes: [VAELoader, CLIPLoader, CLIPTextEncode, UNETLoader, UNETLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, VAEDecode, KSampler, VAEDecode, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, ModelSamplingSD3, LoraLoaderModelOnly, KSampler, SaveImage, ModelSamplingSD3, easy seed, PreviewImage, Int, Int, Note, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 0, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/wan2.2高低噪文生图_2033073357872173058.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2高低噪文生图_2033073357872173058.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（23 个）：
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `SaveImage`
- `ModelSamplingSD3`
- `easy seed`
- `PreviewImage`
- `Int`
- `Int`
- `Note`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `0`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`UNETLoader`、`EmptyHunyuanLatentVideo`、`VAEDecode`、`KSampler`、`LayerUtility: PurgeVRAM V2`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`SaveImage`、`easy seed`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、easy seed

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
