---
name: unknown_workflow_video_lora_sampler_1108
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.619
common_nodes: [BOOLConstant, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, GetNode, ImageBatchMulti, ImageResizeKJv2, LoadImage, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimatePlus BlockSwap, WanAnimatePlus ClipVisionEncode, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus Sampler, WanAnimatePlus SetLoRAs, WanAnimatePlus TextEncodeCached, WanAnimatePlus TorchCompileSettings, WanAnimatePlus VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/scail_2-动作迁移完全体（单图、多参、角色替换）_2068169097623465985.json, 视频生成/图生视频/多图参考 动作迁移 --SCAIL2系列优化版 （清晰布局_小白适用_效果超夯）_2074416012107272194.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1108

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/scail_2-动作迁移完全体（单图、多参、角色替换）_2068169097623465985.json、视频生成/图生视频/多图参考 动作迁移 --SCAIL2系列优化版 （清晰布局_小白适用_效果超夯）_2074416012107272194.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：62%

## 共有节点

全部 2 个 workflow 都包含：
- `BOOLConstant`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `GetNode`
- `ImageBatchMulti`
- `ImageResizeKJv2`
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
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SCAIL_2 Embeds`
- `WanAnimatePlus Sampler`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus TorchCompileSettings`
- `WanAnimatePlus VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `ComfyNumberConvert` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `Int` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
