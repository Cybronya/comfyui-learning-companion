---
key: 图片生成/图生图/多张生成  flux2_klein + 3.5 千问vl_2063287117773623297.json
name: 多张生成  flux2_klein + 3.5 千问vl_2063287117773623297
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/多张生成  flux2_klein + 3.5 千问vl_2063287117773623297.json
hash: 7634f3ee0b897a67
coverage: 0.774194
learned_at: 2026-10-23 12:45:23
nodes: [GH_MaskGrowthBlur, ReferenceLatent, ReferenceLatent, Anything Everywhere3, TextInput_, TextInput_, TextInput_, TextInput_, GuHaiMaskDetect, TextInput_, Fast Groups Bypasser (rgthree), LoadImage, Note, Reroute, Reroute, PreviewImage, CR Overlay Transparent Image, GetImageSize, ImpactConditionalBranch, ImpactConditionalBranch, VAEEncode, VAEEncode, 孤海-自定义颜色, Compare, 图像缩放V2_孤海, TextInput_, TextInput_, 图像缩放V2_孤海, Reroute, LayerUtility: TextBox, TextInput_, LayerUtility: TextBox, easy setNode, easy setNode, easy setNode, easy getNode, easy getNode, Reroute, LayerUtility: TextBox, LayerUtility: TextJoin, llama_cpp_parameters, LoadImage, ReferenceLatent, ReferenceLatent, VAEEncode, ReferenceLatent, ReferenceLatent, LayerUtility: TextBox, LayerUtility: ImageReelComposit, LayerUtility: ImageReel, LayerUtility: TextBox, VAEDecode, LayerUtility: TextBox, Fast Groups Bypasser (rgthree), CR Text, CR Text, easy getNode, TextInput_, TextInput_, 图像缩放V2_孤海, 图像缩放V2_孤海, LayerUtility: TextBox, llama_cpp_model_loader, llama_cpp_instruct_adv, PreviewImage, easy cleanGpuUsed, LayerUtility: TextBox, LayerUtility: TextBox, LoadImage, LayerUtility: TextBox, PreviewImage, LayerUtility: TextBox, LayerUtility: TextBox, LayerUtility: TextBox, easy seed, LayerUtility: TextBox, Reroute, easy getNode, CR Text, GetImageSize, 图像缩放V2_孤海, InpaintModelConditioning, CLIPLoader, VAELoader, SaveImage, Display Any (rgthree), Note, CR Overlay Transparent Image, GetNode, easy forLoopStart, easy mathInt, easy forLoopEnd, SetNode, easy batchAnything, GetNode, CLIPTextEncode, LayerUtility: TextBox, SetNode, LoraLoaderModelOnly, LayerUtility: ImageReelComposit, LayerUtility: ImageReel, SaveImage, CLIPTextEncode, KSampler, UNETLoader, ShowText|pysssss, LayerUtility: TextBox, ImpactSwitch, Fast Groups Bypasser (rgthree), GetNode, ImageConcatFromBatch, Reroute, PreviewImage, PreviewImage, PreviewImage, Image Comparer (rgthree), AIO_Preprocessor, SeedGenerator, LayerUtility: TextBox, INTConstant, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), LayerUtility: TextBox]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 391475039329312, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/多张生成  flux2_klein + 3.5 千问vl_2063287117773623297.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/多张生成  flux2_klein + 3.5 千问vl_2063287117773623297.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（124 个）：
- `GH_MaskGrowthBlur`
- `ReferenceLatent`
- `ReferenceLatent`
- `Anything Everywhere3`
- `TextInput_`
- `TextInput_`
- `TextInput_`
- `TextInput_`
- `GuHaiMaskDetect`
- `TextInput_`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `Note`
- `Reroute`
- `Reroute`
- `PreviewImage`
- `CR Overlay Transparent Image`
- `GetImageSize`
- `ImpactConditionalBranch`
- `ImpactConditionalBranch`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `孤海-自定义颜色`
- `Compare`
- `图像缩放V2_孤海`
- `TextInput_`
- `TextInput_`
- `图像缩放V2_孤海`
- `Reroute`
- `LayerUtility: TextBox`
- `TextInput_`
- `LayerUtility: TextBox`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `Reroute`
- `LayerUtility: TextBox`
- `LayerUtility: TextJoin`
- `llama_cpp_parameters`
- `LoadImage`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `LayerUtility: TextBox`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReel`
- `LayerUtility: TextBox`
- `VAEDecode` ★核心
- `LayerUtility: TextBox`
- `Fast Groups Bypasser (rgthree)`
- `CR Text`
- `CR Text`
- `easy getNode`
- `TextInput_`
- `TextInput_`
- `图像缩放V2_孤海`
- `图像缩放V2_孤海`
- `LayerUtility: TextBox`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `PreviewImage`
- `easy cleanGpuUsed`
- `LayerUtility: TextBox`
- `LayerUtility: TextBox`
- `LoadImage`
- `LayerUtility: TextBox`
- `PreviewImage`
- `LayerUtility: TextBox`
- `LayerUtility: TextBox`
- `LayerUtility: TextBox`
- `easy seed`
- `LayerUtility: TextBox`
- `Reroute`
- `easy getNode`
- `CR Text`
- `GetImageSize`
- `图像缩放V2_孤海`
- `InpaintModelConditioning`
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `Display Any (rgthree)`
- `Note`
- `CR Overlay Transparent Image`
- `GetNode`
- `easy forLoopStart`
- `easy mathInt`
- `easy forLoopEnd`
- `SetNode`
- `easy batchAnything`
- `GetNode`
- `CLIPTextEncode` ★核心
- `LayerUtility: TextBox`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReel`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `ShowText|pysssss`
- `LayerUtility: TextBox`
- `ImpactSwitch`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `ImageConcatFromBatch`
- `Reroute`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `AIO_Preprocessor`
- `SeedGenerator`
- `LayerUtility: TextBox`
- `INTConstant`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: TextBox`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `391475039329312`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（96/124）

**有卡**：`GH_MaskGrowthBlur`、`ReferenceLatent`、`TextInput_`、`GuHaiMaskDetect`、`LoadImage`、`CR Overlay Transparent Image`、`GetImageSize`、`ImpactConditionalBranch`、`VAEEncode`、`孤海-自定义颜色`、`Compare`、`图像缩放V2_孤海`、`LayerUtility: TextBox`、`easy setNode`、`easy getNode`、`LayerUtility: TextJoin`、`llama_cpp_parameters`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`VAEDecode`、`CR Text`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`easy cleanGpuUsed`、`easy seed`、`InpaintModelConditioning`、`CLIPLoader`、`VAELoader`、`SaveImage`、`Display Any (rgthree)`、`easy forLoopStart`、`easy mathInt`、`easy forLoopEnd`、`easy batchAnything`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`KSampler`、`UNETLoader`、`ImageConcatFromBatch`、`AIO_Preprocessor`、`SeedGenerator`、`INTConstant`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
