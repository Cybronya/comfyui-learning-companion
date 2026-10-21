---
key: 图片生成/文生图/Krea2 双采样+Flux.2 Klein高清放大-自动提示词改写文生图_2071886759901884418.json
name: Krea2 双采样+Flux.2 Klein高清放大-自动提示词改写文生图_2071886759901884418
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Krea2 双采样+Flux.2 Klein高清放大-自动提示词改写文生图_2071886759901884418.json
hash: 1a0fce368dd6c6d6
coverage: 0.956522
learned_at: 2026-10-19 23:41:19
nodes: [llama_cpp_model_loader, llama_cpp_parameters, UNETLoader, CLIPLoader, VAELoader, llama_cpp_instruct_adv, ModelSamplingAuraFlow, ConditioningZeroOut, Int, Int, ModelSamplingAuraFlow, KSamplerAdvanced, CLIPLoader, VAELoader, GetImageSize, LayerUtility: PurgeVRAM V2, ImageScaleToTotalPixels, CLIPTextEncode, ConditioningZeroOut, ReferenceLatent, VAEEncode, RandomNoise, CFGGuider, KSamplerSelect, Flux2Scheduler, ReferenceLatent, ImageSharpen, EmptyFlux2LatentImage, ColorMatch, VAEDecode, VAEDecode, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, CR Prompt Text, Image Comparer (rgthree), SaveImage, PreviewAny, INTConstant, INTConstant, SamplerCustomAdvanced, UNETLoader, UNETLoader, EmptyLatentImage, SaveImage, CR Prompt Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 3, "denoise": "simple", "height": 1536, "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize", "width": 1024}
---

# 图片生成/文生图/Krea2 双采样+Flux.2 Klein高清放大-自动提示词改写文生图_2071886759901884418.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Krea2 双采样+Flux.2 Klein高清放大-自动提示词改写文生图_2071886759901884418.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `Int`
- `Int`
- `ModelSamplingAuraFlow`
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `VAELoader`
- `GetImageSize`
- `LayerUtility: PurgeVRAM V2`
- `ImageScaleToTotalPixels`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `ReferenceLatent`
- `ImageSharpen`
- `EmptyFlux2LatentImage`
- `ColorMatch`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `CR Prompt Text`
- `Image Comparer (rgthree)`
- `SaveImage`
- `PreviewAny`
- `INTConstant`
- `INTConstant`
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `CR Prompt Text`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `3`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（44/46）

**有卡**：`llama_cpp_model_loader`、`llama_cpp_parameters`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`llama_cpp_instruct_adv`、`ModelSamplingAuraFlow`、`ConditioningZeroOut`、`Int`、`KSamplerAdvanced`、`GetImageSize`、`LayerUtility: PurgeVRAM V2`、`ImageScaleToTotalPixels`、`CLIPTextEncode`、`ReferenceLatent`、`VAEEncode`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`Flux2Scheduler`、`ImageSharpen`、`EmptyFlux2LatentImage`、`ColorMatch`、`VAEDecode`、`CR Prompt Text`、`SaveImage`、`INTConstant`、`SamplerCustomAdvanced`、`EmptyLatentImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、CFGGuider
