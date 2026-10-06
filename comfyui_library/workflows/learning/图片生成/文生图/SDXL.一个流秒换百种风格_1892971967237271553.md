---
key: 图片生成/文生图/SDXL.一个流秒换百种风格_1892971967237271553.json
name: SDXL.一个流秒换百种风格_1892971967237271553
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SDXL.一个流秒换百种风格_1892971967237271553.json
hash: 65808abc87c96d08
coverage: 0.619048
learned_at: 2026-10-07 03:18:02
nodes: [Reroute, WD14Tagger|pysssss, CLIPTextEncode, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, OpenposePreprocessor, ControlNetApply, PreviewImage, PreviewImage, workflow/cn-depth, PreviewImage, LoadImage, VAEDecode, KSampler, VAEEncode, workflow/cn-canny, ImageScale, SaveImage, SDXLPromptStyler, Note]
patterns: [image_to_image, controlnet]
missing: [WD14Tagger|pysssss, workflow/cn-canny, workflow/cn-depth]
parameters: {"cfg": 6, "checkpoint": "dreamshaperXL_v21TurboDPMSDE.safetensors", "controlnet_strength": 0.8200000000000001, "denoise": 0.8, "sampler_name": "euler_ancestral", "scheduler": "normal", "seed": 570714527648738, "steps": 20}
discoveries: [次要节点 `WD14Tagger|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `workflow/cn-canny` 仅有 ControlNet 的通用知识，没有该节点自己的说明, 次要节点 `workflow/cn-depth` 仅有 ControlNet 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/SDXL.一个流秒换百种风格_1892971967237271553.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SDXL.一个流秒换百种风格_1892971967237271553.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `Reroute`
- `WD14Tagger|pysssss`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `ControlNetLoader`
- `OpenposePreprocessor`
- `ControlNetApply` ★核心
- `PreviewImage`
- `PreviewImage`
- `workflow/cn-depth`
- `PreviewImage`
- `LoadImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAEEncode` ★核心
- `workflow/cn-canny`
- `ImageScale`
- `SaveImage`
- `SDXLPromptStyler`
- `Note`

**识别到的模式**：image_to_image、controlnet

## 关键参数

- `checkpoint` = `dreamshaperXL_v21TurboDPMSDE.safetensors`
- `controlnet_strength` = `0.8200000000000001`
- `seed` = `570714527648738`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `normal`
- `denoise` = `0.8`

## 知识

覆盖率 **62%**（13/21）

**有卡**：`CLIPTextEncode`、`CheckpointLoaderSimple`、`ControlNetLoader`、`OpenposePreprocessor`、`ControlNetApply`、`LoadImage`、`VAEDecode`、`KSampler`、`VAEEncode`、`ImageScale`、`SaveImage`、`SDXLPromptStyler`

**缺卡**（3）：`WD14Tagger|pysssss`、`workflow/cn-canny`、`workflow/cn-depth`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetLoader、OpenposePreprocessor、ControlNetApply

## 学习发现

- 次要节点 `WD14Tagger|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `workflow/cn-canny` 仅有 ControlNet 的通用知识，没有该节点自己的说明
- 次要节点 `workflow/cn-depth` 仅有 ControlNet 的通用知识，没有该节点自己的说明
