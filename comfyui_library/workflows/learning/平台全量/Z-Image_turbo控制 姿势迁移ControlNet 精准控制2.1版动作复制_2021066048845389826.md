---
key: 平台全量/Z-Image_turbo控制 姿势迁移ControlNet 精准控制2.1版动作复制_2021066048845389826.json
name: Z-Image_turbo控制 姿势迁移ControlNet 精准控制2.1版动作复制_2021066048845389826
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Z-Image_turbo控制 姿势迁移ControlNet 精准控制2.1版动作复制_2021066048845389826.json
hash: a589f19d8fa422c7
coverage: 0.875
learned_at: 2026-11-14 01:08:15
nodes: [CLIPLoader, CLIPTextEncode, UNETLoader, CannyEdgePreprocessor, EmptySD3LatentImage, DWPreprocessor, DepthAnythingV2Preprocessor, ModelPatchLoader, QwenImageDiffsynthControlnet, ModelSamplingAuraFlow, PreviewImage, PreviewImage, PreviewImage, KSampler, VAELoader, VAEDecode, CLIPTextEncode, GetImageSize, LoadImage, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, Qwen3_VQA, CR Text Concatenate, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 533513936891145, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Z-Image_turbo控制 姿势迁移ControlNet 精准控制2.1版动作复制_2021066048845389826.json

> 来源文件 `comfyui_library/workflows/平台全量/Z-Image_turbo控制 姿势迁移ControlNet 精准控制2.1版动作复制_2021066048845389826.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CannyEdgePreprocessor`
- `EmptySD3LatentImage`
- `DWPreprocessor`
- `DepthAnythingV2Preprocessor`
- `ModelPatchLoader`
- `QwenImageDiffsynthControlnet`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `LoadImage`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Qwen3_VQA`
- `CR Text Concatenate`
- `CR Text`

## 关键参数

- `seed` = `533513936891145`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`UNETLoader`、`CannyEdgePreprocessor`、`EmptySD3LatentImage`、`DWPreprocessor`、`DepthAnythingV2Preprocessor`、`ModelPatchLoader`、`QwenImageDiffsynthControlnet`、`ModelSamplingAuraFlow`、`KSampler`、`VAELoader`、`VAEDecode`、`GetImageSize`、`LoadImage`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`Qwen3_VQA`、`CR Text Concatenate`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、CannyEdgePreprocessor

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
