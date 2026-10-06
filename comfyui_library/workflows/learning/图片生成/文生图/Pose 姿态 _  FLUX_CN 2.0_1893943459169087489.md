---
key: 图片生成/文生图/Pose 姿态 _  FLUX_CN 2.0_1893943459169087489.json
name: Pose 姿态 _  FLUX_CN 2.0_1893943459169087489
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Pose 姿态 _  FLUX_CN 2.0_1893943459169087489.json
hash: de752ed6e893d2e5
coverage: 0.869565
learned_at: 2026-10-07 03:17:59
nodes: [Joy_caption_two_load, CLIPTextEncodeFlux, CLIPTextEncode, KSampler, Joy_caption_two, LoadImage, VAELoader, easy cleanGpuUsed, Text Concatenate (JPS), TextInput_, ControlNetApplyAdvanced, LoadImage, DWPreprocessor, PreviewImage, SetShakkerLabsUnionControlNetType, SaveImage, UNETLoader, DualCLIPLoader, LoraLoader, LoraLoader, EmptyLatentImage, VAEDecode, ControlNetLoader]
patterns: [text_to_image, lora]
missing: [Text Concatenate (JPS), easy cleanGpuUsed]
parameters: {"batch_size": 2, "cfg": 1, "controlnet_strength": 0.7000000000000001, "denoise": 1, "height": 1536, "lora_name": "秋日森林_秋天女孩_V1.0.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 1043416540105403, "steps": 20, "strength_clip": 1, "strength_model": 0.8, "width": 1024}
discoveries: [次要节点 `Text Concatenate (JPS)` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Pose 姿态 _  FLUX_CN 2.0_1893943459169087489.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Pose 姿态 _  FLUX_CN 2.0_1893943459169087489.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（23 个）：
- `Joy_caption_two_load`
- `CLIPTextEncodeFlux` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `Joy_caption_two`
- `LoadImage`
- `VAELoader`
- `easy cleanGpuUsed`
- `Text Concatenate (JPS)`
- `TextInput_`
- `ControlNetApplyAdvanced` ★核心
- `LoadImage`
- `DWPreprocessor`
- `PreviewImage`
- `SetShakkerLabsUnionControlNetType`
- `SaveImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ControlNetLoader`

**识别到的模式**：text_to_image、lora

## 关键参数

- `seed` = `1043416540105403`
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

覆盖率 **87%**（20/23）

**有卡**：`Joy_caption_two_load`、`CLIPTextEncodeFlux`、`CLIPTextEncode`、`KSampler`、`Joy_caption_two`、`LoadImage`、`VAELoader`、`TextInput_`、`ControlNetApplyAdvanced`、`DWPreprocessor`、`SetShakkerLabsUnionControlNetType`、`SaveImage`、`UNETLoader`、`DualCLIPLoader`、`LoraLoader`、`EmptyLatentImage`、`VAEDecode`、`ControlNetLoader`

**缺卡**（2）：`Text Concatenate (JPS)`、`easy cleanGpuUsed`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced

## 学习发现

- 次要节点 `Text Concatenate (JPS)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
