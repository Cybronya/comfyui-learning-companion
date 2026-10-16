---
key: 视频生成/图生视频/标准版图生视频工作流｜LTX2.5图片转视频工作流_2088108490068946945.json
name: 标准版图生视频工作流｜LTX2.5图片转视频工作流_2088108490068946945
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/标准版图生视频工作流｜LTX2.5图片转视频工作流_2088108490068946945.json
hash: e247f419a4d25184
coverage: 0.878378
learned_at: 2026-10-16 21:28:13
nodes: [KSamplerSelect, ComfyMathExpression, ComfyMathExpression, ResizeImageMaskNode, ComfyMathExpression, ComfyMathExpression, LTXVImgToVideoInplace, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, PrimitiveInt, UNETLoader, VAELoader, VAELoader, CLIPLoader, LatentUpscaleModelLoader, LTXVDualCFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, LTXVLatentUpsampler, LTXVConcatAVLatent, ManualSigmas, LTXVDualCFGGuider, RandomNoise, LTXVSeparateAVLatent, PrimitiveInt, ResolutionSelector, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVConcatAVLatent, CR Text, LoadImage, LTXVPreprocess, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, VHS_VideoCombine, CR Text, RH_LLMAPI_Pro_Node, PreviewAny, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/标准版图生视频工作流｜LTX2.5图片转视频工作流_2088108490068946945.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/标准版图生视频工作流｜LTX2.5图片转视频工作流_2088108490068946945.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（74 个）：
- `KSamplerSelect` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVImgToVideoInplace`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `LTXVDualCFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `LTXVDualCFGGuider`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `PrimitiveInt`
- `ResolutionSelector`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `CR Text`
- `LoadImage`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `CR Text`
- `RH_LLMAPI_Pro_Node`
- `PreviewAny`
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

**有卡**：`KSamplerSelect`、`ComfyMathExpression`、`ResizeImageMaskNode`、`LTXVImgToVideoInplace`、`PrimitiveBoolean`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LatentUpscaleModelLoader`、`LTXVDualCFGGuider`、`RandomNoise`、`ManualSigmas`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`ResolutionSelector`、`CLIPTextEncode`、`LTXVConditioning`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`CR Text`、`LoadImage`、`LTXVPreprocess`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`RH_LLMAPI_Pro_Node`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
