---
name: unknown_workflow_video_lora_sampler_587
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.51
common_nodes: [BatchImagesNode, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, GetNode, ImageResizeKJv2, LoadImage, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMaskV2, SetNode, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimatePlus BlockSwap, WanAnimatePlus ClipVisionEncode V2, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus SCAIL_2 TwoPhase Settings, WanAnimatePlus SamplerFromSettings, WanAnimatePlus SamplerSettings, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus VAELoader, WanVideoTextEncodeCached, WanVideoTorchCompileSettings]
problems: []
missing: []
members: [平台全量/视频-动作迁移-v2-wan2.1-SCAIL2_2079575176957743105.json, 视频生成/图生视频/SCAIL2多视角参考_2077936156414668802.json, 视频生成/图生视频/scail2加强终极人物替换_2081353014853595138.json, 视频生成/图生视频/scail2替换背景_2080680296361586689.json, 视频生成/图生视频/scaile2多参多角色指定角色替换_2081628200786026497.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_587

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/视频-动作迁移-v2-wan2.1-SCAIL2_2079575176957743105.json、视频生成/图生视频/SCAIL2多视角参考_2077936156414668802.json、视频生成/图生视频/scail2加强终极人物替换_2081353014853595138.json、视频生成/图生视频/scail2替换背景_2080680296361586689.json、视频生成/图生视频/scaile2多参多角色指定角色替换_2081628200786026497.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 5 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMaskV2`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus ClipVisionEncode V2`
- `WanAnimatePlus Decode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SCAIL_2 Embeds`
- `WanAnimatePlus SCAIL_2 TwoPhase Settings`
- `WanAnimatePlus SamplerFromSettings`
- `WanAnimatePlus SamplerSettings`
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus VAELoader`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`

**可变部分**（部分 workflow 才有）：
- `Int` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `VHS_LoadVideo` —— 4/5 个有
- `easy clearCacheAll` —— 4/5 个有
- `PlaySound|pysssss` —— 3/5 个有
- `PrimitiveBoolean` —— 3/5 个有
- `SimpleMath+` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `easy mathInt` —— 3/5 个有
- `ImageConcatenate_UTK` —— 2/5 个有
- `RHHiddenNodes` —— 2/5 个有
- `RMBG` —— 2/5 个有
- `Text` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `CM_FloatToInt` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `FillMaskWithColor` —— 1/5 个有
- `GetImageSizeAndCount` —— 1/5 个有
- `GrowMask` —— 1/5 个有
- `INTConstant` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `InvertMask` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `MemoryCleaner` —— 1/5 个有
- `PointsEditor` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `SeCModelLoader` —— 1/5 个有
- `SeCVideoSegmentation` —— 1/5 个有
- `VHS_LoadVideoFFmpeg` —— 1/5 个有
- `WanAnimatePlus ContextOptions` —— 1/5 个有
- `easy indexAnything` —— 1/5 个有
- `easy seed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
