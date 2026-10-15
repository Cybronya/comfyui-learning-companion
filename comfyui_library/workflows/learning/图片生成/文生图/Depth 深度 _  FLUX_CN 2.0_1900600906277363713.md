---
key: 图片生成/文生图/Depth 深度 _  FLUX_CN 2.0_1900600906277363713.json
name: Depth 深度 _  FLUX_CN 2.0_1900600906277363713
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Depth 深度 _  FLUX_CN 2.0_1900600906277363713.json
hash: aeb596cb72875824
coverage: 0.740741
learned_at: 2026-10-10 21:27:14
nodes: [LayerUtility: ImageRemoveAlpha, LayerUtility: ColorPicker, PreviewImage, Joy_caption_two_load, CLIPTextEncodeFlux, CLIPTextEncode, KSampler, LoadImage, Joy_caption_two, LoadImage, VAELoader, easy cleanGpuUsed, Text Concatenate (JPS), TextInput_, SetShakkerLabsUnionControlNetType, ControlNetApplyAdvanced, PreviewImage, SaveImage, UNETLoader, DualCLIPLoader, LoraLoader, LoraLoader, DepthAnythingV2Preprocessor, LayerMask: SegmentAnythingUltra V2, EmptyLatentImage, VAEDecode, ControlNetLoader]
patterns: [text_to_image, lora]
missing: [LayerMask: SegmentAnythingUltra V2, LayerUtility: ColorPicker, LayerUtility: ImageRemoveAlpha, Text Concatenate (JPS), easy cleanGpuUsed]
parameters: {"batch_size": 2, "cfg": 1, "controlnet_strength": 0.7000000000000001, "denoise": 1, "height": 1536, "lora_name": "秋日森林_秋天女孩_V1.0.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 973408485736372, "steps": 20, "strength_clip": 1, "strength_model": 0.8, "width": 1024}
discoveries: [次要节点 `LayerMask: SegmentAnythingUltra V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ColorPicker` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageRemoveAlpha` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate (JPS)` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Depth 深度 _  FLUX_CN 2.0_1900600906277363713.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Depth 深度 _  FLUX_CN 2.0_1900600906277363713.json`

## 结构

**节点**（27 个）：
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ColorPicker`
- `PreviewImage`
- `Joy_caption_two_load`
- `CLIPTextEncodeFlux`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `Joy_caption_two`
- `LoadImage`
- `VAELoader`
- `easy cleanGpuUsed`
- `Text Concatenate (JPS)`
- `TextInput_`
- `SetShakkerLabsUnionControlNetType`
- `ControlNetApplyAdvanced`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `DualCLIPLoader`
- `LoraLoader`
- `LoraLoader`
- `DepthAnythingV2Preprocessor`
- `LayerMask: SegmentAnythingUltra V2`
- `EmptyLatentImage`
- `VAEDecode`
- `ControlNetLoader`

**识别到的模式**：text_to_image、lora

## 关键参数

- `batch_size` = `2`
- `cfg` = `1`
- `controlnet_strength` = `0.7000000000000001`
- `denoise` = `1`
- `height` = `1536`
- `lora_name` = `秋日森林_秋天女孩_V1.0.safetensors`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `973408485736372`
- `steps` = `20`
- `strength_clip` = `1`
- `strength_model` = `0.8`
- `width` = `1024`

## 知识

覆盖率 **74%**（20/27）

**有卡**：`LayerUtility: ImageRemoveAlpha`、`LayerUtility: ColorPicker`、`PreviewImage`、`Joy_caption_two_load`、`CLIPTextEncodeFlux`、`CLIPTextEncode`、`KSampler`、`LoadImage`、`Joy_caption_two`、`VAELoader`、`easy cleanGpuUsed`、`Text Concatenate (JPS)`、`TextInput_`、`SetShakkerLabsUnionControlNetType`、`ControlNetApplyAdvanced`、`SaveImage`、`UNETLoader`、`DualCLIPLoader`

**缺卡**（5）：`LayerMask: SegmentAnythingUltra V2`、`LayerUtility: ColorPicker`、`LayerUtility: ImageRemoveAlpha`、`Text Concatenate (JPS)`、`easy cleanGpuUsed`

## 学习发现

- 次要节点 `LayerMask: SegmentAnythingUltra V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ColorPicker` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageRemoveAlpha` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate (JPS)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
