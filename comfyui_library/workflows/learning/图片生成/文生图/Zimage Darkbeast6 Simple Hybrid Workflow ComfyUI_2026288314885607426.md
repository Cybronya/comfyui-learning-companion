---
key: 图片生成/文生图/Zimage Darkbeast6 Simple Hybrid Workflow ComfyUI_2026288314885607426.json
name: Zimage Darkbeast6 Simple Hybrid Workflow ComfyUI_2026288314885607426
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Zimage Darkbeast6 Simple Hybrid Workflow ComfyUI_2026288314885607426.json
hash: c99d127e599c9d3c
coverage: 0.761905
learned_at: 2026-10-19 22:30:09
nodes: [LoraLoaderModelOnly, ModelSamplingAuraFlow, UNETLoader, LoraLoaderModelOnly, Seed (rgthree), LatentUpscaleBy, UNETLoader, CLIPLoader, Note, SAMLoader, UltralyticsDetectorProvider, MaskToImage, PreviewImage, PreviewImage, PreviewImage, ConditioningZeroOut, Reroute, Reroute, VAELoader, LoadImage, SaveImage, DuckDecodeNode, Note, Note, DuckHideNode, CLIPTextEncode, ConditioningZeroOut, FaceDetailer, ModelSamplingAuraFlow, CLIPLoader, KSampler, EmptySD3LatentImage, KSampler, VAEDecode, VAEDecode, SaveImage, Image Comparer (rgthree), Reroute, KOOK_SaveJPGImage, CLIPTextEncode, CLIPTextEncode, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.75, "sampler_name": "euler", "scheduler": "simple", "seed": 957297162658210, "steps": 10}
---

# 图片生成/文生图/Zimage Darkbeast6 Simple Hybrid Workflow ComfyUI_2026288314885607426.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Zimage Darkbeast6 Simple Hybrid Workflow ComfyUI_2026288314885607426.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Seed (rgthree)`
- `LatentUpscaleBy`
- `UNETLoader` ★核心
- `CLIPLoader`
- `Note`
- `SAMLoader`
- `UltralyticsDetectorProvider`
- `MaskToImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `ConditioningZeroOut`
- `Reroute`
- `Reroute`
- `VAELoader`
- `LoadImage`
- `SaveImage`
- `DuckDecodeNode`
- `Note`
- `Note`
- `DuckHideNode`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `FaceDetailer`
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `Reroute`
- `KOOK_SaveJPGImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `957297162658210`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.75`

## 知识

覆盖率 **76%**（32/42）

**有卡**：`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`UNETLoader`、`Seed (rgthree)`、`LatentUpscaleBy`、`CLIPLoader`、`SAMLoader`、`UltralyticsDetectorProvider`、`MaskToImage`、`ConditioningZeroOut`、`VAELoader`、`LoadImage`、`SaveImage`、`DuckDecodeNode`、`DuckHideNode`、`CLIPTextEncode`、`FaceDetailer`、`KSampler`、`EmptySD3LatentImage`、`VAEDecode`、`KOOK_SaveJPGImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
