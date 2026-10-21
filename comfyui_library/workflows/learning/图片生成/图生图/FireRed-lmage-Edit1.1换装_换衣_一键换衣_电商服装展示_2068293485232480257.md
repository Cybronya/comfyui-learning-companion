---
key: 图片生成/图生图/FireRed-lmage-Edit1.1换装_换衣_一键换衣_电商服装展示_2068293485232480257.json
name: FireRed-lmage-Edit1.1换装_换衣_一键换衣_电商服装展示_2068293485232480257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-lmage-Edit1.1换装_换衣_一键换衣_电商服装展示_2068293485232480257.json
hash: 42778de4f0e38be4
coverage: 0.866667
learned_at: 2026-10-21 00:39:24
nodes: [LoraLoaderModelOnly, CLIPLoader, VAELoader, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, SaveImage, KSampler, ConditioningZeroOut, VAEDecode, UNETLoader, Image Comparer (rgthree), PreviewImage, LoadImage, LoadImage, TextEncodeQwenImageEditPlusAdvance_lrzjason]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 240884129316651, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-lmage-Edit1.1换装_换衣_一键换衣_电商服装展示_2068293485232480257.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-lmage-Edit1.1换装_换衣_一键换衣_电商服装展示_2068293485232480257.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`

## 关键参数

- `seed` = `240884129316651`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`SaveImage`、`KSampler`、`ConditioningZeroOut`、`VAEDecode`、`UNETLoader`、`LoadImage`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
