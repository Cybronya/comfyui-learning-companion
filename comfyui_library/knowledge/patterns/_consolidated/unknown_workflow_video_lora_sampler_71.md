---
name: unknown_workflow_video_lora_sampler_71
type: Unknown Workflow
frequency: 22
level: moderate
coverage: 0.657045
common_nodes: [CLIPVisionLoader, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan+AnimateV2动作迁移工作流_1995333956365115393.json, 视频生成/图生视频/Wan2.2 Animate 动作迁移（手动版）_2053044709232263170.json, 视频生成/图生视频/Wan2.2 Animate动作迁移长视频生成加速版_1969252099450150913.json, 视频生成/图生视频/Wan2.2+Animate+角色替换视频动作迁移+KJ加速版_1993551269581225986.json, 视频生成/图生视频/Wan2.2Animate+DWPose动作模仿工作流！墙裂推荐！表情精准迁移_2038302872932192257.json, 视频生成/图生视频/Wan2.2图生视频人物替换动作迁移_2028365300059611138.json, 视频生成/图生视频/Wan2.2换脸图片换脸视频动作迁移视频换装人物替换动作迁移支持10s视频换脸plus_2052450080971603969.json, 视频生成/图生视频/Wan2.2换脸图片换脸视频动作迁移视频换装人物替换动作迁移支持10s视频换脸plus_2052663395060600834.json, 视频生成/图生视频/Wan2.7+视频换脸  换头换发型+真实自然+视频换脸+人物角色替换+虚拟美女模特_2061612628442705921.json, 视频生成/图生视频/人物换脸 图生视频_2001188538823606273.json, 视频生成/图生视频/人物角色替换_2062336789762895874.json, 视频生成/图生视频/动作模仿动作迁移图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上）_1988865006097797121.json, 视频生成/图生视频/多人换脸图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上_2038207099926224898.json, 视频生成/图生视频/换脸图生视频动作迁移视频换装Wan2.2人物替换动作迁移支持10s以上_2101868247393062913.json, 视频生成/图生视频/换脸图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上_1988497741976395777.json, 视频生成/图生视频/换装换脸+动作迁移 支持生成10s以上 超长时间 视频动作迁移  Wan2.2人物替换动作迁移_2048642449622441986.json, 视频生成/图生视频/视频换脸 高清换头换发型+自定时长+真实自然+视频换脸+人物角色替换_2059815304972292098.json, 视频生成/图生视频/视频换脸 高清换头换发型+自定时长+真实自然+视频换脸+人物角色替换_2064155930153021442.json, 视频生成/图生视频/视频换脸 高清换头换发型+自定时长+真实自然+视频换脸+人物角色替换_2064600210499784705.json, 视频生成/图生视频/视频换脸+高清换头换发型+自定时长+真实自然+视频换脸+人物角色替换_2065330125998219265.json, 视频生成/图生视频/视频换脸+高清换头换发型+自定时长+真实自然+视频换脸+人物角色替换_2068858062965927938.json, 视频生成/图生视频/高清视频换脸换发型+自定时长+真实自然+视频换脸+人物角色替换 (1)_2069968810341396482.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_71

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（视频生成/图生视频/Wan+AnimateV2动作迁移工作流_1995333956365115393.json、视频生成/图生视频/Wan2.2 Animate 动作迁移（手动版）_2053044709232263170.json、视频生成/图生视频/Wan2.2 Animate动作迁移长视频生成加速版_1969252099450150913.json、视频生成/图生视频/Wan2.2+Animate+角色替换视频动作迁移+KJ加速版_1993551269581225986.json、视频生成/图生视频/Wan2.2Animate+DWPose动作模仿工作流！墙裂推荐！表情精准迁移_2038302872932192257.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPVisionLoader`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 21/22 个有
- `FaceMaskFromPoseKeypoints` —— 21/22 个有
- `ImageCropByMaskAndResize` —— 21/22 个有
- `ImageResizeKJv2` —— 21/22 个有
- `JWInteger` —— 21/22 个有
- `PixelPerfectResolution` —— 21/22 个有
- `GetNode` —— 20/22 个有
- `SetNode` —— 20/22 个有
- `easy cleanGpuUsed` —— 20/22 个有
- `ImageConcatMulti` —— 19/22 个有
- `LayerUtility: PurgeVRAM` —— 19/22 个有
- `VHS_VideoInfo` —— 19/22 个有
- `CR Text` —— 18/22 个有
- `Int` —— 18/22 个有
- `LayerUtility: PurgeVRAM V2` —— 18/22 个有
- `PreviewImage` —— 18/22 个有
- `BlockifyMask` —— 17/22 个有
- `DrawMaskOnImage` —— 17/22 个有
- `GrowMask` —— 17/22 个有
- `LayerMask: SegformerB2ClothesUltra` —— 17/22 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 17/22 个有
- `MathExpression|pysssss` —— 17/22 个有
- `GetImageSizeAndCount` —— 2/22 个有
- `MemoryCleaner` —— 2/22 个有
- `PrimitiveStringMultiline` —— 2/22 个有
- `EmptyImage` —— 1/22 个有
- `Fast Groups Bypasser (rgthree)` —— 1/22 个有
- `ImageResize+` —— 1/22 个有
- `LoadVideo` —— 1/22 个有
- `RH_AlibabaWan27VideoEdit` —— 1/22 个有
- `RMBG` —— 1/22 个有
- `SaveImage` —— 1/22 个有
- `SaveVideo` —— 1/22 个有
- `Text` —— 1/22 个有
- `VHS_VideoInfoLoaded` —— 1/22 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
