---
key: 图片生成/图生图/k2深度自由迁移带n离线版v1.2_2094976530387652610.json
name: k2深度自由迁移带n离线版v1.2_2094976530387652610
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/k2深度自由迁移带n离线版v1.2_2094976530387652610.json
hash: 6795c10ed9a47a7c
coverage: 0.916667
learned_at: 2026-10-21 00:45:33
nodes: [PreviewAny, ComfyMathExpression, EmptyLatentImage, VAEDecode, INTConstant, VAEEncode, Krea2EditModelPatch, ConditioningZeroOut, FluxKontextMultiReferenceLatentMethod, Krea2EditGroundedEncode, CR Prompt Text, CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, CLIPTextEncode, ConditioningZeroOut, CLIPLoader, INTConstant, StringConcatenate, CR Prompt Text, CR Prompt Text, TextEncodeQwenImageEditPlus, ShowText|pysssss, StringConcatenate, RHLLMChatNode, RHLLMChatNode, ShowText|pysssss, StringConcatenate, ShowText|pysssss, RHLLMChatNode, UNETLoader, ModelPatchLoader, CR Prompt Text, ModelSamplingAuraFlow, UNETLoader, VAEEncode, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, VAELoader, CLIPLoader, LoraLoaderModelOnly, AIO_Preprocessor, SaveImage, QwenImageDiffsynthControlnet, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": "ddim_uniform", "height": 512, "sampler_name": 1, "scheduler": "ddim", "seed": "enable", "steps": "fixed", "width": 512}
---

# 图片生成/图生图/k2深度自由迁移带n离线版v1.2_2094976530387652610.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/k2深度自由迁移带n离线版v1.2_2094976530387652610.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `PreviewAny`
- `ComfyMathExpression`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `INTConstant`
- `VAEEncode` ★核心
- `Krea2EditModelPatch`
- `ConditioningZeroOut`
- `FluxKontextMultiReferenceLatentMethod`
- `Krea2EditGroundedEncode`
- `CR Prompt Text`
- `CR Prompt Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `CLIPLoader`
- `INTConstant`
- `StringConcatenate`
- `CR Prompt Text`
- `CR Prompt Text`
- `TextEncodeQwenImageEditPlus`
- `ShowText|pysssss`
- `StringConcatenate`
- `RHLLMChatNode`
- `RHLLMChatNode`
- `ShowText|pysssss`
- `StringConcatenate`
- `ShowText|pysssss`
- `RHLLMChatNode`
- `UNETLoader` ★核心
- `ModelPatchLoader`
- `CR Prompt Text`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `AIO_Preprocessor`
- `SaveImage`
- `QwenImageDiffsynthControlnet`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `ddim`
- `denoise` = `ddim_uniform`

## 知识

覆盖率 **92%**（44/48）

**有卡**：`ComfyMathExpression`、`EmptyLatentImage`、`VAEDecode`、`INTConstant`、`VAEEncode`、`Krea2EditModelPatch`、`ConditioningZeroOut`、`FluxKontextMultiReferenceLatentMethod`、`Krea2EditGroundedEncode`、`CR Prompt Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`CLIPTextEncode`、`CLIPLoader`、`StringConcatenate`、`TextEncodeQwenImageEditPlus`、`RHLLMChatNode`、`UNETLoader`、`ModelPatchLoader`、`ModelSamplingAuraFlow`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`AIO_Preprocessor`、`SaveImage`、`QwenImageDiffsynthControlnet`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
