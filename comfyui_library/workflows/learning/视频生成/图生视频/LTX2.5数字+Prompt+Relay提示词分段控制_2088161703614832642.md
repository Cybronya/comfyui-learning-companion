---
key: 视频生成/图生视频/LTX2.5数字+Prompt+Relay提示词分段控制_2088161703614832642.json
name: LTX2.5数字+Prompt+Relay提示词分段控制_2088161703614832642
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5数字+Prompt+Relay提示词分段控制_2088161703614832642.json
hash: 534c95cb03d32f56
coverage: 0.818182
learned_at: 2026-10-16 21:27:37
nodes: [MarkdownNote, LTXVConcatAVLatent, SamplerCustomAdvanced, Reroute, SamplerCustomAdvanced, PrimitiveInt, ComfyMathExpression, ResizeImagesByLongerEdge, LTXVPreprocess, RandomNoise, ManualSigmas, LTXVConcatAVLatent, SetLatentNoiseMask, LTXVAudioVAEEncode, LTXVImgToVideoInplace, LTXVLatentUpsampler, ManualSigmas, Reroute, SolidMask, PrimitiveInt, PrimitiveBoolean, MarkdownNote, LTXVImgToVideoInplace, PrimitiveStringMultiline, LoadAudio, PromptRelaySmartEncode, ConditioningZeroOut, PrimitiveStringMultiline, UNETLoader, CLIPLoader, LatentUpscaleModelLoader, ResizeImageMaskNode, AudioInfo, ComfyMathExpression, EmptyLTXVLatentVideo, CreateVideo, LTXVAudioVAEDecode, VAELoader, VAELoader, LTXVConditioning, ComfyMathExpression, ComfyMathExpression, KSamplerSelect, KSamplerSelect, LTXVDualCFGGuider, RandomNoise, LTXVDualCFGGuider, LTXVSeparateAVLatent, LTXVSeparateAVLatent, VAEDecodeTiled, TrimAudioDuration, LoadImage, PrimitiveInt, PrimitiveInt, SaveVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.5数字+Prompt+Relay提示词分段控制_2088161703614832642.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5数字+Prompt+Relay提示词分段控制_2088161703614832642.json`

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
- `TrimAudioDuration`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `SaveVideo`

## 知识

覆盖率 **82%**（45/55）

**有卡**：`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`RandomNoise`、`ManualSigmas`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`SolidMask`、`PrimitiveBoolean`、`LoadAudio`、`PromptRelaySmartEncode`、`ConditioningZeroOut`、`UNETLoader`、`CLIPLoader`、`LatentUpscaleModelLoader`、`ResizeImageMaskNode`、`AudioInfo`、`EmptyLTXVLatentVideo`、`CreateVideo`、`LTXVAudioVAEDecode`、`VAELoader`、`LTXVConditioning`、`KSamplerSelect`、`LTXVDualCFGGuider`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`TrimAudioDuration`、`LoadImage`、`SaveVideo`

**用到的条目**：VAELoader、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider
