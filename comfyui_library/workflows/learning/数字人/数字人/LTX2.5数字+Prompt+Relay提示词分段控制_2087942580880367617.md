---
key: 数字人/数字人/LTX2.5数字+Prompt+Relay提示词分段控制_2087942580880367617.json
name: LTX2.5数字+Prompt+Relay提示词分段控制_2087942580880367617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.5数字+Prompt+Relay提示词分段控制_2087942580880367617.json
hash: 7d160e1f401e204c
coverage: 0.818182
learned_at: 2026-10-18 19:07:42
nodes: [MarkdownNote, LTXVConcatAVLatent, SamplerCustomAdvanced, Reroute, SamplerCustomAdvanced, PrimitiveInt, ComfyMathExpression, ResizeImagesByLongerEdge, LTXVPreprocess, RandomNoise, ManualSigmas, LTXVConcatAVLatent, SetLatentNoiseMask, LTXVAudioVAEEncode, LTXVImgToVideoInplace, LTXVLatentUpsampler, ManualSigmas, Reroute, SolidMask, PrimitiveInt, PrimitiveBoolean, MarkdownNote, LTXVImgToVideoInplace, PrimitiveStringMultiline, LoadAudio, PromptRelaySmartEncode, ConditioningZeroOut, PrimitiveStringMultiline, UNETLoader, CLIPLoader, LatentUpscaleModelLoader, ResizeImageMaskNode, AudioInfo, ComfyMathExpression, EmptyLTXVLatentVideo, PrimitiveInt, PrimitiveInt, CreateVideo, LTXVAudioVAEDecode, VAELoader, VAELoader, LTXVConditioning, ComfyMathExpression, ComfyMathExpression, KSamplerSelect, KSamplerSelect, LTXVDualCFGGuider, RandomNoise, LTXVDualCFGGuider, LTXVSeparateAVLatent, LTXVSeparateAVLatent, VAEDecodeTiled, SaveVideo, TrimAudioDuration, LoadImage]
patterns: []
missing: []
---

# 数字人/数字人/LTX2.5数字+Prompt+Relay提示词分段控制_2087942580880367617.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.5数字+Prompt+Relay提示词分段控制_2087942580880367617.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `MarkdownNote`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveInt`
- `ComfyMathExpression`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `RandomNoise`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `ManualSigmas`
- `Reroute`
- `SolidMask`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `MarkdownNote`
- `LTXVImgToVideoInplace`
- `PrimitiveStringMultiline`
- `LoadAudio`
- `PromptRelaySmartEncode`
- `ConditioningZeroOut`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `ResizeImageMaskNode`
- `AudioInfo`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `PrimitiveInt`
- `PrimitiveInt`
- `CreateVideo`
- `LTXVAudioVAEDecode` ★核心
- `VAELoader`
- `VAELoader`
- `LTXVConditioning`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `LTXVDualCFGGuider`
- `RandomNoise`
- `LTXVDualCFGGuider`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `SaveVideo`
- `TrimAudioDuration`
- `LoadImage`

## 知识

覆盖率 **82%**（45/55）

**有卡**：`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`RandomNoise`、`ManualSigmas`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`SolidMask`、`PrimitiveBoolean`、`LoadAudio`、`PromptRelaySmartEncode`、`ConditioningZeroOut`、`UNETLoader`、`CLIPLoader`、`LatentUpscaleModelLoader`、`ResizeImageMaskNode`、`AudioInfo`、`EmptyLTXVLatentVideo`、`CreateVideo`、`LTXVAudioVAEDecode`、`VAELoader`、`LTXVConditioning`、`KSamplerSelect`、`LTXVDualCFGGuider`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`SaveVideo`、`TrimAudioDuration`、`LoadImage`

**用到的条目**：VAELoader、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider
