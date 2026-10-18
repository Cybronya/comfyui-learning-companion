---
key: 视频生成/图生视频/图生视频+LTX-2.3+Singularity图生视频 数字人说话唱歌对口型 优化升级 （自动提词_2063429400057704450.json
name: 图生视频+LTX-2.3+Singularity图生视频 数字人说话唱歌对口型 优化升级 （自动提词_2063429400057704450.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频+LTX-2.3+Singularity图生视频 数字人说话唱歌对口型 优化升级 （自动提词_2063429400057704450.json
hash: 967304e91de7b31f
coverage: 0.961538
learned_at: 2026-10-15 22:39:13
nodes: [RandomNoise, LTXVConcatAVLatent, KSamplerSelect, CFGGuider, LTXVCropGuides, LTXVImgToVideoInplace, LTXVAudioVAEDecode, LTXVConditioning, DualCLIPLoader, RandomNoise, VAEDecode, LatentUpscaleModelLoader, SimpleMath+, easy int, easy imageSize, LayerUtility: ImageScaleByAspectRatio V2, ResizeImagesByLongerEdge, easy imageSize, EmptyLTXVLatentVideo, LTXVPreprocess, EmptyImage, easy mathInt, VAELoaderKJ, VAELoaderKJ, LoraLoaderModelOnly, CLIPTextEncode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVConcatAVLatent, KSamplerSelect, CFGGuider, CLIPTextEncode, ManualSigmas, SamplerCustomAdvanced, ImageScaleBy, LTXVImgToVideoInplace, VAEDecode, LTXVSeparateAVLatent, PathchSageAttentionKJ, ManualSigmas, easy int, Note, VHS_VideoCombine, ShowText|pysssss, CR Prompt Text, UNETLoader, LTXVEmptyLatentAudio, SamplerCustomAdvanced, LTXVLatentUpsampler, LoadImage, CR Prompt Text, RH_LLMAPI_Pro_Node]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 361}
---

# 视频生成/图生视频/图生视频+LTX-2.3+Singularity图生视频 数字人说话唱歌对口型 优化升级 （自动提词_2063429400057704450.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2063429400057704450.json`

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
- `CR Prompt Text`
- `UNETLoader` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `LoadImage`
- `CR Prompt Text`
- `RH_LLMAPI_Pro_Node`

## 关键参数

- `width` = `361`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（50/52）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`CFGGuider`、`LTXVCropGuides`、`LTXVImgToVideoInplace`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`DualCLIPLoader`、`VAEDecode`、`LatentUpscaleModelLoader`、`SimpleMath+`、`easy int`、`easy imageSize`、`LayerUtility: ImageScaleByAspectRatio V2`、`ResizeImagesByLongerEdge`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`EmptyImage`、`easy mathInt`、`VAELoaderKJ`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`LTXVSeparateAVLatent`、`ManualSigmas`、`SamplerCustomAdvanced`、`ImageScaleBy`、`PathchSageAttentionKJ`、`VHS_VideoCombine`、`CR Prompt Text`、`UNETLoader`、`LTXVEmptyLatentAudio`、`LTXVLatentUpsampler`、`LoadImage`、`RH_LLMAPI_Pro_Node`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
