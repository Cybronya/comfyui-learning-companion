---
name: unknown_workflow_video_lora_sampler_176
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.625462
common_nodes: [BlockifyMask, CLIPVisionLoader, DWPreprocessor, DrawMaskOnImage, FaceMaskFromPoseKeypoints, GrowMask, ImageConcatMulti, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PixelPerfectResolution, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/手动遮罩视频换装_WanAnimate2.2_1984074108189245442.json, 平台全量/最强视频换装+Animate+Wan2.2=B站艾橘溪_1985658128895225858.json, 平台全量/神气科技-视频换人 Animate Wan2.2_1992781251905998850.json, 平台全量/神气科技-视频换装 Animate Wan2.2_1991356413186277377.json, 平台全量/视频人物替换Animate_1986460629294870529.json, 平台全量/视频人物替换，动作迁移 Animate Wan2.2_2085600675559464962.json, 平台全量/视频换人 Animate Wan2.2_2000071872521924610.json, 平台全量/视频换人 Animate Wan2.2_2001286004759724034.json, 平台全量/视频换人-自动遮罩_2034239663103287297.json, 平台全量/视频换装 Animate Wan2.2_2062034069596237826.json, 数字人/数字人/人物替换Wan-Animate_1969759682535563266.json, 视频生成/图生视频/wan annimateGGUF_1970833810306801666.json, 视频生成/图生视频/人物替换，主播带货，产品展示_2041577855473160193.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_176

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（平台全量/手动遮罩视频换装_WanAnimate2.2_1984074108189245442.json、平台全量/最强视频换装+Animate+Wan2.2=B站艾橘溪_1985658128895225858.json、平台全量/神气科技-视频换人 Animate Wan2.2_1992781251905998850.json、平台全量/神气科技-视频换装 Animate Wan2.2_1991356413186277377.json、平台全量/视频人物替换Animate_1986460629294870529.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 13 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `GrowMask`
- `ImageConcatMulti`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LoadImage`
- `PixelPerfectResolution`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 12/13 个有
- `LayerUtility: PurgeVRAM` —— 12/13 个有
- `SetNode` —— 12/13 个有
- `WanVideoTextEncodeCached` —— 12/13 个有
- `WanVideoLoraSelectMulti` —— 10/13 个有
- `JWInteger` —— 9/13 个有
- `VHS_VideoInfo` —— 9/13 个有
- `LayerMask: SegformerB2ClothesUltra` —— 8/13 个有
- `easy cleanGpuUsed` —— 8/13 个有
- `Int` —— 5/13 个有
- `WanVideoTorchCompileSettings` —— 5/13 个有
- `CM_IntToFloat` —— 4/13 个有
- `GetImageSizeAndCount` —— 4/13 个有
- `LayerMask: LoadSegmentAnythingModels` —— 4/13 个有
- `LayerMask: SegmentAnythingUltra V3` —— 4/13 个有
- `SimpleMath+` —— 4/13 个有
- `RHHiddenNodes` —— 3/13 个有
- `AutoNegativePrompt` —— 1/13 个有
- `CR Prompt Text` —— 1/13 个有
- `Fast Groups Bypasser (rgthree)` —— 1/13 个有
- `Float` —— 1/13 个有
- `GetImageRangeFromBatch` —— 1/13 个有
- `ImageFromBatch+` —— 1/13 个有
- `InvertMask` —— 1/13 个有
- `Label (rgthree)` —— 1/13 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/13 个有
- `PointsEditor` —— 1/13 个有
- `SeCModelLoader` —— 1/13 个有
- `SeCVideoSegmentation` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
