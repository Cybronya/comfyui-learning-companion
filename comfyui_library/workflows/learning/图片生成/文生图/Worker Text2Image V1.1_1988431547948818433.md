---
key: 图片生成/文生图/Worker Text2Image V1.1_1988431547948818433.json
name: Worker Text2Image V1.1_1988431547948818433
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Worker Text2Image V1.1_1988431547948818433.json
hash: d97df9dd7a94470b
coverage: 0.681818
learned_at: 2026-10-10 20:59:15
nodes: [QwenEditResolution, PrimitiveInt, CR Text, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, LoraLoaderModelOnly, ModelSamplingAuraFlow, KSampler, SaveImage, VAEDecode, VAELoader, CLIPLoader, CLIPTextEncode, EmptyLatentImage, InversionDemoLazyIndexSwitch, InversionDemoLazyIndexSwitch, RH_LLMAPI_NODE, CLIPTextEncode, UNETLoader]
patterns: [text_to_image]
missing: [CR Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 16, "sampler_name": "res_2m", "scheduler": "sgm_uniform", "seed": 303793574512573, "steps": 8, "width": 16}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Worker Text2Image V1.1_1988431547948818433.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Worker Text2Image V1.1_1988431547948818433.json`

## 结构

**节点**（22 个）：
- `QwenEditResolution`
- `PrimitiveInt`
- `CR Text`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `InversionDemoLazyIndexSwitch`
- `InversionDemoLazyIndexSwitch`
- `RH_LLMAPI_NODE`
- `CLIPTextEncode`
- `UNETLoader`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `16`
- `sampler_name` = `res_2m`
- `scheduler` = `sgm_uniform`
- `seed` = `303793574512573`
- `steps` = `8`
- `width` = `16`

## 知识

覆盖率 **68%**（15/22）

**有卡**：`QwenEditResolution`、`PrimitiveInt`、`CR Text`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`KSampler`、`SaveImage`、`VAEDecode`、`VAELoader`、`CLIPLoader`

**缺卡**（1）：`CR Text`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
