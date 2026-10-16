---
key: 视频生成/图生视频/LTX2.5数字人+提示词反推_2089579904223498242.json
name: LTX2.5数字人+提示词反推_2089579904223498242
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5数字人+提示词反推_2089579904223498242.json
hash: cd6657ba1c9125da
coverage: 0.816667
learned_at: 2026-10-16 22:02:00
nodes: [MarkdownNote, LTXVConcatAVLatent, SamplerCustomAdvanced, Reroute, SamplerCustomAdvanced, ResizeImagesByLongerEdge, LTXVPreprocess, RandomNoise, ManualSigmas, LTXVConcatAVLatent, SetLatentNoiseMask, LTXVAudioVAEEncode, ManualSigmas, Reroute, SolidMask, LTXVImgToVideoInplace, ConditioningZeroOut, CLIPLoader, LatentUpscaleModelLoader, ResizeImageMaskNode, EmptyLTXVLatentVideo, CreateVideo, LTXVAudioVAEDecode, VAELoader, VAELoader, LTXVConditioning, ComfyMathExpression, ComfyMathExpression, KSamplerSelect, KSamplerSelect, LTXVDualCFGGuider, LTXVSeparateAVLatent, LTXVSeparateAVLatent, VAEDecodeTiled, ComfyMathExpression, PromptRelaySmartEncode, LTXVDualCFGGuider, RandomNoise, ComfyMathExpression, AudioInfo, llama_cpp_parameters, MarkdownNote, llama_cpp_model_loader, llama_cpp_instruct_adv, PrimitiveStringMultiline, UNETLoader, easy cleanGpuUsed, LoadImage, LoadAudio, PrimitiveStringMultiline, PreviewAny, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, LTXVImgToVideoInplace, LTXVLatentUpsampler, TrimAudioDuration, SaveVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.5数字人+提示词反推_2089579904223498242.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5数字人+提示词反推_2089579904223498242.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `MarkdownNote`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `RandomNoise`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `ManualSigmas`
- `Reroute`
- `SolidMask`
- `LTXVImgToVideoInplace`
- `ConditioningZeroOut`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `ResizeImageMaskNode`
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
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `ComfyMathExpression`
- `PromptRelaySmartEncode`
- `LTXVDualCFGGuider`
- `RandomNoise`
- `ComfyMathExpression`
- `AudioInfo`
- `llama_cpp_parameters`
- `MarkdownNote`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `easy cleanGpuUsed`
- `LoadImage`
- `LoadAudio`
- `PrimitiveStringMultiline`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `TrimAudioDuration`
- `SaveVideo`

## 知识

覆盖率 **82%**（49/60）

**有卡**：`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`RandomNoise`、`ManualSigmas`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`SolidMask`、`LTXVImgToVideoInplace`、`ConditioningZeroOut`、`CLIPLoader`、`LatentUpscaleModelLoader`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`CreateVideo`、`LTXVAudioVAEDecode`、`VAELoader`、`LTXVConditioning`、`ComfyMathExpression`、`KSamplerSelect`、`LTXVDualCFGGuider`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`PromptRelaySmartEncode`、`AudioInfo`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`UNETLoader`、`easy cleanGpuUsed`、`LoadImage`、`LoadAudio`、`PrimitiveBoolean`、`LTXVLatentUpsampler`、`TrimAudioDuration`、`SaveVideo`

**用到的条目**：VAELoader、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider
