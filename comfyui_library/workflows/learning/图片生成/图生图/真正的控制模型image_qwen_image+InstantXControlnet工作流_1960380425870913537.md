---
key: 图片生成/图生图/真正的控制模型image_qwen_image+InstantXControlnet工作流_1960380425870913537.json
name: 真正的控制模型image_qwen_image+InstantXControlnet工作流_1960380425870913537
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/真正的控制模型image_qwen_image+InstantXControlnet工作流_1960380425870913537.json
hash: 63c85c08a0ed6e48
coverage: 0.73913
learned_at: 2026-10-23 13:19:32
nodes: [CLIPTextEncode, ModelSamplingAuraFlow, MarkdownNote, Note, MarkdownNote, KSampler, MarkdownNote, Note, EmptySD3LatentImage, VAEDecode, LoadImage, ControlNetApplySD3, CLIPTextEncode, PreviewImage, CLIPLoader, VAELoader, LoraLoaderModelOnly, ControlNetLoader, UNETLoader, ImageConcanate, AIO_Preprocessor, SetUnionControlNetType, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "controlnet_strength": 0.75, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 389744131602480, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/真正的控制模型image_qwen_image+InstantXControlnet工作流_1960380425870913537.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/真正的控制模型image_qwen_image+InstantXControlnet工作流_1960380425870913537.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `MarkdownNote`
- `Note`
- `MarkdownNote`
- `KSampler` ★核心
- `MarkdownNote`
- `Note`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `LoadImage`
- `ControlNetApplySD3` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ControlNetLoader`
- `UNETLoader` ★核心
- `ImageConcanate`
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `SaveImage`

## 关键参数

- `seed` = `389744131602480`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.75`

## 知识

覆盖率 **74%**（17/23）

**有卡**：`CLIPTextEncode`、`ModelSamplingAuraFlow`、`KSampler`、`EmptySD3LatentImage`、`VAEDecode`、`LoadImage`、`ControlNetApplySD3`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`ControlNetLoader`、`UNETLoader`、`ImageConcanate`、`AIO_Preprocessor`、`SetUnionControlNetType`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
