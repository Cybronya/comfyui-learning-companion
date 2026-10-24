---
key: 图片生成/图生图/姿势迁移 Posture Transfer qwen_image_edit_2109441347613716481.json
name: 姿势迁移 Posture Transfer qwen_image_edit_2109441347613716481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/姿势迁移 Posture Transfer qwen_image_edit_2109441347613716481.json
hash: eff8a6b76fde489e
coverage: 0.882353
learned_at: 2026-10-23 12:47:08
nodes: [ModelSamplingAuraFlow, UNETLoader, CFGNorm, VAEDecode, VAELoader, LoraLoaderModelOnly, VAEDecode, VAEDecode, KSampler, KSampler, KSampler, CLIPLoader, ConditioningZeroOut, LayerMask: BiRefNetUltraV2, DWPreprocessor, LayerMask: LoadBiRefNetModelV2, PreviewImage, TextEncodeQwenImageEditPlusPro_lrzjason, Text Concatenate (JPS), CR Text Replace, CR String To Number, ZML_AnyTypeSwitchFive, JjkText, JjkText, easy showAnything, CR Text Replace, SaveImage, 忽略多组孤海, EmptyLatentImage, SaveImage, LoraLoaderModelOnly, SaveImage, LoadImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1480, "sampler_name": "euler", "scheduler": "simple", "seed": 425746756014929, "steps": 4, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/姿势迁移 Posture Transfer qwen_image_edit_2109441347613716481.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/姿势迁移 Posture Transfer qwen_image_edit_2109441347613716481.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（34 个）：
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `CFGNorm`
- `VAEDecode` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `ConditioningZeroOut`
- `LayerMask: BiRefNetUltraV2`
- `DWPreprocessor`
- `LayerMask: LoadBiRefNetModelV2`
- `PreviewImage`
- `TextEncodeQwenImageEditPlusPro_lrzjason`
- `Text Concatenate (JPS)`
- `CR Text Replace`
- `CR String To Number`
- `ZML_AnyTypeSwitchFive`
- `JjkText`
- `JjkText`
- `easy showAnything`
- `CR Text Replace`
- `SaveImage`
- `忽略多组孤海`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `425746756014929`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1480`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（30/34）

**有卡**：`ModelSamplingAuraFlow`、`UNETLoader`、`CFGNorm`、`VAEDecode`、`VAELoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPLoader`、`ConditioningZeroOut`、`LayerMask: BiRefNetUltraV2`、`DWPreprocessor`、`LayerMask: LoadBiRefNetModelV2`、`TextEncodeQwenImageEditPlusPro_lrzjason`、`Text Concatenate (JPS)`、`CR Text Replace`、`CR String To Number`、`ZML_AnyTypeSwitchFive`、`SaveImage`、`忽略多组孤海`、`EmptyLatentImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
