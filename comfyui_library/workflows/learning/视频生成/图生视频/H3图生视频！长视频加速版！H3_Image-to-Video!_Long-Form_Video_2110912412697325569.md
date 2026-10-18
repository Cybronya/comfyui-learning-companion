---
key: 视频生成/图生视频/H3图生视频！长视频加速版！H3_Image-to-Video!_Long-Form_Video_2110912412697325569.json
name: H3图生视频！长视频加速版！H3_Image-to-Video!_Long-Form_Video_2110912412697325569
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/H3图生视频！长视频加速版！H3_Image-to-Video!_Long-Form_Video_2110912412697325569.json
hash: b05e2575228a28cc
coverage: 0.727273
learned_at: 2026-10-18 00:23:01
nodes: [CLIPLoader, ModelAttentionBackend, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, KSamplerSelect, UNETLoader, BasicScheduler, ConditioningZeroOut, ModelPreviewOverrideKJ, SelfLiftAvatarH3Sampler, SetNode, LayerUtility: PurgeVRAM V2, LTXVSeparateAVLatent, LayerUtility: PurgeVRAM V2, VAEDecode, VAEDecodeAudio, LoraLoaderModelOnly, LTXVSeparateAVLatent, VAELoader, ComfyMathExpression, VAELoader, GetNode, SetNode, DF_Int_to_Float, GetNode, MiniMaxH3ReferenceToVideo, LoadImage, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, JjkText]
patterns: []
missing: []
---

# 视频生成/图生视频/H3图生视频！长视频加速版！H3_Image-to-Video!_Long-Form_Video_2110912412697325569.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/H3图生视频！长视频加速版！H3_Image-to-Video!_Long-Form_Video_2110912412697325569.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（33 个）：
- `CLIPLoader`
- `ModelAttentionBackend`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `BasicScheduler`
- `ConditioningZeroOut`
- `ModelPreviewOverrideKJ`
- `SelfLiftAvatarH3Sampler` ★核心
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `LTXVSeparateAVLatent`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVSeparateAVLatent`
- `VAELoader`
- `ComfyMathExpression`
- `VAELoader`
- `GetNode`
- `SetNode`
- `DF_Int_to_Float`
- `GetNode`
- `MiniMaxH3ReferenceToVideo`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `JjkText`

## 知识

覆盖率 **73%**（24/33）

**有卡**：`CLIPLoader`、`ModelAttentionBackend`、`MiniMaxChunkFeedForward`、`MiniMaxLowVRAMAttention`、`KSamplerSelect`、`UNETLoader`、`BasicScheduler`、`ConditioningZeroOut`、`ModelPreviewOverrideKJ`、`SelfLiftAvatarH3Sampler`、`LayerUtility: PurgeVRAM V2`、`LTXVSeparateAVLatent`、`VAEDecode`、`VAEDecodeAudio`、`LoraLoaderModelOnly`、`VAELoader`、`ComfyMathExpression`、`DF_Int_to_Float`、`MiniMaxH3ReferenceToVideo`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect
