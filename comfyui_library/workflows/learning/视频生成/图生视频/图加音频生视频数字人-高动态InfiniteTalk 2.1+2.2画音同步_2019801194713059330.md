---
key: 视频生成/图生视频/图加音频生视频数字人-高动态InfiniteTalk 2.1+2.2画音同步_2019801194713059330.json
name: 图加音频生视频数字人-高动态InfiniteTalk 2.1+2.2画音同步_2019801194713059330.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图加音频生视频数字人-高动态InfiniteTalk 2.1+2.2画音同步_2019801194713059330.json
hash: 65229628579b4cc8
coverage: 0.625
learned_at: 2026-10-15 22:35:04
nodes: [PainterAI2V, VAEDecode, KSamplerAdvanced, easy cleanGpuUsed, KSamplerAdvanced, PathchSageAttentionKJ, UNETLoader, UNETLoader, PathchSageAttentionKJ, CLIPLoader, AudioEncoderEncode, Reroute, Reroute, Reroute, Reroute, Reroute, JWInteger, Reroute, Reroute, Note, LayerUtility: PurgeVRAM, Reroute, Reroute, Reroute, AudioEncoderLoader, Reroute, Reroute, VAELoader, Reroute, Reroute, easy seed, ColorMatch, Note, Reroute, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelPatchLoader, JWInteger, PainterAudioCut, PreviewAny, PreviewAudio, Reroute, ModelSamplingSD3, ModelSamplingSD3, Reroute, Reroute, VHS_VideoCombine, JWInteger, SimpleMath+, LoadAudio, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/图加音频生视频数字人-高动态InfiniteTalk 2.1+2.2画音同步_2019801194713059330.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2019801194713059330.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（56 个）：
- `PainterAI2V`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `AudioEncoderEncode`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `JWInteger`
- `Reroute`
- `Reroute`
- `Note`
- `LayerUtility: PurgeVRAM`
- `Reroute`
- `Reroute`
- `Reroute`
- `AudioEncoderLoader`
- `Reroute`
- `Reroute`
- `VAELoader`
- `Reroute`
- `Reroute`
- `easy seed`
- `ColorMatch`
- `Note`
- `Reroute`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelPatchLoader`
- `JWInteger`
- `PainterAudioCut`
- `PreviewAny`
- `PreviewAudio`
- `Reroute`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `Reroute`
- `Reroute`
- `VHS_VideoCombine`
- `JWInteger`
- `SimpleMath+`
- `LoadAudio`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `CR Prompt Text`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **62%**（35/56）

**有卡**：`PainterAI2V`、`VAEDecode`、`KSamplerAdvanced`、`easy cleanGpuUsed`、`PathchSageAttentionKJ`、`UNETLoader`、`CLIPLoader`、`AudioEncoderEncode`、`JWInteger`、`LayerUtility: PurgeVRAM`、`AudioEncoderLoader`、`VAELoader`、`easy seed`、`ColorMatch`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`ModelPatchLoader`、`PainterAudioCut`、`PreviewAudio`、`ModelSamplingSD3`、`VHS_VideoCombine`、`SimpleMath+`、`LoadAudio`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
