---
key: 图片生成/文生图/Depth 深度 _  FLUX_CN 2.0_1900600906277363713.json
name: Depth 深度 _  FLUX_CN 2.0_1900600906277363713
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Depth 深度 _  FLUX_CN 2.0_1900600906277363713.json
hash: aeb596cb72875824
coverage: 0.925926
learned_at: 2026-10-15 22:26:15
nodes: [LayerUtility: ImageRemoveAlpha, LayerUtility: ColorPicker, PreviewImage, Joy_caption_two_load, CLIPTextEncodeFlux, CLIPTextEncode, KSampler, LoadImage, Joy_caption_two, LoadImage, VAELoader, easy cleanGpuUsed, Text Concatenate (JPS), TextInput_, SetShakkerLabsUnionControlNetType, ControlNetApplyAdvanced, PreviewImage, SaveImage, UNETLoader, DualCLIPLoader, LoraLoader, LoraLoader, DepthAnythingV2Preprocessor, LayerMask: SegmentAnythingUltra V2, EmptyLatentImage, VAEDecode, ControlNetLoader]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 2, "cfg": 1, "controlnet_strength": 0.7000000000000001, "denoise": 1, "height": 1536, "lora_name": "秋日森林_秋天女孩_V1.0.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 973408485736372, "steps": 20, "strength_clip": 1, "strength_model": 0.8, "width": 1024}
---

# 图片生成/文生图/Depth 深度 _  FLUX_CN 2.0_1900600906277363713.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Depth 深度 _  FLUX_CN 2.0_1900600906277363713.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ColorPicker`
- `PreviewImage`
- `Joy_caption_two_load`
- `CLIPTextEncodeFlux` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `LoadImage`
- `Joy_caption_two`
- `LoadImage`
- `VAELoader`
- `easy cleanGpuUsed`
- `Text Concatenate (JPS)`
- `TextInput_`
- `SetShakkerLabsUnionControlNetType`
- `ControlNetApplyAdvanced` ★核心
- `PreviewImage`
- `SaveImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `DepthAnythingV2Preprocessor`
- `LayerMask: SegmentAnythingUltra V2`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ControlNetLoader`

**识别到的模式**：text_to_image、lora

## 关键参数

- `seed` = `973408485736372`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.7000000000000001`
- `lora_name` = `秋日森林_秋天女孩_V1.0.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `2`

## 知识

覆盖率 **93%**（25/27）

**有卡**：`LayerUtility: ImageRemoveAlpha`、`LayerUtility: ColorPicker`、`Joy_caption_two_load`、`CLIPTextEncodeFlux`、`CLIPTextEncode`、`KSampler`、`LoadImage`、`Joy_caption_two`、`VAELoader`、`easy cleanGpuUsed`、`Text Concatenate (JPS)`、`TextInput_`、`SetShakkerLabsUnionControlNetType`、`ControlNetApplyAdvanced`、`SaveImage`、`UNETLoader`、`DualCLIPLoader`、`LoraLoader`、`DepthAnythingV2Preprocessor`、`LayerMask: SegmentAnythingUltra V2`、`EmptyLatentImage`、`VAEDecode`、`ControlNetLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced
