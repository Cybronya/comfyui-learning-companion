---
name: unknown_workflow_video_lora_sampler_373
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.632167
common_nodes: [GetImageSizeAndCount, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoControlEmbeds, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1957318001500549121.json, 视频生成/图生视频/1957996750323822593.json, 视频生成/图生视频/1954008121176051713.json, 视频生成/图生视频/1955648318090067969.json, 视频生成/图生视频/1955903499915677697.json, 视频生成/文生视频/1957329600441413634.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_373

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1957318001500549121.json、视频生成/图生视频/1957996750323822593.json、视频生成/图生视频/1954008121176051713.json、视频生成/图生视频/1955648318090067969.json、视频生成/图生视频/1955903499915677697.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 6 个 workflow 都包含：
- `GetImageSizeAndCount`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DepthAnything_V2` —— 5/6 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 5/6 个有
- `GetNode` —— 5/6 个有
- `ImageConcatMulti` —— 5/6 个有
- `AIO_Preprocessor` —— 4/6 个有
- `WanVideoTorchCompileSettings` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `ImpactInt` —— 3/6 个有
- `SimpleMath+` —— 3/6 个有
- `GetImageRangeFromBatch` —— 2/6 个有
- `ImageBlend` —— 2/6 个有
- `RHHiddenNodes` —— 2/6 个有
- `easy anythingIndexSwitch` —— 2/6 个有
- `ImageBlur` —— 1/6 个有
- `Int` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `VHS_VideoInfoLoaded` —— 1/6 个有
- `easy showAnything` —— 1/6 个有
- `workflow>文本处理` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
