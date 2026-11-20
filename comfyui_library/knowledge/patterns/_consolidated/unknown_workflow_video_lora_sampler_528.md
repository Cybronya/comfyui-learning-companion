---
name: unknown_workflow_video_lora_sampler_528
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.6175
common_nodes: [DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, GetImageSizeAndCount, GetNode, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoControlEmbeds, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2_Funcontrol图生视频（动作迁移）_1954008121176051713.json, 视频生成/图生视频/wanvideo_Fun_2_2_control_深度图控制_1955648318090067969.json, 视频生成/图生视频/【升级版】Wan2.2 极致真人舞蹈动作视频迁移 FunControl_1972907220843302914.json, 视频生成/图生视频/极致真人舞蹈视频迁移(Wan2.2-FunControl)_1954879516944601090.json, 视频生成/文生视频/Wan2.2 极致真人舞蹈动作视频迁移 FunControl_1956170101122891778.json, 视频生成/文生视频/Wan2.2美女舞蹈视频动作迁移_1964248050468274178.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_528

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Wan2.2_Funcontrol图生视频（动作迁移）_1954008121176051713.json、视频生成/图生视频/wanvideo_Fun_2_2_control_深度图控制_1955648318090067969.json、视频生成/图生视频/【升级版】Wan2.2 极致真人舞蹈动作视频迁移 FunControl_1972907220843302914.json、视频生成/图生视频/极致真人舞蹈视频迁移(Wan2.2-FunControl)_1954879516944601090.json、视频生成/文生视频/Wan2.2 极致真人舞蹈动作视频迁移 FunControl_1956170101122891778.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 6 个 workflow 都包含：
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoControlEmbeds`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 5/6 个有
- `DWPreprocessor` —— 4/6 个有
- `ImageBlend` —— 4/6 个有
- `PrimitiveInt` —— 4/6 个有
- `WanVideoEmptyEmbeds` —— 4/6 个有
- `Zoe-DepthMapPreprocessor` —— 4/6 个有
- `AIO_Preprocessor` —— 1/6 个有
- `GetImageRangeFromBatch` —— 1/6 个有
- `ImageBlur` —— 1/6 个有
- `Int` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `VHS_VideoInfoLoaded` —— 1/6 个有
- `easy showAnything` —— 1/6 个有
- `workflow>文本处理` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
