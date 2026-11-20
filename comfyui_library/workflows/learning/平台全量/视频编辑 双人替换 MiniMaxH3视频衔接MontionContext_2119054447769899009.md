---
key: 平台全量/视频编辑 双人替换 MiniMaxH3视频衔接MontionContext_2119054447769899009.json
name: 视频编辑 双人替换 MiniMaxH3视频衔接MontionContext_2119054447769899009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频编辑 双人替换 MiniMaxH3视频衔接MontionContext_2119054447769899009.json
hash: 65beaf9fd9778e9a
coverage: 0.961538
learned_at: 2026-11-14 02:40:45
nodes: [SamplerCustomAdvanced, LayerUtility: PurgeVRAM V2, BasicScheduler, VAEDecode, RandomNoise, VAELoader, CLIPLoader, BasicGuider, KSamplerSelect, PathchSageAttentionKJ, LoraLoaderModelOnly, UNETLoader, ResolutionSelector, MiniMaxH3MemoryEfficientSageAttentionPatch, VAELoader, MiniMaxH3ReferenceToVideo, VRAM_Debug, PrimitiveStringMultiline, VHS_VideoCombine, VHS_LoadVideo, LoadImage, LoadImage, MiniMaxH3MotionContext, MiniMaxH3MotionContextTrim, VAEDecodeAudio, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/视频编辑 双人替换 MiniMaxH3视频衔接MontionContext_2119054447769899009.json

> 来源文件 `comfyui_library/workflows/平台全量/视频编辑 双人替换 MiniMaxH3视频衔接MontionContext_2119054447769899009.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（26 个）：
- `SamplerCustomAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `BasicScheduler`
- `VAEDecode` ★核心
- `RandomNoise`
- `VAELoader`
- `CLIPLoader`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ResolutionSelector`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `VAELoader`
- `MiniMaxH3ReferenceToVideo`
- `VRAM_Debug`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContextTrim`
- `VAEDecodeAudio` ★核心
- `VHS_LoadVideo`

## 知识

覆盖率 **96%**（25/26）

**有卡**：`SamplerCustomAdvanced`、`LayerUtility: PurgeVRAM V2`、`BasicScheduler`、`VAEDecode`、`RandomNoise`、`VAELoader`、`CLIPLoader`、`BasicGuider`、`KSamplerSelect`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`UNETLoader`、`ResolutionSelector`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3ReferenceToVideo`、`VRAM_Debug`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LoadImage`、`MiniMaxH3MotionContext`、`MiniMaxH3MotionContextTrim`、`VAEDecodeAudio`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
