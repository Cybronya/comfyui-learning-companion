---
name: unknown_workflow_video_lora_sampler_270
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.6295
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, GetImageSizeAndCount, INTConstant, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy int]
problems: []
missing: []
members: [平台全量/基于SAM3的视频人物角色迁移_1992938114272477185.json, 平台全量/视频局部迁移1125_1990313307775135746.json, 数字人/数字人/1029alan测-WanAnimate_Sec-人物迁移_动作迁移_长视频循环_1983470782452047874.json, 数字人/数字人/30秒以上-WanAnimate Sec-人物迁移_动作迁移_长视频循环 1029_1983533563104665601.json, 数字人/数字人/WanAnimate动作迁移_1999767180088668161.json, 视频生成/图生视频/40秒以上-WanAnimate Sec-人物迁移_动作迁移_长视频循环_1984495051466293249.json, 视频生成/图生视频/Wan+AnimateV2指定区域迁移工作流_1995369036512997378.json, 视频生成/图生视频/WanAnimate -人物迁移_动作迁移_长视频（动作迁移支持卡通）_2058362232681091073.json, 视频生成/图生视频/WanAnimate_Sec-人物_动作迁移（解决长视频偏色等劣化问题）_2027340250565054465.json, 视频生成/图生视频/WanAnimate_Sec-人物迁移_动作迁移_长视频（动作迁移支持卡通）_2008938707402891265.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_270

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/基于SAM3的视频人物角色迁移_1992938114272477185.json、平台全量/视频局部迁移1125_1990313307775135746.json、数字人/数字人/1029alan测-WanAnimate_Sec-人物迁移_动作迁移_长视频循环_1983470782452047874.json、数字人/数字人/30秒以上-WanAnimate Sec-人物迁移_动作迁移_长视频循环 1029_1983533563104665601.json、数字人/数字人/WanAnimate动作迁移_1999767180088668161.json…）

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
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
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
- `easy int`

**可变部分**（部分 workflow 才有）：
- `GrowMaskWithBlur` —— 9/10 个有
- `PrimitiveInt` —— 9/10 个有
- `SeCModelLoader` —— 9/10 个有
- `SeCVideoSegmentation` —— 9/10 个有
- `easy showAnything` —— 9/10 个有
- `ImageFromBatch` —— 8/10 个有
- `PreviewImage` —— 8/10 个有
- `WanVideoTorchCompileSettings` —— 8/10 个有
- `Fast Groups Bypasser (rgthree)` —— 6/10 个有
- `PointsEditor` —— 6/10 个有
- `CR Text` —— 3/10 个有
- `ColorMatch` —— 2/10 个有
- `DWPreprocessor` —— 2/10 个有
- `Float` —— 2/10 个有
- `PixelPerfectResolution` —— 2/10 个有
- `PrimitiveFloat` —— 2/10 个有
- `Sa2VANodeTpl` —— 2/10 个有
- `SimpleMath+` —— 2/10 个有
- `easy mathInt` —— 2/10 个有
- `ImpactImageBatchToImageList` —— 1/10 个有
- `LayerMask: MaskGrow` —— 1/10 个有
- `LoadSAM3Model` —— 1/10 个有
- `MaskListToMaskBatch` —— 1/10 个有
- `SAM3Segmentation` —— 1/10 个有
- `WanVideoContextOptions` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
