---
name: unknown_workflow_video_lora_sampler_809
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5635
common_nodes: [GetImageSizeAndCount, GetNode, LoadImage, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy int]
problems: []
missing: []
members: [视频生成/图生视频/1980164711092228097.json, 视频生成/图生视频/1924012489724317698.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_809

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1980164711092228097.json、视频生成/图生视频/1924012489724317698.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 2 个 workflow 都包含：
- `GetImageSizeAndCount`
- `GetNode`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `RIFE VFI` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `String Literal` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `WanVideoEasyCache` —— 1/2 个有
- `WanVideoSetRadialAttention` —— 1/2 个有
- `easy float` —— 1/2 个有
- `easy negative` —— 1/2 个有
- `easy positive` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
