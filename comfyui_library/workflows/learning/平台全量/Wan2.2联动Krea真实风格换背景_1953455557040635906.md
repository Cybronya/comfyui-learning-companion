---
key: 平台全量/Wan2.2联动Krea真实风格换背景_1953455557040635906.json
name: Wan2.2联动Krea真实风格换背景_1953455557040635906
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2联动Krea真实风格换背景_1953455557040635906.json
hash: 0ca9f0d07c54956c
coverage: 0.638889
learned_at: 2026-11-14 01:06:22
nodes: [Note, PreviewImage, ImageResize+, GetNode, SetNode, RMBG, SetNode, SetNode, Note, ShowText|pysssss, KepStringLiteral, KepStringLiteral, GLM_Vision_ImageToPrompt, RH_Translator, ShowText|pysssss, Anything Everywhere3, RH_Translator, RH_LLMAPI_NODE, Checkpoint Loader (Simple), GetNode, LayerMask: MaskGrow, GetNode, BrushNet, GetNode, CLIPTextEncode, PreviewImage, BrushNetLoader, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageConcanateOfUtils, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, WanVideoNAG, ShowText|pysssss, LoraLoaderModelOnly, RH_Translator, TeaCache, LoraLoaderModelOnly, LoraLoaderModelOnly, WanVideoNAG, Anything Everywhere3, ModelSamplingSD3, CLIPLoader, VAELoader, UnetLoaderGGUF, CLIPTextEncode, CLIPTextEncode, InpaintModelConditioning, Image Comparer (rgthree), Note, LoadImage, UpscaleModelLoader, Image Tiled, KSampler (Efficient), SetNode, LayerUtility: PurgeVRAM, PreviewImage, LBMSampler, LoadLBMModel, VAELoader, Anything Everywhere3, LoraLoaderModelOnly, LoadImage, Image Comparer (rgthree), KepStringLiteral, GLM_Text_Chat, Text Concatenate, SetNode, ShowText|pysssss, RH_Translator, ShowText|pysssss, CR Text, UnetLoaderGGUF, GetNode, UnetLoaderGGUF, DualCLIPLoader, VAELoader, PathchSageAttentionKJ, Anything Everywhere3, ConditioningZeroOut, LayerMask: MaskStroke, RMBG, MaskPreview+, InpaintModelConditioning, Image Comparer (rgthree), PreviewImage, Note, CLIPLoader, VAELoader, Anything Everywhere3, GetNode, CLIPTextEncode, CLIPTextEncode, Prompts Everywhere, LoadImage, GetNode, SetLatentNoiseMask, LayerUtility: PurgeVRAM, easy seed, PreviewImage, Image Comparer (rgthree), SetNode, LayerMask: MaskGrow, VAEEncode, GetNode, LayerUtility: PurgeVRAM, Note, SetNode, LayerUtility: PurgeVRAM, DualCLIPLoader, UNETLoader, CR Text, CR Text, ShowText|pysssss, Text Concatenate, ShowText|pysssss, RH_Translator, CLIPTextEncode, ConditioningZeroOut, ReferenceLatent, FluxGuidance, FluxKontextImageScale, VAEEncode, SetNode, LayerUtility: PurgeVRAM, easy imageDetailTransfer, LoadImage, Note, GetNode, FluxGuidance, KSampler (Efficient), CLIPTextEncode, Note, CLIPTextEncode, ShowText|pysssss, ShowText|pysssss, GetNode, ShowText|pysssss, ShowText|pysssss, Note, GetNode, LazySwitch1way, SetNode, RMBG, PreviewImage, ImageFromBatch, ImageFromBatch, ImageConcanateOfUtils, LayerUtility: PurgeVRAM, SetNode, Image Comparer (rgthree), LayerColor: AutoAdjustV2, PreviewImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, ImageConcanateOfUtils, ImageUpscaleWithModel, HYPIRImageRestoration, UpscaleModelLoader, ImageUpscaleWithModel, Fast Groups Bypasser (rgthree), LoadImage, String, PreviewImage, PreviewImage, LoadImage, SetNode, Note, KSampler (Efficient), KSampler (Efficient), KSampler (Efficient), GetNode, KSampler (Efficient), SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 938744373356632, "steps": 25}
---

# 平台全量/Wan2.2联动Krea真实风格换背景_1953455557040635906.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2联动Krea真实风格换背景_1953455557040635906.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Process → Output → Other

