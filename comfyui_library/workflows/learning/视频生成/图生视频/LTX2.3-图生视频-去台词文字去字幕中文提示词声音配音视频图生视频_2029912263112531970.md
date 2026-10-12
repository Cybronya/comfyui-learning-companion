---
key: 视频生成/图生视频/LTX2.3-图生视频-去台词文字去字幕中文提示词声音配音视频图生视频_2029912263112531970.json
name: LTX2.3-图生视频-去台词文字去字幕中文提示词声音配音视频图生视频_2029912263112531970
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-图生视频-去台词文字去字幕中文提示词声音配音视频图生视频_2029912263112531970.json
hash: e40640bcd62f1f81
coverage: 0.918367
learned_at: 2026-10-13 01:36:52
nodes: [CFGGuider, LTXVSeparateAVLatent, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVConcatAVLatent, ResizeImagesByLongerEdge, CFGGuider, LTXVScheduler, GetImageSize, CLIPTextEncode, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVCropGuides, VAEDecodeTiled, KSamplerSelect, PrimitiveInt, LTXVEmptyLatentAudio, RandomNoise, RandomNoise, KSamplerSelect, ManualSigmas, LTXVConditioning, ImageScaleBy, LTXVChunkFeedForward, PathchSageAttentionKJ, ModelPatchTorchSettings, ManualSigmas, ManualSigmas, VAELoaderKJ, DualCLIPLoader, VAELoaderKJ, LatentUpscaleModelLoader, LoraLoaderModelOnly, LTXVAudioVAEDecode, LTXVLatentUpsampler, LTXVImgToVideoInplace, ShowText|pysssss, CR Text, llama_cpp_instruct_adv, llama_cpp_model_loader, UNETLoader, CLIPTextEncode, LoadImage, CR Text, ImageScale, VHS_VideoCombine]
patterns: []
missing: [CR Text, CR Text]
parameters: {"batch_size": 1, "height": 24, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 视频生成/图生视频/LTX2.3-图生视频-去台词文字去字幕中文提示词声音配音视频图生视频_2029912263112531970.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3-图生视频-去台词文字去字幕中文提示词声音配音视频图生视频_2029912263112531970.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（49 个）：
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `ResizeImagesByLongerEdge`
- `CFGGuider`
- `LTXVScheduler`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `VAEDecodeTiled` ★核心
- `KSamplerSelect` ★核心
- `PrimitiveInt`
- `LTXVEmptyLatentAudio` ★核心
- `RandomNoise`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConditioning`
- `ImageScaleBy`
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ManualSigmas`
- `ManualSigmas`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `ShowText|pysssss`
- `CR Text`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CR Text`
- `ImageScale`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（45/49）

**有卡**：`CFGGuider`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`ResizeImagesByLongerEdge`、`LTXVScheduler`、`GetImageSize`、`CLIPTextEncode`、`LTXVCropGuides`、`VAEDecodeTiled`、`KSamplerSelect`、`LTXVEmptyLatentAudio`、`RandomNoise`、`ManualSigmas`、`LTXVConditioning`、`ImageScaleBy`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VAELoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`UNETLoader`、`LoadImage`、`ImageScale`、`VHS_VideoCombine`

**缺卡**（2）：`CR Text`、`CR Text`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
