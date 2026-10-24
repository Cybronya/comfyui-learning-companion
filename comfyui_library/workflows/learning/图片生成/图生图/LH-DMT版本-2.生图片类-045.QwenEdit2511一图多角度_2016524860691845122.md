---
key: 图片生成/图生图/LH-DMT版本-2.生图片类-045.QwenEdit2511一图多角度_2016524860691845122.json
name: LH-DMT版本-2.生图片类-045.QwenEdit2511一图多角度_2016524860691845122
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/LH-DMT版本-2.生图片类-045.QwenEdit2511一图多角度_2016524860691845122.json
hash: eaa8c95306b9e368
coverage: 0.875
learned_at: 2026-10-23 11:08:41
nodes: [UnetLoaderGGUF, LoraLoaderModelOnly, Anything Everywhere, LayerUtility: ImageScaleByAspectRatio V2, easy promptLine, KSampler, ConditioningZeroOut, VAEDecode, TextEncodeQwenImageEditPlus, VAEEncode, Note, SaveImage, LoadImage, LoraLoaderModelOnly, CLIPLoader, VAELoader]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 57952829456872, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/LH-DMT版本-2.生图片类-045.QwenEdit2511一图多角度_2016524860691845122.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/LH-DMT版本-2.生图片类-045.QwenEdit2511一图多角度_2016524860691845122.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `Anything Everywhere`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy promptLine`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `Note`
- `SaveImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `57952829456872`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`UnetLoaderGGUF`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy promptLine`、`KSampler`、`ConditioningZeroOut`、`VAEDecode`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`SaveImage`、`LoadImage`、`CLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、TextEncodeQwenImageEditPlus

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
