---
key: comfyui-workflow-templates-json/sd3.5_large_depth.json
name: sd3.5_large_depth
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/sd3.5_large_depth.json
hash: 66e7f349efad7392
official: true
coverage: 0.705882
learned_at: 2026-10-07 21:36:16
nodes: [ControlNetLoader, ImageScaleToTotalPixels, ConditioningZeroOut, CheckpointLoaderSimple, LoadImage, CLIPTextEncode, 6b0ed7ac-f476-44c9-9dad-b3f23ef985f8, KSampler, VAEDecode, VAEEncode, ControlNetApplyAdvanced, EmptySD3LatentImage, SaveImage, MarkdownNote, PreviewImage, MarkdownNote, MarkdownNote]
patterns: [image_to_image]
missing: [6b0ed7ac-f476-44c9-9dad-b3f23ef985f8]
parameters: {"cfg": 8, "checkpoint": "sd3.5_large_fp8_scaled.safetensors", "controlnet_strength": 0.7000000000000002, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 1020711502084247, "steps": 20}
discoveries: [次要节点 `6b0ed7ac-f476-44c9-9dad-b3f23ef985f8` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/sd3.5_large_depth.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/sd3.5_large_depth.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `ControlNetLoader`
- `ImageScaleToTotalPixels`
- `ConditioningZeroOut`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `6b0ed7ac-f476-44c9-9dad-b3f23ef985f8`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `EmptySD3LatentImage`
- `SaveImage`
- `MarkdownNote`
- `PreviewImage`
- `MarkdownNote`
- `MarkdownNote`

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `sd3.5_large_fp8_scaled.safetensors`
- `seed` = `1020711502084247`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `controlnet_strength` = `0.7000000000000002`

## 知识

覆盖率 **71%**（12/17）

**有卡**：`ControlNetLoader`、`ImageScaleToTotalPixels`、`ConditioningZeroOut`、`CheckpointLoaderSimple`、`LoadImage`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`VAEEncode`、`ControlNetApplyAdvanced`、`EmptySD3LatentImage`、`SaveImage`

**缺卡**（1）：`6b0ed7ac-f476-44c9-9dad-b3f23ef985f8`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetApplyAdvanced、ControlNetLoader

## 学习发现

- 次要节点 `6b0ed7ac-f476-44c9-9dad-b3f23ef985f8` 知识库中没有该节点类型的任何知识
