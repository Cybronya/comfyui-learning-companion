---
key: 图片生成/文生图/Flex.2文生图+4倍高清放大_1923949193923055618.json
name: Flex.2文生图+4倍高清放大_1923949193923055618
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flex.2文生图+4倍高清放大_1923949193923055618.json
hash: 28224b0301642ddc
coverage: 0.9375
learned_at: 2026-10-10 20:58:33
nodes: [KSampler, VAELoader, ConditioningZeroOut, Flex2Conditioner, EmptyLatentImage, DualCLIPLoader, CFGZeroStarAndInit, FlexGuidance, UNETLoader, CLIPTextEncode, DeepTranslatorTextNode, ImageUpscaleWithModel, SaveImage, UpscaleModelLoader, VAEDecode, PreviewImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "deis", "scheduler": "beta", "seed": 726210541184116, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Flex.2文生图+4倍高清放大_1923949193923055618.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flex.2文生图+4倍高清放大_1923949193923055618.json`

## 结构

**节点**（16 个）：
- `KSampler`
- `VAELoader`
- `ConditioningZeroOut`
- `Flex2Conditioner`
- `EmptyLatentImage`
- `DualCLIPLoader`
- `CFGZeroStarAndInit`
- `FlexGuidance`
- `UNETLoader`
- `CLIPTextEncode`
- `DeepTranslatorTextNode`
- `ImageUpscaleWithModel`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1536`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `seed` = `726210541184116`
- `steps` = `25`
- `width` = `1024`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`KSampler`、`VAELoader`、`ConditioningZeroOut`、`Flex2Conditioner`、`EmptyLatentImage`、`DualCLIPLoader`、`CFGZeroStarAndInit`、`FlexGuidance`、`UNETLoader`、`CLIPTextEncode`、`DeepTranslatorTextNode`、`ImageUpscaleWithModel`、`SaveImage`、`UpscaleModelLoader`、`VAEDecode`
