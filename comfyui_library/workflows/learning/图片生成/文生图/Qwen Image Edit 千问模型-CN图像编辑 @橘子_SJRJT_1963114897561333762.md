---
key: 图片生成/文生图/Qwen Image Edit 千问模型-CN图像编辑 @橘子_SJRJT_1963114897561333762.json
name: Qwen Image Edit 千问模型-CN图像编辑 @橘子_SJRJT_1963114897561333762.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image Edit 千问模型-CN图像编辑 @橘子_SJRJT_1963114897561333762.json
hash: 4c36d94aaf865399
coverage: 0.777778
learned_at: 2026-10-07 23:54:18
nodes: [VAEDecode, MarkdownNote, EmptyLatentImage, CFGNorm, ModelSamplingAuraFlow, TextEncodeQwenImageEdit, KSampler, VAEEncode, MarkdownNote, MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, AIO_Preprocessor, OpenposePreprocessor, PreviewImage, SetUnionControlNetType, ControlNetApplySD3, CLIPLoader, VAELoader, TextEncodeQwenImageEdit, LoadImage, LoadImage, MarkdownNote, ImageScaleToTotalPixels, SaveImage, UNETLoader, LoraLoaderModelOnly, ControlNetLoader]
patterns: [image_to_image]
missing: [LayerUtility: ImageScaleByAspectRatio V2]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 1.8000000000000003, "denoise": 1, "height": 720, "sampler_name": "euler", "scheduler": "simple", "seed": 31019528826271, "steps": 4, "width": 1280}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image Edit 千问模型-CN图像编辑 @橘子_SJRJT_1963114897561333762.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1963114897561333762.json`

## 结构

**生成流程**：Model → Encode → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `VAEDecode` ★核心
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEdit`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AIO_Preprocessor`
- `OpenposePreprocessor`
- `PreviewImage`
- `SetUnionControlNetType`
- `ControlNetApplySD3` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImageEdit`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `ImageScaleToTotalPixels`
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ControlNetLoader`

**识别到的模式**：image_to_image

## 关键参数

- `width` = `1280`
- `height` = `720`
- `batch_size` = `1`
- `seed` = `31019528826271`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `1.8000000000000003`

## 知识

覆盖率 **78%**（21/27）

**有卡**：`VAEDecode`、`EmptyLatentImage`、`CFGNorm`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEdit`、`KSampler`、`VAEEncode`、`AIO_Preprocessor`、`OpenposePreprocessor`、`SetUnionControlNetType`、`ControlNetApplySD3`、`CLIPLoader`、`VAELoader`、`LoadImage`、`ImageScaleToTotalPixels`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`ControlNetLoader`

**缺卡**（1）：`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
