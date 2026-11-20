---
name: unknown_workflow_video_lora_sampler_235
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.610636
common_nodes: [Audio Duration (mtb), BlockifyMask, CLIPVisionLoader, DWPreprocessor, DrawMaskOnImage, FaceMaskFromPoseKeypoints, GetNode, GrowMask, ImageCropByMaskAndResize, ImageFromBatch+, ImageResizeKJv2, JWInteger, LayerUtility: PurgeVRAM, MaskToImage, PixelPerfectResolution, PrimitiveInt, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, easy sam3ModelLoader, easy sam3VideoSegmentation]
problems: []
missing: []
members: [平台全量/【定制专用】图片压缩包批量视频换装工作流_2050317426197311490.json, 平台全量/【定制专用】批量更换视频人物_服装+视频换背景_2054914231476203522.json, 视频生成/图生视频/Wan animate视频人物替换 效果极佳_2009640204046442497.json, 视频生成/图生视频/Wan+animate视频人物替换+效果极佳_2010983716067217410.json, 视频生成/图生视频/sam语义分割 最强视频换脸+换头_2014336980489871362.json, 视频生成/图生视频/旅拍视频模板换脸-Wan高质量版-VideoFaceSwap_2071227855530455041.json, 视频生成/图生视频/最强视频换脸+换头 Animate Wan2.2_2021386632020103169.json, 视频生成/图生视频/最强视频换脸+换头 Animate Wan2.2_2041848671586750465.json, 视频生成/图生视频/最强视频换脸+换头 Animate Wan2.2（懒人版）_2067973490745106434.json, 视频生成/图生视频/最强视频换脸换头不换背景适合平台美女跳舞动作迁移复刻动作一致_2073689074594050049.json, 视频生成/图生视频/视频换头_2041098212999700482.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_235

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（平台全量/【定制专用】图片压缩包批量视频换装工作流_2050317426197311490.json、平台全量/【定制专用】批量更换视频人物_服装+视频换背景_2054914231476203522.json、视频生成/图生视频/Wan animate视频人物替换 效果极佳_2009640204046442497.json、视频生成/图生视频/Wan+animate视频人物替换+效果极佳_2010983716067217410.json、视频生成/图生视频/sam语义分割 最强视频换脸+换头_2014336980489871362.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 11 个 workflow 都包含：
- `Audio Duration (mtb)`
- `BlockifyMask`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `GrowMask`
- `ImageCropByMaskAndResize`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `JWInteger`
- `LayerUtility: PurgeVRAM`
- `MaskToImage`
- `PixelPerfectResolution`
- `PrimitiveInt`
- `SetNode`
- `SimpleMath+`
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
- `easy cleanGpuUsed`
- `easy sam3ModelLoader`
- `easy sam3VideoSegmentation`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 10/11 个有
- `GIMMVFI_interpolate` —— 10/11 个有
- `LoadImage` —— 10/11 个有
- `GetImageRangeFromBatch` —— 9/11 个有
- `GetImageSizeAndCount` —— 9/11 个有
- `JjkText` —— 9/11 个有
- `Int` —— 6/11 个有
- `Text` —— 4/11 个有
- `PreviewImage` —— 3/11 个有
- `Bjornulf_ShowInt` —— 2/11 个有
- `CR Prompt Text` —— 2/11 个有
- `RHBatchImages:` —— 2/11 个有
- `RHExtractImage` —— 2/11 个有
- `RHHiddenNodes` —— 2/11 个有
- `RHUploadZip` —— 2/11 个有
- `WanVideoTorchCompileSettings` —— 2/11 个有
- `easy forLoopEnd` —— 2/11 个有
- `easy forLoopStart` —— 2/11 个有
- `easy imageCount` —— 2/11 个有
- `easy showAnything` —— 2/11 个有
- `AutoCropFaces` —— 1/11 个有
- `FlashVSRNode` —— 1/11 个有
- `LayerUtility: ImageBlendAdvance` —— 1/11 个有
- `LayerUtility: ImageCombineAlpha` —— 1/11 个有
- `LayerUtility: PurgeVRAM V2` —— 1/11 个有
- `RH_Translator` —— 1/11 个有
- `RIFE VFI` —— 1/11 个有
- `RMBG` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
