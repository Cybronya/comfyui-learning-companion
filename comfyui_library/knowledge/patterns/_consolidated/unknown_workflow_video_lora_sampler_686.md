---
name: unknown_workflow_video_lora_sampler_686
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.84225
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, ImageConcatMulti, ImageResizeKJv2, LoadImage, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, VHS_LoadVideo, VHS_VideoCombine, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus Sampler, WanAnimatePlus SetLoRAs, WanAnimatePlus TextEncodeCached, WanAnimatePlus VAELoader]
problems: []
missing: []
members: [平台全量/WanAnimatePlus+scail2 多帧动作迁移_主角替换_2066357399811878914.json, 平台全量/scail2 动作迁移多图参考_2065807188257497089.json, 平台全量/scail2 多参工作流_2065571076624699394.json, 视频生成/图生视频/SCAIL-2多参考图角色动作迁移与替换——支持长视频_2066386680499761154.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_686

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/WanAnimatePlus+scail2 多帧动作迁移_主角替换_2066357399811878914.json、平台全量/scail2 动作迁移多图参考_2065807188257497089.json、平台全量/scail2 多参工作流_2065571076624699394.json、视频生成/图生视频/SCAIL-2多参考图角色动作迁移与替换——支持长视频_2066386680499761154.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimatePlus Decode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SCAIL_2 Embeds`
- `WanAnimatePlus Sampler`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageBatchMulti` —— 3/4 个有
- `PrimitiveInt` —— 3/4 个有
- `WanAnimatePlus BlockSwap` —— 3/4 个有
- `WanAnimatePlus ContextOptions` —— 3/4 个有
- `PrimitiveBoolean` —— 2/4 个有
- `Bjornulf_ShowInt` —— 1/4 个有
- `CLIPVisionLoader` —— 1/4 个有
- `CM_BoolUnaryOperation` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `FL_ImageBatch` —— 1/4 个有
- `If ANY execute A else B` —— 1/4 个有
- `ImpactConditionalBranch` —— 1/4 个有
- `ImpactNeg` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `ModelPatchMemoryCleaner` —— 1/4 个有
- `PDRatioSelector` —— 1/4 个有
- `WanAnimatePlus ClipVisionEncode` —— 1/4 个有
- `WanVideoBlockSwap` —— 1/4 个有
- `easy int` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
