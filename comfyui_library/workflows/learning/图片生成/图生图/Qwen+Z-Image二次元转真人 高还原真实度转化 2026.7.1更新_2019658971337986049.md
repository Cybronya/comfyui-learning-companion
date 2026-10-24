---
key: 图片生成/图生图/Qwen+Z-Image二次元转真人 高还原真实度转化 2026.7.1更新_2019658971337986049.json
name: Qwen+Z-Image二次元转真人 高还原真实度转化 2026.7.1更新_2019658971337986049
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen+Z-Image二次元转真人 高还原真实度转化 2026.7.1更新_2019658971337986049.json
hash: fd20b1977faad261
coverage: 0.945652
learned_at: 2026-10-23 11:14:48
nodes: [VAELoader, VAEEncode, ConditioningZeroOut, VAEDecode, KSampler, CLIPLoader, ImageScaleToTotalPixels, VAELoader, LayerUtility: PurgeVRAM V2, llama_cpp_model_loader, llama_cpp_parameters, CLIPTextEncode, easy clearCacheAll, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), SaveImage, PreviewAny, easy saveText, SeedVR2LoadDiTModel, ImageScaleBy, KSampler, SaveImage, ColorMatch, LayerUtility: PurgeVRAM V2, easy cleanGpuUsed, LoadImage, LoadImage, LoadImage, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, LoraLoaderModelOnly, LoadImage, ConditioningZeroOut, UNETLoader, LoraLoaderModelOnly, CLIPLoader, easy cleanGpuUsed, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, UNETLoader, LoraLoaderModelOnly, SeedVR2LoadDiTModel, ImageScaleBy, VAEEncode, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, ConditioningZeroOut, SaveImage, SaveImage, CLIPLoader, CR Text, TextEncodeQwenImageEditPlus, Note, KSampler, TextEncodeQwenImageEditPlus, easy cleanGpuUsed, VAEDecode, SaveImage, SaveImage, CLIPTextEncode, VAEEncode, PreviewAny, LoadImage, llama_cpp_model_loader, KSampler, VAEDecode, easy cleanGpuUsed, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, VAEEncode, llama_cpp_parameters, llama_cpp_instruct_adv, easy saveText, CR Text Concatenate, CR Text, UNETLoader, CLIPLoader, VAELoader, CR Text, llama_cpp_instruct_adv, CR Text, UNETLoader, KSampler, CR Text Concatenate, TextEncodeQwenImageEdit, Fast Groups Muter (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.4000000000000001, "sampler_name": "dpmpp_2m_sde", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 864410975105750, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen+Z-Image二次元转真人 高还原真实度转化 2026.7.1更新_2019658971337986049.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen+Z-Image二次元转真人 高还原真实度转化 2026.7.1更新_2019658971337986049.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（92 个）：
- `VAELoader`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `VAELoader`
- `LayerUtility: PurgeVRAM V2`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `CLIPTextEncode` ★核心
- `easy clearCacheAll`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `SaveImage`
- `PreviewAny`
- `easy saveText`
- `SeedVR2LoadDiTModel`
- `ImageScaleBy`
- `KSampler` ★核心
- `SaveImage`
- `ColorMatch`
- `LayerUtility: PurgeVRAM V2`
- `easy cleanGpuUsed`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `easy cleanGpuUsed`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SeedVR2LoadDiTModel`
- `ImageScaleBy`
- `VAEEncode` ★核心
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ConditioningZeroOut`
- `SaveImage`
- `SaveImage`
- `CLIPLoader`
- `CR Text`
- `TextEncodeQwenImageEditPlus`
- `Note`
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlus`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `PreviewAny`
- `LoadImage`
- `llama_cpp_model_loader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `VAEEncode` ★核心
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `easy saveText`
- `CR Text Concatenate`
- `CR Text`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CR Text`
- `llama_cpp_instruct_adv`
- `CR Text`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CR Text Concatenate`
- `TextEncodeQwenImageEdit`
- `Fast Groups Muter (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `864410975105750`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `0.4000000000000001`

## 知识

覆盖率 **95%**（87/92）

**有卡**：`VAELoader`、`VAEEncode`、`ConditioningZeroOut`、`VAEDecode`、`KSampler`、`CLIPLoader`、`ImageScaleToTotalPixels`、`LayerUtility: PurgeVRAM V2`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`CLIPTextEncode`、`easy clearCacheAll`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`easy saveText`、`SeedVR2LoadDiTModel`、`ImageScaleBy`、`ColorMatch`、`easy cleanGpuUsed`、`LoadImage`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`LoraLoaderModelOnly`、`UNETLoader`、`CR Text`、`TextEncodeQwenImageEditPlus`、`llama_cpp_instruct_adv`、`CR Text Concatenate`、`TextEncodeQwenImageEdit`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 4 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
