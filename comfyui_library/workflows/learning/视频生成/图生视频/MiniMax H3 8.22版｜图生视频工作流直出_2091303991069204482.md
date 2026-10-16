---
key: 视频生成/图生视频/MiniMax H3 8.22版｜图生视频工作流直出_2091303991069204482.json
name: MiniMax H3 8.22版｜图生视频工作流直出_2091303991069204482
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3 8.22版｜图生视频工作流直出_2091303991069204482.json
hash: a4c88f4689e45526
coverage: 0.931507
learned_at: 2026-10-16 22:30:34
nodes: [MiniMaxH3MemoryEfficientSageAttentionPatch, LoadImage, LoadImage, LoadAudio, LoadAudio, UNETLoader, SigmasToFloat, KSamplerSelect, VAELoader, ComfyMathExpression, BasicGuider, VAEDecode, VAEDecodeAudio, CLIPLoader, RandomNoise, LoadImage, Lora Loader Stack (rgthree), LoadImage, PixaromaSaveMp4, BasicScheduler, VAELoader, LoadImage, LoadAudio, SamplerCustomAdvanced, easy cleanGpuUsed, easy cleanGpuUsed, MiniMaxH3ReferenceToVideo, LTXVConcatAVLatent, MiniMaxH3TwoPassDetailMixerT8Advanced, BasicGuider, SplitSigmas, SolAttnMiniMax, SamplerCustomAdvanced, MinimaxH3LatentUpscaler3D, LTXVSeparateAVLatent, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, easy cleanGpuUsed, PrimitiveFloat, MiniMaxH3SigmaShift, ResolutionSelector, LoadImage, LoadImage, LoadImage, LoadImage, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MiniMax H3 8.22版｜图生视频工作流直出_2091303991069204482.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3 8.22版｜图生视频工作流直出_2091303991069204482.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（73 个）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `LoadAudio`
- `UNETLoader` ★核心
- `SigmasToFloat`
- `KSamplerSelect` ★核心
- `VAELoader`
- `ComfyMathExpression`
- `BasicGuider`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `CLIPLoader`
- `RandomNoise`
- `LoadImage`
- `Lora Loader Stack (rgthree)`
- `LoadImage`
- `PixaromaSaveMp4`
- `BasicScheduler`
- `VAELoader`
- `LoadImage`
- `LoadAudio`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `MiniMaxH3ReferenceToVideo`
- `LTXVConcatAVLatent`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `BasicGuider`
- `SplitSigmas`
- `SolAttnMiniMax`
- `SamplerCustomAdvanced` ★核心
- `MinimaxH3LatentUpscaler3D`
- `LTXVSeparateAVLatent`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `easy cleanGpuUsed`
- `PrimitiveFloat`
- `MiniMaxH3SigmaShift`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `LoadImage`
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

**有卡**：`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoadImage`、`LoadAudio`、`UNETLoader`、`SigmasToFloat`、`KSamplerSelect`、`VAELoader`、`ComfyMathExpression`、`BasicGuider`、`VAEDecode`、`VAEDecodeAudio`、`CLIPLoader`、`RandomNoise`、`Lora Loader Stack (rgthree)`、`PixaromaSaveMp4`、`BasicScheduler`、`SamplerCustomAdvanced`、`easy cleanGpuUsed`、`MiniMaxH3ReferenceToVideo`、`LTXVConcatAVLatent`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`SplitSigmas`、`SolAttnMiniMax`、`MinimaxH3LatentUpscaler3D`、`LTXVSeparateAVLatent`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`MiniMaxH3SigmaShift`、`ResolutionSelector`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
