---
key: 图片生成/图生图/image_qwen_image_edit_2511_multiangle_camera 尺寸2K限_2019265588102701057.json
name: image_qwen_image_edit_2511_multiangle_camera 尺寸2K限_2019265588102701057
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/image_qwen_image_edit_2511_multiangle_camera 尺寸2K限_2019265588102701057.json
hash: 4eb88e09740b4b56
coverage: 0.947368
learned_at: 2026-10-23 11:37:57
nodes: [FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, VAEEncode, KSampler, VAEDecode, CFGNorm, VAELoader, ModelSamplingAuraFlow, UNETLoader, LoraLoaderModelOnly, CLIPLoader, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, LoadImage, 图像缩放范围孤海, PreviewImage, QwenMultiangleCameraNode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 902343813032432, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/image_qwen_image_edit_2511_multiangle_camera 尺寸2K限_2019265588102701057.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/image_qwen_image_edit_2511_multiangle_camera 尺寸2K限_2019265588102701057.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Output → Other

**节点**（19 个）：
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CFGNorm`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `图像缩放范围孤海`
- `PreviewImage`
- `QwenMultiangleCameraNode`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `902343813032432`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`FluxKontextMultiReferenceLatentMethod`、`VAEEncode`、`KSampler`、`VAEDecode`、`CFGNorm`、`VAELoader`、`ModelSamplingAuraFlow`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`SaveImage`、`TextEncodeQwenImageEditPlus`、`LoadImage`、`图像缩放范围孤海`、`QwenMultiangleCameraNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
