---
key: 视频生成/图生视频/提示词反推｜LTX2.5数字人图生视频生成_2089831012640579585.json
name: 提示词反推｜LTX2.5数字人图生视频生成_2089831012640579585
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/提示词反推｜LTX2.5数字人图生视频生成_2089831012640579585.json
hash: 73212fc8c1704a9e
coverage: 0.850575
learned_at: 2026-10-16 22:02:36
nodes: [LTXVConcatAVLatent, SamplerCustomAdvanced, Reroute, SamplerCustomAdvanced, ResizeImagesByLongerEdge, LTXVPreprocess, RandomNoise, ManualSigmas, LTXVConcatAVLatent, SetLatentNoiseMask, LTXVAudioVAEEncode, ManualSigmas, Reroute, SolidMask, LTXVImgToVideoInplace, ConditioningZeroOut, CLIPLoader, LatentUpscaleModelLoader, ResizeImageMaskNode, EmptyLTXVLatentVideo, CreateVideo, LTXVAudioVAEDecode, VAELoader, VAELoader, LTXVConditioning, ComfyMathExpression, ComfyMathExpression, KSamplerSelect, KSamplerSelect, LTXVDualCFGGuider, LTXVSeparateAVLatent, LTXVSeparateAVLatent, VAEDecodeTiled, ComfyMathExpression, PromptRelaySmartEncode, LTXVDualCFGGuider, RandomNoise, ComfyMathExpression, AudioInfo, llama_cpp_parameters, llama_cpp_model_loader, llama_cpp_instruct_adv, PrimitiveStringMultiline, UNETLoader, easy cleanGpuUsed, LoadImage, LoadAudio, PrimitiveStringMultiline, PreviewAny, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, LTXVImgToVideoInplace, LTXVLatentUpsampler, TrimAudioDuration, SaveVideo, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/提示词反推｜LTX2.5数字人图生视频生成_2089831012640579585.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/提示词反推｜LTX2.5数字人图生视频生成_2089831012640579585.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（87 个）：
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
- `孤海注释`
- `孤海注释`
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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（74/87）

**有卡**：`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`RandomNoise`、`ManualSigmas`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`SolidMask`、`LTXVImgToVideoInplace`、`ConditioningZeroOut`、`CLIPLoader`、`LatentUpscaleModelLoader`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`CreateVideo`、`LTXVAudioVAEDecode`、`VAELoader`、`LTXVConditioning`、`ComfyMathExpression`、`KSamplerSelect`、`LTXVDualCFGGuider`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`PromptRelaySmartEncode`、`AudioInfo`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`UNETLoader`、`easy cleanGpuUsed`、`LoadImage`、`LoadAudio`、`PrimitiveBoolean`、`LTXVLatentUpsampler`、`TrimAudioDuration`、`SaveVideo`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
