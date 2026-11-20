---
name: unknown_workflow_video_lora_sampler_974
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9255
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CR Apply LoRA Stack, CS-MultiImageLoader, CheckpointLoaderSimple, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, ImageResizeKJv2, KSamplerSelect, LoadVideoUI, ModelSamplingSD3, PrimitiveString, SAM3_TrackPreview, SAM3_VideoTrack, SCAIL2FitVideo, UNETLoader, VAELoader, VHS_VideoCombine, easy loraStack]
problems: []
missing: []
members: [平台全量/SCAIL-V2角色动作迁移_V1.0_2081300158494629889.json, 平台全量/SCAIL_V2-多角色动作迁移极简工作流_2081373553664024577.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_974

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/SCAIL-V2角色动作迁移_V1.0_2081300158494629889.json、平台全量/SCAIL_V2-多角色动作迁移极简工作流_2081373553664024577.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Apply LoRA Stack`
- `CS-MultiImageLoader`
- `CheckpointLoaderSimple`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadVideoUI`
- `ModelSamplingSD3`
- `PrimitiveString`
- `SAM3_TrackPreview`
- `SAM3_VideoTrack`
- `SCAIL2FitVideo`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`
- `easy loraStack`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `LoadVideo` —— 1/2 个有
- `SCAIL2ReferencePack` —— 1/2 个有
- `SCAIL2ReferenceSAMBuilder` —— 1/2 个有
- `SCAIL2ScheduledLongVideoWithSAM` —— 1/2 个有
- `SCAIL2SegmentPlanBuilder` —— 1/2 个有
- `SCAIL2SimpleVideo` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
