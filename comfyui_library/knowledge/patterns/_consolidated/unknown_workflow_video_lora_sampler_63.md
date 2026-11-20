---
name: unknown_workflow_video_lora_sampler_63
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.62475
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, GetNode, ImageConcatMulti, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PixelPerfectResolution, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/换脸图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上_2049085267893555202.json, 数字人/数字人/Wan Animate 2.2-角色替换-动作迁移-图生视频-许老师专用_1981594203375443969.json, 数字人/数字人/dnf_scail.json_2081553214935228418.json, 数字人/数字人/人物替换Wan-Animate_1969759682535563266.json, 视频生成/图生视频/Wan2.2图生视频人物替换动作迁移_2028365300059611138.json, 视频生成/图生视频/Wan2.2换脸图片换脸视频动作迁移视频换装人物替换动作迁移支持10s视频换脸plus_2052450080971603969.json, 视频生成/图生视频/Wan2.2换脸图片换脸视频动作迁移视频换装人物替换动作迁移支持10s视频换脸plus_2052663395060600834.json, 视频生成/图生视频/Wan2.7+视频换脸  换头换发型+真实自然+视频换脸+人物角色替换+虚拟美女模特_2061612628442705921.json, 视频生成/图生视频/人物换脸 图生视频_2001188538823606273.json, 视频生成/图生视频/人物替换，主播带货，产品展示_2041577855473160193.json, 视频生成/图生视频/人物角色替换_2062336789762895874.json, 视频生成/图生视频/动作模仿动作迁移图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上）_1988865006097797121.json, 视频生成/图生视频/换脸图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上_1988497741976395777.json, 视频生成/图生视频/换装换脸+动作迁移 支持生成10s以上 超长时间 视频动作迁移  Wan2.2人物替换动作迁移_2048642449622441986.json, 视频生成/图生视频/视频换脸 高清换头换发型+自定时长+真实自然+视频换脸+人物角色替换_2059815304972292098.json, 视频生成/图生视频/视频换脸 高清换头换发型+自定时长+真实自然+视频换脸+人物角色替换_2064155930153021442.json, 视频生成/图生视频/视频换脸 高清换头换发型+自定时长+真实自然+视频换脸+人物角色替换_2064600210499784705.json, 视频生成/图生视频/视频换脸+高清换头换发型+自定时长+真实自然+视频换脸+人物角色替换_2065330125998219265.json, 视频生成/图生视频/视频换脸+高清换头换发型+自定时长+真实自然+视频换脸+人物角色替换_2068858062965927938.json, 视频生成/图生视频/高清视频换脸换发型+自定时长+真实自然+视频换脸+人物角色替换 (1)_2069968810341396482.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_63

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/文生图/换脸图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上_2049085267893555202.json、数字人/数字人/Wan Animate 2.2-角色替换-动作迁移-图生视频-许老师专用_1981594203375443969.json、数字人/数字人/dnf_scail.json_2081553214935228418.json、数字人/数字人/人物替换Wan-Animate_1969759682535563266.json、视频生成/图生视频/Wan2.2图生视频人物替换动作迁移_2028365300059611138.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `ImageConcatMulti`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LoadImage`
- `PixelPerfectResolution`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 19/20 个有
- `DrawMaskOnImage` —— 19/20 个有
- `GrowMask` —— 19/20 个有
- `Int` —— 19/20 个有
- `LayerUtility: PurgeVRAM` —— 18/20 个有
- `WanVideoLoraSelectMulti` —— 18/20 个有
- `JWInteger` —— 17/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 17/20 个有
- `LayerUtility: PurgeVRAM V2` —— 17/20 个有
- `MathExpression|pysssss` —— 17/20 个有
- `CR Text` —— 16/20 个有
- `LayerMask: SegformerB2ClothesUltra` —— 16/20 个有
- `VHS_VideoInfo` —— 16/20 个有
- `easy cleanGpuUsed` —— 16/20 个有
- `PreviewImage` —— 15/20 个有
- `GetImageSizeAndCount` —— 4/20 个有
- `WanVideoTorchCompileSettings` —— 3/20 个有
- `CM_IntToFloat` —— 2/20 个有
- `LayerMask: LoadSegmentAnythingModels` —— 2/20 个有
- `LayerMask: SegmentAnythingUltra V3` —— 2/20 个有
- `MemoryCleaner` —— 2/20 个有
- `RHHiddenNodes` —— 2/20 个有
- `RMBG` —— 2/20 个有
- `SimpleMath+` —— 2/20 个有
- `AutoNegativePrompt` —— 1/20 个有
- `DF_Int_to_Float` —— 1/20 个有
- `Fast Groups Bypasser (rgthree)` —— 1/20 个有
- `LoadVideo` —— 1/20 个有
- `PrimitiveStringMultiline` —— 1/20 个有
- `RH_AlibabaWan27VideoEdit` —— 1/20 个有
- `SaveVideo` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
