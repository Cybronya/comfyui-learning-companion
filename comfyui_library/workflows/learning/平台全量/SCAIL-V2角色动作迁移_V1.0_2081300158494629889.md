---
key: 平台全量/SCAIL-V2角色动作迁移_V1.0_2081300158494629889.json
name: SCAIL-V2角色动作迁移_V1.0_2081300158494629889
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SCAIL-V2角色动作迁移_V1.0_2081300158494629889.json
hash: 8bb044d402fb27cc
coverage: 0.88
learned_at: 2026-11-14 00:55:16
nodes: [GIMMVFI_interpolate, SCAIL2FitVideo, CLIPVisionLoader, VAELoader, CheckpointLoaderSimple, LoadVideoUI, ModelSamplingSD3, KSamplerSelect, BasicScheduler, CLIPTextEncode, SAM3_VideoTrack, UNETLoader, CLIPLoader, CR Apply LoRA Stack, DownloadAndLoadGIMMVFIModel, SCAIL2ScheduledLongVideoWithSAM, SCAIL2SegmentPlanBuilder, CS-MultiImageLoader, PrimitiveString, 孤海注释, 孤海注释, ImageResizeKJv2, VHS_VideoCombine, SAM3_TrackPreview, easy loraStack]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 平台全量/SCAIL-V2角色动作迁移_V1.0_2081300158494629889.json

> 来源文件 `comfyui_library/workflows/平台全量/SCAIL-V2角色动作迁移_V1.0_2081300158494629889.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（25 个）：
- `GIMMVFI_interpolate`
- `SCAIL2FitVideo`
- `CLIPVisionLoader`
- `VAELoader`
- `CheckpointLoaderSimple` ★核心
- `LoadVideoUI`
- `ModelSamplingSD3`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `SAM3_VideoTrack`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CR Apply LoRA Stack`
- `DownloadAndLoadGIMMVFIModel`
- `SCAIL2ScheduledLongVideoWithSAM`
- `SCAIL2SegmentPlanBuilder`
- `CS-MultiImageLoader`
- `PrimitiveString`
- `孤海注释`
- `孤海注释`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `SAM3_TrackPreview`
- `easy loraStack`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **88%**（22/25）

**有卡**：`GIMMVFI_interpolate`、`SCAIL2FitVideo`、`CLIPVisionLoader`、`VAELoader`、`CheckpointLoaderSimple`、`LoadVideoUI`、`ModelSamplingSD3`、`KSamplerSelect`、`BasicScheduler`、`CLIPTextEncode`、`SAM3_VideoTrack`、`UNETLoader`、`CLIPLoader`、`CR Apply LoRA Stack`、`DownloadAndLoadGIMMVFIModel`、`SCAIL2ScheduledLongVideoWithSAM`、`SCAIL2SegmentPlanBuilder`、`CS-MultiImageLoader`、`ImageResizeKJv2`、`VHS_VideoCombine`、`SAM3_TrackPreview`、`easy loraStack`

**用到的条目**：VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPLoader、CLIPTextEncode、KSamplerSelect、CR Apply LoRA Stack、easy loraStack
