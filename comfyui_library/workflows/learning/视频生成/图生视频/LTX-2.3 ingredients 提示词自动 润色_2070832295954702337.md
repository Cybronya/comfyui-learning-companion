---
key: 视频生成/图生视频/LTX-2.3 ingredients 提示词自动 润色_2070832295954702337.json
name: LTX-2.3 ingredients 提示词自动 润色_2070832295954702337.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3 ingredients 提示词自动 润色_2070832295954702337.json
hash: 506400acf46643d9
coverage: 0.840909
learned_at: 2026-10-15 22:40:42
nodes: [LTXVConditioning, CFGGuider, KSamplerSelect, LTXVCropGuides, EmptyLTXVLatentVideo, CheckpointLoaderSimple, LTXICLoRALoaderModelOnly, LTXAVTextEncoderLoader, LTXVPreprocess, LTXVImgToVideoConditionOnly, LTXVEmptyLatentAudio, LTXAddVideoICLoRAGuide, LTXVConcatAVLatent, LTXFloatToInt, CLIPTextEncode, llama_cpp_parameters, RepeatImageBatch, SamplerCustomAdvanced, RandomNoise, LTXVSeparateAVLatent, ManualSigmas, CreateVideo, LTXVAudioVAELoader, SaveVideo, LoraLoaderModelOnly, PreviewAny, PrimitiveInt, llama_cpp_model_loader, llama_cpp_instruct_adv, ResizeImageMaskNode, LTXVAudioVAEDecode, LTXVTiledVAEDecode, LoadImage, CreateVideo, GetVideoComponents, CLIPTextEncode, PreviewAny, PreviewImage, GetImageSize, PrimitiveFloat, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveBoolean, Fast Groups Bypasser (rgthree), JjkText]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX-2.3 ingredients 提示词自动 润色_2070832295954702337.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2070832295954702337.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `LTXVConditioning`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVCropGuides`
- `EmptyLTXVLatentVideo`
- `CheckpointLoaderSimple` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVPreprocess`
- `LTXVImgToVideoConditionOnly`
- `LTXVEmptyLatentAudio` ★核心
- `LTXAddVideoICLoRAGuide`
- `LTXVConcatAVLatent`
- `LTXFloatToInt`
- `CLIPTextEncode` ★核心
- `llama_cpp_parameters`
- `RepeatImageBatch`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `CreateVideo`
- `LTXVAudioVAELoader`
- `SaveVideo`
- `LoraLoaderModelOnly` ★核心
- `PreviewAny`
- `PrimitiveInt`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `ResizeImageMaskNode`
- `LTXVAudioVAEDecode` ★核心
- `LTXVTiledVAEDecode` ★核心
- `LoadImage`
- `CreateVideo`
- `GetVideoComponents`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `PreviewImage`
- `GetImageSize`
- `PrimitiveFloat`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveBoolean`
- `Fast Groups Bypasser (rgthree)`
- `JjkText`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（37/44）

**有卡**：`LTXVConditioning`、`CFGGuider`、`KSamplerSelect`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`CheckpointLoaderSimple`、`LTXICLoRALoaderModelOnly`、`LTXAVTextEncoderLoader`、`LTXVPreprocess`、`LTXVImgToVideoConditionOnly`、`LTXVEmptyLatentAudio`、`LTXAddVideoICLoRAGuide`、`LTXVConcatAVLatent`、`LTXFloatToInt`、`CLIPTextEncode`、`llama_cpp_parameters`、`RepeatImageBatch`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVSeparateAVLatent`、`ManualSigmas`、`CreateVideo`、`LTXVAudioVAELoader`、`SaveVideo`、`LoraLoaderModelOnly`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`ResizeImageMaskNode`、`LTXVAudioVAEDecode`、`LTXVTiledVAEDecode`、`LoadImage`、`GetVideoComponents`、`GetImageSize`、`LayerUtility: ImageScaleByAspectRatio V2`、`PrimitiveBoolean`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
