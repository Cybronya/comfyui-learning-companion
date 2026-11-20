---
name: unknown_workflow_video_sampler_83
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6055
common_nodes: [ColorMatch, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAddFlashVSRInput, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoExtraModelSelect, WanVideoFlashVSRDecoderLoader, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/视频高清 视频变清晰 极速 FlashVSR_1979851667522883585.json, 视频生成/图生视频/视频高清+视频超分+极速+FlashVSR_2075028488192610306.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_83

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/视频高清 视频变清晰 极速 FlashVSR_1979851667522883585.json、视频生成/图生视频/视频高清+视频超分+极速+FlashVSR_2075028488192610306.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
- `ColorMatch`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
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
- `FlashVSRNode` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
