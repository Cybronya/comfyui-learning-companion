---
name: unknown_workflow_video_lora_sampler_199
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.6275
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, GetImageSizeAndCount, GrowMaskWithBlur, INTConstant, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SeCModelLoader, SeCVideoSegmentation, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/4号工作流跳舞_2085004895417098242.json, 数字人/数字人/1029alan测-WanAnimate_Sec-人物迁移_动作迁移_长视频循环_1983470782452047874.json, 数字人/数字人/30秒以上-WanAnimate Sec-人物迁移_动作迁移_长视频循环 1029_1983533563104665601.json, 数字人/数字人/Sec版本-视频人物替换-Wan Animate20251017_1978992368751906818.json, 数字人/数字人/WanAnimate动作迁移_1999767180088668161.json, 数字人/数字人/视频人物替换电商跨境wan2.2-Animate_1988091546115416066.json, 视频生成/图生视频/40秒以上-WanAnimate Sec-人物迁移_动作迁移_长视频循环_1984495051466293249.json, 视频生成/图生视频/Wan+AnimateV2指定区域迁移工作流_1995369036512997378.json, 视频生成/图生视频/WanAnimate -人物迁移_动作迁移_长视频（动作迁移支持卡通）_2058362232681091073.json, 视频生成/图生视频/WanAnimate_Sec-人物迁移_动作迁移_长视频（动作迁移支持卡通）_2008938707402891265.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_199

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/4号工作流跳舞_2085004895417098242.json、数字人/数字人/1029alan测-WanAnimate_Sec-人物迁移_动作迁移_长视频循环_1983470782452047874.json、数字人/数字人/30秒以上-WanAnimate Sec-人物迁移_动作迁移_长视频循环 1029_1983533563104665601.json、数字人/数字人/Sec版本-视频人物替换-Wan Animate20251017_1978992368751906818.json、数字人/数字人/WanAnimate动作迁移_1999767180088668161.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 10 个 workflow 都包含：
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
- `SeCModelLoader`
- `SeCVideoSegmentation`
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
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch` —— 8/10 个有
- `PointsEditor` —— 8/10 个有
- `PreviewImage` —— 8/10 个有
- `PrimitiveInt` —— 8/10 个有
- `easy int` —— 8/10 个有
- `WanVideoTorchCompileSettings` —— 7/10 个有
- `Fast Groups Bypasser (rgthree)` —— 6/10 个有
- `SetNode` —— 3/10 个有
- `ColorMatch` —— 2/10 个有
- `ConvertAny2Int` —— 2/10 个有
- `DWPreprocessor` —— 2/10 个有
- `GetNode` —— 2/10 个有
- `ImageConcatMulti` —— 2/10 个有
- `PixelPerfectResolution` —— 2/10 个有
- `PrimitiveFloat` —— 2/10 个有
- `Sa2VANodeTpl` —— 2/10 个有
- `SimpleMath+` —— 2/10 个有
- `Text` —— 2/10 个有
- `easy float` —— 2/10 个有
- `easy mathInt` —— 2/10 个有
- `Bjornulf_ShowInt` —— 1/10 个有
- `CR Text` —— 1/10 个有
- `Float` —— 1/10 个有
- `ImageUpscaleWithModelBatched` —— 1/10 个有
- `RIFE VFI` —— 1/10 个有
- `UpscaleModelLoader` —— 1/10 个有
- `VHS_VideoInfo` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
