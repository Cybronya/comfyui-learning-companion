---
key: 平台全量/QwenEditRemix-AIO2.0超强合集_2038973183948230657.json
name: QwenEditRemix-AIO2.0超强合集_2038973183948230657
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/QwenEditRemix-AIO2.0超强合集_2038973183948230657.json
hash: cb6f8bdc27819303
coverage: 0.773585
learned_at: 2026-11-14 00:53:14
nodes: [Fast Groups Bypasser (rgthree), LoadImage, ConditioningZeroOut, KSampler, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, ConditioningZeroOut, KSampler, PreviewImage, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, GrowMask, KSampler, Image Comparer (rgthree), ConditioningZeroOut, DrawMaskOnImage, PreviewImage, Mask Fill Holes, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, SDPoseOODLoader, PreviewImage, KSampler, ConditioningZeroOut, TextEncodeQwenImageEditPlusAdvance_lrzjason, ConditioningZeroOut, Image Comparer (rgthree), VAEDecode, VAEDecode, easy setNode, VAEDecode, easy setNode, VAEDecode, easy setNode, VAEDecode, easy setNode, easy getNode, easy getNode, easy getNode, easy getNode, SaveImage, SaveImage, SaveImage, SaveImage, ImagePadForOutpaint, TextEncodeQwenImageEditPlusAdvance_lrzjason, easy promptLine, SDPoseOODProcessor, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImageEditPlusAdvance_lrzjason, Any Switch (rgthree), SaveImage, KSampler, ConditioningZeroOut, CLIPTextEncode, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, EmptyLatentImage, Anything Everywhere3, SeedVR2VideoUpscaler, Reroute, SeedVR2LoadDiTModel, Reroute, SeedVR2LoadVAEModel, easy getNode, easy setNode, SaveImage, KSampler, VAEDecode, easy setNode, llama_cpp_parameters, LayerUtility: ImageScaleByAspectRatio V2, PurgeVRAM_UTK, PurgeVRAM_UTK, ProcessString, Any Switch (rgthree), easy getNode, CheckpointLoaderSimple, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, CR Text, easy showAnything, SaveImage, easy showAnything, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), TextEncodeQwenImageEditPlusAdvance_lrzjason, llama_cpp_model_loader, llama_cpp_instruct_adv]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "Qwen-Image-Edit-Remix-AIO-v2.0.safetensors", "denoise": 1, "height": 1536, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 635105918165865, "steps": 4, "width": 864}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/QwenEditRemix-AIO2.0超强合集_2038973183948230657.json

> 来源文件 `comfyui_library/workflows/平台全量/QwenEditRemix-AIO2.0超强合集_2038973183948230657.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（106 个）：
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GrowMask`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `ConditioningZeroOut`
- `DrawMaskOnImage`
- `PreviewImage`
- `Mask Fill Holes`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SDPoseOODLoader`
- `PreviewImage`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `easy setNode`
- `VAEDecode` ★核心
- `easy setNode`
- `VAEDecode` ★核心
- `easy setNode`
- `VAEDecode` ★核心
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `ImagePadForOutpaint`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `easy promptLine`
- `SDPoseOODProcessor`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `Any Switch (rgthree)`
- `SaveImage`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `EmptyLatentImage` ★核心
- `Anything Everywhere3`
- `SeedVR2VideoUpscaler`
- `Reroute`
- `SeedVR2LoadDiTModel`
- `Reroute`
- `SeedVR2LoadVAEModel`
- `easy getNode`
- `easy setNode`
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy setNode`
- `llama_cpp_parameters`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PurgeVRAM_UTK`
- `PurgeVRAM_UTK`
- `ProcessString`
- `Any Switch (rgthree)`
- `easy getNode`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `CR Text`
- `easy showAnything`
- `SaveImage`
- `easy showAnything`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `635105918165865`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `864`
- `height` = `1536`
- `batch_size` = `1`
- `checkpoint` = `Qwen-Image-Edit-Remix-AIO-v2.0.safetensors`

## 知识

覆盖率 **77%**（82/106）

**有卡**：`LoadImage`、`ConditioningZeroOut`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`GrowMask`、`DrawMaskOnImage`、`Mask Fill Holes`、`SDPoseOODLoader`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`VAEDecode`、`easy setNode`、`easy getNode`、`SaveImage`、`ImagePadForOutpaint`、`easy promptLine`、`SDPoseOODProcessor`、`CLIPTextEncode`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`EmptyLatentImage`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`PurgeVRAM_UTK`、`ProcessString`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`CR Text`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage

## 参数体检

发现 6 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
