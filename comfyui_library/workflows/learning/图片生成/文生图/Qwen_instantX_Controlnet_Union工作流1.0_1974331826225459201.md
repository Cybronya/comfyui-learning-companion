---
key: 图片生成/文生图/Qwen_instantX_Controlnet_Union工作流1.0_1974331826225459201.json
name: Qwen_instantX_Controlnet_Union工作流1.0_1974331826225459201
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen_instantX_Controlnet_Union工作流1.0_1974331826225459201.json
hash: 299bb3ba68a3297c
coverage: 0.782609
learned_at: 2026-10-10 20:59:09
nodes: [SaveImage, CLIPLoader, UNETLoader, ModelSamplingAuraFlow, VAELoader, CLIPTextEncode, SaveImage, ImageConcatMulti, PreviewImage, VAEDecode, KSampler, ControlNetLoader, EmptySD3LatentImage, Reroute, LayerUtility: ImageScaleByAspectRatio V2, Reroute, LoraLoaderModelOnly, AIO_Preprocessor, SetUnionControlNetType, LoadImage, ControlNetApplySD3, CLIPTextEncode, MarkdownNote]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1.5, "controlnet_strength": 0.75, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 52738987569456, "steps": 8}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen_instantX_Controlnet_Union工作流1.0_1974331826225459201.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen_instantX_Controlnet_Union工作流1.0_1974331826225459201.json`

## 结构

**节点**（23 个）：
- `SaveImage`
- `CLIPLoader`
- `UNETLoader`
- `ModelSamplingAuraFlow`
- `VAELoader`
- `CLIPTextEncode`
- `SaveImage`
- `ImageConcatMulti`
- `PreviewImage`
- `VAEDecode`
- `KSampler`
- `ControlNetLoader`
- `EmptySD3LatentImage`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `LoraLoaderModelOnly`
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `LoadImage`
- `ControlNetApplySD3`
- `CLIPTextEncode`
- `MarkdownNote`

## 关键参数

- `cfg` = `1.5`
- `controlnet_strength` = `0.75`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `52738987569456`
- `steps` = `8`

## 知识

覆盖率 **78%**（18/23）

**有卡**：`SaveImage`、`CLIPLoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`VAELoader`、`CLIPTextEncode`、`ImageConcatMulti`、`PreviewImage`、`VAEDecode`、`KSampler`、`ControlNetLoader`、`EmptySD3LatentImage`、`Reroute`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderModelOnly`、`AIO_Preprocessor`

**缺卡**（1）：`LayerUtility: ImageScaleByAspectRatio V2`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
