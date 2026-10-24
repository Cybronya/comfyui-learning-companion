---
key: 图片生成/图生图/F.2Klein自动换装一致性强_2057732864199970817.json
name: F.2Klein自动换装一致性强_2057732864199970817
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2Klein自动换装一致性强_2057732864199970817.json
hash: f3697133e8f69906
coverage: 0.8
learned_at: 2026-10-23 10:52:48
nodes: [CLIPLoader, VAELoader, VAEDecode, PreviewImage, LoadImage, ConditioningZeroOut, Flux2KleinEditTextEncode_EditUtils, PreviewImage, Note, SaveImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, RMBG, LoadImage, Image Comparer (rgthree), Int, EmptyFlux2LatentImage, UNETLoader, LoraLoaderModelOnly, CR Prompt Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 278458734724141, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/F.2Klein自动换装一致性强_2057732864199970817.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2Klein自动换装一致性强_2057732864199970817.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `PreviewImage`
- `LoadImage`
- `ConditioningZeroOut`
- `Flux2KleinEditTextEncode_EditUtils`
- `PreviewImage`
- `Note`
- `SaveImage`
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RMBG`
- `LoadImage`
- `Image Comparer (rgthree)`
- `Int`
- `EmptyFlux2LatentImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`

## 关键参数

- `seed` = `278458734724141`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **80%**（16/20）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`LoadImage`、`ConditioningZeroOut`、`Flux2KleinEditTextEncode_EditUtils`、`SaveImage`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`RMBG`、`Int`、`EmptyFlux2LatentImage`、`UNETLoader`、`LoraLoaderModelOnly`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
