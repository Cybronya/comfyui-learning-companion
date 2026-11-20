---
name: unknown_workflow_video_lora_sampler_994
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8535
common_nodes: [CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ImageCompositeMasked, ImageResizeKJv2, LayerUtility: ColorImage V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SAM3_TrackToMask, SAM3_VideoTrack, SCAIL2ColoredMask, VHS_LoadVideo, VHS_VideoCombine, WanAnimatePlus BlockSwap, WanAnimatePlus ClipVisionEncode V2, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus SamplerFromSettings, WanAnimatePlus SamplerSettings, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/带货口播影视视频人物替换（无限时长）--scail2 sam组合工作流_2069424521005850625.json, 视频生成/图生视频/SCAIL2-无限时长-带货数字人替换_2069293271733596161.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_994

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/带货口播影视视频人物替换（无限时长）--scail2 sam组合工作流_2069424521005850625.json、视频生成/图生视频/SCAIL2-无限时长-带货数字人替换_2069293271733596161.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SAM3_TrackToMask`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus ClipVisionEncode V2`
- `WanAnimatePlus Decode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SCAIL_2 Embeds`
- `WanAnimatePlus SamplerFromSettings`
- `WanAnimatePlus SamplerSettings`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
