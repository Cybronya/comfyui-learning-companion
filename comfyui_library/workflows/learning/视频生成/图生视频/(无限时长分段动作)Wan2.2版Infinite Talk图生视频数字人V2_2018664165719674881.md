---
key: 视频生成/图生视频/(无限时长分段动作)Wan2.2版Infinite Talk图生视频数字人V2_2018664165719674881.json
name: (无限时长分段动作)Wan2.2版Infinite Talk图生视频数字人V2_2018664165719674881.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2018664165719674881.json
hash: c21b44e2ae1bca74
coverage: 0.853659
learned_at: 2026-10-15 22:34:58
nodes: [CLIPLoader, CLIPTextEncode, VAELoader, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, AudioEncoderLoader, ModelPatchLoader, KSamplerAdvanced, UNETLoader, UNETLoader, LoraLoaderModelOnly, KSamplerAdvanced, PreviewAny, LoadImage, VAEDecode, GetImageSizeAndCount, MathExpression|pysssss, ColorMatch, Note, Note, Note, ImageFromBatch, LoadAudio, AudioEncoderEncode, PainterAudioCut, AudioInfo, PainterAI2V, easy showAnything, CLIPTextEncode, VHS_VideoCombine, JWInteger, Note, JWInteger, ImageConcanate, VHS_VideoCombine, ShowAnything|Mie, CR Prompt Text, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/(无限时长分段动作)Wan2.2版Infinite Talk图生视频数字人V2_2018664165719674881.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2018664165719674881.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（41 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `AudioEncoderLoader`
- `ModelPatchLoader`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `PreviewAny`
- `LoadImage`
- `VAEDecode` ★核心
- `GetImageSizeAndCount`
- `MathExpression|pysssss`
- `ColorMatch`
- `Note`
- `Note`
- `Note`
- `ImageFromBatch`
- `LoadAudio`
- `AudioEncoderEncode`
- `PainterAudioCut`
- `AudioInfo`
- `PainterAI2V`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `JWInteger`
- `Note`
- `JWInteger`
- `ImageConcanate`
- `VHS_VideoCombine`
- `ShowAnything|Mie`
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **85%**（35/41）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`AudioEncoderLoader`、`ModelPatchLoader`、`KSamplerAdvanced`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`VAEDecode`、`GetImageSizeAndCount`、`MathExpression|pysssss`、`ColorMatch`、`ImageFromBatch`、`LoadAudio`、`AudioEncoderEncode`、`PainterAudioCut`、`AudioInfo`、`PainterAI2V`、`VHS_VideoCombine`、`JWInteger`、`ImageConcanate`、`ShowAnything|Mie`、`CR Prompt Text`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
