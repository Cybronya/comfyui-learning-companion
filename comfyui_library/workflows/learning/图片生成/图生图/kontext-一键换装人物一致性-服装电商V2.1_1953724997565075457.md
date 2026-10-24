---
key: 图片生成/图生图/kontext-一键换装人物一致性-服装电商V2.1_1953724997565075457.json
name: kontext-一键换装人物一致性-服装电商V2.1_1953724997565075457
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/kontext-一键换装人物一致性-服装电商V2.1_1953724997565075457.json
hash: 5b18549a874f3fc3
coverage: 0.882353
learned_at: 2026-10-23 11:39:06
nodes: [LoadImage, PulidFluxEvaClipLoader, ConditioningZeroOut, VAEEncode, ReferenceLatent, ShowText|pysssss, PulidFluxInsightFaceLoader, SaveImage, SaveImage, ImageStitch, VAEDecode, FluxGuidance, KSampler, CLIPTextEncode, ApplyPulidFlux, DualCLIPLoader, ImageResizeKJ, Text Concatenate (JPS), StringFunction|pysssss, Florence2Run, CR Text, LoadImage, Joy_caption_two, Joy_caption_two_load, LoadImage, UNETLoader, VAELoader, PulidFluxModelLoader, PreviewImage, Florence2ModelLoader, Note, Note, CR Text, CR Text]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 762088581033057, "steps": 25}
---

# 图片生成/图生图/kontext-一键换装人物一致性-服装电商V2.1_1953724997565075457.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/kontext-一键换装人物一致性-服装电商V2.1_1953724997565075457.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `LoadImage`
- `PulidFluxEvaClipLoader`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ShowText|pysssss`
- `PulidFluxInsightFaceLoader`
- `SaveImage`
- `SaveImage`
- `ImageStitch`
- `VAEDecode` ★核心
- `FluxGuidance`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ApplyPulidFlux`
- `DualCLIPLoader`
- `ImageResizeKJ`
- `Text Concatenate (JPS)`
- `StringFunction|pysssss`
- `Florence2Run`
- `CR Text`
- `LoadImage`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `LoadImage`
- `UNETLoader` ★核心
- `VAELoader`
- `PulidFluxModelLoader`
- `PreviewImage`
- `Florence2ModelLoader`
- `Note`
- `Note`
- `CR Text`
- `CR Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `762088581033057`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（30/34）

**有卡**：`LoadImage`、`PulidFluxEvaClipLoader`、`ConditioningZeroOut`、`VAEEncode`、`ReferenceLatent`、`PulidFluxInsightFaceLoader`、`SaveImage`、`ImageStitch`、`VAEDecode`、`FluxGuidance`、`KSampler`、`CLIPTextEncode`、`ApplyPulidFlux`、`DualCLIPLoader`、`ImageResizeKJ`、`Text Concatenate (JPS)`、`StringFunction|pysssss`、`Florence2Run`、`CR Text`、`Joy_caption_two`、`Joy_caption_two_load`、`UNETLoader`、`VAELoader`、`PulidFluxModelLoader`、`Florence2ModelLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
