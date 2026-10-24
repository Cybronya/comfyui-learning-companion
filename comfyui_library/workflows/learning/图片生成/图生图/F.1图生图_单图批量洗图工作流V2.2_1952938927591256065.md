---
key: 图片生成/图生图/F.1图生图_单图批量洗图工作流V2.2_1952938927591256065.json
name: F.1图生图_单图批量洗图工作流V2.2_1952938927591256065
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.1图生图_单图批量洗图工作流V2.2_1952938927591256065.json
hash: e2c52f20eb35c38c
coverage: 0.78125
learned_at: 2026-10-23 10:52:38
nodes: [ConditioningZeroOut, InstructPixToPixConditioning, easy imageIndexSwitch, VAEEncode, AIO_Preprocessor, Florence2Run, ShowText|pysssss, VAEDecode, ImpactInt, Note, LoadImage, ImageResizeKJ, SaveImage, Image Comparer (rgthree), Load Image Batch, PrimitiveFloat, PrimitiveFloat, Note, CLIPVisionLoader, CLIPVisionEncode, StyleModelApply, LoraLoader, StyleModelLoader, FluxGuidance, LoraLoader, VAELoader, CLIPTextEncode, Florence2ModelLoader, DualCLIPLoader, UNETLoader, KSampler, PreviewImage]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "denoise": 1, "lora_name": "F.1光影斑驳_光影质感增强_遥远的炼丹师V1.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 1067620805498580, "steps": 25, "strength_clip": 1, "strength_model": 0.8}
---

# 图片生成/图生图/F.1图生图_单图批量洗图工作流V2.2_1952938927591256065.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.1图生图_单图批量洗图工作流V2.2_1952938927591256065.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `ConditioningZeroOut`
- `InstructPixToPixConditioning`
- `easy imageIndexSwitch`
- `VAEEncode` ★核心
- `AIO_Preprocessor`
- `Florence2Run`
- `ShowText|pysssss`
- `VAEDecode` ★核心
- `ImpactInt`
- `Note`
- `LoadImage`
- `ImageResizeKJ`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Load Image Batch`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `Note`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `StyleModelApply`
- `LoraLoader` ★核心
- `StyleModelLoader`
- `FluxGuidance`
- `LoraLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `Florence2ModelLoader`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `PreviewImage`

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `F.1光影斑驳_光影质感增强_遥远的炼丹师V1.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `1`
- `seed` = `1067620805498580`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（25/32）

**有卡**：`ConditioningZeroOut`、`InstructPixToPixConditioning`、`easy imageIndexSwitch`、`VAEEncode`、`AIO_Preprocessor`、`Florence2Run`、`VAEDecode`、`ImpactInt`、`LoadImage`、`ImageResizeKJ`、`SaveImage`、`Load Image Batch`、`CLIPVisionLoader`、`CLIPVisionEncode`、`StyleModelApply`、`LoraLoader`、`StyleModelLoader`、`FluxGuidance`、`VAELoader`、`CLIPTextEncode`、`Florence2ModelLoader`、`DualCLIPLoader`、`UNETLoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
