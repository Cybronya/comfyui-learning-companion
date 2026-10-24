---
key: 图片生成/图生图/wan2.2重绘细化 api 最长边 2560_1955465383026180097.json
name: wan2.2重绘细化 api 最长边 2560_1955465383026180097
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2重绘细化 api 最长边 2560_1955465383026180097.json
hash: 1282698bc6714d7d
coverage: 0.882353
learned_at: 2026-10-23 11:46:09
nodes: [GetImageSize, MathExpression|pysssss, LayerUtility: If , LayerUtility: If , MathExpression|pysssss, MathExpression|pysssss, ImageScale, MathExpression|pysssss, LayerUtility: BooleanOperatorV2, easy imageScaleDownToSize, CLIPTextEncode, VAEEncode, VAELoader, PathchSageAttentionKJ, CLIPTextEncode, PreviewImage, UpscaleModelLoader, easy showAnything, easy showAnything, LayerUtility: BooleanOperatorV2, SeargeIntegerConstant, ImageUpscaleWithModel, LayerUtility: GetImageSize, LayerUtility: GetImageSize, RH_Captioner, VAEDecode, ShowText|pysssss, CLIPLoader, UNETLoader, LoadImage, SaveImage, LoraLoaderModelOnly, KSampler, ModelSamplingSD3]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.24000000000000005, "sampler_name": "euler", "scheduler": "kl_optimal", "seed": 489023690457826, "steps": 10}
---

# 图片生成/图生图/wan2.2重绘细化 api 最长边 2560_1955465383026180097.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2重绘细化 api 最长边 2560_1955465383026180097.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `GetImageSize`
- `MathExpression|pysssss`
- `LayerUtility: If `
- `LayerUtility: If `
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `ImageScale`
- `MathExpression|pysssss`
- `LayerUtility: BooleanOperatorV2`
- `easy imageScaleDownToSize`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `VAELoader`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `UpscaleModelLoader`
- `easy showAnything`
- `easy showAnything`
- `LayerUtility: BooleanOperatorV2`
- `SeargeIntegerConstant`
- `ImageUpscaleWithModel`
- `LayerUtility: GetImageSize`
- `LayerUtility: GetImageSize`
- `RH_Captioner`
- `VAEDecode` ★核心
- `ShowText|pysssss`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadImage`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `ModelSamplingSD3`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `489023690457826`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `kl_optimal`
- `denoise` = `0.24000000000000005`

## 知识

覆盖率 **88%**（30/34）

**有卡**：`GetImageSize`、`MathExpression|pysssss`、`LayerUtility: If `、`ImageScale`、`LayerUtility: BooleanOperatorV2`、`easy imageScaleDownToSize`、`CLIPTextEncode`、`VAEEncode`、`VAELoader`、`PathchSageAttentionKJ`、`UpscaleModelLoader`、`SeargeIntegerConstant`、`ImageUpscaleWithModel`、`LayerUtility: GetImageSize`、`RH_Captioner`、`VAEDecode`、`CLIPLoader`、`UNETLoader`、`LoadImage`、`SaveImage`、`LoraLoaderModelOnly`、`KSampler`、`ModelSamplingSD3`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
