---
key: 平台全量/人物换装换脸 服饰提取 人物精准换装 加速版  SeedVR2.5 + TTP 分块高清放大_2013510838342131714.json
name: 人物换装换脸 服饰提取 人物精准换装 加速版  SeedVR2.5 + TTP 分块高清放大_2013510838342131714
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/人物换装换脸 服饰提取 人物精准换装 加速版  SeedVR2.5 + TTP 分块高清放大_2013510838342131714.json
hash: 734ae70fc2f51fa8
coverage: 0.875
learned_at: 2026-11-14 01:37:31
nodes: [CLIPLoader, VAELoader, VAEEncode, TextEncodeQwenImageEditPlus, ModelSamplingAuraFlow, CFGNorm, UNETLoader, KSampler, LoraLoaderModelOnly, MarkdownNote, ConditioningZeroOut, ImageScaleToTotalPixels, VAEDecode, easy imageConcat, easy imageConcat, PrimitiveStringMultiline, PrimitiveStringMultiline, ImageScaleToTotalPixels, CR Simple Image Compare, SaveImage, SaveImage, LoadImage, LoadImage, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 403168258312600, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/人物换装换脸 服饰提取 人物精准换装 加速版  SeedVR2.5 + TTP 分块高清放大_2013510838342131714.json

> 来源文件 `comfyui_library/workflows/平台全量/人物换装换脸 服饰提取 人物精准换装 加速版  SeedVR2.5 + TTP 分块高清放大_2013510838342131714.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `ConditioningZeroOut`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `easy imageConcat`
- `easy imageConcat`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ImageScaleToTotalPixels`
- `CR Simple Image Compare`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `403168258312600`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEEncode`、`TextEncodeQwenImageEditPlus`、`ModelSamplingAuraFlow`、`CFGNorm`、`UNETLoader`、`KSampler`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`ImageScaleToTotalPixels`、`VAEDecode`、`easy imageConcat`、`CR Simple Image Compare`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
