---
key: 图片生成/图生图/qwen2511生图+z洗图-PAULHE-v2.0_2059847791656132609.json
name: qwen2511生图+z洗图-PAULHE-v2.0_2059847791656132609
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen2511生图+z洗图-PAULHE-v2.0_2059847791656132609.json
hash: cd262c252f9f3b2e
coverage: 0.62963
learned_at: 2026-10-23 11:43:31
nodes: [ConditioningZeroOut, SetNode, SetNode, Fast Groups Bypasser (rgthree), CLIPTextEncode, SetNode, GetNode, llama_cpp_unload_model, easy showAnything, easy cleanGpuUsed, ModelSamplingAuraFlow, VAELoader, Note, LoraLoaderModelOnly, PrimitiveFloat, VAEEncode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, CFGNorm, PrimitiveFloat, PrimitiveInt, PrimitiveBoolean, PrimitiveInt, FluxKontextImageScale, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, ImageStitch, VAEDecode, ShowText|pysssss, Number Counter, SeedVR2LoadVAEModel, FlowMatchEulerDiscreteScheduler (Custom), SplitSigmasDenoise, llama_cpp_instruct_adv, PreviewImage, Image Comparer (rgthree), SetNode, SetNode, KSamplerAdvanced, GetNode, GetNode, GetNode, GetNode, SeedVR2VideoUpscaler, easy cleanGpuUsed, ImageStitch, Image Comparer (rgthree), SaveImage, KSamplerSelect, SaveImage, UNETLoader, CLIPLoaderGGUF, VAELoader, UNETLoader, CLIPLoader, easy cleanGpuUsed, VAEEncode, SetNode, SeedVR2LoadDiTModel, SamplerCustom, VAEDecode, GetNode, KSampler, Note, llama_cpp_parameters, llama_cpp_model_loader, SetNode, llama_cpp_unload_model, ShowText|pysssss, llama_cpp_parameters, TextInput_, llama_cpp_model_loader, easy showAnything, LoraLoaderModelOnly, llama_cpp_instruct_adv, TextInput_, TextInput_, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 44122223236642, "steps": 40}
---

# 图片生成/图生图/qwen2511生图+z洗图-PAULHE-v2.0_2059847791656132609.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen2511生图+z洗图-PAULHE-v2.0_2059847791656132609.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（81 个）：
- `ConditioningZeroOut`
- `SetNode`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
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
- `Number Counter`
- `SeedVR2LoadVAEModel`
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
- `UNETLoader` ★核心
- `CLIPLoaderGGUF`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `easy cleanGpuUsed`
- `VAEEncode` ★核心
- `SetNode`
- `SeedVR2LoadDiTModel`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `KSampler` ★核心
- `Note`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `SetNode`
- `llama_cpp_unload_model`
- `ShowText|pysssss`
- `llama_cpp_parameters`
- `TextInput_`
- `llama_cpp_model_loader`
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `llama_cpp_instruct_adv`
- `TextInput_`
- `TextInput_`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `44122223236642`
- `steps` = `40`
- `cfg` = `3`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **63%**（51/81）

**有卡**：`ConditioningZeroOut`、`CLIPTextEncode`、`llama_cpp_unload_model`、`easy cleanGpuUsed`、`ModelSamplingAuraFlow`、`VAELoader`、`LoraLoaderModelOnly`、`VAEEncode`、`FluxKontextMultiReferenceLatentMethod`、`CFGNorm`、`PrimitiveBoolean`、`FluxKontextImageScale`、`TextEncodeQwenImageEditPlus`、`ImageStitch`、`VAEDecode`、`Number Counter`、`SeedVR2LoadVAEModel`、`FlowMatchEulerDiscreteScheduler (Custom)`、`SplitSigmasDenoise`、`llama_cpp_instruct_adv`、`KSamplerAdvanced`、`SeedVR2VideoUpscaler`、`SaveImage`、`KSamplerSelect`、`UNETLoader`、`CLIPLoaderGGUF`、`CLIPLoader`、`SeedVR2LoadDiTModel`、`SamplerCustom`、`KSampler`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`TextInput_`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
