---
name: unknown_workflow_video_lora_sampler_264
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.6048
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, GetImageSizeAndCount, GrowMaskWithBlur, INTConstant, ImageFromBatch, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PointsEditor, PoseAndFaceDetection, PreviewImage, PrimitiveInt, SeCModelLoader, SeCVideoSegmentation, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/WanAnimate_视频编辑v1(换背景换脸)_2003270400027033602.json, 平台全量/WanAnimate人物迁移_1999742727044689922.json, 平台全量/Work-Fisher-WanAnimate_Sec-人物迁移_动作迁移_长视频循环_1980138368380080129.json, 平台全量/hgjuwhghweighwighweikghwekhweghwewwegw_2000403006531174402.json, 平台全量/htujerhkgohshiowehgkpwegwerhgwe_2015603011342569473.json, 平台全量/wanvideo_WanAnimate_secnode_1978001589359235074.json, 平台全量/动作模仿_2081237456011218945.json, 平台全量/最强人物迁移_动作迁移_长视频循环_2033043274088321025.json, 平台全量/视频_2000476368859262977.json, 视频生成/图生视频/Work-Fisher-WanAnimate_Sec-人物迁移_动作迁移_长视频循环_2018160297319604226.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_264

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/WanAnimate_视频编辑v1(换背景换脸)_2003270400027033602.json、平台全量/WanAnimate人物迁移_1999742727044689922.json、平台全量/Work-Fisher-WanAnimate_Sec-人物迁移_动作迁移_长视频循环_1980138368380080129.json、平台全量/hgjuwhghweighwighweikghwekhweghwewwegw_2000403006531174402.json、平台全量/htujerhkgohshiowehgkpwegwerhgwe_2015603011342569473.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 10 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PointsEditor`
- `PoseAndFaceDetection`
- `PreviewImage`
- `PrimitiveInt`
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

**可变部分**（部分 workflow 才有）：
- `WanVideoTorchCompileSettings` —— 9/10 个有
- `easy int` —— 9/10 个有
- `easy showAnything` —— 9/10 个有
- `Fast Groups Bypasser (rgthree)` —— 5/10 个有
- `GetNode` —— 4/10 个有
- `ImageUpscaleWithModelBatched` —— 4/10 个有
- `RIFE VFI` —— 4/10 个有
- `SetNode` —— 4/10 个有
- `UpscaleModelLoader` —— 4/10 个有
- `Bjornulf_ShowInt` —— 2/10 个有
- `MathExpression|pysssss` —— 2/10 个有
- `VHS_VideoInfo` —— 2/10 个有
- `easy cleanGpuUsed` —— 2/10 个有
- `BitwiseAndMask` —— 1/10 个有
- `CoordinatePlotter` —— 1/10 个有
- `ImageBlend` —— 1/10 个有
- `InvertMask` —— 1/10 个有
- `SubtractMask` —— 1/10 个有
- `easy sam3ModelLoader` —— 1/10 个有
- `easy sam3VideoSegmentation` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
