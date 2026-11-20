---
name: unknown_workflow_video_lora_sampler_271
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.5796
common_nodes: [CLIPVisionLoader, GetNode, ImageResizeKJv2, LoadImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/视频去水印去字幕_2041890719736012802.json, 数字人/数字人/Animate+light2x加速做动_2000076812296351745.json, 数字人/数字人/Wan Animate 2.2-角色替换-动作迁移-图生视频-许老师专用_1981594203375443969.json, 数字人/数字人/Wan Animate2.2换脸V1_2000858355855917057.json, 数字人/数字人/Wan-Animate视频表情动作模仿-人物替换_1970690946574807042.json, 数字人/数字人/wan2.2 animate 一张图片生成跳舞视频_1942136597947301890.json, 数字人/数字人/wanvideo_WanAnimate_角色替换工作流_1969720507606200322.json, 视频生成/图生视频/Animate优化人物一致性精准替换_1969765016436154369.json, 视频生成/图生视频/Animate优化人物一致性精准替换【人物动作表情背景】_1971382393225592834.json, 视频生成/图生视频/Animate优化颜色匹配精准替换人换脸_1971226836661420034.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_271

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/视频去水印去字幕_2041890719736012802.json、数字人/数字人/Animate+light2x加速做动_2000076812296351745.json、数字人/数字人/Wan Animate 2.2-角色替换-动作迁移-图生视频-许老师专用_1981594203375443969.json、数字人/数字人/Wan Animate2.2换脸V1_2000858355855917057.json、数字人/数字人/Wan-Animate视频表情动作模仿-人物替换_1970690946574807042.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 9/10 个有
- `DWPreprocessor` —— 9/10 个有
- `DrawMaskOnImage` —— 9/10 个有
- `FaceMaskFromPoseKeypoints` —— 9/10 个有
- `ImageCropByMaskAndResize` —— 9/10 个有
- `PixelPerfectResolution` —— 9/10 个有
- `DownloadAndLoadSAM2Model` —— 8/10 个有
- `GetImageSizeAndCount` —— 8/10 个有
- `GrowMask` —— 8/10 个有
- `PointsEditor` —— 8/10 个有
- `Sam2Segmentation` —— 8/10 个有
- `INTConstant` —— 7/10 个有
- `ImageConcatMulti` —— 7/10 个有
- `PreviewImage` —— 6/10 个有
- `WanVideoTorchCompileSettings` —— 5/10 个有
- `JWInteger` —— 4/10 个有
- `Text` —— 4/10 个有
- `VHS_VideoInfo` —— 4/10 个有
- `easy cleanGpuUsed` —— 4/10 个有
- `LayerUtility: PurgeVRAM` —— 3/10 个有
- `WanVideoEncode` —— 3/10 个有
- `WanVideoUni3C_ControlnetLoader` —— 3/10 个有
- `WanVideoUni3C_embeds` —— 3/10 个有
- `easy showAnything` —— 3/10 个有
- `Int` —— 2/10 个有
- `Bjornulf_ShowInt` —— 1/10 个有
- `Bookmark (rgthree)` —— 1/10 个有
- `Frame Select` —— 1/10 个有
- `ImageBatchGet` —— 1/10 个有
- `ImageFromBatch` —— 1/10 个有
- `ImitationHueNode` —— 1/10 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/10 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/10 个有
- `LayerUtility: PurgeVRAM V2` —— 1/10 个有
- `LoadRembgByBiRefNetModel` —— 1/10 个有
- `Preview from image [Crystools]` —— 1/10 个有
- `RembgByBiRefNet` —— 1/10 个有
- `Textbox` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
