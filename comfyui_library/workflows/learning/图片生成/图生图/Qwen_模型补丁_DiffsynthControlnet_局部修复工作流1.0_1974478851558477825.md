---
key: 图片生成/图生图/Qwen_模型补丁_DiffsynthControlnet_局部修复工作流1.0_1974478851558477825.json
name: Qwen_模型补丁_DiffsynthControlnet_局部修复工作流1.0_1974478851558477825
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_模型补丁_DiffsynthControlnet_局部修复工作流1.0_1974478851558477825.json
hash: 47d05fbc6d095c31
coverage: 0.833333
learned_at: 2026-10-23 11:21:41
nodes: [EmptySD3LatentImage, CLIPTextEncode, CLIPLoader, VAELoader, ModelSamplingAuraFlow, UNETLoader, PreviewImage, VAEDecode, AIO_Preprocessor, QwenImageDiffsynthControlnet, LayerUtility: ImageScaleByAspectRatio V2, Reroute, Reroute, SaveImage, LoraLoaderModelOnly, ModelPatchLoader, ImageConcatMulti, MaskToImage, LoadImage, InvertMask, KSampler, SaveImage, CLIPTextEncode, MarkdownNote]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 106, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen_模型补丁_DiffsynthControlnet_局部修复工作流1.0_1974478851558477825.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_模型补丁_DiffsynthControlnet_局部修复工作流1.0_1974478851558477825.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `AIO_Preprocessor`
- `QwenImageDiffsynthControlnet`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `Reroute`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `ModelPatchLoader`
- `ImageConcatMulti`
- `MaskToImage`
- `LoadImage`
- `InvertMask`
- `KSampler` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `MarkdownNote`

## 关键参数

- `seed` = `106`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`EmptySD3LatentImage`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`UNETLoader`、`VAEDecode`、`AIO_Preprocessor`、`QwenImageDiffsynthControlnet`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`LoraLoaderModelOnly`、`ModelPatchLoader`、`ImageConcatMulti`、`MaskToImage`、`LoadImage`、`InvertMask`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
