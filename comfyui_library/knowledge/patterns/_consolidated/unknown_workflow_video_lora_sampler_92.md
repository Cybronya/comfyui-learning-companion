---
name: unknown_workflow_video_lora_sampler_92
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.534667
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PixelPerfectResolution, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Wan Animate2.2主体迁移（自动裁剪脸部）v1_1969661416292687873.json, 平台全量/Wan Animate2.2动作迁移（背景不替换，自动裁剪脸部）v2_1969466395891298305.json, 平台全量/Wan-Animate 影视级_角色替换+动作迁移_1969183959009665026.json, 平台全量/WanAnimate 场景九 多人视频精准替换_1970434198735646721.json, 平台全量/WanAnimate 场景五 AI视频换人换背景_1970395458956894209.json, 平台全量/WanAnimate 场景八 人物A的动作+B的表情混合迁移_1970434028912472066.json, 平台全量/WanAnimate 场景四 AI视频换装_1970392164461146114.json, 平台全量/WanAnimate 角色替换 动作参考_1985274480073261058.json, 平台全量/WanAnimate+场景三+视频换脸_2038810875125047297.json, 平台全量/WanAnimate+场景三+视频换脸_2039327486156214273.json, 平台全量/WanAnimate+场景三+视频换脸_2062371997207846914.json, 平台全量/WanAnimate人物迁移_1969925819596480513.json, 平台全量/表情动作迁移-WanAnimate KJ_2004156714289143809.json, 平台全量/香蕉+WanAnimate视频编辑_1970134990010937345.json, 视频生成/图生视频/Wan Animate2.2 替身出演，形神境随_1969559616474542081.json, 视频生成/图生视频/WanAnimate真人舞蹈-视频动作和表情迁移_1968952890041778177.json, 视频生成/图生视频/WanAnimate角色替换+动作参考- FXAI_1970797508848984065.json, 视频生成/图生视频/WanAnimate角色替换+动作参考-By Aiwood_1969039434375176194.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_92

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（平台全量/Wan Animate2.2主体迁移（自动裁剪脸部）v1_1969661416292687873.json、平台全量/Wan Animate2.2动作迁移（背景不替换，自动裁剪脸部）v2_1969466395891298305.json、平台全量/Wan-Animate 影视级_角色替换+动作迁移_1969183959009665026.json、平台全量/WanAnimate 场景九 多人视频精准替换_1970434198735646721.json、平台全量/WanAnimate 场景五 AI视频换人换背景_1970395458956894209.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：53%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `GetImageSizeAndCount`
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
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 17/18 个有
- `DownloadAndLoadSAM2Model` —— 17/18 个有
- `DrawMaskOnImage` —— 17/18 个有
- `GrowMask` —— 17/18 个有
- `PointsEditor` —— 17/18 个有
- `Sam2Segmentation` —— 17/18 个有
- `INTConstant` —— 16/18 个有
- `WanVideoContextOptions` —— 16/18 个有
- `PreviewImage` —— 9/18 个有
- `GetImageRangeFromBatch` —— 6/18 个有
- `easy showAnything` —— 5/18 个有
- `AudioCropProcessUTK` —— 3/18 个有
- `ColorMatch` —— 3/18 个有
- `MathExpression|pysssss` —— 3/18 个有
- `Text Multiline` —— 3/18 个有
- `WanVideoLoraSelect` —— 3/18 个有
- `BboxDetectorSEGS` —— 2/18 个有
- `CR Prompt Text` —— 2/18 个有
- `GetImageSize` —— 2/18 个有
- `ImageFromBatch+` —— 2/18 个有
- `JWInteger` —— 2/18 个有
- `SegsToCombinedMask` —— 2/18 个有
- `UltralyticsDetectorProvider` —— 2/18 个有
- `easy compare` —— 2/18 个有
- `easy ifElse` —— 2/18 个有
- `easy imageCropFromMask` —— 2/18 个有
- `RH_Nano_Banana_Image2Image` —— 1/18 个有
- `SaveImage` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
