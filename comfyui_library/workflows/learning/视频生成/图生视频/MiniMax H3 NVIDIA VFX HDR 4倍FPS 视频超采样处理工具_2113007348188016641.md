---
key: 视频生成/图生视频/MiniMax H3 NVIDIA VFX HDR 4倍FPS 视频超采样处理工具_2113007348188016641.json
name: MiniMax H3 NVIDIA VFX HDR 4倍FPS 视频超采样处理工具_2113007348188016641
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3 NVIDIA VFX HDR 4倍FPS 视频超采样处理工具_2113007348188016641.json
hash: 86700ff7a07b818d
coverage: 0.931507
learned_at: 2026-10-26 22:12:16
nodes: [MiniMaxH3SigmaShift, ResolutionSelector, PrimitiveFloat, ComfyMathExpression, RandomNoise, MiniMaxH3ReferenceToVideo, BasicGuider, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, CreateVideo, KSamplerSelect, BasicScheduler, RandomNoise, SamplerCustomAdvanced, CreateVideo, CLIPLoader, VAELoader, VAELoader, BasicGuider, LTXVConcatAVLatent, UNETLoader, LoraLoaderModelOnly, Textbox, LoadImage, RTXVideoFrameGeneration, SaveVideo, LTXVSeparateAVLatent, MinimaxH3LatentUpscaler3D, SaveVideo, CreateVideo, RTXTrueHDR, RTXVideoSuperResolutionV2, RTXVideoSuperResolutionV2, SaveVideo, CreateVideo, SaveVideo, VAEDecodeAudio, VAEDecode, CreateVideo, SaveVideo, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MiniMax H3 NVIDIA VFX HDR 4倍FPS 视频超采样处理工具_2113007348188016641.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3 NVIDIA VFX HDR 4倍FPS 视频超采样处理工具_2113007348188016641.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（73 个）：
- `MiniMaxH3SigmaShift`
- `ResolutionSelector`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `RandomNoise`
- `MiniMaxH3ReferenceToVideo`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `BasicGuider`
- `LTXVConcatAVLatent`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Textbox`
- `LoadImage`
- `RTXVideoFrameGeneration`
- `SaveVideo`
- `LTXVSeparateAVLatent`
- `MinimaxH3LatentUpscaler3D`
- `SaveVideo`
- `CreateVideo`
- `RTXTrueHDR`
- `RTXVideoSuperResolutionV2`
- `RTXVideoSuperResolutionV2`
- `SaveVideo`
- `CreateVideo`
- `SaveVideo`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
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
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`
- `SaveImage`

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

覆盖率 **93%**（68/73）

**有卡**：`MiniMaxH3SigmaShift`、`ResolutionSelector`、`ComfyMathExpression`、`RandomNoise`、`MiniMaxH3ReferenceToVideo`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`VAEDecode`、`VAEDecodeAudio`、`CreateVideo`、`CLIPLoader`、`VAELoader`、`LTXVConcatAVLatent`、`UNETLoader`、`LoraLoaderModelOnly`、`Textbox`、`LoadImage`、`RTXVideoFrameGeneration`、`SaveVideo`、`LTXVSeparateAVLatent`、`MinimaxH3LatentUpscaler3D`、`RTXTrueHDR`、`RTXVideoSuperResolutionV2`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
