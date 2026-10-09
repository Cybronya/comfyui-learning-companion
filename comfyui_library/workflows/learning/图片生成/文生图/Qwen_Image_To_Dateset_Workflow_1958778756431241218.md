---
key: 图片生成/文生图/Qwen_Image_To_Dateset_Workflow_1958778756431241218.json
name: Qwen_Image_To_Dateset_Workflow_1958778756431241218.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen_Image_To_Dateset_Workflow_1958778756431241218.json
hash: 765fa05f001cfe48
coverage: 0.666667
learned_at: 2026-10-07 23:31:38
nodes: [SetNode, SetNode, GetNode, GetNode, GetNode, VAEEncode, VAEEncode, VAEDecode, KSampler, KSampler, CR Image Grid Panel, PreviewImage, LoadImage, ImageListToImageBatch, SaveImage, UNETLoader, VAELoader, CLIPLoader, UpscaleModelLoader, SetNode, SetNode, Lora Loader Stack (rgthree), ModelPassThrough, ImageScaleToTotalPixels, CR Prompt List, TextEncodeQwenImageEdit, GetNode, ModelSamplingAuraFlow, CLIPTextEncode, CFGNorm, VAEDecode, PreviewImage, CheckpointLoaderSimple, CLIPTextEncode, CLIPTextEncode, ImageScaleBy, ImageScaleToTotalPixels, UpscaleModelLoader, ImageUpscaleWithModel]
patterns: [image_to_image]
missing: [CR Image Grid Panel, CR Prompt List, Lora Loader Stack (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "epicrealismXL_vxviiCrystalclear.safetensors", "denoise": 1, "sampler_name": "res_2s", "scheduler": "simple", "seed": 5834920396131, "steps": 8}
discoveries: [次要节点 `CR Image Grid Panel` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt List` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `Lora Loader Stack (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen_Image_To_Dateset_Workflow_1958778756431241218.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1958778756431241218.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `CR Image Grid Panel`
- `PreviewImage`
- `LoadImage`
- `ImageListToImageBatch`
- `SaveImage`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `UpscaleModelLoader`
- `SetNode`
- `SetNode`
- `Lora Loader Stack (rgthree)`
- `ModelPassThrough`
- `ImageScaleToTotalPixels`
- `CR Prompt List`
- `TextEncodeQwenImageEdit`
- `GetNode`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `CFGNorm`
- `VAEDecode` ★核心
- `PreviewImage`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `5834920396131`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `epicrealismXL_vxviiCrystalclear.safetensors`

## 知识

覆盖率 **67%**（26/39）

**有卡**：`VAEEncode`、`VAEDecode`、`KSampler`、`LoadImage`、`ImageListToImageBatch`、`SaveImage`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`UpscaleModelLoader`、`ModelPassThrough`、`ImageScaleToTotalPixels`、`TextEncodeQwenImageEdit`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`CFGNorm`、`CheckpointLoaderSimple`、`ImageScaleBy`、`ImageUpscaleWithModel`

**缺卡**（3）：`CR Image Grid Panel`、`CR Prompt List`、`Lora Loader Stack (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Image Grid Panel` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt List` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `Lora Loader Stack (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
