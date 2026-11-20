---
name: unknown_workflow_video_lora_sampler_495
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.717833
common_nodes: [DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, GetImageSizeAndCount, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoControlEmbeds, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/wan2.2-动作迁移-Fun_control加速lora-4步极速-3种控制方式_1956575761157246978.json, 平台全量/控制+参考-Wan2_2-Fun_1954777610963214338.json, 视频生成/图生视频/Wan2.2ControlNet生视频_1957996750323822593.json, 视频生成/图生视频/动作迁移-Wan2.2-深度图控制版本_1955886992418590722.json, 视频生成/图生视频/🐳wan2_2 FUN 控制模型姿态复刻【跳舞转绘等】🦋_1955903499915677697.json, 视频生成/文生视频/通义万相wan2.2视频转绘视频人物替换视频换脸V1.0_1957329600441413634.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_495

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/wan2.2-动作迁移-Fun_control加速lora-4步极速-3种控制方式_1956575761157246978.json、平台全量/控制+参考-Wan2_2-Fun_1954777610963214338.json、视频生成/图生视频/Wan2.2ControlNet生视频_1957996750323822593.json、视频生成/图生视频/动作迁移-Wan2.2-深度图控制版本_1955886992418590722.json、视频生成/图生视频/🐳wan2_2 FUN 控制模型姿态复刻【跳舞转绘等】🦋_1955903499915677697.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 6 个 workflow 都包含：
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `SetNode` —— 5/6 个有
- `WanVideoTorchCompileSettings` —— 5/6 个有
- `AIO_Preprocessor` —— 4/6 个有
- `GetNode` —— 4/6 个有
- `ImageConcatMulti` —— 4/6 个有
- `GetImageRangeFromBatch` —— 3/6 个有
- `ImpactInt` —— 3/6 个有
- `SimpleMath+` —— 3/6 个有
- `easy anythingIndexSwitch` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `ImageBlend` —— 2/6 个有
- `Canny` —— 1/6 个有
- `FloatToSigmas` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `String Literal` —— 1/6 个有
- `StringToFloatList` —— 1/6 个有
- `WanVideoEmptyEmbeds` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
