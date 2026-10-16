---
key: 视频生成/图生视频/LTX-2.3 Singularity首尾帧生视频（自动提词示优化版）V2_2063144368743206913.json
name: LTX-2.3 Singularity首尾帧生视频（自动提词示优化版）V2_2063144368743206913.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2063144368743206913.json
hash: aa724ae5b6ba256d
coverage: 0.964286
learned_at: 2026-10-15 22:39:10
nodes: [RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, KSamplerSelect, LTXVAudioVAEDecode, LTXVConditioning, LTXVConcatAVLatent, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPTextEncode, CFGGuider, DualCLIPLoader, RandomNoise, PathchSageAttentionKJ, VAEDecode, LTXVAudioVAEDecode, VAEDecode, CLIPTextEncode, LatentUpscaleModelLoader, LTXVEmptyLatentAudio, SimpleMath+, easy int, easy imageSize, ImageScaleBy, LayerUtility: ImageScaleByAspectRatio V2, easy imageSize, EmptyImage, easy mathInt, ResizeImagesByLongerEdge, LayerUtility: ImageScaleByAspectRatio V2, EmptyLTXVLatentVideo, LTXVPreprocess, VAELoaderKJ, VAELoaderKJ, ShowText|pysssss, LTXVPreprocess, easy int, UNETLoader, SamplerCustomAdvanced, Note, ResizeImagesByLongerEdge, RH_LLMAPI_Pro_Node, LTXVImgToVideoInplaceKJ, LoadImage, CR Text, VHS_VideoCombine, LoadImage, ManualSigmas, LoraLoaderModelOnly, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 361}
---

# 视频生成/图生视频/LTX-2.3 Singularity首尾帧生视频（自动提词示优化版）V2_2063144368743206913.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2063144368743206913.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（56 个）：
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `KSamplerSelect` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `DualCLIPLoader`
- `RandomNoise`
- `PathchSageAttentionKJ`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LatentUpscaleModelLoader`
- `LTXVEmptyLatentAudio` ★核心
- `SimpleMath+`
- `easy int`
- `easy imageSize`
- `ImageScaleBy`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageSize`
- `EmptyImage`
- `easy mathInt`
- `ResizeImagesByLongerEdge`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `ShowText|pysssss`
- `LTXVPreprocess`
- `easy int`
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `Note`
- `ResizeImagesByLongerEdge`
- `RH_LLMAPI_Pro_Node`
- `LTXVImgToVideoInplaceKJ`
- `LoadImage`
- `CR Text`
- `VHS_VideoCombine`
- `LoadImage`
- `ManualSigmas`
- `LoraLoaderModelOnly` ★核心
- `CR Text`

## 关键参数

- `width` = `361`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（54/56）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`DualCLIPLoader`、`PathchSageAttentionKJ`、`VAEDecode`、`LatentUpscaleModelLoader`、`LTXVEmptyLatentAudio`、`SimpleMath+`、`easy int`、`easy imageSize`、`ImageScaleBy`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyImage`、`easy mathInt`、`ResizeImagesByLongerEdge`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`VAELoaderKJ`、`UNETLoader`、`RH_LLMAPI_Pro_Node`、`LTXVImgToVideoInplaceKJ`、`LoadImage`、`CR Text`、`VHS_VideoCombine`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
