---
key: 图片生成/图生图/krea2-角色四视图生成2.0_2099850078163918849.json
name: krea2-角色四视图生成2.0_2099850078163918849
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/krea2-角色四视图生成2.0_2099850078163918849.json
hash: cf80178d9252feee
coverage: 0.882353
learned_at: 2026-10-21 00:45:47
nodes: [LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, CLIPLoader, Krea2EditGroundedEncode, KSampler, VAELoader, kkPadImageToCanvas, LoraLoaderModelOnly, UNETLoader, Krea2OstrisEditModelPatch, FluxKontextMultiReferenceLatentMethod, VAEEncode, FluxKontextMultiReferenceLatentMethod, PreviewImage, LoadImage, VAEDecode, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 367654382187925, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/krea2-角色四视图生成2.0_2099850078163918849.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/krea2-角色四视图生成2.0_2099850078163918849.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `CLIPLoader`
- `Krea2EditGroundedEncode`
- `KSampler` ★核心
- `VAELoader`
- `kkPadImageToCanvas`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `Krea2OstrisEditModelPatch`
- `FluxKontextMultiReferenceLatentMethod`
- `VAEEncode` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `PreviewImage`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `367654382187925`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`Krea2EditGroundedEncode`、`KSampler`、`VAELoader`、`kkPadImageToCanvas`、`LoraLoaderModelOnly`、`UNETLoader`、`Krea2OstrisEditModelPatch`、`FluxKontextMultiReferenceLatentMethod`、`VAEEncode`、`LoadImage`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、FluxKontextMultiReferenceLatentMethod

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
