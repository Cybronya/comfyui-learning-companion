---
key: 视频生成/图生视频/数字Prompt+Relay提示词分段控制｜LTX2.5图生视频工作流_2088361067079618561.json
name: 数字Prompt+Relay提示词分段控制｜LTX2.5图生视频工作流_2088361067079618561
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/数字Prompt+Relay提示词分段控制｜LTX2.5图生视频工作流_2088361067079618561.json
hash: cafc25ab9997f602
coverage: 0.85
learned_at: 2026-10-16 21:43:55
nodes: [LTXVConcatAVLatent, SamplerCustomAdvanced, Reroute, SamplerCustomAdvanced, PrimitiveInt, ComfyMathExpression, ResizeImagesByLongerEdge, LTXVPreprocess, RandomNoise, ManualSigmas, LTXVConcatAVLatent, SetLatentNoiseMask, LTXVAudioVAEEncode, LTXVImgToVideoInplace, LTXVLatentUpsampler, ManualSigmas, Reroute, SolidMask, PrimitiveInt, PrimitiveBoolean, LTXVImgToVideoInplace, PrimitiveStringMultiline, LoadAudio, PromptRelaySmartEncode, ConditioningZeroOut, PrimitiveStringMultiline, UNETLoader, CLIPLoader, LatentUpscaleModelLoader, ResizeImageMaskNode, AudioInfo, ComfyMathExpression, EmptyLTXVLatentVideo, CreateVideo, LTXVAudioVAEDecode, VAELoader, VAELoader, LTXVConditioning, ComfyMathExpression, ComfyMathExpression, KSamplerSelect, KSamplerSelect, LTXVDualCFGGuider, RandomNoise, LTXVDualCFGGuider, LTXVSeparateAVLatent, LTXVSeparateAVLatent, VAEDecodeTiled, TrimAudioDuration, LoadImage, PrimitiveInt, PrimitiveInt, SaveVideo, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/数字Prompt+Relay提示词分段控制｜LTX2.5图生视频工作流_2088361067079618561.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/数字Prompt+Relay提示词分段控制｜LTX2.5图生视频工作流_2088361067079618561.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（80 个）：
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
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **85%**（68/80）

**有卡**：`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`RandomNoise`、`ManualSigmas`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`SolidMask`、`PrimitiveBoolean`、`LoadAudio`、`PromptRelaySmartEncode`、`ConditioningZeroOut`、`UNETLoader`、`CLIPLoader`、`LatentUpscaleModelLoader`、`ResizeImageMaskNode`、`AudioInfo`、`EmptyLTXVLatentVideo`、`CreateVideo`、`LTXVAudioVAEDecode`、`VAELoader`、`LTXVConditioning`、`KSamplerSelect`、`LTXVDualCFGGuider`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`TrimAudioDuration`、`LoadImage`、`SaveVideo`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
