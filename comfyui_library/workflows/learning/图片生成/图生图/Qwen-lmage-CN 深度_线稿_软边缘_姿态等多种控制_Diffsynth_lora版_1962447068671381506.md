---
key: 图片生成/图生图/Qwen-lmage-CN 深度_线稿_软边缘_姿态等多种控制_Diffsynth_lora版_1962447068671381506.json
name: Qwen-lmage-CN 深度_线稿_软边缘_姿态等多种控制_Diffsynth_lora版_1962447068671381506
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-lmage-CN 深度_线稿_软边缘_姿态等多种控制_Diffsynth_lora版_1962447068671381506.json
hash: 9769fbd530635f71
coverage: 0.615385
learned_at: 2026-10-23 11:18:51
nodes: [AIO_Preprocessor, AIO_Preprocessor, PreviewImage, PreviewImage, PreviewImage, VAEEncode, Anything Everywhere, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, Fast Groups Bypasser (rgthree), ReferenceLatent, ConditioningZeroOut, ReferenceLatent, MarkdownNote, CLIPTextEncode, Image Comparer (rgthree), LoraLoaderModelOnly, ModelSamplingAuraFlow, DWPreprocessor, AIO_Preprocessor, CR Image Input Switch (4 way), Fast Groups Bypasser (rgthree), CLIPTextEncode, CR Conditioning Input Switch, MarkdownNote, MarkdownNote, UNETLoader, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, Fast Groups Bypasser (rgthree), PreviewImage, VAEDecode, KSampler, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1066893374827409, "steps": 20}
---

# 图片生成/图生图/Qwen-lmage-CN 深度_线稿_软边缘_姿态等多种控制_Diffsynth_lora版_1962447068671381506.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-lmage-CN 深度_线稿_软边缘_姿态等多种控制_Diffsynth_lora版_1962447068671381506.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `VAEEncode` ★核心
- `Anything Everywhere`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Fast Groups Bypasser (rgthree)`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `DWPreprocessor`
- `AIO_Preprocessor`
- `CR Image Input Switch (4 way)`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `CR Conditioning Input Switch`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `PreviewImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1066893374827409`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **62%**（24/39）

**有卡**：`AIO_Preprocessor`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`VAELoader`、`ReferenceLatent`、`ConditioningZeroOut`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`DWPreprocessor`、`CR Image Input Switch (4 way)`、`CR Conditioning Input Switch`、`UNETLoader`、`LoadImage`、`VAEDecode`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
