---
key: 图片生成/图生图/paulhe-qwen2511生图+z洗图-v1.0_2059618383544541185.json
name: paulhe-qwen2511生图+z洗图-v1.0_2059618383544541185
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/paulhe-qwen2511生图+z洗图-v1.0_2059618383544541185.json
hash: 2a4c1efd4ecc3dff
coverage: 0.626667
learned_at: 2026-10-23 11:41:31
nodes: [ConditioningZeroOut, SetNode, SetNode, Fast Groups Bypasser (rgthree), CLIPTextEncode, SetNode, GetNode, SetNode, llama_cpp_unload_model, easy showAnything, easy cleanGpuUsed, ModelSamplingAuraFlow, VAELoader, Note, LoraLoaderModelOnly, PrimitiveFloat, VAEEncode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, CFGNorm, PrimitiveFloat, PrimitiveInt, PrimitiveBoolean, PrimitiveInt, FluxKontextImageScale, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, ImageStitch, VAEDecode, ShowText|pysssss, TextInput_, Number Counter, SeedVR2LoadVAEModel, llama_cpp_parameters, ImageScaleBy, FlowMatchEulerDiscreteScheduler (Custom), SplitSigmasDenoise, llama_cpp_instruct_adv, PreviewImage, Image Comparer (rgthree), SetNode, SetNode, KSamplerAdvanced, GetNode, GetNode, GetNode, GetNode, SeedVR2VideoUpscaler, easy cleanGpuUsed, ImageStitch, Image Comparer (rgthree), SaveImage, KSamplerSelect, SaveImage, TextInput_, LoadImage, UNETLoader, CLIPLoaderGGUF, VAELoader, UNETLoader, CLIPLoader, llama_cpp_model_loader, easy cleanGpuUsed, VAEEncode, SetNode, SeedVR2LoadDiTModel, SamplerCustom, VAEDecode, GetNode, LoraLoaderModelOnly, KSampler, Note]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1021316662153560, "steps": 40}
---

# 图片生成/图生图/paulhe-qwen2511生图+z洗图-v1.0_2059618383544541185.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/paulhe-qwen2511生图+z洗图-v1.0_2059618383544541185.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（75 个）：
- `ConditioningZeroOut`
- `SetNode`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `llama_cpp_unload_model`
- `easy showAnything`
- `easy cleanGpuUsed`
- `ModelSamplingAuraFlow`
- `VAELoader`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `VAEEncode` ★核心
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `CFGNorm`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `FluxKontextImageScale`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `ImageStitch`
- `VAEDecode` ★核心
- `ShowText|pysssss`
- `TextInput_`
- `Number Counter`
- `SeedVR2LoadVAEModel`
- `llama_cpp_parameters`
- `ImageScaleBy`
- `FlowMatchEulerDiscreteScheduler (Custom)`
- `SplitSigmasDenoise`
- `llama_cpp_instruct_adv`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SetNode`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SeedVR2VideoUpscaler`
- `easy cleanGpuUsed`
- `ImageStitch`
- `Image Comparer (rgthree)`
- `SaveImage`
- `KSamplerSelect` ★核心
- `SaveImage`
- `TextInput_`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoaderGGUF`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `llama_cpp_model_loader`
- `easy cleanGpuUsed`
- `VAEEncode` ★核心
- `SetNode`
- `SeedVR2LoadDiTModel`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1021316662153560`
- `steps` = `40`
- `cfg` = `3`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **63%**（47/75）

**有卡**：`ConditioningZeroOut`、`CLIPTextEncode`、`llama_cpp_unload_model`、`easy cleanGpuUsed`、`ModelSamplingAuraFlow`、`VAELoader`、`LoraLoaderModelOnly`、`VAEEncode`、`FluxKontextMultiReferenceLatentMethod`、`CFGNorm`、`PrimitiveBoolean`、`FluxKontextImageScale`、`TextEncodeQwenImageEditPlus`、`ImageStitch`、`VAEDecode`、`TextInput_`、`Number Counter`、`SeedVR2LoadVAEModel`、`llama_cpp_parameters`、`ImageScaleBy`、`FlowMatchEulerDiscreteScheduler (Custom)`、`SplitSigmasDenoise`、`llama_cpp_instruct_adv`、`KSamplerAdvanced`、`SeedVR2VideoUpscaler`、`SaveImage`、`KSamplerSelect`、`LoadImage`、`UNETLoader`、`CLIPLoaderGGUF`、`CLIPLoader`、`llama_cpp_model_loader`、`SeedVR2LoadDiTModel`、`SamplerCustom`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
