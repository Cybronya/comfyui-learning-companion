---
key: 图片生成/文生图/Z-image批量文生图+放大 提示词行 浮云1.14_2011020840770478081.json
name: Z-image批量文生图+放大 提示词行 浮云1.14_2011020840770478081
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image批量文生图+放大 提示词行 浮云1.14_2011020840770478081.json
hash: 1251a8c6bf2d2c13
coverage: 0.923077
learned_at: 2026-10-19 22:01:05
nodes: [CLIPLoader, ConditioningZeroOut, CLIPTextEncode, VAELoader, UNETLoader, CR Text Replace, JDCN_StringToList, CR Prompt Text, CR Prompt Text, CR Text, CR Text, RH_LLMAPI_Pro_Node, Text Concatenate, ProcessString, easy showAnything, EmptyLatentImage, CR Prompt Text, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, ImageScaleBy, VAEDecode, SaveImage, KSampler, SeedVR2VideoUpscaler, Image Comparer (rgthree), SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 734601660130182, "steps": 10, "width": 1080}
---

# 图片生成/文生图/Z-image批量文生图+放大 提示词行 浮云1.14_2011020840770478081.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image批量文生图+放大 提示词行 浮云1.14_2011020840770478081.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `CLIPLoader`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `CR Text Replace`
- `JDCN_StringToList`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Text`
- `CR Text`
- `RH_LLMAPI_Pro_Node`
- `Text Concatenate`
- `ProcessString`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `CR Prompt Text`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `ImageScaleBy`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `734601660130182`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`CLIPLoader`、`ConditioningZeroOut`、`CLIPTextEncode`、`VAELoader`、`UNETLoader`、`CR Text Replace`、`JDCN_StringToList`、`CR Prompt Text`、`CR Text`、`RH_LLMAPI_Pro_Node`、`Text Concatenate`、`ProcessString`、`EmptyLatentImage`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`ImageScaleBy`、`VAEDecode`、`SaveImage`、`KSampler`、`SeedVR2VideoUpscaler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader
