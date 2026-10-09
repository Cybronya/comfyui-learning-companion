---
key: 图片生成/文生图/Flex.2文生图+4倍高清放大_1923949193923055618.json
name: Flex.2文生图+4倍高清放大_1923949193923055618.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flex.2文生图+4倍高清放大_1923949193923055618.json
hash: 28224b0301642ddc
coverage: 0.9375
learned_at: 2026-10-07 22:22:44
nodes: [KSampler, VAELoader, ConditioningZeroOut, Flex2Conditioner, EmptyLatentImage, DualCLIPLoader, CFGZeroStarAndInit, FlexGuidance, UNETLoader, CLIPTextEncode, DeepTranslatorTextNode, ImageUpscaleWithModel, SaveImage, UpscaleModelLoader, VAEDecode, PreviewImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "deis", "scheduler": "beta", "seed": 726210541184116, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Flex.2文生图+4倍高清放大_1923949193923055618.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1923949193923055618.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `KSampler` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `Flex2Conditioner`
- `EmptyLatentImage` ★核心
- `DualCLIPLoader`
- `CFGZeroStarAndInit`
- `FlexGuidance`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `DeepTranslatorTextNode`
- `ImageUpscaleWithModel`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode` ★核心
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `726210541184116`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`KSampler`、`VAELoader`、`ConditioningZeroOut`、`Flex2Conditioner`、`EmptyLatentImage`、`DualCLIPLoader`、`CFGZeroStarAndInit`、`FlexGuidance`、`UNETLoader`、`CLIPTextEncode`、`DeepTranslatorTextNode`、`ImageUpscaleWithModel`、`SaveImage`、`UpscaleModelLoader`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、UNETLoader、CFGZeroStarAndInit
