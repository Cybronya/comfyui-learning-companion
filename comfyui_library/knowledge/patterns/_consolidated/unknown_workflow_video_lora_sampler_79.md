---
name: unknown_workflow_video_lora_sampler_79
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.593167
common_nodes: [Audio Duration (mtb), BlockifyMask, CLIPVisionLoader, DWPreprocessor, DrawMaskOnImage, FaceMaskFromPoseKeypoints, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, GrowMask, ImageCropByMaskAndResize, ImageFromBatch+, ImageResizeKJv2, JWInteger, LayerUtility: PurgeVRAM, LoadImage, PixelPerfectResolution, PrimitiveInt, SetNode, SimpleMath+, VHS_LoadVideo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, easy sam3ModelLoader, easy sam3VideoSegmentation]
problems: []
missing: []
members: [图片生成/反推提示词/test11_2017053406745075714.json, 数字人/数字人/已知最强视频换脸模型 Animate Wan2.2_2007046777135964161.json, 视频生成/图生视频/Animate Wan2.2 人物视频换装V2_2005855972839092225.json, 视频生成/图生视频/Animate Wan2.2 最强视频换头+换脸_2082828374803832834.json, 视频生成/图生视频/Animate Wan2.2 最强视频换头+换脸_2101148000168005634.json, 视频生成/图生视频/Animate+Wan2.2+最强视频换脸+换头_2005836350404395009.json, 视频生成/图生视频/AnimateWan2.2 视频换人V2+单人多人_2005891179520688129.json, 视频生成/图生视频/Wan animate视频人物替换 效果极佳_2009640204046442497.json, 视频生成/图生视频/Wan+animate视频人物替换+效果极佳_2010983716067217410.json, 视频生成/图生视频/sam语义分割 最强视频换脸+换头_2014336980489871362.json, 视频生成/图生视频/旅拍视频模板换脸-Wan高质量版-VideoFaceSwap_2071227855530455041.json, 视频生成/图生视频/最强视频换脸+换头 Animate Wan2.2_2009317533723136001.json, 视频生成/图生视频/最强视频换脸+换头 Animate Wan2.2_2021386632020103169.json, 视频生成/图生视频/最强视频换脸+换头 Animate Wan2.2_2041848671586750465.json, 视频生成/图生视频/最强视频换脸+换头 Animate Wan2.2（懒人版）_2067973490745106434.json, 视频生成/图生视频/最强视频换脸换头不换背景适合平台美女跳舞动作迁移复刻动作一致_2073689074594050049.json, 视频生成/图生视频/第一种最强视频换脸+换头_2041849392579219457.json, 视频生成/图生视频/视频换头_2041098212999700482.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_79

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/反推提示词/test11_2017053406745075714.json、数字人/数字人/已知最强视频换脸模型 Animate Wan2.2_2007046777135964161.json、视频生成/图生视频/Animate Wan2.2 人物视频换装V2_2005855972839092225.json、视频生成/图生视频/Animate Wan2.2 最强视频换头+换脸_2082828374803832834.json、视频生成/图生视频/Animate Wan2.2 最强视频换头+换脸_2101148000168005634.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 18 个 workflow 都包含：
- `Audio Duration (mtb)`
- `BlockifyMask`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `ImageCropByMaskAndResize`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `JWInteger`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `PixelPerfectResolution`
- `PrimitiveInt`
- `SetNode`
- `SimpleMath+`
- `VHS_LoadVideo`
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
- `easy cleanGpuUsed`
- `easy sam3ModelLoader`
- `easy sam3VideoSegmentation`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 17/18 个有
- `GIMMVFI_interpolate` —— 17/18 个有
- `VHS_VideoCombine` —— 17/18 个有
- `JjkText` —— 16/18 个有
- `Int` —— 15/18 个有
- `MaskToImage` —— 14/18 个有
- `CM_IntToFloat` —— 4/18 个有
- `VHS_VideoInfo` —— 4/18 个有
- `easy showAnything` —— 4/18 个有
- `SaveImage` —— 2/18 个有
- `TT_img_enc` —— 2/18 个有
- `Text` —— 2/18 个有
- `WanVideoTorchCompileSettings` —— 2/18 个有
- `AutoCropFaces` —— 1/18 个有
- `FlashVSRNode` —— 1/18 个有
- `PreviewImage` —— 1/18 个有
- `RIFE VFI` —— 1/18 个有
- `TextOverlay` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
