---
key: 视频生成/文生视频/双采文生图生视频｜ltx2.5视频生成工作流_2088134700161396737.json
name: 双采文生图生视频｜ltx2.5视频生成工作流_2088134700161396737
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/双采文生图生视频｜ltx2.5视频生成工作流_2088134700161396737.json
hash: c4067fe15d58dfea
coverage: 0.813953
learned_at: 2026-10-11 20:53:53
nodes: [LTXVAudioVAEDecode, LTXFloatToInt, LTXVEmptyLatentAudio, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, ComfySwitchNode, ComfySwitchNode, PrimitiveStringMultiline, LTXVAudioVAEDecode, CreateVideo, VAEDecodeTiled, LTXVPreprocess, LTXFloatToInt, ComfySwitchNode, ComfySwitchNode, PrimitiveFloat, ManualSigmas, KSamplerSelect, CFGGuider, RandomNoise, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, PrimitiveFloat, PrimitiveFloat, PrimitiveInt, ComfyMathExpression, RandomNoise, LTXVImgToVideoInplace, CFGGuider, KSamplerSelect, LTXVLatentUpsampler, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, PrimitiveFloat, PrimitiveInt, ComfyMathExpression, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXVSeparateAVLatent, SamplerCustomAdvanced, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, RandomNoise, CFGGuider, ManualSigmas, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVConcatAVLatent, KSamplerSelect, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPLoader, CLIPLoader, LatentUpscaleModelLoader, UNETLoader, VAELoader, PrimitiveFloat, VAELoader, ResizeImageMaskNode, ComfyNotNode, PrimitiveBoolean, LTXVImgToVideoInplace, SaveVideo, PrimitiveFloat, LoadImage, ComfyNotNode, VAELoader, PrimitiveStringMultiline, PrimitiveStringMultiline, VAELoader, LatentUpscaleModelLoader, PrimitiveFloat, PrimitiveFloat, PrimitiveBoolean, LTXVImgToVideoInplace, ResizeImageMaskNode, LTXVPreprocess, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), EmptyLTXVLatentVideo, EmptyLTXVLatentVideo, Fast Groups Bypasser (rgthree), CLIPLoader, CLIPLoader, LoadImage, VAEDecodeTiled, CreateVideo, SaveVideo, UNETLoader, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/双采文生图生视频｜ltx2.5视频生成工作流_2088134700161396737.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/双采文生图生视频｜ltx2.5视频生成工作流_2088134700161396737.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（129 个）：
- `LTXVAudioVAEDecode` ★核心
- `LTXFloatToInt`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `LTXVPreprocess`
- `LTXFloatToInt`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PrimitiveFloat`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveInt`
- `ComfyMathExpression`
- `RandomNoise`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVLatentUpsampler` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `TextGenerateLTX2Prompt`
- `TextGenerateLTX2Prompt`
- `TextGenerateLTX2Prompt`
- `TextGenerateLTX2Prompt`
- `PrimitiveFloat`
- `PrimitiveInt`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `CFGGuider`
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CLIPLoader`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `PrimitiveFloat`
- `VAELoader`
- `ResizeImageMaskNode`
- `ComfyNotNode`
- `PrimitiveBoolean`
- `LTXVImgToVideoInplace`
- `SaveVideo`
- `PrimitiveFloat`
- `LoadImage`
- `ComfyNotNode`
- `VAELoader`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveBoolean`
- `LTXVImgToVideoInplace`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `EmptyLTXVLatentVideo`
- `EmptyLTXVLatentVideo`
- `Fast Groups Bypasser (rgthree)`
- `CLIPLoader`
- `CLIPLoader`
- `LoadImage`
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `SaveVideo`
- `UNETLoader` ★核心
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

覆盖率 **81%**（105/129）

**有卡**：`LTXVAudioVAEDecode`、`LTXFloatToInt`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`CreateVideo`、`VAEDecodeTiled`、`LTXVPreprocess`、`ManualSigmas`、`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`CLIPTextEncode`、`LTXVConditioning`、`ComfyMathExpression`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`TextGenerateLTX2Prompt`、`CLIPLoader`、`LatentUpscaleModelLoader`、`UNETLoader`、`VAELoader`、`ResizeImageMaskNode`、`ComfyNotNode`、`PrimitiveBoolean`、`SaveVideo`、`LoadImage`、`EmptyLTXVLatentVideo`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
