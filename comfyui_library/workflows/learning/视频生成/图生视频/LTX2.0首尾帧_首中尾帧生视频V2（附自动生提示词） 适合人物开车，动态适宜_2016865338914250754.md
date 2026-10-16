---
key: 视频生成/图生视频/LTX2.0首尾帧_首中尾帧生视频V2（附自动生提示词） 适合人物开车，动态适宜_2016865338914250754.json
name: LTX2.0首尾帧_首中尾帧生视频V2（附自动生提示词） 适合人物开车，动态适宜_2016865338914250754.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2016865338914250754.json
hash: 21b65efb6fad5cff
coverage: 0.475
learned_at: 2026-10-15 22:34:43
nodes: [CFGGuider, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVEmptyLatentAudio, CLIPTextEncode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, LatentUpscaleModelLoader, GetNode, GetNode, GetNode, SetNode, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, GetNode, LoraLoaderModelOnly, GetNode, LTXVConcatAVLatent, RandomNoise, GetNode, Label (rgthree), ImageConcatMulti, PreviewImage, Qwen3_VQA, Label (rgthree), Label (rgthree), DF_Int_to_Float, GetNode, DF_Int_to_Float, GetNode, INTConstant, KSamplerSelect, GetNode, LTXVLatentUpsampler, GetNode, GetNode, GetNode, GetNode, RandomNoise, LTXVFirstLastFrameControl_TTP, LTXVAudioVAELoader, LTXAVTextEncoderLoader, ManualSigmas, CheckpointLoaderSimple, LoraLoaderModelOnly, CheckpointLoaderSimple, SetNode, LTXVAudioVAELoader, LTXAVTextEncoderLoader, JoinStrings, SamplerCustomAdvanced, LoadImage, LoadImage, MarkdownNote, MarkdownNote, Label (rgthree), GetNode, GetNode, GetNode, LTXVFirstLastFrameControl_TTP, LTXVConcatAVLatent, SetNode, LTXVPreprocess, PreviewImage, ImageResizeKJv2, GetNode, GetNode, ImageResizeKJv2, LTXVPreprocess, PreviewImage, LTXVMiddleFrame_TTP, LTXVPreprocess, ImageResizeKJv2, PreviewImage, LoadImage, SetNode, GetNode, GetNode, SetNode, SetNode, CM_FloatToInt, JWIntegerDiv, GetNode, EmptyLTXVLatentVideo, GetNode, JWIntegerDiv, CM_FloatToInt, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConditioning, SetNode, CM_IntToFloat, CFGGuider, KSamplerSelect, LTXVScheduler, GetNode, LTXVSeparateAVLatent, SamplerCustomAdvanced, GetNode, GetNode, SetNode, SetNode, LTXVSeparateAVLatent, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, ShowText|pysssss, easy showAnything, MarkdownNote, TextInput_, ShellAgentPluginOutputText, INTConstant, INTConstant, INTConstant, SetNode, SetNode, VAEDecode, LTXVAudioVAEDecode, VHS_VideoCombine, VAEDecode, LTXVAudioVAEDecode, VHS_VideoCombine, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, INTConstant, TextInput_, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-distilled-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.0首尾帧_首中尾帧生视频V2（附自动生提示词） 适合人物开车，动态适宜_2016865338914250754.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2016865338914250754.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（160 个）：
- `CFGGuider`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LatentUpscaleModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `GetNode`
- `Label (rgthree)`
- `ImageConcatMulti`
- `PreviewImage`
- `Qwen3_VQA`
- `Label (rgthree)`
- `Label (rgthree)`
- `DF_Int_to_Float`
- `GetNode`
- `DF_Int_to_Float`
- `GetNode`
- `INTConstant`
- `KSamplerSelect` ★核心
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `LTXVFirstLastFrameControl_TTP`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `ManualSigmas`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `JoinStrings`
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `MarkdownNote`
- `Label (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVFirstLastFrameControl_TTP`
- `LTXVConcatAVLatent`
- `SetNode`
- `LTXVPreprocess`
- `PreviewImage`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `PreviewImage`
- `LTXVMiddleFrame_TTP`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `PreviewImage`
- `LoadImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `CM_FloatToInt`
- `JWIntegerDiv`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `JWIntegerDiv`
- `CM_FloatToInt`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `SetNode`
- `CM_IntToFloat`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ShowText|pysssss`
- `easy showAnything`
- `MarkdownNote`
- `TextInput_`
- `ShellAgentPluginOutputText`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `TextInput_`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-distilled-fp8.safetensors`

## 知识

覆盖率 **48%**（76/160）

**有卡**：`CFGGuider`、`CLIPTextEncode`、`LTXVEmptyLatentAudio`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`LTXVConcatAVLatent`、`RandomNoise`、`Label (rgthree)`、`ImageConcatMulti`、`Qwen3_VQA`、`DF_Int_to_Float`、`INTConstant`、`KSamplerSelect`、`LTXVLatentUpsampler`、`LTXVFirstLastFrameControl_TTP`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`ManualSigmas`、`CheckpointLoaderSimple`、`JoinStrings`、`SamplerCustomAdvanced`、`LoadImage`、`LTXVPreprocess`、`ImageResizeKJv2`、`LTXVMiddleFrame_TTP`、`CM_FloatToInt`、`JWIntegerDiv`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`CM_IntToFloat`、`LTXVScheduler`、`LTXVSeparateAVLatent`、`TextInput_`、`ShellAgentPluginOutputText`、`VAEDecode`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
