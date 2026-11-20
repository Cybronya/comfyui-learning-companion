---
name: unknown_workflow_video_lora_sampler_639
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.60175
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, GetImageSizeAndCount, INTConstant, ImageFromBatch, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PointsEditor, PoseAndFaceDetection, PreviewImage, PrimitiveInt, SeCModelLoader, SeCVideoSegmentation, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/4号工作流跳舞_2085004895417098242.json, 平台全量/5.其他类型-4.迁移类-1.wan-40-50系显卡-001.WanAnimate动作迁移工作流_2018323117768187906.json, 平台全量/JY金鱼-Animate_Mix_v3.2_1977042531110277121.json, 平台全量/WanAnimate_Sec-人物迁移_动作迁移_1992675730513522689.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_639

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/4号工作流跳舞_2085004895417098242.json、平台全量/5.其他类型-4.迁移类-1.wan-40-50系显卡-001.WanAnimate动作迁移工作流_2018323117768187906.json、平台全量/JY金鱼-Animate_Mix_v3.2_1977042531110277121.json、平台全量/WanAnimate_Sec-人物迁移_动作迁移_1992675730513522689.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 4 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetImageSizeAndCount`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `GrowMaskWithBlur` —— 3/4 个有
- `easy int` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `ImageUpscaleWithModelBatched` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `UpscaleModelLoader` —— 2/4 个有
- `Bjornulf_ShowInt` —— 1/4 个有
- `CoordinatePlotter` —— 1/4 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/4 个有
- `EmptyImage` —— 1/4 个有
- `GIMMVFI_interpolate` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `GrowMask` —— 1/4 个有
- `ImageBlend` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `ImageUpscaleWithModel` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `PlaySound|pysssss` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `RHBatchImages:` —— 1/4 个有
- `RIFE VFI` —— 1/4 个有
- `SAM2Segment` —— 1/4 个有
- `VHS_VideoInfo` —— 1/4 个有
- `WanVideoLoraSelect` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
