---
key: 视频生成/图生视频/LTX-2.3 ingredients 提示词自动 润色低配_2070881520012849153.json
name: LTX-2.3 ingredients 提示词自动 润色低配_2070881520012849153.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2070881520012849153.json
hash: 42bd91a7ddb78511
coverage: 0.847826
learned_at: 2026-10-15 22:40:43
nodes: [CFGGuider, KSamplerSelect, LTXVCropGuides, EmptyLTXVLatentVideo, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LTXVPreprocess, LTXVImgToVideoConditionOnly, LTXVEmptyLatentAudio, LTXAddVideoICLoRAGuide, LTXFloatToInt, RepeatImageBatch, RandomNoise, ManualSigmas, CreateVideo, LTXVAudioVAELoader, SaveVideo, PreviewAny, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, LTXVAudioVAEDecode, LoadImage, CreateVideo, GetImageSize, ResizeImageMaskNode, LoraLoaderModelOnly, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, PreviewImage, easy cleanGpuUsed, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, LTXVTiledVAEDecode, LTXVConditioning, CLIPTextEncode, GetVideoComponents, CLIPTextEncode, LTXICLoRALoaderModelOnly, RH_LLMAPI_NODE, easy cleanGpuUsed, JjkText, ComfySwitchNode, PrimitiveBoolean, PreviewAny]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX-2.3 ingredients 提示词自动 润色低配_2070881520012849153.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2070881520012849153.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVCropGuides`
- `EmptyLTXVLatentVideo`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVPreprocess`
- `LTXVImgToVideoConditionOnly`
- `LTXVEmptyLatentAudio` ★核心
- `LTXAddVideoICLoRAGuide`
- `LTXFloatToInt`
- `RepeatImageBatch`
- `RandomNoise`
- `ManualSigmas`
- `CreateVideo`
- `LTXVAudioVAELoader`
- `SaveVideo`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `LTXVAudioVAEDecode` ★核心
- `LoadImage`
- `CreateVideo`
- `GetImageSize`
- `ResizeImageMaskNode`
- `LoraLoaderModelOnly` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `PreviewImage`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVTiledVAEDecode` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `GetVideoComponents`
- `CLIPTextEncode` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `RH_LLMAPI_NODE`
- `easy cleanGpuUsed`
- `JjkText`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `PreviewAny`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（39/46）

**有卡**：`CFGGuider`、`KSamplerSelect`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LTXVPreprocess`、`LTXVImgToVideoConditionOnly`、`LTXVEmptyLatentAudio`、`LTXAddVideoICLoRAGuide`、`LTXFloatToInt`、`RepeatImageBatch`、`RandomNoise`、`ManualSigmas`、`CreateVideo`、`LTXVAudioVAELoader`、`SaveVideo`、`PrimitiveBoolean`、`LTXVAudioVAEDecode`、`LoadImage`、`GetImageSize`、`ResizeImageMaskNode`、`LoraLoaderModelOnly`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`easy cleanGpuUsed`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVTiledVAEDecode`、`LTXVConditioning`、`CLIPTextEncode`、`GetVideoComponents`、`LTXICLoRALoaderModelOnly`、`RH_LLMAPI_NODE`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
