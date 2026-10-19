---
name: unknown_workflow_video_sampler_vae_59
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.6925
common_nodes: [DrawViTPose, GetImageSizeAndCount, ImageResizeKJv2, OnnxDetectionModelLoader, PoseAndFaceDetection, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1980564316481044481.json, 视频生成/图生视频/1981764143114010626.json, 视频生成/图生视频/1969243872620650498.json, 视频生成/图生视频/2006252507227496450.json, 视频生成/图生视频/2006246424253571074.json, 视频生成/图生视频/wan2.2 animate视频换头视频换脸工作流_1977864752590454786.json, 视频生成/图生视频/1992409563280330754.json, 视频生成/图生视频/2051920241860591618.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_59

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/1980564316481044481.json、视频生成/图生视频/1981764143114010626.json、视频生成/图生视频/1969243872620650498.json、视频生成/图生视频/2006252507227496450.json、视频生成/图生视频/2006246424253571074.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 8 个 workflow 都包含：
- `DrawViTPose`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 7/8 个有
- `DownloadAndLoadSAM2Model` —— 7/8 个有
- `DrawMaskOnImage` —— 7/8 个有
- `GrowMaskWithBlur` —— 7/8 个有
- `LoadImage` —— 7/8 个有
- `Sam2Segmentation` —— 7/8 个有
- `CLIPVisionLoader` —— 6/8 个有
- `WanVideoClipVisionEncode` —— 6/8 个有
- `GetNode` —— 5/8 个有
- `INTConstant` —— 5/8 个有
- `LayerUtility: PurgeVRAM V2` —— 5/8 个有
- `SetNode` —— 5/8 个有
- `WanVideoLoraSelectMulti` —— 5/8 个有
- `WanVideoSetLoRAs` —— 5/8 个有
- `VHS_VideoInfo` —— 4/8 个有
- `WanVideoContextOptions` —— 4/8 个有
- `CR Text` —— 3/8 个有
- `ImageConcatMulti` —— 3/8 个有
- `ImageFromBatch+` —— 3/8 个有
- `PrimitiveInt` —— 3/8 个有
- `SimpleMath+` —— 3/8 个有
- `WanVideoLoraSelect` —— 3/8 个有
- `WanVideoTorchCompileSettings` —— 3/8 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/8 个有
- `GIMMVFI_interpolate` —— 2/8 个有
- `Label (rgthree)` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `Text Multiline` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `Bookmark (rgthree)` —— 1/8 个有
- `PrimitiveFloat` —— 1/8 个有
- `RHHiddenNodes` —— 1/8 个有
- `RH_Nano_Banana2_Image2Image` —— 1/8 个有
- `SDPoseOODLoader` —— 1/8 个有
- `SDPoseOODProcessor` —— 1/8 个有
- `SaveImage` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
