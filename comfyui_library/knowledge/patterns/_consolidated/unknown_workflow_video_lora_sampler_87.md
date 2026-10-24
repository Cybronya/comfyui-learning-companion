---
name: unknown_workflow_video_lora_sampler_87
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.67
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, ImageConcatMulti, ImageCropByMaskAndResize, ImageResizeKJv2, LayerUtility: PurgeVRAM, LoadImage, PixelPerfectResolution, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/优化加速升级Wan Animate动作迁移v2版_1983091241221038082.json, 视频生成/图生视频/全新图片跳舞 保留原图背景 Animate Wan2.2_2018250280189562881.json, 视频生成/图生视频/啊癫 Wan2.2 Animate 视频换人 视频人物替换_1970522090514358273.json, 视频生成/图生视频/啊癫 全新图片跳舞 保留原图背景 Animate Wan2.2_1970493244759044098.json, 视频生成/图生视频/多人换脸图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上_2038207099926224898.json, 视频生成/图生视频/快速踩健身自行车_2081656460194443265.json, 视频生成/图生视频/扭pp_2082449087105953793.json, 视频生成/图生视频/换脸+换装+换人多合一（换脸换装换人）图生视频动作迁移视频换装Wan2.2人物替换动作迁移_2001911262554537986.json, 视频生成/图生视频/换脸图生视频动作迁移视频换装Wan2.2人物替换动作迁移支持10s以上_2101868247393062913.json, 视频生成/图生视频/换脸图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上_1988497741976395777.json, 视频生成/图生视频/换装换脸+动作迁移 支持生成10s以上 超长时间 视频动作迁移  Wan2.2人物替换动作迁移_2048642449622441986.json, 视频生成/图生视频/视频换脸 高清换头换发型+自定时长+真实自然+视频换脸+人物角色替换_2059815304972292098.json, 视频生成/图生视频/视频换脸 高清换头换发型+自定时长+真实自然+视频换脸+人物角色替换_2064155930153021442.json, 视频生成/图生视频/视频换脸 高清换头换发型+自定时长+真实自然+视频换脸+人物角色替换_2064600210499784705.json, 视频生成/图生视频/视频换脸+高清换头换发型+自定时长+真实自然+视频换脸+人物角色替换_2065330125998219265.json, 视频生成/图生视频/视频换脸+高清换头换发型+自定时长+真实自然+视频换脸+人物角色替换_2068858062965927938.json, 视频生成/图生视频/视频换脸换装换人多合一（48g换脸换装换人）图生视频动作迁移视频换装_2001967162547924993.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_87

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/优化加速升级Wan Animate动作迁移v2版_1983091241221038082.json、视频生成/图生视频/全新图片跳舞 保留原图背景 Animate Wan2.2_2018250280189562881.json、视频生成/图生视频/啊癫 Wan2.2 Animate 视频换人 视频人物替换_1970522090514358273.json、视频生成/图生视频/啊癫 全新图片跳舞 保留原图背景 Animate Wan2.2_1970493244759044098.json、视频生成/图生视频/多人换脸图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上_2038207099926224898.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `ImageConcatMulti`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `PixelPerfectResolution`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
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
- `GetNode` —— 16/17 个有
- `JWInteger` —— 16/17 个有
- `SetNode` —— 16/17 个有
- `easy cleanGpuUsed` —— 16/17 个有
- `BlockifyMask` —— 14/17 个有
- `DrawMaskOnImage` —— 14/17 个有
- `GrowMask` —— 14/17 个有
- `LayerMask: SegformerB2ClothesUltra` —— 14/17 个有
- `Int` —— 13/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 12/17 个有
- `CR Text` —— 11/17 个有
- `LayerUtility: PurgeVRAM V2` —— 11/17 个有
- `MathExpression|pysssss` —— 11/17 个有
- `PreviewImage` —— 11/17 个有
- `LoadSAM3Model` —— 2/17 个有
- `MaskListToMaskBatch` —— 2/17 个有
- `MaskToImage` —— 2/17 个有
- `RH_Translator` —— 2/17 个有
- `SAM3Segmentation` —— 2/17 个有
- `SimpleMath+` —— 2/17 个有
- `Text` —— 2/17 个有
- `easy imageBatchToImageList` —— 2/17 个有
- `easy imageListToImageBatch` —— 2/17 个有
- `easy sam3ModelLoader` —— 2/17 个有
- `easy sam3VideoSegmentation` —— 2/17 个有
- `CR Prompt Text` —— 1/17 个有
- `EmptyImage` —— 1/17 个有
- `FirstFrameSelector` —— 1/17 个有
- `SaveImage` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
