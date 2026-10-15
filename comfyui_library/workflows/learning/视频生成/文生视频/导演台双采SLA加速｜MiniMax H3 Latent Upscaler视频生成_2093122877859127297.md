---
key: 视频生成/文生视频/导演台双采SLA加速｜MiniMax H3 Latent Upscaler视频生成_2093122877859127297.json
name: 导演台双采SLA加速｜MiniMax H3 Latent Upscaler视频生成_2093122877859127297
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/导演台双采SLA加速｜MiniMax H3 Latent Upscaler视频生成_2093122877859127297.json
hash: fefae22ca0cd4c49
coverage: 0.769231
learned_at: 2026-10-15 22:48:33
nodes: [KSamplerSelect, BasicGuider, ComfyMathExpression, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, easy clearCacheAll, SetNode, RandomNoise, VAEDecodeAudio, VAEDecode, easy cleanGpuUsed, GetNode, GetNode, SetNode, MiniMaxH3ImageToVideo, ImageScaleToMaxDimension, PrimitiveFloat, PrimitiveFloat, SamplerCustomAdvanced, MiniMaxH3SigmaShift, CLIPTextEncode, BasicScheduler, VisualizeSigmasKJ, RandomNoise, KSamplerSelect, LoadImage, VAELoader, VAELoader, CLIPLoader, VAELoader, VAELoader, SetNode, SetNode, LoraLoaderModelOnly, LTXAVTextEncoderLoader, VHS_VideoCombine, VHS_VideoCombine, SpectrumApplyMiniMaxH3, SolAttnPatch, UNETLoader, UNETLoader, LoraLoaderModelOnly, LTXVSpatioTemporalTiledVAEDecode, LTXVLoopingSampler, VAEEncodeTiled, LTXVConditioning, CFGGuider, ManualSigmas, LoraLoaderModelOnly, BasicScheduler, PathchSageAttentionKJ, LoadImage, ResizeImageMaskNode, ResizeImageMaskNode, SetNode, SetNode, ResolutionSelector, PrimitiveStringMultiline, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/导演台双采SLA加速｜MiniMax H3 Latent Upscaler视频生成_2093122877859127297.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/导演台双采SLA加速｜MiniMax H3 Latent Upscaler视频生成_2093122877859127297.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（91 个）：
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `easy clearCacheAll`
- `SetNode`
- `RandomNoise`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `SetNode`
- `MiniMaxH3ImageToVideo`
- `ImageScaleToMaxDimension`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3SigmaShift`
- `CLIPTextEncode` ★核心
- `BasicScheduler`
- `VisualizeSigmasKJ`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LoadImage`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SpectrumApplyMiniMaxH3`
- `SolAttnPatch`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVSpatioTemporalTiledVAEDecode` ★核心
- `LTXVLoopingSampler` ★核心
- `VAEEncodeTiled` ★核心
- `LTXVConditioning`
- `CFGGuider`
- `ManualSigmas`
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `PathchSageAttentionKJ`
- `LoadImage`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `SetNode`
- `SetNode`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
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
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
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

覆盖率 **77%**（70/91）

**有卡**：`KSamplerSelect`、`BasicGuider`、`ComfyMathExpression`、`easy clearCacheAll`、`RandomNoise`、`VAEDecodeAudio`、`VAEDecode`、`easy cleanGpuUsed`、`MiniMaxH3ImageToVideo`、`ImageScaleToMaxDimension`、`SamplerCustomAdvanced`、`MiniMaxH3SigmaShift`、`CLIPTextEncode`、`BasicScheduler`、`VisualizeSigmasKJ`、`LoadImage`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`LTXAVTextEncoderLoader`、`VHS_VideoCombine`、`SpectrumApplyMiniMaxH3`、`SolAttnPatch`、`UNETLoader`、`LTXVSpatioTemporalTiledVAEDecode`、`LTXVLoopingSampler`、`VAEEncodeTiled`、`LTXVConditioning`、`CFGGuider`、`ManualSigmas`、`PathchSageAttentionKJ`、`ResizeImageMaskNode`、`ResolutionSelector`、`KSampler`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
