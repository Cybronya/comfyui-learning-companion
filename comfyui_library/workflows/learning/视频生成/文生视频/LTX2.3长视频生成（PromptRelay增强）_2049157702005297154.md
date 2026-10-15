---
key: 视频生成/文生视频/LTX2.3长视频生成（PromptRelay增强）_2049157702005297154.json
name: LTX2.3长视频生成（PromptRelay增强）_2049157702005297154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3长视频生成（PromptRelay增强）_2049157702005297154.json
hash: 4c93b11ef8a2cd96
coverage: 0.884058
learned_at: 2026-10-15 22:45:14
nodes: [CFGGuider, LTXVLatentUpsampler, VAEDecodeTiled, SamplerCustomAdvanced, PrimitiveStringMultiline, UNETLoader, PathchSageAttentionKJ, VAELoaderKJ, DualCLIPLoader, ManualSigmas, LTXVConditioning, EmptyLTXVLatentVideo, LTXVConcatAVLatent, SolidMask, TrimAudioDuration, LTXVAudioVAEEncode, LTXVEmptyLatentAudio, SetLatentNoiseMask, ResizeImagesByLongerEdge, INTConstant, ResizeImageMaskNode, INTConstant, VHS_VideoCombine, llama_cpp_model_loader, VRAM_Debug, easy showAnything, Reroute, LTXVSeparateAVLatent, VAELoaderKJ, VAEDecode, VHS_VideoCombine, llama_cpp_instruct_adv, PrimitiveStringMultiline, Text Multiline, PrimitiveBoolean, LoadAudio, Switch any [Crystools], LTXVCropGuides, INTConstant, CM_IntToFloat, easy showAnything, CM_FloatToInt, PrimitiveBoolean, PrimitiveInt, CFGGuider, ComfyMathExpression, PrimitiveFloat, ManualSigmas, LTXVPreprocess, LoraLoaderModelOnly, LatentUpscaleModelLoader, LoadImage, CLIPTextEncode, LTXVAudioVAEDecode, KSamplerSelect, KSamplerSelect, LTXVImgToVideoInplace, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, ComfyMathExpression, ComfyMathExpression, LTXVImgToVideoInplace, MarkdownNote, PromptRelayEncodeTimeline, RandomNoise, RandomNoise, RTXVideoSuperResolution]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.3长视频生成（PromptRelay增强）_2049157702005297154.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3长视频生成（PromptRelay增强）_2049157702005297154.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（69 个）：
- `CFGGuider`
- `LTXVLatentUpsampler` ★核心
- `VAEDecodeTiled` ★核心
- `SamplerCustomAdvanced` ★核心
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `ManualSigmas`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `SolidMask`
- `TrimAudioDuration`
- `LTXVAudioVAEEncode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `SetLatentNoiseMask`
- `ResizeImagesByLongerEdge`
- `INTConstant`
- `ResizeImageMaskNode`
- `INTConstant`
- `VHS_VideoCombine`
- `llama_cpp_model_loader`
- `VRAM_Debug`
- `easy showAnything`
- `Reroute`
- `LTXVSeparateAVLatent`
- `VAELoaderKJ`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `llama_cpp_instruct_adv`
- `PrimitiveStringMultiline`
- `Text Multiline`
- `PrimitiveBoolean`
- `LoadAudio`
- `Switch any [Crystools]`
- `LTXVCropGuides`
- `INTConstant`
- `CM_IntToFloat`
- `easy showAnything`
- `CM_FloatToInt`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `CFGGuider`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `ManualSigmas`
- `LTXVPreprocess`
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVImgToVideoInplace`
- `MarkdownNote`
- `PromptRelayEncodeTimeline`
- `RandomNoise`
- `RandomNoise`
- `RTXVideoSuperResolution`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（61/69）

**有卡**：`CFGGuider`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`SamplerCustomAdvanced`、`UNETLoader`、`PathchSageAttentionKJ`、`VAELoaderKJ`、`DualCLIPLoader`、`ManualSigmas`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`SolidMask`、`TrimAudioDuration`、`LTXVAudioVAEEncode`、`LTXVEmptyLatentAudio`、`SetLatentNoiseMask`、`ResizeImagesByLongerEdge`、`INTConstant`、`ResizeImageMaskNode`、`VHS_VideoCombine`、`llama_cpp_model_loader`、`VRAM_Debug`、`LTXVSeparateAVLatent`、`VAEDecode`、`llama_cpp_instruct_adv`、`Text Multiline`、`PrimitiveBoolean`、`LoadAudio`、`Switch any [Crystools]`、`LTXVCropGuides`、`CM_IntToFloat`、`CM_FloatToInt`、`ComfyMathExpression`、`LTXVPreprocess`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`LoadImage`、`CLIPTextEncode`、`LTXVAudioVAEDecode`、`KSamplerSelect`、`LTXVImgToVideoInplace`、`PromptRelayEncodeTimeline`、`RandomNoise`、`RTXVideoSuperResolution`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
