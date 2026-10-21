---
key: 图片生成/文生图/Z-Image_turbo控制姿态ControlNe_2038525013095092225.json
name: Z-Image_turbo控制姿态ControlNe_2038525013095092225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image_turbo控制姿态ControlNe_2038525013095092225.json
hash: 2346ce7e5d0ee39e
coverage: 0.857143
learned_at: 2026-10-21 02:55:59
nodes: [CLIPLoader, CLIPTextEncode, UNETLoader, ModelPatchLoader, QwenImageDiffsynthControlnet, ModelSamplingAuraFlow, KSampler, VAELoader, VAEDecode, GetImageSize, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, PreviewImage, CannyEdgePreprocessor, PreviewImage, DepthAnythingV2Preprocessor, DWPreprocessor, CLIPTextEncode, PreviewImage, EmptySD3LatentImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 533513936891145, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-Image_turbo控制姿态ControlNe_2038525013095092225.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image_turbo控制姿态ControlNe_2038525013095092225.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `ModelPatchLoader`
- `QwenImageDiffsynthControlnet`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `GetImageSize`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `PreviewImage`
- `CannyEdgePreprocessor`
- `PreviewImage`
- `DepthAnythingV2Preprocessor`
- `DWPreprocessor`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `EmptySD3LatentImage`

## 关键参数

- `seed` = `533513936891145`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`UNETLoader`、`ModelPatchLoader`、`QwenImageDiffsynthControlnet`、`ModelSamplingAuraFlow`、`KSampler`、`VAELoader`、`VAEDecode`、`GetImageSize`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`SaveImage`、`CannyEdgePreprocessor`、`DepthAnythingV2Preprocessor`、`DWPreprocessor`、`EmptySD3LatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、DepthAnythingV2Preprocessor

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
