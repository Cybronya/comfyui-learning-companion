---
name: unknown_workflow_video_lora_sampler_193
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.712
common_nodes: [CLIPVisionLoader, DWPreprocessor, ImageResizeKJv2, LoadImage, PixelPerfectResolution, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Wan2.2 animate 动作迁移KJ版_1976818662579621890.json, 平台全量/Wan2.2 animate 视频人物、背景更换_1977377943250968578.json, 平台全量/Wan2.2 animate 视频衣服替换_1977227006632972289.json, 平台全量/Wan2.2 animate表情动作迁移（适合中近景））_1970410230880346113.json, 平台全量/Wan2.2-Animate 动作表情迁移 动作模仿 跳舞视频工作流_2052800204788776962.json, 平台全量/Wan2.2-Animate视频多合1工作流 (动作参考、角色替换、视频换装换L换万物)_1997641273764941825.json, 数字人/数字人/AI模仿mean girl表情打量别人，Wan-Animate数字人初体验_1969328742353039362.json, 视频生成/图生视频/Wan-Animate-动作参考-KJ_1969398350657318913.json, 视频生成/图生视频/Wan-Animate-角色替换-KJ_1962703044544737281.json, 视频生成/图生视频/Wan-Animate-角色替换-人物唱歌-KJ_1969620771280744450.json, 视频生成/图生视频/Wan-Animate-角色替换-小鸟摇-KJ_1969608004544983041.json, 视频生成/图生视频/Wan-Animate动作表情迁移遮罩_1969402248658907137.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_193

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（平台全量/Wan2.2 animate 动作迁移KJ版_1976818662579621890.json、平台全量/Wan2.2 animate 视频人物、背景更换_1977377943250968578.json、平台全量/Wan2.2 animate 视频衣服替换_1977227006632972289.json、平台全量/Wan2.2 animate表情动作迁移（适合中近景））_1970410230880346113.json、平台全量/Wan2.2-Animate 动作表情迁移 动作模仿 跳舞视频工作流_2052800204788776962.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `ImageResizeKJv2`
- `LoadImage`
- `PixelPerfectResolution`
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
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `FaceMaskFromPoseKeypoints` —— 11/12 个有
- `ImageCropByMaskAndResize` —— 11/12 个有
- `BlockifyMask` —— 10/12 个有
- `DownloadAndLoadSAM2Model` —— 10/12 个有
- `DrawMaskOnImage` —— 10/12 个有
- `Sam2Segmentation` —— 10/12 个有
- `GetImageSizeAndCount` —— 9/12 个有
- `PointsEditor` —— 9/12 个有
- `WanVideoSetLoRAs` —— 9/12 个有
- `GrowMask` —— 8/12 个有
- `PreviewImage` —— 8/12 个有
- `INTConstant` —— 7/12 个有
- `SimpleMath+` —— 7/12 个有
- `ImageConcatMulti` —— 6/12 个有
- `GetNode` —— 5/12 个有
- `Int` —— 5/12 个有
- `SetNode` —— 5/12 个有
- `AudioCropProcessUTK` —— 4/12 个有
- `GetImageRangeFromBatch` —— 4/12 个有
- `easy cleanGpuUsed` —— 3/12 个有
- `Fast Groups Muter (rgthree)` —— 2/12 个有
- `GrowMaskWithBlur` —— 2/12 个有
- `Switch image [Crystools]` —— 2/12 个有
- `VHS_VideoInfoLoaded` —— 2/12 个有
- `easy showAnything` —— 2/12 个有
- `Bjornulf_ShowInt` —— 1/12 个有
- `DownloadAndLoadFlorence2Model` —— 1/12 个有
- `Florence2Run` —— 1/12 个有
- `Florence2toCoordinates` —— 1/12 个有
- `InvertMask` —— 1/12 个有
- `Label (rgthree)` —— 1/12 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/12 个有
- `MaskToImage` —— 1/12 个有
- `Mix Color By Mask` —— 1/12 个有
- `RMBG` —— 1/12 个有
- `SaveImage` —— 1/12 个有
- `TT_img_enc` —— 1/12 个有
- `VHS_VideoInfo` —— 1/12 个有
- `WanVideoContextOptions` —— 1/12 个有
- `easy clearCacheAll` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
