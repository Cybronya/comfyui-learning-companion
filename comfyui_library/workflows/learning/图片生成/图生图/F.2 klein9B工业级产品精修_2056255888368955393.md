---
key: 图片生成/图生图/F.2 klein9B工业级产品精修_2056255888368955393.json
name: F.2 klein9B工业级产品精修_2056255888368955393
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2 klein9B工业级产品精修_2056255888368955393.json
hash: 1879a569c04cc3b9
coverage: 0.941176
learned_at: 2026-10-23 10:52:40
nodes: [VAELoader, CLIPTextEncode, VAEDecode, ReferenceLatent, VAEEncode, EmptyFlux2LatentImage, CLIPLoader, SaveImage, Image Comparer (rgthree), UNETLoader, ConditioningZeroOut, LoadImage, KSampler, CR Prompt Text, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, Int]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 762036173294153, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/F.2 klein9B工业级产品精修_2056255888368955393.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2 klein9B工业级产品精修_2056255888368955393.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `EmptyFlux2LatentImage`
- `CLIPLoader`
- `SaveImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `LoadImage`
- `KSampler` ★核心
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `762036173294153`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`ReferenceLatent`、`VAEEncode`、`EmptyFlux2LatentImage`、`CLIPLoader`、`SaveImage`、`UNETLoader`、`ConditioningZeroOut`、`LoadImage`、`KSampler`、`CR Prompt Text`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
