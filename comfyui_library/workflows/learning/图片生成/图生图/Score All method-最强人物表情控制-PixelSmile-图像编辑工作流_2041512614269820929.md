---
key: 图片生成/图生图/Score All method-最强人物表情控制-PixelSmile-图像编辑工作流_2041512614269820929.json
name: Score All method-最强人物表情控制-PixelSmile-图像编辑工作流_2041512614269820929
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Score All method-最强人物表情控制-PixelSmile-图像编辑工作流_2041512614269820929.json
hash: b1d02e603a833bd8
coverage: 0.869565
learned_at: 2026-10-23 11:24:24
nodes: [ModelSamplingAuraFlow, LoraLoaderModelOnly, TextEncodeQwenImageEditPlus, KSampler, CustomAddLabel, LoraLoaderModelOnly, UNETLoader, PixelSmileConditioning, TextEncodeQwenImageEditPlus, ConditioningZeroOut, VAEDecode, ImageConcanate, SaveImage, SaveImage, CLIPLoader, VAELoader, RH_Translator, LoadImage, VAEEncode, easy showAnything, Note, Float, Note]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 1078177546550140, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Score All method-最强人物表情控制-PixelSmile-图像编辑工作流_2041512614269820929.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Score All method-最强人物表情控制-PixelSmile-图像编辑工作流_2041512614269820929.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `CustomAddLabel`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PixelSmileConditioning`
- `TextEncodeQwenImageEditPlus`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `ImageConcanate`
- `SaveImage`
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `RH_Translator`
- `LoadImage`
- `VAEEncode` ★核心
- `easy showAnything`
- `Note`
- `Float`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1078177546550140`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`TextEncodeQwenImageEditPlus`、`KSampler`、`CustomAddLabel`、`UNETLoader`、`PixelSmileConditioning`、`ConditioningZeroOut`、`VAEDecode`、`ImageConcanate`、`SaveImage`、`CLIPLoader`、`VAELoader`、`RH_Translator`、`LoadImage`、`VAEEncode`、`Float`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
