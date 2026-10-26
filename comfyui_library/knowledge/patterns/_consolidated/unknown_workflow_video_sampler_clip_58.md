---
name: unknown_workflow_video_sampler_clip_58
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.5526
common_nodes: [CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, GetNode, LoadImage, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimatePlus BlockSwap, WanAnimatePlus ClipVisionEncode, WanAnimatePlus Decode, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus Sampler, WanAnimatePlus TextEncodeCached, WanAnimatePlus VAELoader]
problems: []
missing: []
members: [数字人/数字人/SCAIL2动作迁移+角色替换合集 支持长视频_2066182560610340865.json, 视频生成/图生视频/81.SCAIL2优化版+多图参考_2096980051706339330.json, 视频生成/图生视频/SCAIL2 动作迁移+角色替换_2070706889247252481.json, 视频生成/图生视频/SCAIL2 动作迁移（多图参考）_2079086131693572098.json, 视频生成/图生视频/SCAIL2 多人替换（动作迁移）_2083425183460843521.json, 视频生成/图生视频/SCAIL2 角色替换&动作迁移_2076542724727201794.json, 视频生成/图生视频/SCAIL2动作迁移+角色替换动作迁移话音同步 长视频 工作流V1.0_2066527706170351617.json, 视频生成/图生视频/SCAIL2动作迁移+角色替换合集 支持长视频_2066377947686199298.json, 视频生成/图生视频/scail_2-动作迁移完全体（单图、多参、角色替换）_2068169097623465985.json, 视频生成/图生视频/电商带货 动作迁移+角色替换合集 支持长视频  SCAIL2_2073480668717346817.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_58

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（数字人/数字人/SCAIL2动作迁移+角色替换合集 支持长视频_2066182560610340865.json、视频生成/图生视频/81.SCAIL2优化版+多图参考_2096980051706339330.json、视频生成/图生视频/SCAIL2 动作迁移+角色替换_2070706889247252481.json、视频生成/图生视频/SCAIL2 动作迁移（多图参考）_2079086131693572098.json、视频生成/图生视频/SCAIL2 多人替换（动作迁移）_2083425183460843521.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `GetNode`
- `LoadImage`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus ClipVisionEncode`
- `WanAnimatePlus Decode`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SCAIL_2 Embeds`
- `WanAnimatePlus Sampler`
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus VAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 9/10 个有
- `ImageConcanate` —— 9/10 个有
- `Switch any [Crystools]` —— 9/10 个有
- `easy imageRemBg` —— 9/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/10 个有
- `WanAnimatePlus LoraSelect` —— 6/10 个有
- `easy boolean` —— 6/10 个有
- `Fast Groups Bypasser (rgthree)` —— 5/10 个有
- `Label (rgthree)` —— 5/10 个有
- `BOOLConstant` —— 4/10 个有
- `ImageBatchMulti` —— 4/10 个有
- `ImageResizeKJv2` —— 4/10 个有
- `WanAnimatePlus LoraSelectMulti` —— 4/10 个有
- `WanAnimatePlus SetLoRAs` —— 4/10 个有
- `WanAnimatePlus TorchCompileSettings` —— 4/10 个有
- `GetImageRangeFromBatch` —— 3/10 个有
- `ImageConcatMulti` —— 3/10 个有
- `WanAnimatePlus ContextOptions` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `GetImageSize` —— 1/10 个有
- `Int` —— 1/10 个有
- `LoadAudio` —— 1/10 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/10 个有
- `SaveImage` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
