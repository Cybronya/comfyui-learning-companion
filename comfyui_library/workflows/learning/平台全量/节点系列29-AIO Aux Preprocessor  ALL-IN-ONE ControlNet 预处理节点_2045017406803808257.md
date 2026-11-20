---
key: 平台全量/节点系列29-AIO Aux Preprocessor  ALL-IN-ONE ControlNet 预处理节点_2045017406803808257.json
name: 节点系列29-AIO Aux Preprocessor  ALL-IN-ONE ControlNet 预处理节点_2045017406803808257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/节点系列29-AIO Aux Preprocessor  ALL-IN-ONE ControlNet 预处理节点_2045017406803808257.json
hash: 5c695469cca5bc5a
coverage: 0.75
learned_at: 2026-11-14 02:32:30
nodes: [Reroute, UNETLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, VAELoader, ModelPatchLoader, EmptySD3LatentImage, Seed (rgthree), VAEDecode, Image Comparer (rgthree), Image Comparer (rgthree), ConditioningZeroOut, LoadImage, CLIPTextEncode, KSampler, CLIPLoader, VAELoader, ModelPatchLoader, EmptySD3LatentImage, Seed (rgthree), ModelSamplingAuraFlow, VAEDecode, Image Comparer (rgthree), Image Comparer (rgthree), PreviewImage, ConditioningZeroOut, QwenImageDiffsynthControlnet, UNETLoader, LoadImage, CLIPTextEncode, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, LoadImage, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, LoadImage, AIO_Preprocessor, PreviewImage, LoadImage, ModelSamplingAuraFlow, AIO_Preprocessor, QwenImageDiffsynthControlnet, AIO_Preprocessor, PreviewImage, PreviewImage, SaveImage, PreviewImage, PreviewImage, PreviewImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 969839779407136, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/节点系列29-AIO Aux Preprocessor  ALL-IN-ONE ControlNet 预处理节点_2045017406803808257.json

> 来源文件 `comfyui_library/workflows/平台全量/节点系列29-AIO Aux Preprocessor  ALL-IN-ONE ControlNet 预处理节点_2045017406803808257.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `Reroute`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `VAELoader`
- `ModelPatchLoader`
- `EmptySD3LatentImage`
- `Seed (rgthree)`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `ConditioningZeroOut`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelPatchLoader`
- `EmptySD3LatentImage`
- `Seed (rgthree)`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `ConditioningZeroOut`
- `QwenImageDiffsynthControlnet`
- `UNETLoader` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `LoadImage`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `LoadImage`
- `AIO_Preprocessor`
- `PreviewImage`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `AIO_Preprocessor`
- `QwenImageDiffsynthControlnet`
- `AIO_Preprocessor`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`

## 关键参数

- `seed` = `969839779407136`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **75%**（39/52）

**有卡**：`UNETLoader`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`VAELoader`、`ModelPatchLoader`、`EmptySD3LatentImage`、`Seed (rgthree)`、`VAEDecode`、`ConditioningZeroOut`、`LoadImage`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`QwenImageDiffsynthControlnet`、`SaveImage`、`AIO_Preprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
