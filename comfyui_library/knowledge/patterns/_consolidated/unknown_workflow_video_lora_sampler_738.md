---
name: unknown_workflow_video_lora_sampler_738
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPVisionLoader, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, Text Multiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1977940340936167425.json, 视频生成/图生视频/1945016400298827777.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_738

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1977940340936167425.json、视频生成/图生视频/1945016400298827777.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Text Multiline`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DF_Int_to_Float` —— 1/2 个有
- `ImageUpscaleWithModelBatched` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `Int` —— 1/2 个有
- `LazySwitchKJ` —— 1/2 个有
- `MultiplyNode` —— 1/2 个有
- `NumberClamp` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `WanVideoFreeInitArgs` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有
- `sanmi IntToBOOLEAN` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
