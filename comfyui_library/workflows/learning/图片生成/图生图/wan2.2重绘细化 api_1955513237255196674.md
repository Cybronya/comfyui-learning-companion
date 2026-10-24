---
key: 图片生成/图生图/wan2.2重绘细化 api_1955513237255196674.json
name: wan2.2重绘细化 api_1955513237255196674
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2重绘细化 api_1955513237255196674.json
hash: d46fba19d39a3fe0
coverage: 0.861111
learned_at: 2026-10-23 11:46:10
nodes: [GetImageSize, MathExpression|pysssss, LayerUtility: If , LayerUtility: If , MathExpression|pysssss, MathExpression|pysssss, easy showAnything, ImageScale, easy showAnything, MathExpression|pysssss, LayerUtility: BooleanOperatorV2, LayerUtility: BooleanOperatorV2, ImageUpscaleWithModel, easy imageScaleDownToSize, CLIPTextEncode, VAELoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, VAEDecode, ImageConcanate, CLIPTextEncode, RH_Captioner, ShowText|pysssss, SaveImage, KSampler, UpscaleModelLoader, LoadImage, VAEEncode, SeargeIntegerConstant, PreviewImage, PreviewImage, easy float]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.16, "sampler_name": "res_multistep", "scheduler": "kl_optimal", "seed": 859969845992108, "steps": 10}
---

# 图片生成/图生图/wan2.2重绘细化 api_1955513237255196674.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2重绘细化 api_1955513237255196674.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `GetImageSize`
- `MathExpression|pysssss`
- `LayerUtility: If `
- `LayerUtility: If `
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `easy showAnything`
- `ImageScale`
- `easy showAnything`
- `MathExpression|pysssss`
- `LayerUtility: BooleanOperatorV2`
- `LayerUtility: BooleanOperatorV2`
- `ImageUpscaleWithModel`
- `easy imageScaleDownToSize`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `ImageConcanate`
- `CLIPTextEncode` ★核心
- `RH_Captioner`
- `ShowText|pysssss`
- `SaveImage`
- `KSampler` ★核心
- `UpscaleModelLoader`
- `LoadImage`
- `VAEEncode` ★核心
- `SeargeIntegerConstant`
- `PreviewImage`
- `PreviewImage`
- `easy float`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `859969845992108`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `kl_optimal`
- `denoise` = `0.16`

## 知识

覆盖率 **86%**（31/36）

**有卡**：`GetImageSize`、`MathExpression|pysssss`、`LayerUtility: If `、`ImageScale`、`LayerUtility: BooleanOperatorV2`、`ImageUpscaleWithModel`、`easy imageScaleDownToSize`、`CLIPTextEncode`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAEDecode`、`ImageConcanate`、`RH_Captioner`、`SaveImage`、`KSampler`、`UpscaleModelLoader`、`LoadImage`、`VAEEncode`、`SeargeIntegerConstant`、`easy float`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
