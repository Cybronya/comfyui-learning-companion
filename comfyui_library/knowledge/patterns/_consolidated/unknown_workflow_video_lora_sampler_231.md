---
name: unknown_workflow_video_lora_sampler_231
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.6075
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, GetImageSizeAndCount, GrowMaskWithBlur, INTConstant, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/4号工作流跳舞_2085004895417098242.json, 视频生成/图生视频/40秒以上-WanAnimate Sec-人物迁移_动作迁移_长视频循环_1984495051466293249.json, 视频生成/图生视频/AI换人术把你代入名场面，本来应该从从容容游刃有余_1976931314983161857.json, 视频生成/图生视频/Wan+AnimateV2指定区域迁移工作流_1995369036512997378.json, 视频生成/图生视频/WanAnimate -人物迁移_动作迁移_长视频（动作迁移支持卡通）_2058362232681091073.json, 视频生成/图生视频/WanAnimate_Sec-人物_动作迁移（解决长视频偏色等劣化问题）_2027340250565054465.json, 视频生成/图生视频/WanAnimate_Sec-人物迁移_动作迁移_长视频（动作迁移支持卡通）_2008938707402891265.json, 视频生成/图生视频/Work-Fisher-WanAnimate_Sec-人物迁移_动作迁移_长视频循环_2018160297319604226.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_231

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/4号工作流跳舞_2085004895417098242.json、视频生成/图生视频/40秒以上-WanAnimate Sec-人物迁移_动作迁移_长视频循环_1984495051466293249.json、视频生成/图生视频/AI换人术把你代入名场面，本来应该从从容容游刃有余_1976931314983161857.json、视频生成/图生视频/Wan+AnimateV2指定区域迁移工作流_1995369036512997378.json、视频生成/图生视频/WanAnimate -人物迁移_动作迁移_长视频（动作迁移支持卡通）_2058362232681091073.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 8 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
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
- `ImageFromBatch` —— 7/8 个有
- `PrimitiveInt` —— 7/8 个有
- `SeCModelLoader` —— 7/8 个有
- `SeCVideoSegmentation` —— 7/8 个有
- `WanVideoTorchCompileSettings` —— 7/8 个有
- `easy int` —— 7/8 个有
- `easy showAnything` —— 7/8 个有
- `Fast Groups Bypasser (rgthree)` —— 6/8 个有
- `PointsEditor` —— 5/8 个有
- `ColorMatch` —— 2/8 个有
- `DWPreprocessor` —— 2/8 个有
- `PixelPerfectResolution` —— 2/8 个有
- `PrimitiveFloat` —— 2/8 个有
- `Sa2VANodeTpl` —— 2/8 个有
- `SetNode` —— 2/8 个有
- `SimpleMath+` —— 2/8 个有
- `WanVideoContextOptions` —— 2/8 个有
- `easy mathInt` —— 2/8 个有
- `Bjornulf_ShowInt` —— 1/8 个有
- `CR Text` —— 1/8 个有
- `DownloadAndLoadSAM2Model` —— 1/8 个有
- `Float` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `ImageUpscaleWithModelBatched` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `RIFE VFI` —— 1/8 个有
- `Sam2Segmentation` —— 1/8 个有
- `UpscaleModelLoader` —— 1/8 个有
- `VHS_VideoInfo` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
