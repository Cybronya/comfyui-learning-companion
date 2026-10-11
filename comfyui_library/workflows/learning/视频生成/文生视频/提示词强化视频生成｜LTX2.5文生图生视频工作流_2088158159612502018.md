---
key: 视频生成/文生视频/提示词强化视频生成｜LTX2.5文生图生视频工作流_2088158159612502018.json
name: 提示词强化视频生成｜LTX2.5文生图生视频工作流_2088158159612502018
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/提示词强化视频生成｜LTX2.5文生图生视频工作流_2088158159612502018.json
hash: 254467251a0fd1b0
coverage: 0.853333
learned_at: 2026-10-11 20:53:54
nodes: [UNETLoader, LTXVConditioning, VAELoader, VAELoader, CLIPTextEncode, KSamplerSelect, LatentUpscaleModelLoader, LTXVDualCFGGuider, SamplerCustomAdvanced, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, ResizeImageMaskNode, ComfyMathExpression, ComfyMathExpression, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, RandomNoise, ManualSigmas, LTXVDualCFGGuider, KSamplerSelect, LTXVSeparateAVLatent, PrimitiveInt, CLIPTextEncode, LTXVPreprocess, PreviewAny, LTXVAudioVAEDecode, RandomNoise, ManualSigmas, LTXVConcatAVLatent, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVImgToVideoInplace, ComfySwitchNode, PrimitiveBoolean, TextGenerateLTX2Prompt, VAEDecodeTiled, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, PrimitiveStringMultiline, LoadImage, PrimitiveBoolean, CLIPLoader, CLIPLoader, PrimitiveInt, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/提示词强化视频生成｜LTX2.5文生图生视频工作流_2088158159612502018.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/提示词强化视频生成｜LTX2.5文生图生视频工作流_2088158159612502018.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（75 个）：
- `UNETLoader` ★核心
- `LTXVConditioning`
- `VAELoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `LatentUpscaleModelLoader`
- `LTXVDualCFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `RandomNoise`
- `ManualSigmas`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `PreviewAny`
- `LTXVAudioVAEDecode` ★核心
- `RandomNoise`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplace`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `TextGenerateLTX2Prompt`
- `VAEDecodeTiled` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `LoadImage`
- `PrimitiveBoolean`
- `CLIPLoader`
- `CLIPLoader`
- `PrimitiveInt`
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

覆盖率 **85%**（64/75）

**有卡**：`UNETLoader`、`LTXVConditioning`、`VAELoader`、`CLIPTextEncode`、`KSamplerSelect`、`LatentUpscaleModelLoader`、`LTXVDualCFGGuider`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`ResizeImageMaskNode`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`RandomNoise`、`ManualSigmas`、`LTXVPreprocess`、`LTXVAudioVAEDecode`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`PrimitiveBoolean`、`TextGenerateLTX2Prompt`、`VAEDecodeTiled`、`VHS_VideoCombine`、`LoadImage`、`CLIPLoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
