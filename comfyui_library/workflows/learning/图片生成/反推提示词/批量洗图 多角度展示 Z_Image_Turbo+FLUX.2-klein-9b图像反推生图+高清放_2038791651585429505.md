---
key: 图片生成/反推提示词/批量洗图 多角度展示 Z_Image_Turbo+FLUX.2-klein-9b图像反推生图+高清放_2038791651585429505.json
name: 批量洗图 多角度展示 Z_Image_Turbo+FLUX.2-klein-9b图像反推生图+高清放_2038791651585429505
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/批量洗图 多角度展示 Z_Image_Turbo+FLUX.2-klein-9b图像反推生图+高清放_2038791651585429505.json
hash: 566d58fa68888b56
coverage: 0.95122
learned_at: 2026-10-26 01:48:08
nodes: [ModelSamplingAuraFlow, CLIPTextEncode, CLIPTextEncode, VAEDecode, KSamplerSelect, RandomNoise, CFGGuider, ConditioningZeroOut, ReferenceLatent, VAEDecode, ReferenceLatent, ImageScaleToTotalPixels, VAEEncode, LayerFilter: Sharp & Soft, ImageSharpen, CLIPTextEncode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, BasicScheduler, VAEEncode, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, PreviewAny, llama_cpp_model_loader, ImageScaleDownToSize, llama_cpp_instruct_adv, LayerUtility: PurgeVRAM, INTConstant, INTConstant, EmptySD3LatentImage, LoadImage, Text Multiline, KSampler, SamplerCustomAdvanced, Image Comparer (rgthree), SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 745733151975406, "steps": 10}
---

# 图片生成/反推提示词/批量洗图 多角度展示 Z_Image_Turbo+FLUX.2-klein-9b图像反推生图+高清放_2038791651585429505.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/批量洗图 多角度展示 Z_Image_Turbo+FLUX.2-klein-9b图像反推生图+高清放_2038791651585429505.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `VAEDecode` ★核心
- `ReferenceLatent`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `LayerFilter: Sharp & Soft`
- `ImageSharpen`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `BasicScheduler`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PreviewAny`
- `llama_cpp_model_loader`
- `ImageScaleDownToSize`
- `llama_cpp_instruct_adv`
- `LayerUtility: PurgeVRAM`
- `INTConstant`
- `INTConstant`
- `EmptySD3LatentImage`
- `LoadImage`
- `Text Multiline`
- `KSampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `745733151975406`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **95%**（39/41）

**有卡**：`ModelSamplingAuraFlow`、`CLIPTextEncode`、`VAEDecode`、`KSamplerSelect`、`RandomNoise`、`CFGGuider`、`ConditioningZeroOut`、`ReferenceLatent`、`ImageScaleToTotalPixels`、`VAEEncode`、`LayerFilter: Sharp & Soft`、`ImageSharpen`、`LayerUtility: PurgeVRAM`、`BasicScheduler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`llama_cpp_model_loader`、`ImageScaleDownToSize`、`llama_cpp_instruct_adv`、`INTConstant`、`EmptySD3LatentImage`、`LoadImage`、`Text Multiline`、`KSampler`、`SamplerCustomAdvanced`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
