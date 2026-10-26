---
name: unknown_workflow_video_sampler_20
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.666667
common_nodes: [ColorMatch, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddFlashVSRInput, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoExtraModelSelect, WanVideoFlashVSRDecoderLoader, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/视频变清晰 Flash VSR_1979901489286123522.json, 数字人/数字人/视频高清 视频变清晰 极速 FlashVSR_1979851667522883585.json, 视频生成/图生视频/视频高清+视频超分+极速+FlashVSR_2075028488192610306.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_20

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/视频变清晰 Flash VSR_1979901489286123522.json、数字人/数字人/视频高清 视频变清晰 极速 FlashVSR_1979851667522883585.json、视频生成/图生视频/视频高清+视频超分+极速+FlashVSR_2075028488192610306.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 3 个 workflow 都包含：
- `ColorMatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddFlashVSRInput`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoExtraModelSelect`
- `WanVideoFlashVSRDecoderLoader`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 2/3 个有
- `VHS_VideoInfo` —— 2/3 个有
- `FlashVSRNode` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `VHS_VideoInfoSource` —— 1/3 个有
- `WanVideoTorchCompileSettings` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
