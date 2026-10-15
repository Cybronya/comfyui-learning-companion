---
key: 图片生成/文生图/Canny _  FLUX_CN 2.0_1900592230405390338.json
name: Canny _  FLUX_CN 2.0_1900592230405390338
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Canny _  FLUX_CN 2.0_1900592230405390338.json
hash: 6f52835fc207d5a0
coverage: 0.925926
learned_at: 2026-10-15 22:26:13
nodes: [LayerUtility: ImageRemoveAlpha, LayerUtility: ColorPicker, PreviewImage, SetShakkerLabsUnionControlNetType, Joy_caption_two_load, CLIPTextEncodeFlux, CLIPTextEncode, ControlNetApplyAdvanced, Canny, PreviewImage, KSampler, LoadImage, Joy_caption_two, LoadImage, VAELoader, easy cleanGpuUsed, Text Concatenate (JPS), TextInput_, UNETLoader, LoraLoader, LoraLoader, LayerMask: SegmentAnythingUltra V2, DualCLIPLoader, VAEDecode, EmptyLatentImage, SaveImage, ControlNetLoader]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 2, "cfg": 1, "controlnet_strength": 0.7000000000000001, "denoise": 1, "height": 1536, "lora_name": "秋日森林_秋天女孩_V1.0.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 216378008676655, "steps": 20, "strength_clip": 1, "strength_model": 0.8, "width": 1024}
---

# 图片生成/文生图/Canny _  FLUX_CN 2.0_1900592230405390338.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Canny _  FLUX_CN 2.0_1900592230405390338.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ColorPicker`
- `PreviewImage`
- `SetShakkerLabsUnionControlNetType`
- `Joy_caption_two_load`
- `CLIPTextEncodeFlux` ★核心
- `CLIPTextEncode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `Canny`
- `PreviewImage`
- `KSampler` ★核心
- `LoadImage`
- `Joy_caption_two`
- `LoadImage`
- `VAELoader`
- `easy cleanGpuUsed`
- `Text Concatenate (JPS)`
- `TextInput_`
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LayerMask: SegmentAnythingUltra V2`
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `ControlNetLoader`

**识别到的模式**：text_to_image、lora

## 关键参数

- `controlnet_strength` = `0.7000000000000001`
- `seed` = `216378008676655`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `秋日森林_秋天女孩_V1.0.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `2`

## 知识

覆盖率 **93%**（25/27）

**有卡**：`LayerUtility: ImageRemoveAlpha`、`LayerUtility: ColorPicker`、`SetShakkerLabsUnionControlNetType`、`Joy_caption_two_load`、`CLIPTextEncodeFlux`、`CLIPTextEncode`、`ControlNetApplyAdvanced`、`Canny`、`KSampler`、`LoadImage`、`Joy_caption_two`、`VAELoader`、`easy cleanGpuUsed`、`Text Concatenate (JPS)`、`TextInput_`、`UNETLoader`、`LoraLoader`、`LayerMask: SegmentAnythingUltra V2`、`DualCLIPLoader`、`VAEDecode`、`EmptyLatentImage`、`SaveImage`、`ControlNetLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced
