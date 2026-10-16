---
key: 视频生成/图生视频/二次采样视频生成｜LTX2.5图生视频人物运镜直出_2089489478942547970.json
name: 二次采样视频生成｜LTX2.5图生视频人物运镜直出_2089489478942547970
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/二次采样视频生成｜LTX2.5图生视频人物运镜直出_2089489478942547970.json
hash: 81194b2c0930af6e
coverage: 0.871795
learned_at: 2026-10-16 22:02:24
nodes: [CLIPTextEncode, KSamplerSelect, PrimitiveInt, UNETLoader, VAELoader, PrimitiveInt, CLIPLoader, ResizeImageMaskNode, EmptyLTXVLatentVideo, ComfySwitchNode, LTXVConditioning, LTXVConcatAVLatent, LTXVDualCFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoInplace, PurgeVRAM_UTK, LTXVConcatAVLatent, RandomNoise, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, SamplerCustomAdvanced, CreateVideo, SaveVideo, CLIPTextEncode, LTXVDualCFGGuider, PrimitiveStringMultiline, PrimitiveInt, PrimitiveInt, ResolutionSelector, VAELoader, CLIPLoader, PrimitiveBoolean, LTXVPreprocess, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, LTXVEmptyLatentAudio, RandomNoise, TextGenerateLTX2Prompt, LTXVImgToVideoInplace, LatentUpscaleModelLoader, ManualSigmas, LoadImage, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/二次采样视频生成｜LTX2.5图生视频人物运镜直出_2089489478942547970.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/二次采样视频生成｜LTX2.5图生视频人物运镜直出_2089489478942547970.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（78 个）：
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `PrimitiveInt`
- `UNETLoader` ★核心
- `VAELoader`
- `PrimitiveInt`
- `CLIPLoader`
- `ResizeImageMaskNode`
- `EmptyLTXVLatentVideo`
- `ComfySwitchNode`
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `PurgeVRAM_UTK`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `LTXVDualCFGGuider`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `PrimitiveInt`
- `ResolutionSelector`
- `VAELoader`
- `CLIPLoader`
- `PrimitiveBoolean`
- `LTXVPreprocess`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `RandomNoise`
- `TextGenerateLTX2Prompt`
- `LTXVImgToVideoInplace`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `LoadImage`
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

覆盖率 **87%**（68/78）

**有卡**：`CLIPTextEncode`、`KSamplerSelect`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`LTXVConcatAVLatent`、`LTXVDualCFGGuider`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`PurgeVRAM_UTK`、`RandomNoise`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`SaveVideo`、`ResolutionSelector`、`PrimitiveBoolean`、`LTXVPreprocess`、`ComfyMathExpression`、`LTXVEmptyLatentAudio`、`TextGenerateLTX2Prompt`、`LatentUpscaleModelLoader`、`LoadImage`、`LoraLoaderModelOnly`、`KSampler`、`solarL_SaveImagesToZip`、`VAEDecode`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
