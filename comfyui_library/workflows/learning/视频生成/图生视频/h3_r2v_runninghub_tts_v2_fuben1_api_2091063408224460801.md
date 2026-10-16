---
key: 视频生成/图生视频/h3_r2v_runninghub_tts_v2_fuben1_api_2091063408224460801.json
name: h3_r2v_runninghub_tts_v2_fuben1_api_2091063408224460801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/h3_r2v_runninghub_tts_v2_fuben1_api_2091063408224460801.json
hash: a2afe59801447b5d
coverage: 0.945946
learned_at: 2026-10-16 22:30:50
nodes: [SaveVideo, ResolutionSelector, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, BasicGuider, UNETLoader, CLIPLoader, RandomNoise, CreateVideo, ComfyMathExpression, PrimitiveFloat, MiniMaxH3ReferenceToVideo, easy indexTTSGenerate, MiniMaxH3AudioLatentControlT8, easy indexTTSAudioMerge, PrimitiveStringMultiline, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadAudio, LoadAudio, LoadAudio, easy downloadIndexTTSAndLoadModel, LoadAudio, LoadAudio, LoadAudio, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/h3_r2v_runninghub_tts_v2_fuben1_api_2091063408224460801.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/h3_r2v_runninghub_tts_v2_fuben1_api_2091063408224460801.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（37 个）：
- `SaveVideo`
- `ResolutionSelector`
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `UNETLoader` ★核心
- `CLIPLoader`
- `RandomNoise`
- `CreateVideo`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `MiniMaxH3ReferenceToVideo`
- `easy indexTTSGenerate`
- `MiniMaxH3AudioLatentControlT8`
- `easy indexTTSAudioMerge`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `easy downloadIndexTTSAndLoadModel`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **95%**（35/37）

**有卡**：`SaveVideo`、`ResolutionSelector`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`BasicGuider`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`CreateVideo`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`easy indexTTSGenerate`、`MiniMaxH3AudioLatentControlT8`、`easy indexTTSAudioMerge`、`LoadImage`、`LoadAudio`、`easy downloadIndexTTSAndLoadModel`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
