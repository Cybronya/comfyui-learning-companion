---
key: 视频生成/图生视频/I2V首帧图直出片｜LTX-2.5图生视频音画同步_2093777187555074049.json
name: I2V首帧图直出片｜LTX-2.5图生视频音画同步_2093777187555074049
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/I2V首帧图直出片｜LTX-2.5图生视频音画同步_2093777187555074049.json
hash: 2249e4e6e7edf260
coverage: 0.8625
learned_at: 2026-10-16 23:42:00
nodes: [SaveVideo, ResolutionSelector, CLIPLoader, TextGenerateLTX2Prompt, PrimitiveBoolean, CLIPTextEncode, PrimitiveStringMultiline, ComfySwitchNode, UNETLoader, PreviewAny, PrimitiveInt, PrimitiveBoolean, LTXVConditioning, VAELoader, VAELoader, PrimitiveInt, CLIPTextEncode, CLIPLoader, PrimitiveInt, KSamplerSelect, RandomNoise, ManualSigmas, PrimitiveInt, LatentUpscaleModelLoader, LTXVDualCFGGuider, SamplerCustomAdvanced, LTXVImgToVideoInplace, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LTXVConcatAVLatent, ComfyMathExpression, ComfyMathExpression, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVLatentUpsampler, LTXVImgToVideoInplace, ComfyMathExpression, ComfyMathExpression, RandomNoise, LTXVConcatAVLatent, ManualSigmas, LTXVDualCFGGuider, KSamplerSelect, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, ImageFromBatch, SaveImage, SaveAudio, VHS_VideoCombine, LoadImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/I2V首帧图直出片｜LTX-2.5图生视频音画同步_2093777187555074049.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/I2V首帧图直出片｜LTX-2.5图生视频音画同步_2093777187555074049.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（80 个）：
- `SaveVideo`
- `ResolutionSelector`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `PreviewAny`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `LTXVConditioning`
- `VAELoader`
- `VAELoader`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `PrimitiveInt`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `ManualSigmas`
- `PrimitiveInt`
- `LatentUpscaleModelLoader`
- `LTXVDualCFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplace`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `ImageFromBatch`
- `SaveImage`
- `SaveAudio`
- `VHS_VideoCombine`
- `LoadImage`
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

覆盖率 **86%**（69/80）

**有卡**：`SaveVideo`、`ResolutionSelector`、`CLIPLoader`、`TextGenerateLTX2Prompt`、`PrimitiveBoolean`、`CLIPTextEncode`、`UNETLoader`、`LTXVConditioning`、`VAELoader`、`KSamplerSelect`、`RandomNoise`、`ManualSigmas`、`LatentUpscaleModelLoader`、`LTXVDualCFGGuider`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`ComfyMathExpression`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`ImageFromBatch`、`SaveImage`、`SaveAudio`、`VHS_VideoCombine`、`LoadImage`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
