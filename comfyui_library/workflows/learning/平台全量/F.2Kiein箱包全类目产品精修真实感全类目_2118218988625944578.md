---
key: 平台全量/F.2Kiein箱包全类目产品精修真实感全类目_2118218988625944578.json
name: F.2Kiein箱包全类目产品精修真实感全类目_2118218988625944578
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/F.2Kiein箱包全类目产品精修真实感全类目_2118218988625944578.json
hash: a005930400e7d749
coverage: 0.928571
learned_at: 2026-11-14 00:24:08
nodes: [ConditioningZeroOut, VAEEncode, VAELoader, KSampler, ReferenceLatent, VAEDecode, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, LoadImage, UNETLoader, Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 717534979294943, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/F.2Kiein箱包全类目产品精修真实感全类目_2118218988625944578.json

> 来源文件 `comfyui_library/workflows/平台全量/F.2Kiein箱包全类目产品精修真实感全类目_2118218988625944578.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `VAELoader`
- `KSampler` ★核心
- `ReferenceLatent`
- `VAEDecode` ★核心
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `717534979294943`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`ConditioningZeroOut`、`VAEEncode`、`VAELoader`、`KSampler`、`ReferenceLatent`、`VAEDecode`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`LoadImage`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
