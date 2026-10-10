---
key: 视频生成/文生视频/声色俱全！LTX2.3-图生视频-匹配原图比例-高质量音视频！自定义Lora_2031651024238288898.json
name: 声色俱全！LTX2.3-图生视频-匹配原图比例-高质量音视频！自定义Lora_2031651024238288898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/声色俱全！LTX2.3-图生视频-匹配原图比例-高质量音视频！自定义Lora_2031651024238288898.json
hash: 6411e87dab5ee691
coverage: 0.854839
learned_at: 2026-10-11 03:16:52
nodes: [CFGGuider, RandomNoise, ManualSigmas, llama_cpp_instruct_adv, LTXVConcatAVLatent, KSamplerSelect, LTXVImgToVideoInplace, LTXVSeparateAVLatent, SamplerCustomAdvanced, ManualSigmas, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVCropGuides, LTXVLatentUpsampler, LoraLoaderModelOnly, LTXVScheduler, KSamplerSelect, SamplerCustomAdvanced, RandomNoise, CFGGuider, GetNode, llama_cpp_model_loader, CM_IntToFloat, SetNode, LTXVImgToVideoInplace, EmptyLTXVLatentVideo, UNETLoader, ManualSigmas, PathchSageAttentionKJ, ModelPatchTorchSettings, DualCLIPLoader, LatentUpscaleModelLoader, Anything Everywhere3, VAELoaderKJ, VAELoaderKJ, LTXVEmptyLatentAudio, INTConstant, CLIPTextEncode, LTXVConditioning, CLIPTextEncode, GetNode, LTXVPreprocess, ImageScaleBy, ImageScale, LTXVChunkFeedForward, INTConstant, ResizeImagesByLongerEdge, SimpleCalculatorKJ, CR Text, LayerUtility: ImageScaleByAspectRatio V2, GetImageSize, GetNode, SaveImage, TT_img_enc, VHS_VideoCombine, VAEDecodeTiled, LTXVAudioVAEDecode, ShowText|pysssss, LoraLoaderModelOnly, INTConstant, CR Text, LoadImage]
patterns: []
missing: [CR Text, CR Text, LayerUtility: ImageScaleByAspectRatio V2]
parameters: {"batch_size": 1, "height": 24, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/声色俱全！LTX2.3-图生视频-匹配原图比例-高质量音视频！自定义Lora_2031651024238288898.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/声色俱全！LTX2.3-图生视频-匹配原图比例-高质量音视频！自定义Lora_2031651024238288898.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `CFGGuider`
- `RandomNoise`
- `ManualSigmas`
- `llama_cpp_instruct_adv`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CFGGuider`
- `GetNode`
- `llama_cpp_model_loader`
- `CM_IntToFloat`
- `SetNode`
- `LTXVImgToVideoInplace`
- `EmptyLTXVLatentVideo`
- `UNETLoader` ★核心
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `Anything Everywhere3`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LTXVEmptyLatentAudio` ★核心
- `INTConstant`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `GetNode`
- `LTXVPreprocess`
- `ImageScaleBy`
- `ImageScale`
- `LTXVChunkFeedForward`
- `INTConstant`
- `ResizeImagesByLongerEdge`
- `SimpleCalculatorKJ`
- `CR Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSize`
- `GetNode`
- `SaveImage`
- `TT_img_enc`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `ShowText|pysssss`
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `CR Text`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（53/62）

**有卡**：`CFGGuider`、`RandomNoise`、`ManualSigmas`、`llama_cpp_instruct_adv`、`LTXVConcatAVLatent`、`KSamplerSelect`、`LTXVImgToVideoInplace`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LoraLoaderModelOnly`、`LTXVScheduler`、`llama_cpp_model_loader`、`CM_IntToFloat`、`EmptyLTXVLatentVideo`、`UNETLoader`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`LTXVEmptyLatentAudio`、`INTConstant`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVPreprocess`、`ImageScaleBy`、`ImageScale`、`LTXVChunkFeedForward`、`ResizeImagesByLongerEdge`、`SimpleCalculatorKJ`、`GetImageSize`、`SaveImage`、`TT_img_enc`、`VHS_VideoCombine`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LoadImage`

**缺卡**（3）：`CR Text`、`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
