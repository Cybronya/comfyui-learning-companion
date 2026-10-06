---
key: 图片生成/文生图/Canny _  FLUX_CN 2.0_1900592230405390338.json
name: Canny _  FLUX_CN 2.0_1900592230405390338
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Canny _  FLUX_CN 2.0_1900592230405390338.json
hash: 6f52835fc207d5a0
coverage: 0.740741
learned_at: 2026-10-07 03:17:51
nodes: [LayerUtility: ImageRemoveAlpha, LayerUtility: ColorPicker, PreviewImage, SetShakkerLabsUnionControlNetType, Joy_caption_two_load, CLIPTextEncodeFlux, CLIPTextEncode, ControlNetApplyAdvanced, Canny, PreviewImage, KSampler, LoadImage, Joy_caption_two, LoadImage, VAELoader, easy cleanGpuUsed, Text Concatenate (JPS), TextInput_, UNETLoader, LoraLoader, LoraLoader, LayerMask: SegmentAnythingUltra V2, DualCLIPLoader, VAEDecode, EmptyLatentImage, SaveImage, ControlNetLoader]
patterns: [text_to_image, lora]
missing: [LayerMask: SegmentAnythingUltra V2, LayerUtility: ColorPicker, LayerUtility: ImageRemoveAlpha, Text Concatenate (JPS), easy cleanGpuUsed]
parameters: {"batch_size": 2, "cfg": 1, "controlnet_strength": 0.7000000000000001, "denoise": 1, "height": 1536, "lora_name": "秋日森林_秋天女孩_V1.0.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 216378008676655, "steps": 20, "strength_clip": 1, "strength_model": 0.8, "width": 1024}
discoveries: [次要节点 `LayerMask: SegmentAnythingUltra V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ColorPicker` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageRemoveAlpha` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate (JPS)` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
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

覆盖率 **74%**（20/27）

**有卡**：`SetShakkerLabsUnionControlNetType`、`Joy_caption_two_load`、`CLIPTextEncodeFlux`、`CLIPTextEncode`、`ControlNetApplyAdvanced`、`Canny`、`KSampler`、`LoadImage`、`Joy_caption_two`、`VAELoader`、`TextInput_`、`UNETLoader`、`LoraLoader`、`DualCLIPLoader`、`VAEDecode`、`EmptyLatentImage`、`SaveImage`、`ControlNetLoader`

**缺卡**（5）：`LayerMask: SegmentAnythingUltra V2`、`LayerUtility: ColorPicker`、`LayerUtility: ImageRemoveAlpha`、`Text Concatenate (JPS)`、`easy cleanGpuUsed`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced

## 学习发现

- 次要节点 `LayerMask: SegmentAnythingUltra V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ColorPicker` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageRemoveAlpha` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate (JPS)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
