---
name: unknown_workflow_video_lora_sampler_491
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7696
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ImageBatchMulti, ImageResizeKJv2, LoadImage, SAM3_VideoTrack, SCAIL2ColoredMask, VHS_LoadVideo, VHS_VideoCombine, WanAnimatePlus BlockSwap, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus Sampler, WanAnimatePlus SetLoRAs, WanAnimatePlus TextEncodeCached, WanAnimatePlus VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Scail2+卡通角色动作迁移+全节点注释_2072321050989383682.json, 视频生成/图生视频/Scail2多图参考人物替换工作流_2072172131533803521.json, 视频生成/图生视频/最强运镜最强迁移-SCAIL2 多图参考工作流_2065963015316525057.json, 视频生成/文生视频/SCAIL-2 Multi-Reference Character Swap_2072998835137585152.json, 视频生成/文生视频/SCAIL-2 Multi-Reference Motion Guide_2072998836324573184.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_491

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Scail2+卡通角色动作迁移+全节点注释_2072321050989383682.json、视频生成/图生视频/Scail2多图参考人物替换工作流_2072172131533803521.json、视频生成/图生视频/最强运镜最强迁移-SCAIL2 多图参考工作流_2065963015316525057.json、视频生成/文生视频/SCAIL-2 Multi-Reference Character Swap_2072998835137585152.json、视频生成/文生视频/SCAIL-2 Multi-Reference Motion Guide_2072998836324573184.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus Decode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SCAIL_2 Embeds`
- `WanAnimatePlus Sampler`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus VAELoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 3/5 个有
- `GIMMVFI_interpolate` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `WanAnimatePlus ContextOptions` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `RIFE VFI` —— 2/5 个有
- `SimpleMath+` —— 2/5 个有
- `easy int` —— 2/5 个有
- `孤海注释` —— 2/5 个有
- `EmptyImage` —— 1/5 个有
- `ImageCompositeMasked` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `SAM3_TrackToMask` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
