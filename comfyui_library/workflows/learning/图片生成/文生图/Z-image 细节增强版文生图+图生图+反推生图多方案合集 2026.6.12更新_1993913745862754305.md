---
key: 图片生成/文生图/Z-image 细节增强版文生图+图生图+反推生图多方案合集 2026.6.12更新_1993913745862754305.json
name: Z-image 细节增强版文生图+图生图+反推生图多方案合集 2026.6.12更新_1993913745862754305
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image 细节增强版文生图+图生图+反推生图多方案合集 2026.6.12更新_1993913745862754305.json
hash: f1dcb83faf05859e
coverage: 0.706294
learned_at: 2026-10-19 21:32:57
nodes: [LayerUtility: JoyCaptionBeta1, SaveImage, LayerUtility: JoyCaptionBeta1ExtraOptions, RH_Translator, Image Comparer (rgthree), Int, KSampler, Int, CLIPLoader, EmptyLatentImage, LayerUtility: LoadJoyCaptionBeta1Model, GenerateNoise, LGNoiseInjectionLatent, EmptyLatentImage, ConditioningZeroOut, LoadImage, CR Text, LoadImage, CLIPLoader, PrimitiveNode, Note, ShowText|pysssss, EmptyLatentImage, VAELoader, LoadImage, LoadImage, Image Comparer (rgthree), LoadImage, Image Comparer (rgthree), Image Comparer (rgthree), VAEDecode, Note, LoadImage, Note, SaveImage, Note, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, VAEEncode, ConditioningZeroOut, UNETLoader, LoraLoaderModelOnly, CR Text, CLIPTextEncode, Note, CLIPLoader, VAELoader, Int, Int, ConditioningZeroOut, VAEDecode, Note, VAELoader, KSampler, VAEDecode, ConditioningZeroOut, CLIPTextEncode, EmptyLatentImage, VAEDecode, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, PrimitiveStringMultiline, ConditioningZeroOut, LoraLoaderModelOnly, Note, CLIPTextEncode, Note, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), Note, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Note, CLIPTextEncode, Note, KSamplerAdvanced, Note, Note, KSamplerAdvanced, PrimitiveStringMultiline, CLIPTextEncode, VAEDecode, CLIPTextEncode, KSampler, EmptySD3LatentImage, Note, Note, TTResolutionSelector, Note, PreviewImage, ImageScaleBy, SaveImage, SeedVR2VideoUpscaler, Note, ImageCASharpening+, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, easy cleanGpuUsed, easy int, Note, PathchSageAttentionKJ, CheckpointLoaderSimple, Note, Note, UNETLoader, Note, VAELoader, SaveImage, UNETLoader, UNETLoader, SaveImage, KSampler, SaveImage, UNETLoader, CLIPLoader, VAELoader, PrimitiveInt, MarkdownNote, QwenImageEngineer, ConditioningZeroOut, VAEDecode, UNETLoader, VAELoader, ClipLoaderGGUF, Fast Groups Muter (rgthree), RH_Translator, PreviewAny, CR Prompt Text, SaveImage, CLIPTextEncode, PreviewAny, LoraLoaderModelOnly, KSampler, EmptySD3LatentImage, Note]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "Z-Image-Base-8steps-White_Marble-AIO_v2-fp8.safetensors", "denoise": 1, "height": 1920, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 756928185685469, "steps": 10, "width": 1280}
---

# 图片生成/文生图/Z-image 细节增强版文生图+图生图+反推生图多方案合集 2026.6.12更新_1993913745862754305.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image 细节增强版文生图+图生图+反推生图多方案合集 2026.6.12更新_1993913745862754305.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（143 个）：
- `LayerUtility: JoyCaptionBeta1`
- `SaveImage`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `RH_Translator`
- `Image Comparer (rgthree)`
- `Int`
- `KSampler` ★核心
- `Int`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `GenerateNoise`
- `LGNoiseInjectionLatent`
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`
- `LoadImage`
- `CR Text`
- `LoadImage`
- `CLIPLoader`
- `PrimitiveNode`
- `Note`
- `ShowText|pysssss`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `Note`
- `LoadImage`
- `Note`
- `SaveImage`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `CLIPTextEncode` ★核心
- `Note`
- `CLIPLoader`
- `VAELoader`
- `Int`
- `Int`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `Note`
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `CLIPTextEncode` ★核心
- `Note`
- `KSamplerAdvanced` ★核心
- `Note`
- `Note`
- `KSamplerAdvanced` ★核心
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `Note`
- `Note`
- `TTResolutionSelector`
- `Note`
- `PreviewImage`
- `ImageScaleBy`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `Note`
- `ImageCASharpening+`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `easy cleanGpuUsed`
- `easy int`
- `Note`
- `PathchSageAttentionKJ`
- `CheckpointLoaderSimple` ★核心
- `Note`
- `Note`
- `UNETLoader` ★核心
- `Note`
- `VAELoader`
- `SaveImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `KSampler` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PrimitiveInt`
- `MarkdownNote`
- `QwenImageEngineer`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `ClipLoaderGGUF`
- `Fast Groups Muter (rgthree)`
- `RH_Translator`
- `PreviewAny`
- `CR Prompt Text`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `Note`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `756928185685469`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1280`
- `height` = `1920`
- `batch_size` = `1`
- `checkpoint` = `Z-Image-Base-8steps-White_Marble-AIO_v2-fp8.safetensors`

## 知识

覆盖率 **71%**（101/143）

**有卡**：`LayerUtility: JoyCaptionBeta1`、`SaveImage`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`RH_Translator`、`Int`、`KSampler`、`CLIPLoader`、`EmptyLatentImage`、`LayerUtility: LoadJoyCaptionBeta1Model`、`GenerateNoise`、`LGNoiseInjectionLatent`、`ConditioningZeroOut`、`LoadImage`、`CR Text`、`VAELoader`、`VAEDecode`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`UNETLoader`、`CLIPTextEncode`、`KSamplerAdvanced`、`EmptySD3LatentImage`、`TTResolutionSelector`、`ImageScaleBy`、`SeedVR2VideoUpscaler`、`ImageCASharpening+`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`easy cleanGpuUsed`、`easy int`、`PathchSageAttentionKJ`、`CheckpointLoaderSimple`、`QwenImageEngineer`、`ClipLoaderGGUF`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader
