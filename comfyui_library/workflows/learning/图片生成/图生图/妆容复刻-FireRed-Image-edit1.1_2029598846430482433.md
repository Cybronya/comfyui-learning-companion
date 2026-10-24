---
key: 图片生成/图生图/妆容复刻-FireRed-Image-edit1.1_2029598846430482433.json
name: 妆容复刻-FireRed-Image-edit1.1_2029598846430482433
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/妆容复刻-FireRed-Image-edit1.1_2029598846430482433.json
hash: 73d2cd01b8b55726
coverage: 0.958333
learned_at: 2026-10-23 12:46:50
nodes: [Int, LoadImage, LoadImage, Float, PrimitiveNode, SaveImage, iToolsCompareImage, VAEEncode, KSampler, VAEDecode, TextInput_, FluxKontextImageScale, EnhancedLoadDiffusionModel, easy imageSwitch, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingAuraFlow, LayerUtility: ImageScaleByAspectRatio V2, FluxKontextImageScale, CLIPLoader, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, VAELoader, CFGNorm]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "dpmpp_2m_sde_gpu", "scheduler": "karras", "seed": 667831304975976, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/妆容复刻-FireRed-Image-edit1.1_2029598846430482433.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/妆容复刻-FireRed-Image-edit1.1_2029598846430482433.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `Int`
- `LoadImage`
- `LoadImage`
- `Float`
- `PrimitiveNode`
- `SaveImage`
- `iToolsCompareImage`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TextInput_`
- `FluxKontextImageScale`
- `EnhancedLoadDiffusionModel`
- `easy imageSwitch`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FluxKontextImageScale`
- `CLIPLoader`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `VAELoader`
- `CFGNorm`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `667831304975976`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m_sde_gpu`
- `scheduler` = `karras`
- `denoise` = `1`

## 知识

覆盖率 **96%**（23/24）

**有卡**：`Int`、`LoadImage`、`Float`、`SaveImage`、`iToolsCompareImage`、`VAEEncode`、`KSampler`、`VAEDecode`、`TextInput_`、`FluxKontextImageScale`、`EnhancedLoadDiffusionModel`、`easy imageSwitch`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`TextEncodeQwenImageEditPlus`、`VAELoader`、`CFGNorm`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、CFGNorm、TextEncodeQwenImageEditPlus

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
