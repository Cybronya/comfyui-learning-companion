---
key: 图片生成/图生图/Z-IMAGE洗图 qwen3.5反推_2042416675500335106.json
name: Z-IMAGE洗图 qwen3.5反推_2042416675500335106
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-IMAGE洗图 qwen3.5反推_2042416675500335106.json
hash: 50031765a6758b77
coverage: 0.565217
learned_at: 2026-10-23 11:29:11
nodes: [ModelPatchLoader, AIO_Preprocessor, Note, Note, ModelSamplingAuraFlow, Note, INTConstant, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, easy seed, QwenImageDiffsynthControlnet, EmptyLatentImage, Reroute, Reroute, Reroute, ConditioningZeroOut, Reroute, Reroute, Reroute, Reroute, INTConstant, Reroute, Reroute, Reroute, Reroute, Reroute, LayerUtility: ImageScaleByAspectRatio V2, ShowText|pysssss, CLIPTextEncode, Reroute, Reroute, Reroute, CLIPLoader, Qwen3_VQA, Reroute, KSamplerAdvanced, KSamplerAdvanced, ImageScaleToTotalPixels, VAEDecode, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, PreviewImage, UNETLoader, PreviewImage, AIO_Preprocessor, VAELoader, ModelSamplingAuraFlow, INTConstant, AIO_Preprocessor, Reroute, easy cleanGpuUsed, SetNode, SomethingToString, GetNode, SetNode, GetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, Mute / Bypass Repeater (rgthree), llama_cpp_parameters, TextInput_, llama_cpp_instruct_adv, llama_cpp_model_loader, Fast Groups Bypasser (rgthree), easy showAnything, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 10, "denoise": "simple", "height": 1080, "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize", "width": 1920}
---

# 图片生成/图生图/Z-IMAGE洗图 qwen3.5反推_2042416675500335106.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-IMAGE洗图 qwen3.5反推_2042416675500335106.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `ModelPatchLoader`
- `AIO_Preprocessor`
- `Note`
- `Note`
- `ModelSamplingAuraFlow`
- `Note`
- `INTConstant`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy seed`
- `QwenImageDiffsynthControlnet`
- `EmptyLatentImage` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `ConditioningZeroOut`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `INTConstant`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `CLIPLoader`
- `Qwen3_VQA`
- `Reroute`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `UNETLoader` ★核心
- `PreviewImage`
- `AIO_Preprocessor`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `INTConstant`
- `AIO_Preprocessor`
- `Reroute`
- `easy cleanGpuUsed`
- `SetNode`
- `SomethingToString`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Mute / Bypass Repeater (rgthree)`
- `llama_cpp_parameters`
- `TextInput_`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `Fast Groups Bypasser (rgthree)`
- `easy showAnything`
- `LoadImage`

## 关键参数

- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **57%**（39/69）

**有卡**：`ModelPatchLoader`、`AIO_Preprocessor`、`ModelSamplingAuraFlow`、`INTConstant`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy seed`、`QwenImageDiffsynthControlnet`、`EmptyLatentImage`、`ConditioningZeroOut`、`CLIPTextEncode`、`CLIPLoader`、`Qwen3_VQA`、`KSamplerAdvanced`、`ImageScaleToTotalPixels`、`VAEDecode`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`UNETLoader`、`VAELoader`、`easy cleanGpuUsed`、`SomethingToString`、`Mute / Bypass Repeater (rgthree)`、`llama_cpp_parameters`、`TextInput_`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage、UNETLoader
