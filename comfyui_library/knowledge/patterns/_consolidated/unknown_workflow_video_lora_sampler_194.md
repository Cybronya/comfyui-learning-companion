---
name: unknown_workflow_video_lora_sampler_194
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.86825
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Wan2.2+Animate+V2视频水印去除_2003126840954880002.json, 视频生成/图生视频/02角色迁移更新+全节点注释_2055549996304478210.json, 视频生成/图生视频/Wan2.2 Animate-动作迁移_2011410598436806658.json, 视频生成/图生视频/Wan2.2 Animate-动作迁移_2011439752528011266.json, 视频生成/图生视频/Wan2.2 Animate：角色动画革新，表演艺术的完美复刻！角色替换、动作迁移、图生视频_1969217356767653890.json, 视频生成/图生视频/Wan2.2+Animate：角色替换、动作迁移、图生视频 美女跳舞视频，表演艺术的完美复刻！_1979432276058607617.json, 视频生成/图生视频/Wan2.2-Animate-视频动作迁移_2067088794045734914.json, 视频生成/图生视频/Wan2.2-Animate-视频动作迁移_2069232638564593665.json, 视频生成/图生视频/Wan2.2-Animate-视频换脸+换装+动作模仿+迁移跳舞_1993696432154755073.json, 视频生成/图生视频/Wan2.2_Animate-动作迁移_2116655055440007170.json, 视频生成/图生视频/wan 2.2 Animate 视频动作迁移，人物替换，图生视频，脸部参考，基础用法简单演示_1970498046612172801.json, 视频生成/图生视频/wan2.2-animate动作迁移_1969648359260758017.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_194

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（平台全量/Wan2.2+Animate+V2视频水印去除_2003126840954880002.json、视频生成/图生视频/02角色迁移更新+全节点注释_2055549996304478210.json、视频生成/图生视频/Wan2.2 Animate-动作迁移_2011410598436806658.json、视频生成/图生视频/Wan2.2 Animate-动作迁移_2011439752528011266.json、视频生成/图生视频/Wan2.2 Animate：角色动画革新，表演艺术的完美复刻！角色替换、动作迁移、图生视频_1969217356767653890.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
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
- `DWPreprocessor` —— 11/12 个有
- `FaceMaskFromPoseKeypoints` —— 11/12 个有
- `ImageCropByMaskAndResize` —— 11/12 个有
- `PixelPerfectResolution` —— 11/12 个有
- `WanVideoLoraSelectMulti` —— 10/12 个有
- `GetImageSizeAndCount` —— 9/12 个有
- `JWInteger` —— 9/12 个有
- `ImageConcatMulti` —— 8/12 个有
- `RHHiddenNodes` —— 7/12 个有
- `Text` —— 7/12 个有
- `BlockifyMask` —— 5/12 个有
- `DrawMaskOnImage` —— 5/12 个有
- `GrowMask` —— 5/12 个有
- `WanVideoAnimateEmbeds` —— 5/12 个有
- `PreviewImage` —— 3/12 个有
- `SetNode` —— 3/12 个有
- `DownloadAndLoadSAM2Model` —— 2/12 个有
- `GetImageSize+` —— 2/12 个有
- `GetNode` —— 2/12 个有
- `LayerMask: SegformerB2ClothesUltra` —— 2/12 个有
- `PointsEditor` —— 2/12 个有
- `Sam2Segmentation` —— 2/12 个有
- `WanVideoLoraSelect` —— 2/12 个有
- `Fast Muter (rgthree)` —— 1/12 个有
- `INTConstant` —— 1/12 个有
- `LayerMask: BiRefNetUltraV2` —— 1/12 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/12 个有
- `LayerUtility: CropByMask V2` —— 1/12 个有
- `LayerUtility: PurgeVRAM` —— 1/12 个有
- `RH_Captioner` —— 1/12 个有
- `SimpleMath+` —— 1/12 个有
- `WanVideoTorchCompileSettings` —— 1/12 个有
- `easy cleanGpuUsed` —— 1/12 个有
- `easy sam3ModelLoader` —— 1/12 个有
- `easy sam3VideoSegmentation` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
