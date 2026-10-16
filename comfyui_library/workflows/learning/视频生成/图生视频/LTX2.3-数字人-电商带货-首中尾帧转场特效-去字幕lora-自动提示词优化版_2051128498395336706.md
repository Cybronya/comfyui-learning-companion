---
key: 视频生成/图生视频/LTX2.3-数字人-电商带货-首中尾帧转场特效-去字幕lora-自动提示词优化版_2051128498395336706.json
name: LTX2.3-数字人-电商带货-首中尾帧转场特效-去字幕lora-自动提示词优化版_2051128498395336706.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2051128498395336706.json
hash: 9f6fe0bc0cee637a
coverage: 0.984375
learned_at: 2026-10-15 22:37:21
nodes: [ManualSigmas, LTXVConcatAVLatent, LTXVCropGuides, LTXVSeparateAVLatent, LTXVPreprocess, LTXVPreprocess, LTXVPreprocess, SimpleMath+, ImageResizeKJv2, LatentUpscaleModelLoader, VAELoaderKJ, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, ComfyMathExpression, ComfyMathExpression, ImageResizeKJv2, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, CLIPTextEncode, CLIPTextEncode, CustomAddLabel, KSamplerSelect, CFGGuider, LTXVLatentUpsampler, RH_LLMAPI_Pro_Node, easy showAnything, KSamplerSelect, LTXVImgToVideoInplace, CFGGuider, ManualSigmas, LTXVConcatAVLatent, RandomNoise, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVAudioVAEDecode, VAEDecodeTiled, CreateVideo, ImageResizeKJv2, RandomNoise, SamplerCustomAdvanced, GetVideoComponents, ComfyMathExpression, LoraLoaderModelOnly, LoraLoaderModelOnly, MultiTextConcatenate, ttN concat, RH_Utils, Int, Int, TTResolutionSelector, LoadImage, LoadImage, Text, LTXVAddGuideMulti, LTXVConditioning, UNETLoader, DualCLIPLoader, LoadImage, VHS_VideoCombine, VHS_VideoCombine, LoraLoaderModelOnly, VAELoaderKJ, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3-数字人-电商带货-首中尾帧转场特效-去字幕lora-自动提示词优化版_2051128498395336706.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2051128498395336706.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（64 个）：
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `SimpleMath+`
- `ImageResizeKJv2`
- `LatentUpscaleModelLoader`
- `VAELoaderKJ`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ImageResizeKJv2`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CustomAddLabel`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `LTXVLatentUpsampler` ★核心
- `RH_LLMAPI_Pro_Node`
- `easy showAnything`
- `KSamplerSelect` ★核心
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `ImageResizeKJv2`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `GetVideoComponents`
- `ComfyMathExpression`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MultiTextConcatenate`
- `ttN concat`
- `RH_Utils`
- `Int`
- `Int`
- `TTResolutionSelector`
- `LoadImage`
- `LoadImage`
- `Text`
- `LTXVAddGuideMulti`
- `LTXVConditioning`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **98%**（63/64）

**有卡**：`ManualSigmas`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVPreprocess`、`SimpleMath+`、`ImageResizeKJv2`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`ResizeImagesByLongerEdge`、`ComfyMathExpression`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`CustomAddLabel`、`KSamplerSelect`、`CFGGuider`、`LTXVLatentUpsampler`、`RH_LLMAPI_Pro_Node`、`LTXVImgToVideoInplace`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`CreateVideo`、`GetVideoComponents`、`LoraLoaderModelOnly`、`MultiTextConcatenate`、`ttN concat`、`RH_Utils`、`Int`、`TTResolutionSelector`、`LoadImage`、`Text`、`LTXVAddGuideMulti`、`LTXVConditioning`、`UNETLoader`、`DualCLIPLoader`、`VHS_VideoCombine`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
