---
name: unknown_workflow_video_upscale_lora_10
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.6305
common_nodes: [GetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, Primitive integer [Crystools], RIFE VFI, SetNode, SimpleMath+, TextCombinerTwo, VHS_VideoCombine, Video_Upscale_With_Model, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoMagCache, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/首尾帧-FusionX_VACE_放大_补帧_1933343489382096898.json, 视频生成/图生视频/一键将图像转换为2K高清动态壁纸_1930433955672264705.json, 视频生成/图生视频/图像组合编辑-FusionX_VACE_1929787256947773441.json, 视频生成/图生视频/图生视频-FusionX_VACE_自动补帧放大_1935165726103937025.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_10

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/首尾帧-FusionX_VACE_放大_补帧_1933343489382096898.json、视频生成/图生视频/一键将图像转换为2K高清动态壁纸_1930433955672264705.json、视频生成/图生视频/图像组合编辑-FusionX_VACE_1929787256947773441.json、视频生成/图生视频/图生视频-FusionX_VACE_自动补帧放大_1935165726103937025.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 4 个 workflow 都包含：
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `RIFE VFI`
- `SetNode`
- `SimpleMath+`
- `TextCombinerTwo`
- `VHS_VideoCombine`
- `Video_Upscale_With_Model`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoMagCache`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 3/4 个有
- `GetImageSizeAndCount` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `RH_Captioner` —— 3/4 个有
- `RH_Prompter` —— 3/4 个有
- `WanVideoVACEEncode` —— 3/4 个有
- `WanVideoVACEStartToEndFrame` —— 3/4 个有
- `Anything Everywhere` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `ImageFromBatch+` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `WanVideoEncode` —— 1/4 个有
- `WanVideoPhantomEmbeds` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
