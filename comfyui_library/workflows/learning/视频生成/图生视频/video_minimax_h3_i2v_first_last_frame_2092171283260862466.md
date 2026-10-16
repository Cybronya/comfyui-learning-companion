---
key: 视频生成/图生视频/video_minimax_h3_i2v_first_last_frame_2092171283260862466.json
name: video_minimax_h3_i2v_first_last_frame_2092171283260862466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/video_minimax_h3_i2v_first_last_frame_2092171283260862466.json
hash: 2227cffc2012ab05
coverage: 0.9375
learned_at: 2026-10-16 22:59:34
nodes: [BasicGuider, RandomNoise, SamplerCustomAdvanced, VAEDecodeAudio, Label (rgthree), Label (rgthree), CLIPLoader, VAELoader, VAELoader, UNETLoader, ComfyMathExpression, MiniMaxH3ImageToVideo, CreateVideo, VAEDecode, Label (rgthree), Label (rgthree), Label (rgthree), SaveVideo, Label (rgthree), Label (rgthree), PrimitiveFloat, Label (rgthree), PrimitiveInt, KSamplerSelect, BasicScheduler, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, easy positive, LayerUtility: ImageScaleByAspectRatio V2, YK_LoadImageFromURL, LayerUtility: ImageScaleByAspectRatio V2, YK_LoadImageFromURL]
patterns: []
missing: []
---

# 视频生成/图生视频/video_minimax_h3_i2v_first_last_frame_2092171283260862466.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/video_minimax_h3_i2v_first_last_frame_2092171283260862466.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeAudio` ★核心
- `Label (rgthree)`
- `Label (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ComfyMathExpression`
- `MiniMaxH3ImageToVideo`
- `CreateVideo`
- `VAEDecode` ★核心
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `SaveVideo`
- `Label (rgthree)`
- `Label (rgthree)`
- `PrimitiveFloat`
- `Label (rgthree)`
- `PrimitiveInt`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `easy positive`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `YK_LoadImageFromURL`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `YK_LoadImageFromURL`

## 知识

覆盖率 **94%**（30/32）

**有卡**：`BasicGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEDecodeAudio`、`Label (rgthree)`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`ComfyMathExpression`、`MiniMaxH3ImageToVideo`、`CreateVideo`、`VAEDecode`、`SaveVideo`、`KSamplerSelect`、`BasicScheduler`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderModelOnly`、`easy positive`、`LayerUtility: ImageScaleByAspectRatio V2`、`YK_LoadImageFromURL`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio
