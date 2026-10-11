---
key: 视频生成/文生视频/LTX 2.3 IC-LoRA 视频上色工作流（手动提示）_2035643489333022722.json
name: LTX 2.3 IC-LoRA 视频上色工作流（手动提示）_2035643489333022722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.3 IC-LoRA 视频上色工作流（手动提示）_2035643489333022722.json
hash: 5edad4ae36e5b2eb
coverage: 0.954545
learned_at: 2026-10-11 03:48:34
nodes: [LTXVAudioVAEDecode, VAEDecodeTiled, KSamplerSelect, LTXVConditioning, LTXAddVideoICLoRAGuide, LTXVConcatAVLatent, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, EmptyLTXVLatentVideo, SamplerCustomAdvanced, LTXVCropGuides, LTXVSeparateAVLatent, DWPreprocessor, LTXVAudioVAELoader, CheckpointLoaderSimple, GemmaAPITextEncode, PrimitiveString, CLIPTextEncode, LTXVPreprocess, CM_FloatToInt, CFGGuider, ResizeImageMaskNode, GetImageSize, ManualSigmas, SimpleMath+, GemmaAPITextEncode, RandomNoise, CannyEdgePreprocessor, DepthCrafter, DownloadAndLoadDepthCrafterModel, LoraLoaderModelOnly, LTXAVTextEncoderLoader, LTXICLoRALoaderModelOnly, PrimitiveBoolean, CLIPTextEncode, VHS_VideoInfoLoaded, SaveVideo, CreateVideo, ResizeImageMaskNode, VHS_VideoCombine, LoadImage, Image_Resize_longsize, image_scale_pixel_v2, VHS_LoadVideo]
patterns: []
missing: [SimpleMath+]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX 2.3 IC-LoRA 视频上色工作流（手动提示）_2035643489333022722.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.3 IC-LoRA 视频上色工作流（手动提示）_2035643489333022722.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `LTXAddVideoICLoRAGuide`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVImgToVideoConditionOnly`
- `EmptyLTXVLatentVideo`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `DWPreprocessor`
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `GemmaAPITextEncode`
- `PrimitiveString`
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `CM_FloatToInt`
- `CFGGuider`
- `ResizeImageMaskNode`
- `GetImageSize`
- `ManualSigmas`
- `SimpleMath+`
- `GemmaAPITextEncode`
- `RandomNoise`
- `CannyEdgePreprocessor`
- `DepthCrafter`
- `DownloadAndLoadDepthCrafterModel`
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `LTXICLoRALoaderModelOnly` ★核心
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `VHS_VideoInfoLoaded`
- `SaveVideo`
- `CreateVideo`
- `ResizeImageMaskNode`
- `VHS_VideoCombine`
- `LoadImage`
- `Image_Resize_longsize`
- `image_scale_pixel_v2`
- `VHS_LoadVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **95%**（42/44）

**有卡**：`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`KSamplerSelect`、`LTXVConditioning`、`LTXAddVideoICLoRAGuide`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`LTXVImgToVideoConditionOnly`、`EmptyLTXVLatentVideo`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`DWPreprocessor`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`GemmaAPITextEncode`、`CLIPTextEncode`、`LTXVPreprocess`、`CM_FloatToInt`、`CFGGuider`、`ResizeImageMaskNode`、`GetImageSize`、`ManualSigmas`、`RandomNoise`、`CannyEdgePreprocessor`、`DepthCrafter`、`DownloadAndLoadDepthCrafterModel`、`LoraLoaderModelOnly`、`LTXAVTextEncoderLoader`、`LTXICLoRALoaderModelOnly`、`PrimitiveBoolean`、`VHS_VideoInfoLoaded`、`SaveVideo`、`CreateVideo`、`VHS_VideoCombine`、`LoadImage`、`Image_Resize_longsize`、`image_scale_pixel_v2`、`VHS_LoadVideo`

**缺卡**（1）：`SimpleMath+`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CannyEdgePreprocessor、DepthCrafter、DownloadAndLoadDepthCrafterModel、CFGGuider

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
