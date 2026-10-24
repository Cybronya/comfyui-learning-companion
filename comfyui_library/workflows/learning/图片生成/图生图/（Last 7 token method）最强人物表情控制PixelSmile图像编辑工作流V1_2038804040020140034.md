---
key: 图片生成/图生图/（Last 7 token method）最强人物表情控制PixelSmile图像编辑工作流V1_2038804040020140034.json
name: （Last 7 token method）最强人物表情控制PixelSmile图像编辑工作流V1_2038804040020140034
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（Last 7 token method）最强人物表情控制PixelSmile图像编辑工作流V1_2038804040020140034.json
hash: b90a0bccbc3ba3c9
coverage: 0.851852
learned_at: 2026-10-23 13:37:14
nodes: [ModelSamplingAuraFlow, EmptySD3LatentImage, TextEncodeQwenImageEditPlus, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, VAEEncode, KSampler, ConditioningZeroOut, VAEDecode, TextEncodeQwenImageEditPlus, ImageConcanate, SaveImage, AddLabel, CR Prompt Text, ReplaceText, easy showAnything, LoadImage, PreviewImage, CR Prompt Text, SaveImage, PixelSmileConditioning, Note, Note, Float]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 1034276022462256, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/（Last 7 token method）最强人物表情控制PixelSmile图像编辑工作流V1_2038804040020140034.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（Last 7 token method）最强人物表情控制PixelSmile图像编辑工作流V1_2038804040020140034.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `ModelSamplingAuraFlow`
- `EmptySD3LatentImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlus`
- `ImageConcanate`
- `SaveImage`
- `AddLabel`
- `CR Prompt Text`
- `ReplaceText`
- `easy showAnything`
- `LoadImage`
- `PreviewImage`
- `CR Prompt Text`
- `SaveImage`
- `PixelSmileConditioning`
- `Note`
- `Note`
- `Float`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1034276022462256`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（23/27）

**有卡**：`ModelSamplingAuraFlow`、`EmptySD3LatentImage`、`TextEncodeQwenImageEditPlus`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`VAEEncode`、`KSampler`、`ConditioningZeroOut`、`VAEDecode`、`ImageConcanate`、`SaveImage`、`AddLabel`、`CR Prompt Text`、`ReplaceText`、`LoadImage`、`PixelSmileConditioning`、`Float`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
