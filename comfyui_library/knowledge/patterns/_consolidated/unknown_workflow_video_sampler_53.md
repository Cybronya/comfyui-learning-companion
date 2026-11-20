---
name: unknown_workflow_video_sampler_53
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.96
common_nodes: [GetImageSizeAndCount, ImageResizeKJv2, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoInfoLoaded, WanVideoAddFlashVSRInput, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoExtraModelSelect, WanVideoFlashVSRDecoderLoader, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings]
problems: []
missing: []
members: [平台全量/快速视频超分_FlashVSR_upscale_1978745331083005954.json, 平台全量/视频高清化工作流FlashVSR_1981312792114397185.json, 平台全量/视频高清处理丨FlashVSR视频高清工作流_1980106656715542530.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_53

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/快速视频超分_FlashVSR_upscale_1978745331083005954.json、平台全量/视频高清化工作流FlashVSR_1981312792114397185.json、平台全量/视频高清处理丨FlashVSR视频高清工作流_1980106656715542530.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoInfoLoaded`
- `WanVideoAddFlashVSRInput`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoExtraModelSelect`
- `WanVideoFlashVSRDecoderLoader`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `ColorMatch` —— 1/3 个有
- `ColorMatch_UTK` —— 1/3 个有
- `CreateVideo` —— 1/3 个有
- `GetImagesFromBatchIndexed` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `SaveVideo` —— 1/3 个有
- `WanVideoBlockSwap` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
