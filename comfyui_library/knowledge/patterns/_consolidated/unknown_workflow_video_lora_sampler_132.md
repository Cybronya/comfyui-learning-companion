---
name: unknown_workflow_video_lora_sampler_132
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.7375
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, ImageResizeKJv2, LayerUtility: PurgeVRAM, LoadImage, PixelPerfectResolution, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/优化加速升级Wan Animate动作迁移v2版_1983091241221038082.json, 视频生成/图生视频/全新图片跳舞 保留原图背景 Animate Wan2.2_2018250280189562881.json, 视频生成/图生视频/啊癫 Wan2.2 Animate 视频换人 视频人物替换_1970522090514358273.json, 视频生成/图生视频/啊癫 全新图片跳舞 保留原图背景 Animate Wan2.2_1970493244759044098.json, 视频生成/图生视频/图生视频 -快生成- AI动作模仿+跳舞+剑舞-Animate wan2.2_2034534867488219137.json, 视频生成/图生视频/图生视频 快生成 AI动作模仿+跳舞+剑舞-Animate wan2.2_2034431517451096065.json, 视频生成/图生视频/图生视频 快生成 AI动作模仿+跳舞+剑舞-Animate wan2.2_2046830049172656129.json, 视频生成/图生视频/图生视频+快生成Animate+wan2.2_2047135621176627201.json, 视频生成/图生视频/多人换脸图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上_2038207099926224898.json, 视频生成/图生视频/快速踩健身自行车_2081656460194443265.json, 视频生成/图生视频/扭pp_2082449087105953793.json, 视频生成/图生视频/换脸+换装+换人多合一（换脸换装换人）图生视频动作迁移视频换装Wan2.2人物替换动作迁移_2001911262554537986.json, 视频生成/图生视频/换脸图生视频动作迁移视频换装Wan2.2人物替换动作迁移支持10s以上_2101868247393062913.json, 视频生成/图生视频/视频换脸换装换人多合一（48g换脸换装换人）图生视频动作迁移视频换装_2001967162547924993.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_132

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/优化加速升级Wan Animate动作迁移v2版_1983091241221038082.json、视频生成/图生视频/全新图片跳舞 保留原图背景 Animate Wan2.2_2018250280189562881.json、视频生成/图生视频/啊癫 Wan2.2 Animate 视频换人 视频人物替换_1970522090514358273.json、视频生成/图生视频/啊癫 全新图片跳舞 保留原图背景 Animate Wan2.2_1970493244759044098.json、视频生成/图生视频/图生视频 -快生成- AI动作模仿+跳舞+剑舞-Animate wan2.2_2034534867488219137.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
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
- `GetNode` —— 13/14 个有
- `JWInteger` —— 13/14 个有
- `SetNode` —— 13/14 个有
- `easy cleanGpuUsed` —— 13/14 个有
- `ImageConcatMulti` —— 10/14 个有
- `BlockifyMask` —— 7/14 个有
- `DrawMaskOnImage` —— 7/14 个有
- `GrowMask` —— 7/14 个有
- `LayerMask: SegformerB2ClothesUltra` —— 7/14 个有
- `Int` —— 6/14 个有
- `SimpleMath+` —— 6/14 个有
- `Text` —— 6/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/14 个有
- `CR Text` —— 4/14 个有
- `LayerUtility: PurgeVRAM V2` —— 4/14 个有
- `MathExpression|pysssss` —— 4/14 个有
- `PreviewImage` —— 4/14 个有
- `PrimitiveInt` —— 4/14 个有
- `ttN float` —— 4/14 个有
- `LoadSAM3Model` —— 2/14 个有
- `MaskListToMaskBatch` —— 2/14 个有
- `MaskToImage` —— 2/14 个有
- `RH_Translator` —— 2/14 个有
- `SAM3Segmentation` —— 2/14 个有
- `easy imageBatchToImageList` —— 2/14 个有
- `easy imageListToImageBatch` —— 2/14 个有
- `easy sam3ModelLoader` —— 2/14 个有
- `easy sam3VideoSegmentation` —— 2/14 个有
- `CR Prompt Text` —— 1/14 个有
- `EmptyImage` —— 1/14 个有
- `FirstFrameSelector` —— 1/14 个有
- `SaveImage` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
