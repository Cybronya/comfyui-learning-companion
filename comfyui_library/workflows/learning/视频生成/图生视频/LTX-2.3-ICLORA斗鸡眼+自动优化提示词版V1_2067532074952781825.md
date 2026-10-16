---
key: 视频生成/图生视频/LTX-2.3-ICLORA斗鸡眼+自动优化提示词版V1_2067532074952781825.json
name: LTX-2.3-ICLORA斗鸡眼+自动优化提示词版V1_2067532074952781825.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2067532074952781825.json
hash: eeb4250eb0040880
coverage: 0.977778
learned_at: 2026-10-15 22:40:04
nodes: [PathchSageAttentionKJ, LTXAVTextEncoderLoader, LTXVEmptyLatentAudio, LTX2SamplingPreviewOverride, LTXVConcatAVLatent, KSamplerSelect, LTXVCropGuides, LTXVAudioVAELoader, LTXAddVideoICLoRAGuide, RandomNoise, Seed (rgthree), SamplerCustomAdvanced, LTXVSeparateAVLatent, CheckpointLoaderSimple, LTXVPreprocess, LTXVImgToVideoConditionOnly, CFGGuider, GetImageRangeFromBatch, easy imageSize, VAEEncodeForInpaint, RepeatImageBatch, Image To Mask, SimpleMath+, LoraLoaderModelOnly, VAEDecodeTiled, ManualSigmas, ResizeImageMaskNode, LayerUtility: ColorImage, ResizeImageMaskNode, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, VHS_VideoInfoLoaded, CreateVideo, easy showAnything, ManualSigmas, ImageConcanate, LTXVConditioning, CLIPTextEncode, CLIPTextEncode, CR Prompt Text, CR Prompt Text, VHS_LoadVideo, RHLLMChatNode, LTXICLoRALoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX-2.3-ICLORA斗鸡眼+自动优化提示词版V1_2067532074952781825.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067532074952781825.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（45 个）：
- `PathchSageAttentionKJ`
- `LTXAVTextEncoderLoader`
- `LTXVEmptyLatentAudio` ★核心
- `LTX2SamplingPreviewOverride`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `LTXVCropGuides`
- `LTXVAudioVAELoader`
- `LTXAddVideoICLoRAGuide`
- `RandomNoise`
- `Seed (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CheckpointLoaderSimple` ★核心
- `LTXVPreprocess`
- `LTXVImgToVideoConditionOnly`
- `CFGGuider`
- `GetImageRangeFromBatch`
- `easy imageSize`
- `VAEEncodeForInpaint` ★核心
- `RepeatImageBatch`
- `Image To Mask`
- `SimpleMath+`
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `ManualSigmas`
- `ResizeImageMaskNode`
- `LayerUtility: ColorImage`
- `ResizeImageMaskNode`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `CreateVideo`
- `easy showAnything`
- `ManualSigmas`
- `ImageConcanate`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `CR Prompt Text`
- `VHS_LoadVideo`
- `RHLLMChatNode`
- `LTXICLoRALoaderModelOnly` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **98%**（44/45）

**有卡**：`PathchSageAttentionKJ`、`LTXAVTextEncoderLoader`、`LTXVEmptyLatentAudio`、`LTX2SamplingPreviewOverride`、`LTXVConcatAVLatent`、`KSamplerSelect`、`LTXVCropGuides`、`LTXVAudioVAELoader`、`LTXAddVideoICLoRAGuide`、`RandomNoise`、`Seed (rgthree)`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`CheckpointLoaderSimple`、`LTXVPreprocess`、`LTXVImgToVideoConditionOnly`、`CFGGuider`、`GetImageRangeFromBatch`、`easy imageSize`、`VAEEncodeForInpaint`、`RepeatImageBatch`、`Image To Mask`、`SimpleMath+`、`LoraLoaderModelOnly`、`VAEDecodeTiled`、`ManualSigmas`、`ResizeImageMaskNode`、`LayerUtility: ColorImage`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoInfoLoaded`、`CreateVideo`、`ImageConcanate`、`LTXVConditioning`、`CLIPTextEncode`、`CR Prompt Text`、`VHS_LoadVideo`、`RHLLMChatNode`、`LTXICLoRALoaderModelOnly`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、Seed (rgthree)
