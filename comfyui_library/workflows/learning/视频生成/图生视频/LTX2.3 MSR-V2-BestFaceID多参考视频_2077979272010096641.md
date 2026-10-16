---
key: 视频生成/图生视频/LTX2.3 MSR-V2-BestFaceID多参考视频_2077979272010096641.json
name: LTX2.3 MSR-V2-BestFaceID多参考视频_2077979272010096641.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2077979272010096641.json
hash: 97477d2bd01134a9
coverage: 0.923077
learned_at: 2026-10-15 22:41:47
nodes: [LTXVAudioVAEDecode, LTXVSeparateAVLatent, VAEDecode, SamplerCustomAdvanced, KSamplerSelect, RandomNoise, INTConstant, INTConstant, LTXVAudioVAELoader, StringConcatenate, INTConstant, TextInput_, StringConcatenate, PreviewAny, PreviewAny, PreviewAny, TTP_text_mix, TextInput_, PreviewAny, StringReplace, StringReplace, CreateVideo, RH_LLMAPI_NODE, TextInput_, LoadImage, LoadImage, LTXVEmptyLatentAudio, LiconMSR, StringConcatenate, SplitStringByDelimiter, TextGenerate, LTXAVTextEncoderLoader, LowVRAMCheckpointLoader, LTXICLoRALoaderModelOnly, LTXVCropGuides, EmptyLTXVLatentVideo, ManualSigmas, CropFace, LTXIdentityOverlapConditioning, CFGGuider, CropFace, LoadImage, SaveVideo, CLIPTextEncode, LTXVConcatAVLatent, LTXIdentityOverlapConditioning, LTX2_NAG, LTXAddVideoICLoRAGuide, LTXVConditioning, CLIPTextEncode, LoraLoaderModelOnly, PromptRelayEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 50, "width": 241}
---

# 视频生成/图生视频/LTX2.3 MSR-V2-BestFaceID多参考视频_2077979272010096641.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2077979272010096641.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（52 个）：
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `INTConstant`
- `INTConstant`
- `LTXVAudioVAELoader`
- `StringConcatenate`
- `INTConstant`
- `TextInput_`
- `StringConcatenate`
- `PreviewAny`
- `PreviewAny`
- `PreviewAny`
- `TTP_text_mix`
- `TextInput_`
- `PreviewAny`
- `StringReplace`
- `StringReplace`
- `CreateVideo`
- `RH_LLMAPI_NODE`
- `TextInput_`
- `LoadImage`
- `LoadImage`
- `LTXVEmptyLatentAudio` ★核心
- `LiconMSR`
- `StringConcatenate`
- `SplitStringByDelimiter`
- `TextGenerate`
- `LTXAVTextEncoderLoader`
- `LowVRAMCheckpointLoader` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXVCropGuides`
- `EmptyLTXVLatentVideo`
- `ManualSigmas`
- `CropFace`
- `LTXIdentityOverlapConditioning`
- `CFGGuider`
- `CropFace`
- `LoadImage`
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `LTXIdentityOverlapConditioning`
- `LTX2_NAG`
- `LTXAddVideoICLoRAGuide`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PromptRelayEncode`

## 关键参数

- `width` = `241`
- `height` = `50`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **92%**（48/52）

**有卡**：`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`VAEDecode`、`SamplerCustomAdvanced`、`KSamplerSelect`、`RandomNoise`、`INTConstant`、`LTXVAudioVAELoader`、`StringConcatenate`、`TextInput_`、`TTP_text_mix`、`StringReplace`、`CreateVideo`、`RH_LLMAPI_NODE`、`LoadImage`、`LTXVEmptyLatentAudio`、`LiconMSR`、`SplitStringByDelimiter`、`TextGenerate`、`LTXAVTextEncoderLoader`、`LowVRAMCheckpointLoader`、`LTXICLoRALoaderModelOnly`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`ManualSigmas`、`CropFace`、`LTXIdentityOverlapConditioning`、`CFGGuider`、`SaveVideo`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`LTX2_NAG`、`LTXAddVideoICLoRAGuide`、`LTXVConditioning`、`LoraLoaderModelOnly`、`PromptRelayEncode`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
