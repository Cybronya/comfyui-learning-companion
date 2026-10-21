---
name: unknown_workflow_video_lora_sampler_185
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8591
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SCAIL2ScheduledLongVideoWithSAM, SCAIL2SegmentPlanBuilder, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2070317114317164545.json, 视频生成/图生视频/2072165934445457410.json, 视频生成/图生视频/2072211393461448705.json, 视频生成/图生视频/2072215800739614722.json, 视频生成/图生视频/Scail2视频角色替换TTP单图版_2083759017431756801.json, 视频生成/图生视频/2072151352708517889.json, 视频生成/图生视频/2069624919830384641.json, 视频生成/图生视频/2071482062011453441.json, 视频生成/图生视频/2072216679937036289.json, 视频生成/图生视频/scail2视频角色替换TTP多参版_2083763864499474433.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_185

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2070317114317164545.json、视频生成/图生视频/2072165934445457410.json、视频生成/图生视频/2072211393461448705.json、视频生成/图生视频/2072215800739614722.json、视频生成/图生视频/Scail2视频角色替换TTP单图版_2083759017431756801.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SCAIL2ScheduledLongVideoWithSAM`
- `SCAIL2SegmentPlanBuilder`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `DiffusionModelLoaderKJ` —— 9/10 个有
- `ImageResizeKJv2` —— 9/10 个有
- `CR Text` —— 8/10 个有
- `PrimitiveInt` —— 8/10 个有
- `SetNode` —— 2/10 个有
- `VHS_VideoInfo` —— 2/10 个有
- `GetNode` —— 1/10 个有
- `INTConstant` —— 1/10 个有
- `ImageResize+` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `PreviewAny` —— 1/10 个有
- `Primitive integer [Crystools]` —— 1/10 个有
- `SimpleMath+` —— 1/10 个有
- `UNETLoader` —— 1/10 个有
- `easy anythingIndexSwitch` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
