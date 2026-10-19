---
key: 数字人/数字人/LTX2.5数字-agent调用版_2100471648406294530.json
name: LTX2.5数字-agent调用版_2100471648406294530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.5数字-agent调用版_2100471648406294530.json
hash: 606af9979dfacb14
coverage: 0.818182
learned_at: 2026-10-19 00:19:10
nodes: [MarkdownNote, LTXVConcatAVLatent, SamplerCustomAdvanced, Reroute, SamplerCustomAdvanced, PrimitiveInt, ComfyMathExpression, ResizeImagesByLongerEdge, LTXVPreprocess, RandomNoise, ManualSigmas, LTXVConcatAVLatent, SetLatentNoiseMask, LTXVAudioVAEEncode, LTXVImgToVideoInplace, LTXVLatentUpsampler, ManualSigmas, Reroute, SolidMask, PrimitiveInt, PrimitiveBoolean, MarkdownNote, LTXVImgToVideoInplace, PromptRelaySmartEncode, ConditioningZeroOut, UNETLoader, CLIPLoader, LatentUpscaleModelLoader, ResizeImageMaskNode, AudioInfo, ComfyMathExpression, EmptyLTXVLatentVideo, PrimitiveInt, PrimitiveInt, CreateVideo, LTXVAudioVAEDecode, VAELoader, VAELoader, LTXVConditioning, ComfyMathExpression, ComfyMathExpression, KSamplerSelect, KSamplerSelect, LTXVDualCFGGuider, RandomNoise, LTXVDualCFGGuider, LTXVSeparateAVLatent, LTXVSeparateAVLatent, VAEDecodeTiled, SaveVideo, TrimAudioDuration, LoadImage, PrimitiveStringMultiline, PrimitiveStringMultiline, LoadAudio]
patterns: []
missing: []
---

# 数字人/数字人/LTX2.5数字-agent调用版_2100471648406294530.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.5数字-agent调用版_2100471648406294530.json`

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
- `PromptRelaySmartEncode`
- `ConditioningZeroOut`
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
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `LoadAudio`

## 知识

覆盖率 **82%**（45/55）

**有卡**：`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`RandomNoise`、`ManualSigmas`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`SolidMask`、`PrimitiveBoolean`、`PromptRelaySmartEncode`、`ConditioningZeroOut`、`UNETLoader`、`CLIPLoader`、`LatentUpscaleModelLoader`、`ResizeImageMaskNode`、`AudioInfo`、`EmptyLTXVLatentVideo`、`CreateVideo`、`LTXVAudioVAEDecode`、`VAELoader`、`LTXVConditioning`、`KSamplerSelect`、`LTXVDualCFGGuider`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`SaveVideo`、`TrimAudioDuration`、`LoadImage`、`LoadAudio`

**用到的条目**：VAELoader、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider
