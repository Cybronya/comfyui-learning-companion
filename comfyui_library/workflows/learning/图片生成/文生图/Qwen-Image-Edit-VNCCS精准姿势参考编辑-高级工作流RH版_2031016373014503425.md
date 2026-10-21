---
key: 图片生成/文生图/Qwen-Image-Edit-VNCCS精准姿势参考编辑-高级工作流RH版_2031016373014503425.json
name: Qwen-Image-Edit-VNCCS精准姿势参考编辑-高级工作流RH版_2031016373014503425
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-Edit-VNCCS精准姿势参考编辑-高级工作流RH版_2031016373014503425.json
hash: 07257606825d4f84
coverage: 0.597403
learned_at: 2026-10-19 22:45:38
nodes: [GetNode, GetNode, PreviewImage, SetNode, TextEncodeQwenImageEditPlus, GetNode, GetNode, TextEncodeQwenImageEditPlus, Note, VAEEncode, DWPreprocessor, Fast Groups Bypasser (rgthree), Note, PreviewImage, ShowText|pysssss, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, Any Switch (rgthree), SetNode, LoraLoaderModelOnly, VNCCS_PoseStudio, VAELoader, SetNode, Any Switch (rgthree), LoaderGGUF, UNETLoader, CLIPLoader, GetNode, CFGNorm, Any Switch (rgthree), Any Switch (rgthree), SetNode, Fast Groups Bypasser (rgthree), Any Switch (rgthree), GetNode, Fast Groups Bypasser (rgthree), CLIPLoader, SetNode, VAELoader, GetNode, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, SaveImage, VAEEncode, JjkConcat, ShowText|pysssss, KSampler, AILab_QwenVL, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, Note, ImageScaleToTotalPixels, DWPreprocessor, ModelSamplingAuraFlow, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, GetNode, Note, VAEDecode, VAEDecode, SaveImage, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, LatentUpscaleBy, ImageScaleBy, KSampler, KSampler, SaveImage, LoadImage, LoadImage, Textbox, Textbox]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.4000000000000001, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 649596066901899, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen-Image-Edit-VNCCS精准姿势参考编辑-高级工作流RH版_2031016373014503425.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-Edit-VNCCS精准姿势参考编辑-高级工作流RH版_2031016373014503425.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（77 个）：
- `GetNode`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImageEditPlus`
- `Note`
- `VAEEncode` ★核心
- `DWPreprocessor`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `PreviewImage`
- `ShowText|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `Any Switch (rgthree)`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `VNCCS_PoseStudio`
- `VAELoader`
- `SetNode`
- `Any Switch (rgthree)`
- `LoaderGGUF`
- `UNETLoader` ★核心
- `CLIPLoader`
- `GetNode`
- `CFGNorm`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `Any Switch (rgthree)`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `VAEEncode` ★核心
- `JjkConcat`
- `ShowText|pysssss`
- `KSampler` ★核心
- `AILab_QwenVL`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `Note`
- `ImageScaleToTotalPixels`
- `DWPreprocessor`
- `ModelSamplingAuraFlow`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `GetNode`
- `Note`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `LatentUpscaleBy`
- `ImageScaleBy`
- `KSampler` ★核心
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `Textbox`
- `Textbox`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `649596066901899`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `0.4000000000000001`

## 知识

覆盖率 **60%**（46/77）

**有卡**：`TextEncodeQwenImageEditPlus`、`VAEEncode`、`DWPreprocessor`、`LoraLoaderModelOnly`、`VNCCS_PoseStudio`、`VAELoader`、`LoaderGGUF`、`UNETLoader`、`CLIPLoader`、`CFGNorm`、`CLIPTextEncode`、`SaveImage`、`JjkConcat`、`KSampler`、`AILab_QwenVL`、`ImageScaleToTotalPixels`、`ModelSamplingAuraFlow`、`FluxKontextMultiReferenceLatentMethod`、`VAEDecode`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`LatentUpscaleBy`、`ImageScaleBy`、`LoadImage`、`Textbox`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
