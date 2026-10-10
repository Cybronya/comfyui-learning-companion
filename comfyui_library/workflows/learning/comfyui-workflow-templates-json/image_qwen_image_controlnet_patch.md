---
key: comfyui-workflow-templates-json/image_qwen_image_controlnet_patch.json
name: image_qwen_image_controlnet_patch
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_image_controlnet_patch.json
hash: 8fb8d9baac5ff34e
official: true
coverage: 0.8
learned_at: 2026-10-10 22:48:31
nodes: [ImageScaleToTotalPixels, QwenImageDiffsynthControlnet, ModelSamplingAuraFlow, MarkdownNote, VAEDecode, ModelPatchLoader, VAELoader, UNETLoader, VAEEncode, Note, CLIPLoader, PreviewImage, Canny, SaveImage, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, KSampler, MarkdownNote, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 91832422759220, "steps": 20}
---

# comfyui-workflow-templates-json/image_qwen_image_controlnet_patch.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_image_controlnet_patch.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `ImageScaleToTotalPixels`
- `QwenImageDiffsynthControlnet`
- `ModelSamplingAuraFlow`
- `MarkdownNote`
- `VAEDecode` ★核心
- `ModelPatchLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `Note`
- `CLIPLoader`
- `PreviewImage`
- `Canny`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `MarkdownNote`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `91832422759220`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（16/20）

**有卡**：`ImageScaleToTotalPixels`、`QwenImageDiffsynthControlnet`、`ModelSamplingAuraFlow`、`VAEDecode`、`ModelPatchLoader`、`VAELoader`、`UNETLoader`、`VAEEncode`、`CLIPLoader`、`Canny`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`KSampler`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
