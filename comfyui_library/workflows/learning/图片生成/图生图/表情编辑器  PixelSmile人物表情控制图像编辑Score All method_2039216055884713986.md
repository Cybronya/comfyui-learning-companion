---
key: 图片生成/图生图/表情编辑器  PixelSmile人物表情控制图像编辑Score All method_2039216055884713986.json
name: 表情编辑器  PixelSmile人物表情控制图像编辑Score All method_2039216055884713986
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/表情编辑器  PixelSmile人物表情控制图像编辑Score All method_2039216055884713986.json
hash: c2e1e6d42ea2d2b2
coverage: 0.807692
learned_at: 2026-10-23 13:25:29
nodes: [ModelSamplingAuraFlow, EmptySD3LatentImage, TextEncodeQwenImageEditPlus, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, VAEEncode, KSampler, ConditioningZeroOut, VAEDecode, TextEncodeQwenImageEditPlus, PixelSmileConditioning, PreviewImage, ImageConcanate, AddLabel, Float, easy showAnything, SaveImage, SaveImage, LoadImage, Note, Note, Note, CR Prompt Text]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 874225575295141, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/表情编辑器  PixelSmile人物表情控制图像编辑Score All method_2039216055884713986.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/表情编辑器  PixelSmile人物表情控制图像编辑Score All method_2039216055884713986.json`

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
- `PreviewImage`
- `ImageConcanate`
- `AddLabel`
- `Float`
- `easy showAnything`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `Note`
- `Note`
- `Note`
- `CR Prompt Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `874225575295141`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（21/26）

**有卡**：`ModelSamplingAuraFlow`、`EmptySD3LatentImage`、`TextEncodeQwenImageEditPlus`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`VAEEncode`、`KSampler`、`ConditioningZeroOut`、`VAEDecode`、`PixelSmileConditioning`、`ImageConcanate`、`AddLabel`、`Float`、`SaveImage`、`LoadImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
