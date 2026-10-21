---
key: 图片生成/文生图/Z-Image+TTP seedvr2.5.15放大 极致写实文生图 直出8K_2026498649596891138.json
name: Z-Image+TTP seedvr2.5.15放大 极致写实文生图 直出8K_2026498649596891138
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image+TTP seedvr2.5.15放大 极致写实文生图 直出8K_2026498649596891138.json
hash: b38b17ed0da79623
coverage: 0.787879
learned_at: 2026-10-19 22:29:58
nodes: [ModelSamplingAuraFlow, CLIPTextEncode, CR Text Concatenate, UNETLoader, CLIPLoader, KSampler, VAELoader, SaveImage, CR SDXL Aspect Ratio, Text, ImageResize+, VAEDecode, ImageScaleBy, easy float, GetImageSize+, GetImageSize+, Note, easy showAnything, easy showAnything, ImageScaleBy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy showAnything, easy showAnything, ImageResize+, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, Note, Note, Lora Loader Stack (rgthree), Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "sgm_uniform", "seed": 631204852699820, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-Image+TTP seedvr2.5.15放大 极致写实文生图 直出8K_2026498649596891138.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image+TTP seedvr2.5.15放大 极致写实文生图 直出8K_2026498649596891138.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `CR Text Concatenate`
- `UNETLoader` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `VAELoader`
- `SaveImage`
- `CR SDXL Aspect Ratio`
- `Text`
- `ImageResize+`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `easy float`
- `GetImageSize+`
- `GetImageSize+`
- `Note`
- `easy showAnything`
- `easy showAnything`
- `ImageScaleBy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `easy showAnything`
- `easy showAnything`
- `ImageResize+`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `Note`
- `Note`
- `Lora Loader Stack (rgthree)`
- `Text`

## 关键参数

- `seed` = `631204852699820`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **79%**（26/33）

**有卡**：`ModelSamplingAuraFlow`、`CLIPTextEncode`、`CR Text Concatenate`、`UNETLoader`、`CLIPLoader`、`KSampler`、`VAELoader`、`SaveImage`、`CR SDXL Aspect Ratio`、`Text`、`ImageResize+`、`VAEDecode`、`ImageScaleBy`、`easy float`、`GetImageSize+`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`TTP_Image_Assy`、`Lora Loader Stack (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
