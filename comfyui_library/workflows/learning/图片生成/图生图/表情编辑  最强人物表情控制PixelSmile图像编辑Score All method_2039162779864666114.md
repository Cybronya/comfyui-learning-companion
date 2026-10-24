---
key: 图片生成/图生图/表情编辑  最强人物表情控制PixelSmile图像编辑Score All method_2039162779864666114.json
name: 表情编辑  最强人物表情控制PixelSmile图像编辑Score All method_2039162779864666114
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/表情编辑  最强人物表情控制PixelSmile图像编辑Score All method_2039162779864666114.json
hash: d357cab3a943a4f7
coverage: 0.807692
learned_at: 2026-10-23 13:25:29
nodes: [ModelSamplingAuraFlow, EmptySD3LatentImage, TextEncodeQwenImageEditPlus, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, VAEEncode, KSampler, ConditioningZeroOut, VAEDecode, TextEncodeQwenImageEditPlus, PixelSmileConditioning, Note, Note, Note, PreviewImage, ImageConcanate, AddLabel, CR Prompt Text, Float, LoadImage, easy showAnything, SaveImage, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 271207970982933, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/表情编辑  最强人物表情控制PixelSmile图像编辑Score All method_2039162779864666114.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/表情编辑  最强人物表情控制PixelSmile图像编辑Score All method_2039162779864666114.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
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
- `PixelSmileConditioning`
- `Note`
- `Note`
- `Note`
- `PreviewImage`
- `ImageConcanate`
- `AddLabel`
- `CR Prompt Text`
- `Float`
- `LoadImage`
- `easy showAnything`
- `SaveImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `271207970982933`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（21/26）

**有卡**：`ModelSamplingAuraFlow`、`EmptySD3LatentImage`、`TextEncodeQwenImageEditPlus`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`VAEEncode`、`KSampler`、`ConditioningZeroOut`、`VAEDecode`、`PixelSmileConditioning`、`ImageConcanate`、`AddLabel`、`CR Prompt Text`、`Float`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
