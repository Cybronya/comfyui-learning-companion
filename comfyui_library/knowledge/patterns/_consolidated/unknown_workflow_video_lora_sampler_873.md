---
name: unknown_workflow_video_lora_sampler_873
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.645
common_nodes: [AddLabel, Bjornulf_ShowStringText, ColorMatch, DWPreprocessor, GetImageSizeAndCount, GetNode, ImageConcanate, ImageResizeKJv2, Int2String, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, RH_LLMAPI_NODE, SetNode, ShowText, SimpleCondition+, Text Multiline, VHS_LoadVideo, VHS_LoadVideoFFmpeg, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoBlockSwap, WanVideoDecode, WanVideoEasyCache, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoFreeInitArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetRadialAttention, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy cleanGpuUsed, easy clearCacheAll, preview_mask]
problems: []
missing: []
members: [视频生成/图生视频/1948987211699105793.json, 视频生成/文生视频/1955564554321367042.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_873

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1948987211699105793.json、视频生成/文生视频/1955564554321367042.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `AddLabel`
- `Bjornulf_ShowStringText`
- `ColorMatch`
- `DWPreprocessor`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcanate`
- `ImageResizeKJv2`
- `Int2String`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `SetNode`
- `ShowText`
- `SimpleCondition+`
- `Text Multiline`
- `VHS_LoadVideo`
- `VHS_LoadVideoFFmpeg`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEasyCache`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoFreeInitArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetRadialAttention`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `preview_mask`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
