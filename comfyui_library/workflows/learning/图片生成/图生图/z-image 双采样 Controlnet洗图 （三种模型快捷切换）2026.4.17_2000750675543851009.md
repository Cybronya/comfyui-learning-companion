---
key: 图片生成/图生图/z-image 双采样 Controlnet洗图 （三种模型快捷切换）2026.4.17_2000750675543851009.json
name: z-image 双采样 Controlnet洗图 （三种模型快捷切换）2026.4.17_2000750675543851009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/z-image 双采样 Controlnet洗图 （三种模型快捷切换）2026.4.17_2000750675543851009.json
hash: 827fc62fa2c81178
coverage: 0.660377
learned_at: 2026-10-23 11:46:33
nodes: [ShowText|pysssss, Qwen3_VQA, Note, ImpactSwitch, easy int, LoadImage, easy int, AIO_Preprocessor, LayerUtility: ImageReelComposit, LayerUtility: ImageReel, SeedVR2LoadVAEModel, Note, CLIPTextEncode, ConditioningZeroOut, LayerUtility: PurgeVRAM V2, PlaySound|pysssss, PreviewImage, PreviewImage, PreviewImage, AIO_Preprocessor, DWPreprocessor, Note, Note, Note, Note, Image Comparer (rgthree), UNETLoader, CLIPLoader, VAELoader, QwenImageDiffsynthControlnet, CheckpointLoaderSimple, Note, Note, KSamplerAdvanced, INTConstant, ModelPatchLoader, Fast Groups Bypasser (rgthree), SaveImage, KSamplerAdvanced, LoraLoaderModelOnly, PreviewImage, CR Aspect Ratio, ImageScaleToTotalPixels, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), PreviewImage, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, VAEDecode, LoadImage, LoadImage, LoadImage, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 14, "checkpoint": "redcraftRedzimageUpdatedDEC03_redzimage15AIO.safetensors", "denoise": "sgm_uniform", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/z-image 双采样 Controlnet洗图 （三种模型快捷切换）2026.4.17_2000750675543851009.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/z-image 双采样 Controlnet洗图 （三种模型快捷切换）2026.4.17_2000750675543851009.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `ShowText|pysssss`
- `Qwen3_VQA`
- `Note`
- `ImpactSwitch`
- `easy int`
- `LoadImage`
- `easy int`
- `AIO_Preprocessor`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReel`
- `SeedVR2LoadVAEModel`
- `Note`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `LayerUtility: PurgeVRAM V2`
- `PlaySound|pysssss`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `AIO_Preprocessor`
- `DWPreprocessor`
- `Note`
- `Note`
- `Note`
- `Note`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImageDiffsynthControlnet`
- `CheckpointLoaderSimple` ★核心
- `Note`
- `Note`
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `ModelPatchLoader`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `CR Aspect Ratio`
- `ImageScaleToTotalPixels`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImage`

## 关键参数

- `checkpoint` = `redcraftRedzimageUpdatedDEC03_redzimage15AIO.safetensors`
- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `14`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `sgm_uniform`

## 知识

覆盖率 **66%**（35/53）

**有卡**：`Qwen3_VQA`、`easy int`、`LoadImage`、`AIO_Preprocessor`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`SeedVR2LoadVAEModel`、`CLIPTextEncode`、`ConditioningZeroOut`、`LayerUtility: PurgeVRAM V2`、`PlaySound|pysssss`、`DWPreprocessor`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImageDiffsynthControlnet`、`CheckpointLoaderSimple`、`KSamplerAdvanced`、`INTConstant`、`ModelPatchLoader`、`SaveImage`、`LoraLoaderModelOnly`、`CR Aspect Ratio`、`ImageScaleToTotalPixels`、`LayerUtility: ImageScaleByAspectRatio V2`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
