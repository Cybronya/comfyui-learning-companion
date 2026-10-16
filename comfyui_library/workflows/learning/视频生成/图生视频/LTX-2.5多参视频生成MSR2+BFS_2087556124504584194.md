---
key: 视频生成/图生视频/LTX-2.5多参视频生成MSR2+BFS_2087556124504584194.json
name: LTX-2.5多参视频生成MSR2+BFS_2087556124504584194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.5多参视频生成MSR2+BFS_2087556124504584194.json
hash: f8598ece28d5f0b8
coverage: 0.978261
learned_at: 2026-10-16 21:27:31
nodes: [CLIPTextEncode, KSamplerSelect, BasicScheduler, ModelSamplingSD3, VHS_VideoCombine, ImageResizeKJv2, ImageResizeKJv2, LTXVChunkFeedForward, LTX2AttentionTunerPatch, ComfyNumberConvert, LoadImage, SimpleCalculatorKJ, ImageResizeKJv2, LTXVEmptyLatentAudio, LTXVConditioning, EmptyLTXVLatentVideo, LiconMSR, ImageResizeKJv2, INTConstant, INTConstant, INTConstant, PrimitiveFloat, LTXVSeparateAVLatent, PathchSageAttentionKJ, LTXVConcatAVLatent, VAEDecode, LTXVAudioVAEDecode, SamplerCustomAdvanced, CLIPLoader, LTXAddVideoICLoRAGuide, RandomNoise, LTXVDualCFGGuider, LTXVImgToVideoInplace, LoadImage, UNETLoader, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, LTXICLoRALoaderModelOnly, LoraLoaderModelOnly, VAELoaderKJ, VAELoaderKJ, LoadImage, LoadImage, PromptRelayEncode, LTX2SamplingPreviewOverride, LTXVCropGuides]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 241}
---

# 视频生成/图生视频/LTX-2.5多参视频生成MSR2+BFS_2087556124504584194.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX-2.5多参视频生成MSR2+BFS_2087556124504584194.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（46 个）：
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LTXVChunkFeedForward`
- `LTX2AttentionTunerPatch`
- `ComfyNumberConvert`
- `LoadImage`
- `SimpleCalculatorKJ`
- `ImageResizeKJv2`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LiconMSR`
- `ImageResizeKJv2`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `PrimitiveFloat`
- `LTXVSeparateAVLatent`
- `PathchSageAttentionKJ`
- `LTXVConcatAVLatent`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CLIPLoader`
- `LTXAddVideoICLoRAGuide`
- `RandomNoise`
- `LTXVDualCFGGuider`
- `LTXVImgToVideoInplace`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LoadImage`
- `LoadImage`
- `PromptRelayEncode`
- `LTX2SamplingPreviewOverride`
- `LTXVCropGuides`

## 关键参数

- `width` = `241`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **98%**（45/46）

**有卡**：`CLIPTextEncode`、`KSamplerSelect`、`BasicScheduler`、`ModelSamplingSD3`、`VHS_VideoCombine`、`ImageResizeKJv2`、`LTXVChunkFeedForward`、`LTX2AttentionTunerPatch`、`ComfyNumberConvert`、`LoadImage`、`SimpleCalculatorKJ`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LiconMSR`、`INTConstant`、`LTXVSeparateAVLatent`、`PathchSageAttentionKJ`、`LTXVConcatAVLatent`、`VAEDecode`、`LTXVAudioVAEDecode`、`SamplerCustomAdvanced`、`CLIPLoader`、`LTXAddVideoICLoRAGuide`、`RandomNoise`、`LTXVDualCFGGuider`、`LTXVImgToVideoInplace`、`UNETLoader`、`LoraLoaderModelOnly`、`LTXICLoRALoaderModelOnly`、`VAELoaderKJ`、`PromptRelayEncode`、`LTX2SamplingPreviewOverride`、`LTXVCropGuides`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
