---
key: 视频生成/图生视频/一致性加强版V1图生视频｜LTX2.5视频生成工作流_2088127153224380418.json
name: 一致性加强版V1图生视频｜LTX2.5视频生成工作流_2088127153224380418
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/一致性加强版V1图生视频｜LTX2.5视频生成工作流_2088127153224380418.json
hash: 7485a4dffc8c1026
coverage: 0.878378
learned_at: 2026-10-16 21:28:00
nodes: [PrimitiveInt, PrimitiveInt, PrimitiveInt, LTXVSeparateAVLatent, KSamplerSelect, ManualSigmas, LTXVConditioning, KSamplerSelect, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, RandomNoise, LTXVConcatAVLatent, RandomNoise, ResizeImageMaskNode, LTXVPreprocess, LTXVLatentUpsampler, ComfyMathExpression, ComfyMathExpression, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPTextEncode, CLIPTextEncode, VAELoader, VAELoader, CLIPLoader, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVImgToVideoInplace, LTXVImgToVideoInplace, LTXVDualCFGGuider, UNETLoader, LTXVDualCFGGuider, ManualSigmas, CR Text, LoadImage, PrimitiveBoolean, RH_LLMAPI_Pro_Node, PreviewAny, VHS_VideoCombine, LatentUpscaleModelLoader, ResolutionSelector, PrimitiveInt, CR Text, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/一致性加强版V1图生视频｜LTX2.5视频生成工作流_2088127153224380418.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/一致性加强版V1图生视频｜LTX2.5视频生成工作流_2088127153224380418.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（74 个）：
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `LTXVLatentUpsampler` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVImgToVideoInplace`
- `LTXVImgToVideoInplace`
- `LTXVDualCFGGuider`
- `UNETLoader` ★核心
- `LTXVDualCFGGuider`
- `ManualSigmas`
- `CR Text`
- `LoadImage`
- `PrimitiveBoolean`
- `RH_LLMAPI_Pro_Node`
- `PreviewAny`
- `VHS_VideoCombine`
- `LatentUpscaleModelLoader`
- `ResolutionSelector`
- `PrimitiveInt`
- `CR Text`
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

覆盖率 **88%**（65/74）

**有卡**：`LTXVSeparateAVLatent`、`KSamplerSelect`、`ManualSigmas`、`LTXVConditioning`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`RandomNoise`、`ResizeImageMaskNode`、`LTXVPreprocess`、`LTXVLatentUpsampler`、`CLIPTextEncode`、`VAELoader`、`CLIPLoader`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVImgToVideoInplace`、`LTXVDualCFGGuider`、`UNETLoader`、`CR Text`、`LoadImage`、`PrimitiveBoolean`、`RH_LLMAPI_Pro_Node`、`VHS_VideoCombine`、`LatentUpscaleModelLoader`、`ResolutionSelector`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
