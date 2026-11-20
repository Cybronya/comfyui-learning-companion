---
name: unknown_workflow_video_lora_sampler_942
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.569
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PixelPerfectResolution, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Wan-Animate​​角色动画 (Character Animation)_1969434671211814914.json, 视频生成/文生视频/Wan-Animate角色替换 (Character Replacement)_1969435322595635201.json, 视频生成/文生视频/🦖Wan Animate2.2换主体_1970311265270853633.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_942

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/Wan-Animate​​角色动画 (Character Animation)_1969434671211814914.json、视频生成/文生视频/Wan-Animate角色替换 (Character Replacement)_1969435322595635201.json、视频生成/文生视频/🦖Wan Animate2.2换主体_1970311265270853633.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 3 个 workflow 都包含：
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
- `BlockifyMask` —— 2/3 个有
- `DownloadAndLoadSAM2Model` —— 2/3 个有
- `DrawMaskOnImage` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `GrowMask` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `PointsEditor` —— 2/3 个有
- `Sam2Segmentation` —— 2/3 个有
- `WanVideoContextOptions` —— 2/3 个有
- `Bjornulf_ShowInt` —— 1/3 个有
- `CR Prompt Text` —— 1/3 个有
- `ImageGetSize` —— 1/3 个有
- `ImageResize` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `LayerMask: LoadFlorence2Model` —— 1/3 个有
- `LayerUtility: Florence2Image2Prompt` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `ResizeLongestToNode` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `WanVideoEncode` —— 1/3 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/3 个有
- `WanVideoUni3C_embeds` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
