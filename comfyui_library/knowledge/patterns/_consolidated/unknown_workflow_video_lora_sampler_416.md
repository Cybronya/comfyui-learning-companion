---
name: unknown_workflow_video_lora_sampler_416
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.562
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, DiffusionModelLoaderKJ, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, GetNode, ImageResizeKJv2, KSamplerSelect, Label (rgthree), LoraLoaderModelOnly, ModelSamplingSD3, SCAIL2ScheduledLongVideoWithSAM, SCAIL2SegmentPlanBuilder, SetNode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/ComfyUI SCAIL 2 Face Detailer 视频换脸 公开版_2075051126759710722.json, 平台全量/SCAIL 2 Face Detailer 视频换装_2086065069724626946.json, 视频生成/图生视频/ComfyUI SCAIL 2 Face Detailer 视频换装_2075051785387069442.json, 视频生成/图生视频/ComfyUI SCAIL 2 Face Detailer 视频换装_2107354460371636226.json, 视频生成/图生视频/ComfyUI SCAIL 2 动作迁移极简长视频生成_2075049712163581954.json, 视频生成/图生视频/ComfyUI SCAIL 2 动作迁移极简长视频生成_2100839392154841090.json, 视频生成/图生视频/ComfyUI SCAIL 2 极简长视频生成 单图_2100862026611519490.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_416

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/ComfyUI SCAIL 2 Face Detailer 视频换脸 公开版_2075051126759710722.json、平台全量/SCAIL 2 Face Detailer 视频换装_2086065069724626946.json、视频生成/图生视频/ComfyUI SCAIL 2 Face Detailer 视频换装_2075051785387069442.json、视频生成/图生视频/ComfyUI SCAIL 2 Face Detailer 视频换装_2107354460371636226.json、视频生成/图生视频/ComfyUI SCAIL 2 动作迁移极简长视频生成_2075049712163581954.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DiffusionModelLoaderKJ`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `Label (rgthree)`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SCAIL2ScheduledLongVideoWithSAM`
- `SCAIL2SegmentPlanBuilder`
- `SetNode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `CS-MultiImageLoader` —— 6/7 个有
- `Fast Groups Bypasser (rgthree)` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `LoadImage` —— 5/7 个有
- `SaveImage` —— 5/7 个有
- `GetImageSize` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `PrimitiveBoolean` —— 4/7 个有
- `PrimitiveInt` —— 4/7 个有
- `SCAIL2AlignReferenceFaceToCrop` —— 4/7 个有
- `SCAIL2FaceCompositeBack` —— 4/7 个有
- `SCAIL2HeadTrackCrop` —— 4/7 个有
- `SimpleMath+` —— 4/7 个有
- `easy ifElse` —— 4/7 个有
- `ComfySwitchNode` —— 3/7 个有
- `FilmGrain` —— 3/7 个有
- `ImageConcatMulti` —— 3/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
