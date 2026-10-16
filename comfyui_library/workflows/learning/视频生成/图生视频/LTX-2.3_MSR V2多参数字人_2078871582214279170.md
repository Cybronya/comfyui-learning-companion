---
key: 视频生成/图生视频/LTX-2.3_MSR V2多参数字人_2078871582214279170.json
name: LTX-2.3_MSR V2多参数字人_2078871582214279170.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2078871582214279170.json
hash: 05e50028fb1b0be0
coverage: 0.926829
learned_at: 2026-10-15 22:41:56
nodes: [LowVRAMCheckpointLoader, LTXAVTextEncoderLoader, CLIPTextEncode, LTXVConditioning, LTX2_NAG, LTXVAudioVAEDecode, LTXVSeparateAVLatent, LTXVConcatAVLatent, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, PromptRelayEncode, CreateVideo, ComfyMathExpression, VAEDecode, LoadImage, ManualSigmas, LTXVCropGuides, LTXAddVideoICLoRAGuide, EmptyLTXVLatentVideo, TrimAudioDuration, AudioInfo, ComfyMathExpression, INTConstant, INTConstant, LTXICLoRALoaderModelOnly, LTXVAudioVAELoader, LiconMSR, LoadImage, LoadImage, PrimitiveInt, RandomNoise, SetLatentNoiseMask, LTXVAudioVAEEncode, SolidMask, SaveVideo, PrimitiveStringMultiline, PrimitiveStringMultiline, LoadImage, LoadImage, LoadAudio]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors"}
---

# 视频生成/图生视频/LTX-2.3_MSR V2多参数字人_2078871582214279170.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2078871582214279170.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（41 个）：
- `LowVRAMCheckpointLoader` ★核心
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTX2_NAG`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `PromptRelayEncode`
- `CreateVideo`
- `ComfyMathExpression`
- `VAEDecode` ★核心
- `LoadImage`
- `ManualSigmas`
- `LTXVCropGuides`
- `LTXAddVideoICLoRAGuide`
- `EmptyLTXVLatentVideo`
- `TrimAudioDuration`
- `AudioInfo`
- `ComfyMathExpression`
- `INTConstant`
- `INTConstant`
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `LiconMSR`
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`
- `RandomNoise`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `SaveVideo`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `LoadAudio`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **93%**（38/41）

**有卡**：`LowVRAMCheckpointLoader`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`LTXVConditioning`、`LTX2_NAG`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`PromptRelayEncode`、`CreateVideo`、`ComfyMathExpression`、`VAEDecode`、`LoadImage`、`ManualSigmas`、`LTXVCropGuides`、`LTXAddVideoICLoRAGuide`、`EmptyLTXVLatentVideo`、`TrimAudioDuration`、`AudioInfo`、`INTConstant`、`LTXICLoRALoaderModelOnly`、`LTXVAudioVAELoader`、`LiconMSR`、`RandomNoise`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`SolidMask`、`SaveVideo`、`LoadAudio`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent
