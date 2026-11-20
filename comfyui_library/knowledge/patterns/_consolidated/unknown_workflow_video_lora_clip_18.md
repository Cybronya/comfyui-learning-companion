---
name: unknown_workflow_video_lora_clip_18
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.528
common_nodes: [AnyBooleanSwitch, BatchImagesNode, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, GetNode, INTConstant, ImageFromBatch, ImageResizeKJv2, Int, LoadImage, PrimitiveBoolean, SAM3_VideoTrack, SetNode, SimpleMath+, Text, VHS_LoadVideo, VHS_VideoCombine, WanAnimatePlus BlockSwap, WanAnimatePlus ClipVisionEncode, WanAnimatePlus ContextOptions, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus SetLoRAs, WanAnimatePlus TextEncodeCached, WanAnimatePlus VAELoader, WanVideoLoraSelectMulti, WanVideoTeaCache, easy cleanGpuUsed, easy int]
problems: []
missing: []
members: [平台全量/涛哥专属 Scail2 动作迁移 多参考图 人物替换_2071600140175110146.json, 视频生成/图生视频/Scail2 动作迁移 多参考图 人物替换 长视频不劣化_2065812297293062146.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_18

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/涛哥专属 Scail2 动作迁移 多参考图 人物替换_2071600140175110146.json、视频生成/图生视频/Scail2 动作迁移 多参考图 人物替换 长视频不劣化_2065812297293062146.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：53%

## 共有节点

全部 2 个 workflow 都包含：
- `AnyBooleanSwitch`
- `BatchImagesNode`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `GetNode`
- `INTConstant`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `PrimitiveBoolean`
- `SAM3_VideoTrack`
- `SetNode`
- `SimpleMath+`
- `Text`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus ClipVisionEncode`
- `WanAnimatePlus ContextOptions`
- `WanAnimatePlus Decode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SCAIL_2 Embeds`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus VAELoader`
- `WanVideoLoraSelectMulti`
- `WanVideoTeaCache`
- `easy cleanGpuUsed`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `BOOLConstant` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `Primitive integer [Crystools]` —— 1/2 个有
- `SCAIL2ColoredMask` —— 1/2 个有
- `SCAIL2ColoredMaskV2` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有
- `VHS_VideoInfoLoaded` —— 1/2 个有
- `WanAnimatePlus SCAIL_2 TwoPhase Settings` —— 1/2 个有
- `WanAnimatePlus Sampler` —— 1/2 个有
- `WanAnimatePlus SamplerFromSettings` —— 1/2 个有
- `WanAnimatePlus SamplerSettings` —— 1/2 个有
- `WanAnimatePlus TorchCompileSettings` —— 1/2 个有
- `easy boolean` —— 1/2 个有
- `easy float` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
