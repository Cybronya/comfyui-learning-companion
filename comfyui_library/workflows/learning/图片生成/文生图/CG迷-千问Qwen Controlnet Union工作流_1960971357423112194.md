---
key: 图片生成/文生图/CG迷-千问Qwen Controlnet Union工作流_1960971357423112194.json
name: CG迷-千问Qwen Controlnet Union工作流_1960971357423112194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/CG迷-千问Qwen Controlnet Union工作流_1960971357423112194.json
hash: 7ec74052bb8e4207
coverage: 0.842105
learned_at: 2026-10-10 21:26:39
nodes: [EmptySD3LatentImage, VAEDecode, SaveImage, KSampler, ModelSamplingAuraFlow, CLIPTextEncode, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, SetUnionControlNetType, ControlNetApplySD3, PreviewImage, AIO_Preprocessor, ControlNetLoader, LoadImage, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, MarkdownNote]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1.5, "controlnet_strength": 0.75, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 569868966801842, "steps": 8}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/CG迷-千问Qwen Controlnet Union工作流_1960971357423112194.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/CG迷-千问Qwen Controlnet Union工作流_1960971357423112194.json`

## 结构

**节点**（19 个）：
- `EmptySD3LatentImage`
- `VAEDecode`
- `SaveImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetUnionControlNetType`
- `ControlNetApplySD3`
- `PreviewImage`
- `AIO_Preprocessor`
- `ControlNetLoader`
- `LoadImage`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly`
- `MarkdownNote`

## 关键参数

- `cfg` = `1.5`
- `controlnet_strength` = `0.75`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `569868966801842`
- `steps` = `8`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`EmptySD3LatentImage`、`VAEDecode`、`SaveImage`、`KSampler`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`SetUnionControlNetType`、`ControlNetApplySD3`、`PreviewImage`、`AIO_Preprocessor`、`ControlNetLoader`、`LoadImage`、`UNETLoader`、`CLIPLoader`

**缺卡**（1）：`LayerUtility: ImageScaleByAspectRatio V2`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
