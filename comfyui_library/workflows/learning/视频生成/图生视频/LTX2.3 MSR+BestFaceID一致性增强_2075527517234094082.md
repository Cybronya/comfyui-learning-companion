---
key: 视频生成/图生视频/LTX2.3 MSR+BestFaceID一致性增强_2075527517234094082.json
name: LTX2.3 MSR+BestFaceID一致性增强_2075527517234094082.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2075527517234094082.json
hash: 9d906b285612864e
coverage: 0.918367
learned_at: 2026-10-15 22:41:25
nodes: [LTXVAudioVAEDecode, LTXVSeparateAVLatent, LTXVCropGuides, VAEDecode, SamplerCustomAdvanced, ManualSigmas, KSamplerSelect, RandomNoise, EmptyLTXVLatentVideo, CFGGuider, LTXVConcatAVLatent, CreateVideo, LoraLoaderModelOnly, INTConstant, INTConstant, LTXVAudioVAELoader, LoadImage, LTXICLoRALoaderModelOnly, LiconMSR, LTXVConditioning, CLIPTextEncode, LTXVEmptyLatentAudio, StringConcatenate, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXIdentityOverlapConditioning, LoadImage, LTXIdentityOverlapConditioning, CropFace, INTConstant, CLIPTextEncode, TextInput_, StringConcatenate, PreviewAny, TextGenerate, StringConcatenate, PreviewAny, SplitStringByDelimiter, PreviewAny, TTP_text_mix, TextInput_, PreviewAny, RH_LLMAPI_NODE, TextInput_, LoadImage, LowVRAMCheckpointLoader, StringReplace, StringReplace, SaveVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 50, "width": 241}
---

# 视频生成/图生视频/LTX2.3 MSR+BestFaceID一致性增强_2075527517234094082.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2075527517234094082.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（49 个）：
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `EmptyLTXVLatentVideo`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `CreateVideo`
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `INTConstant`
- `LTXVAudioVAELoader`
- `LoadImage`
- `LTXICLoRALoaderModelOnly` ★核心
- `LiconMSR`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `StringConcatenate`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXIdentityOverlapConditioning`
- `LoadImage`
- `LTXIdentityOverlapConditioning`
- `CropFace`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `TextInput_`
- `StringConcatenate`
- `PreviewAny`
- `TextGenerate`
- `StringConcatenate`
- `PreviewAny`
- `SplitStringByDelimiter`
- `PreviewAny`
- `TTP_text_mix`
- `TextInput_`
- `PreviewAny`
- `RH_LLMAPI_NODE`
- `TextInput_`
- `LoadImage`
- `LowVRAMCheckpointLoader` ★核心
- `StringReplace`
- `StringReplace`
- `SaveVideo`

## 关键参数

- `width` = `241`
- `height` = `50`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **92%**（45/49）

**有卡**：`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`VAEDecode`、`SamplerCustomAdvanced`、`ManualSigmas`、`KSamplerSelect`、`RandomNoise`、`EmptyLTXVLatentVideo`、`CFGGuider`、`LTXVConcatAVLatent`、`CreateVideo`、`LoraLoaderModelOnly`、`INTConstant`、`LTXVAudioVAELoader`、`LoadImage`、`LTXICLoRALoaderModelOnly`、`LiconMSR`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVEmptyLatentAudio`、`StringConcatenate`、`LTXAVTextEncoderLoader`、`LTXAddVideoICLoRAGuide`、`LTXIdentityOverlapConditioning`、`CropFace`、`TextInput_`、`TextGenerate`、`SplitStringByDelimiter`、`TTP_text_mix`、`RH_LLMAPI_NODE`、`LowVRAMCheckpointLoader`、`StringReplace`、`SaveVideo`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
