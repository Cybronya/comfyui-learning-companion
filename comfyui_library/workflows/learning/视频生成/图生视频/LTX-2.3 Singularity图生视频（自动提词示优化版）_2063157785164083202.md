---
key: 视频生成/图生视频/LTX-2.3 Singularity图生视频（自动提词示优化版）_2063157785164083202.json
name: LTX-2.3 Singularity图生视频（自动提词示优化版）_2063157785164083202.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3 Singularity图生视频（自动提词示优化版）_2063157785164083202.json
hash: 2d629682264ec660
coverage: 0.961538
learned_at: 2026-10-15 22:39:10
nodes: [RandomNoise, LTXVConcatAVLatent, KSamplerSelect, CFGGuider, LTXVCropGuides, LTXVImgToVideoInplace, LTXVAudioVAEDecode, LTXVConditioning, DualCLIPLoader, RandomNoise, VAEDecode, LatentUpscaleModelLoader, SimpleMath+, easy int, easy imageSize, LayerUtility: ImageScaleByAspectRatio V2, ResizeImagesByLongerEdge, easy imageSize, EmptyLTXVLatentVideo, LTXVPreprocess, EmptyImage, easy mathInt, VAELoaderKJ, VAELoaderKJ, LoraLoaderModelOnly, CLIPTextEncode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVConcatAVLatent, KSamplerSelect, CFGGuider, CLIPTextEncode, ManualSigmas, SamplerCustomAdvanced, ImageScaleBy, LTXVImgToVideoInplace, VAEDecode, LTXVSeparateAVLatent, PathchSageAttentionKJ, ManualSigmas, easy int, Note, VHS_VideoCombine, ShowText|pysssss, LoadImage, RH_LLMAPI_Pro_Node, CR Prompt Text, CR Prompt Text, UNETLoader, LTXVEmptyLatentAudio, SamplerCustomAdvanced, LTXVLatentUpsampler]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 361}
---

# 视频生成/图生视频/LTX-2.3 Singularity图生视频（自动提词示优化版）_2063157785164083202.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2063157785164083202.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（52 个）：
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `DualCLIPLoader`
- `RandomNoise`
- `VAEDecode` ★核心
- `LatentUpscaleModelLoader`
- `SimpleMath+`
- `easy int`
- `easy imageSize`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ResizeImagesByLongerEdge`
- `easy imageSize`
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `EmptyImage`
- `easy mathInt`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `ImageScaleBy`
- `LTXVImgToVideoInplace`
- `VAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `PathchSageAttentionKJ`
- `ManualSigmas`
- `easy int`
- `Note`
- `VHS_VideoCombine`
- `ShowText|pysssss`
- `LoadImage`
- `RH_LLMAPI_Pro_Node`
- `CR Prompt Text`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心

## 关键参数

- `width` = `361`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（50/52）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`CFGGuider`、`LTXVCropGuides`、`LTXVImgToVideoInplace`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`DualCLIPLoader`、`VAEDecode`、`LatentUpscaleModelLoader`、`SimpleMath+`、`easy int`、`easy imageSize`、`LayerUtility: ImageScaleByAspectRatio V2`、`ResizeImagesByLongerEdge`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`EmptyImage`、`easy mathInt`、`VAELoaderKJ`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`LTXVSeparateAVLatent`、`ManualSigmas`、`SamplerCustomAdvanced`、`ImageScaleBy`、`PathchSageAttentionKJ`、`VHS_VideoCombine`、`LoadImage`、`RH_LLMAPI_Pro_Node`、`CR Prompt Text`、`UNETLoader`、`LTXVEmptyLatentAudio`、`LTXVLatentUpsampler`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
