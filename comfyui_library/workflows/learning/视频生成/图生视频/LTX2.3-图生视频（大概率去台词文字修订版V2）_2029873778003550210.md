---
key: 视频生成/图生视频/LTX2.3-图生视频（大概率去台词文字修订版V2）_2029873778003550210.json
name: LTX2.3-图生视频（大概率去台词文字修订版V2）_2029873778003550210.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-图生视频（大概率去台词文字修订版V2）_2029873778003550210.json
hash: 5d1b2518caaa5210
coverage: 0.959184
learned_at: 2026-10-15 22:35:23
nodes: [CFGGuider, LTXVSeparateAVLatent, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVConcatAVLatent, ResizeImagesByLongerEdge, CLIPTextEncode, CFGGuider, LTXVScheduler, GetImageSize, CLIPTextEncode, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVCropGuides, VAEDecodeTiled, KSamplerSelect, PrimitiveInt, LTXVEmptyLatentAudio, RandomNoise, RandomNoise, KSamplerSelect, ManualSigmas, LTXVConditioning, ImageScaleBy, LTXVChunkFeedForward, PathchSageAttentionKJ, ModelPatchTorchSettings, ManualSigmas, ManualSigmas, VHS_VideoCombine, UNETLoader, VAELoaderKJ, DualCLIPLoader, VAELoaderKJ, LatentUpscaleModelLoader, LoraLoaderModelOnly, LTXVAudioVAEDecode, LTXVLatentUpsampler, LTXVImgToVideoInplace, CR Text, ShowText|pysssss, llama_cpp_instruct_adv, llama_cpp_model_loader, LoadImage, CR Text, ImageScale]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX2.3-图生视频（大概率去台词文字修订版V2）_2029873778003550210.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2029873778003550210.json`

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
- `CLIPTextEncode` ★核心
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
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `CR Text`
- `ShowText|pysssss`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `LoadImage`
- `CR Text`
- `ImageScale`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（47/49）

**有卡**：`CFGGuider`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`ResizeImagesByLongerEdge`、`CLIPTextEncode`、`LTXVScheduler`、`GetImageSize`、`LTXVCropGuides`、`VAEDecodeTiled`、`KSamplerSelect`、`LTXVEmptyLatentAudio`、`RandomNoise`、`ManualSigmas`、`LTXVConditioning`、`ImageScaleBy`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VHS_VideoCombine`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`CR Text`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`LoadImage`、`ImageScale`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
