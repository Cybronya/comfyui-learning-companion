---
key: 音频生成/音频生成/Wan2.2图生视频动态字幕+画外音（indexTTS2）_1983724744073781249.json
name: Wan2.2图生视频动态字幕+画外音（indexTTS2）_1983724744073781249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/Wan2.2图生视频动态字幕+画外音（indexTTS2）_1983724744073781249.json
hash: 354311179aefb2b7
coverage: 0.806452
learned_at: 2026-10-18 01:46:55
nodes: [LoadImage, PrimitiveInt, MarkdownNote, KSamplerAdvanced, ModelSamplingSD3, UNETLoader, UNETLoader, ModelSamplingSD3, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, LoadImage, CR Text, LoadAudio, SaveAudioMP3, easy downloadIndexTTSAndLoadModel, easy indexTTSGenerateSimple, CR Text, VHS_VideoCombine, KSamplerAdvanced, SimpleMath+, CLIPTextEncode, CLIPTextEncode, CLIPLoader, WanImageToVideo, VAELoader, VAEDecode, 孤海-取色器, PrimitiveNode, PrimitiveNode, HAIGC_VideoSubtitleEnhanced]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1.5, "scheduler": "uni_pc", "seed": "enable", "steps": "randomize"}
---

# 音频生成/音频生成/Wan2.2图生视频动态字幕+画外音（indexTTS2）_1983724744073781249.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/Wan2.2图生视频动态字幕+画外音（indexTTS2）_1983724744073781249.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（31 个）：
- `LoadImage`
- `PrimitiveInt`
- `MarkdownNote`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `LoadImage`
- `CR Text`
- `LoadAudio`
- `SaveAudioMP3`
- `easy downloadIndexTTSAndLoadModel`
- `easy indexTTSGenerateSimple`
- `CR Text`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `WanImageToVideo`
- `VAELoader`
- `VAEDecode` ★核心
- `孤海-取色器`
- `PrimitiveNode`
- `PrimitiveNode`
- `HAIGC_VideoSubtitleEnhanced`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1.5`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **81%**（25/31）

**有卡**：`LoadImage`、`KSamplerAdvanced`、`ModelSamplingSD3`、`UNETLoader`、`VHS_VideoCombine`、`CR Text`、`LoadAudio`、`SaveAudioMP3`、`easy downloadIndexTTSAndLoadModel`、`easy indexTTSGenerateSimple`、`SimpleMath+`、`CLIPTextEncode`、`CLIPLoader`、`WanImageToVideo`、`VAELoader`、`VAEDecode`、`孤海-取色器`、`HAIGC_VideoSubtitleEnhanced`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、SaveAudioMP3
