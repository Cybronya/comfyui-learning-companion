---
key: 图片生成/文生图/Worker Text2Image V1.1_1988431547948818433.json
name: Worker Text2Image V1.1_1988431547948818433.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Worker Text2Image V1.1_1988431547948818433.json
hash: d97df9dd7a94470b
coverage: 0.681818
learned_at: 2026-10-09 21:16:01
nodes: [QwenEditResolution, PrimitiveInt, CR Text, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, LoraLoaderModelOnly, ModelSamplingAuraFlow, KSampler, SaveImage, VAEDecode, VAELoader, CLIPLoader, CLIPTextEncode, EmptyLatentImage, InversionDemoLazyIndexSwitch, InversionDemoLazyIndexSwitch, RH_LLMAPI_NODE, CLIPTextEncode, UNETLoader]
patterns: [text_to_image]
missing: [CR Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 16, "sampler_name": "res_2m", "scheduler": "sgm_uniform", "seed": 303793574512573, "steps": 8, "width": 16}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Worker Text2Image V1.1_1988431547948818433.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1988431547948818433.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（22 个）：
- `QwenEditResolution`
- `PrimitiveInt`
- `CR Text`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `InversionDemoLazyIndexSwitch`
- `InversionDemoLazyIndexSwitch`
- `RH_LLMAPI_NODE`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `303793574512573`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `width` = `16`
- `height` = `16`
- `batch_size` = `1`

## 知识

覆盖率 **68%**（15/22）

**有卡**：`QwenEditResolution`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`KSampler`、`SaveImage`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`EmptyLatentImage`、`InversionDemoLazyIndexSwitch`、`RH_LLMAPI_NODE`、`UNETLoader`

**缺卡**（1）：`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
