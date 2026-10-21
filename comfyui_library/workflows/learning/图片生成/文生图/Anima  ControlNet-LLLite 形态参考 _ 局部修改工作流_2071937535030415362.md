---
key: 图片生成/文生图/Anima  ControlNet-LLLite 形态参考 _ 局部修改工作流_2071937535030415362.json
name: Anima  ControlNet-LLLite 形态参考 _ 局部修改工作流_2071937535030415362
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima  ControlNet-LLLite 形态参考 _ 局部修改工作流_2071937535030415362.json
hash: c71150cb810b05fb
coverage: 0.836538
learned_at: 2026-10-19 23:40:50
nodes: [CLIPLoader, CR Image Input Switch, AIO_Preprocessor, KSamplerAdvanced, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, AIO_Preprocessor, Mask Fill Holes, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, LoadImage, EmptyLatentImage, Int, Int, CLIPTextEncode, ImpactSEGSLabelAssign, WildcardPromptFromString, CLIPTextEncode, llama_cpp_instruct_adv, StringListToString, PreviewImage, PreviewImage, SaveImage, VAELoader, SAMLoader, ImpactMakeTileSEGS, MediaPipeFaceMeshDetectorProvider //Inspire, UltralyticsDetectorProvider, UpscaleModelLoader, SEGSPreview, PreviewImage, MaskPreview+, llama_cpp_parameters, llama_cpp_model_loader, ShowText|pysssss, ShowText|pysssss, MathExpression|pysssss, SaveImage, UNETLoader, CLIPLoader, FaceDetailer, LoraLoaderModelOnly, CR Seed, ImageUpscaleWithModel, easy float, LoadImage, LoadImage, MarkdownNote, PixaromaLabel, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveImage, easy seed, Int, UNETLoader, CLIPLoader, LoraLoaderModelOnly, AnimaLLLiteApply, InpaintModelConditioning, CLIPTextEncode, KSampler, VAELoader, VAEDecode, VAEDecode, KSampler, PreviewImage, KSamplerAdvanced, VAELoader, easy seed, LoadImage, RH_Translator, PreviewImage, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, CR Text Concatenate, AnimaLLLiteApply, CR Text, MathExpression|pysssss, CLIPTextEncode, Fast Groups Bypasser (rgthree), ImageScaleBy, Image Comparer (rgthree), DetailerForEach, Image Comparer (rgthree), ResolutionMaster, CLIPTextEncode, PreviewImage, PreviewImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, VAEDecode, PixaromaLabel, ShowText|pysssss, RHHiddenNodes, CR Text, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, Fast Groups Bypasser (rgthree)]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 40, "denoise": "simple", "height": 1536, "sampler_name": 4.5, "scheduler": "er_sde", "seed": "enable", "steps": "randomize", "width": 1024}
---

# 图片生成/文生图/Anima  ControlNet-LLLite 形态参考 _ 局部修改工作流_2071937535030415362.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima  ControlNet-LLLite 形态参考 _ 局部修改工作流_2071937535030415362.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（104 个）：
- `CLIPLoader`
- `CR Image Input Switch`
- `AIO_Preprocessor`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AIO_Preprocessor`
- `Mask Fill Holes`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `EmptyLatentImage` ★核心
- `Int`
- `Int`
- `CLIPTextEncode` ★核心
- `ImpactSEGSLabelAssign`
- `WildcardPromptFromString`
- `CLIPTextEncode` ★核心
- `llama_cpp_instruct_adv`
- `StringListToString`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `VAELoader`
- `SAMLoader`
- `ImpactMakeTileSEGS`
- `MediaPipeFaceMeshDetectorProvider //Inspire`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `SEGSPreview`
- `PreviewImage`
- `MaskPreview+`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `MathExpression|pysssss`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `FaceDetailer`
- `LoraLoaderModelOnly` ★核心
- `CR Seed`
- `ImageUpscaleWithModel`
- `easy float`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `PixaromaLabel`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `easy seed`
- `Int`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `AnimaLLLiteApply`
- `InpaintModelConditioning`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `easy seed`
- `LoadImage`
- `RH_Translator`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Text Concatenate`
- `AnimaLLLiteApply`
- `CR Text`
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `ImageScaleBy`
- `Image Comparer (rgthree)`
- `DetailerForEach`
- `Image Comparer (rgthree)`
- `ResolutionMaster`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `VAEDecode` ★核心
- `PixaromaLabel`
- `ShowText|pysssss`
- `RHHiddenNodes`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `40`
- `sampler_name` = `4.5`
- `scheduler` = `er_sde`
- `denoise` = `simple`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（87/104）

**有卡**：`CLIPLoader`、`CR Image Input Switch`、`AIO_Preprocessor`、`KSamplerAdvanced`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`Mask Fill Holes`、`CLIPTextEncode`、`LoadImage`、`EmptyLatentImage`、`Int`、`ImpactSEGSLabelAssign`、`WildcardPromptFromString`、`llama_cpp_instruct_adv`、`StringListToString`、`SaveImage`、`VAELoader`、`SAMLoader`、`ImpactMakeTileSEGS`、`MediaPipeFaceMeshDetectorProvider //Inspire`、`UltralyticsDetectorProvider`、`UpscaleModelLoader`、`SEGSPreview`、`MaskPreview+`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`MathExpression|pysssss`、`UNETLoader`、`FaceDetailer`、`LoraLoaderModelOnly`、`CR Seed`、`ImageUpscaleWithModel`、`easy float`、`PixaromaLabel`、`easy seed`、`AnimaLLLiteApply`、`InpaintModelConditioning`、`KSampler`、`RH_Translator`、`CR Text Concatenate`、`CR Text`、`ImageScaleBy`、`DetailerForEach`、`ResolutionMaster`、`RHHiddenNodes`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage
