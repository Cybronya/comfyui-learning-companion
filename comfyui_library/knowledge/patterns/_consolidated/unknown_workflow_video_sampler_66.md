---
name: unknown_workflow_video_sampler_66
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6665
common_nodes: [Bjornulf_ShowInt, GetNode, Int, LoadWanVideoT5TextEncoder, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddFlashVSRInput, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoExtraModelSelect, WanVideoFlashVSRDecoderLoader, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode]
problems: []
missing: []
members: [平台全量/1键模糊视频高清修复-FlashVSR-20251021_1980463391397601282.json, 平台全量/【FlashVSR+ComfyUI】一键把模糊视频变高清！头发丝都能看清！🎬⚡_1979581500872101889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_66

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/1键模糊视频高清修复-FlashVSR-20251021_1980463391397601282.json、平台全量/【FlashVSR+ComfyUI】一键把模糊视频变高清！头发丝都能看清！🎬⚡_1979581500872101889.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `Bjornulf_ShowInt`
- `GetNode`
- `Int`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddFlashVSRInput`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoExtraModelSelect`
- `WanVideoFlashVSRDecoderLoader`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy float` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
