---
name: unknown_workflow_video_lora_sampler_480
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.5676
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CS-MultiImageLoader, CheckpointLoaderSimple, DiffusionModelLoaderKJ, DownloadAndLoadGIMMVFIModel, Fast Groups Bypasser (rgthree), GIMMVFI_interpolate, GetNode, ImageResizeKJv2, KSamplerSelect, Label (rgthree), LoraLoaderModelOnly, ModelSamplingSD3, PrimitiveStringMultiline, SCAIL2ScheduledLongVideoWithSAM, SCAIL2SegmentPlanBuilder, SetNode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [视频生成/图生视频/ComfyUI SCAIL 2 Face Detailer 视频换装_2075051785387069442.json, 视频生成/图生视频/ComfyUI SCAIL 2 Face Detailer 视频换装_2107354460371636226.json, 视频生成/图生视频/ComfyUI SCAIL 2 动作迁移极简长视频生成_2075049712163581954.json, 视频生成/图生视频/ComfyUI SCAIL 2 动作迁移极简长视频生成_2100839392154841090.json, 视频生成/图生视频/ComfyUI SCAIL 2 极简长视频生成 单图_2100862026611519490.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_480

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/ComfyUI SCAIL 2 Face Detailer 视频换装_2075051785387069442.json、视频生成/图生视频/ComfyUI SCAIL 2 Face Detailer 视频换装_2107354460371636226.json、视频生成/图生视频/ComfyUI SCAIL 2 动作迁移极简长视频生成_2075049712163581954.json、视频生成/图生视频/ComfyUI SCAIL 2 动作迁移极简长视频生成_2100839392154841090.json、视频生成/图生视频/ComfyUI SCAIL 2 极简长视频生成 单图_2100862026611519490.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CS-MultiImageLoader`
- `CheckpointLoaderSimple`
- `DiffusionModelLoaderKJ`
- `DownloadAndLoadGIMMVFIModel`
- `Fast Groups Bypasser (rgthree)`
- `GIMMVFI_interpolate`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `Label (rgthree)`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PrimitiveStringMultiline`
- `SCAIL2ScheduledLongVideoWithSAM`
- `SCAIL2SegmentPlanBuilder`
- `SetNode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/5 个有
- `SaveImage` —— 4/5 个有
- `FilmGrain` —— 3/5 个有
- `ComfySwitchNode` —— 2/5 个有
- `GetImageSize` —— 2/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `PrimitiveBoolean` —— 2/5 个有
- `PrimitiveInt` —— 2/5 个有
- `SCAIL2AlignReferenceFaceToCrop` —— 2/5 个有
- `SCAIL2FaceCompositeBack` —— 2/5 个有
- `SCAIL2HeadTrackCrop` —— 2/5 个有
- `SimpleMath+` —— 2/5 个有
- `easy ifElse` —— 2/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
