---
name: unknown_workflow_video_lora_sampler_384
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.6595
common_nodes: [GetImageSizeAndCount, ImageConcatMulti, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoControlEmbeds, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1972907220843302914.json, 视频生成/图生视频/1955886992418590722.json, 视频生成/图生视频/1954879516944601090.json, 视频生成/图生视频/1955559935833620481.json, 视频生成/文生视频/1956170101122891778.json, 视频生成/文生视频/1964248050468274178.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_384

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1972907220843302914.json、视频生成/图生视频/1955886992418590722.json、视频生成/图生视频/1954879516944601090.json、视频生成/图生视频/1955559935833620481.json、视频生成/文生视频/1956170101122891778.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 6 个 workflow 都包含：
- `GetImageSizeAndCount`
- `ImageConcatMulti`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 5/6 个有
- `DepthAnything_V2` —— 5/6 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 5/6 个有
- `GetNode` —— 5/6 个有
- `ImageBlend` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `Zoe-DepthMapPreprocessor` —— 5/6 个有
- `PrimitiveInt` —— 4/6 个有
- `WanVideoEmptyEmbeds` —— 4/6 个有
- `GetImageRangeFromBatch` —— 1/6 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/6 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有
- `RH_Translator` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
