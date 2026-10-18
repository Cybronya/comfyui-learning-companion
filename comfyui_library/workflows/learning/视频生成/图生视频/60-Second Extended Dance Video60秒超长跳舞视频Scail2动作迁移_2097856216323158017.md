---
key: 视频生成/图生视频/60-Second Extended Dance Video60秒超长跳舞视频Scail2动作迁移_2097856216323158017.json
name: 60-Second Extended Dance Video60秒超长跳舞视频Scail2动作迁移_2097856216323158017
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/60-Second Extended Dance Video60秒超长跳舞视频Scail2动作迁移_2097856216323158017.json
hash: dff159679e2a6981
coverage: 0.717391
learned_at: 2026-10-17 01:27:50
nodes: [SCAIL2FitVideo, WanChunkFeedForward, LoraLoaderModelOnly, ModelSamplingSD3, KSamplerSelect, CLIPLoader, CLIPTextEncode, VAELoader, CLIPVisionLoader, CheckpointLoaderSimple, CLIPTextEncode, SAM3_VideoTrack, SCAIL2ReferencePack, SCAIL2ReferenceSAMBuilder, ShowText|pysssss, ImageResizeKJv2, SimpleMath+, SimpleMath+, ImageResizeKJv2, LayerUtility: PurgeVRAM, SetNode, GetNode, GetNode, JjkText, AILab_QwenVL, LoraLoaderModelOnly, SCAIL2SimpleVideo, SetNode, SetNode, GetNode, LayerUtility: PurgeVRAM, SetNode, GetNode, CreateVideo, SimpleMath+, Int, JjkText, CLIPTextEncode, DiffusionModelLoaderKJ, RIFE VFI, BasicScheduler, VHS_LoadVideo, LoadImage, PrimitiveInt, PrimitiveInt, SaveVideo]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 视频生成/图生视频/60-Second Extended Dance Video60秒超长跳舞视频Scail2动作迁移_2097856216323158017.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/60-Second Extended Dance Video60秒超长跳舞视频Scail2动作迁移_2097856216323158017.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（46 个）：
- `SCAIL2FitVideo`
- `WanChunkFeedForward`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `KSamplerSelect` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `SAM3_VideoTrack`
- `SCAIL2ReferencePack`
- `SCAIL2ReferenceSAMBuilder`
- `ShowText|pysssss`
- `ImageResizeKJv2`
- `SimpleMath+`
- `SimpleMath+`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `GetNode`
- `GetNode`
- `JjkText`
- `AILab_QwenVL`
- `LoraLoaderModelOnly` ★核心
- `SCAIL2SimpleVideo`
- `SetNode`
- `SetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `GetNode`
- `CreateVideo`
- `SimpleMath+`
- `Int`
- `JjkText`
- `CLIPTextEncode` ★核心
- `DiffusionModelLoaderKJ`
- `RIFE VFI`
- `BasicScheduler`
- `VHS_LoadVideo`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `SaveVideo`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **72%**（33/46）

**有卡**：`SCAIL2FitVideo`、`WanChunkFeedForward`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`KSamplerSelect`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`CLIPVisionLoader`、`CheckpointLoaderSimple`、`SAM3_VideoTrack`、`SCAIL2ReferencePack`、`SCAIL2ReferenceSAMBuilder`、`ImageResizeKJv2`、`SimpleMath+`、`LayerUtility: PurgeVRAM`、`AILab_QwenVL`、`SCAIL2SimpleVideo`、`CreateVideo`、`Int`、`DiffusionModelLoaderKJ`、`RIFE VFI`、`BasicScheduler`、`VHS_LoadVideo`、`LoadImage`、`SaveVideo`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、CLIPVisionLoader