**节点**（180 个）：
- `Note`
- `PreviewImage`
- `ImageResize+`
- `GetNode`
- `SetNode`
- `RMBG`
- `SetNode`
- `SetNode`
- `Note`
- `ShowText|pysssss`
- `KepStringLiteral`
- `KepStringLiteral`
- `GLM_Vision_ImageToPrompt`
- `RH_Translator`
- `ShowText|pysssss`
- `Anything Everywhere3`
- `RH_Translator`
- `RH_LLMAPI_NODE`
- `Checkpoint Loader (Simple)`
- `GetNode`
- `LayerMask: MaskGrow`
- `GetNode`
- `BrushNet`
- `GetNode`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `BrushNetLoader`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageConcanateOfUtils`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `WanVideoNAG`
- `ShowText|pysssss`
- `LoraLoaderModelOnly` ★核心
- `RH_Translator`
- `TeaCache`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanVideoNAG`
- `Anything Everywhere3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `InpaintModelConditioning`
- `Image Comparer (rgthree)`
- `Note`
- `LoadImage`
- `UpscaleModelLoader`
- `Image Tiled`
- `KSampler (Efficient)` ★核心
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `LBMSampler` ★核心
- `LoadLBMModel`
- `VAELoader`
- `Anything Everywhere3`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `Image Comparer (rgthree)`
- `KepStringLiteral`
- `GLM_Text_Chat`
- `Text Concatenate`
- `SetNode`
- `ShowText|pysssss`
- `RH_Translator`
- `ShowText|pysssss`
- `CR Text`
- `UnetLoaderGGUF` ★核心
- `GetNode`
- `UnetLoaderGGUF` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `PathchSageAttentionKJ`
- `Anything Everywhere3`
- `ConditioningZeroOut`
- `LayerMask: MaskStroke`
- `RMBG`
- `MaskPreview+`
- `InpaintModelConditioning`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `Note`
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Prompts Everywhere`
- `LoadImage`
- `GetNode`
- `SetLatentNoiseMask`
- `LayerUtility: PurgeVRAM`
- `easy seed`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SetNode`
- `LayerMask: MaskGrow`
- `VAEEncode` ★核心
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `Note`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `CR Text`
- `CR Text`
- `ShowText|pysssss`
- `Text Concatenate`
- `ShowText|pysssss`
- `RH_Translator`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `FluxGuidance`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `easy imageDetailTransfer`
- `LoadImage`
- `Note`
- `GetNode`
- `FluxGuidance`
- `KSampler (Efficient)` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `ShowText|pysssss`
- `GetNode`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `Note`
- `GetNode`
- `LazySwitch1way`
- `SetNode`
- `RMBG`
- `PreviewImage`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageConcanateOfUtils`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `Image Comparer (rgthree)`
- `LayerColor: AutoAdjustV2`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `ImageConcanateOfUtils`
- `ImageUpscaleWithModel`
- `HYPIRImageRestoration`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `String`
- `PreviewImage`
- `PreviewImage`
- `LoadImage`
- `SetNode`
- `Note`
- `KSampler (Efficient)` ★核心
- `KSampler (Efficient)` ★核心
- `KSampler (Efficient)` ★核心
- `GetNode`
- `KSampler (Efficient)` ★核心
- `SaveImage`

## 关键参数

- `seed` = `938744373356632`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **64%**（115/180）

**有卡**：`ImageResize+`、`RMBG`、`KepStringLiteral`、`GLM_Vision_ImageToPrompt`、`RH_Translator`、`RH_LLMAPI_NODE`、`Checkpoint Loader (Simple)`、`LayerMask: MaskGrow`、`BrushNet`、`CLIPTextEncode`、`BrushNetLoader`、`ImageFromBatch`、`ImageConcanateOfUtils`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`WanVideoNAG`、`TeaCache`、`CLIPLoader`、`VAELoader`、`UnetLoaderGGUF`、`InpaintModelConditioning`、`LoadImage`、`UpscaleModelLoader`、`Image Tiled`、`KSampler (Efficient)`、`LayerUtility: PurgeVRAM`、`LBMSampler`、`LoadLBMModel`、`GLM_Text_Chat`、`Text Concatenate`、`CR Text`、`DualCLIPLoader`、`ConditioningZeroOut`、`LayerMask: MaskStroke`、`MaskPreview+`、`Prompts Everywhere`、`SetLatentNoiseMask`、`easy seed`、`VAEEncode`、`UNETLoader`、`ReferenceLatent`、`FluxGuidance`、`FluxKontextImageScale`、`easy imageDetailTransfer`、`LazySwitch1way`、`LayerColor: AutoAdjustV2`、`ImageUpscaleWithModel`、`HYPIRImageRestoration`、`String`、`SaveImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、easy seed
