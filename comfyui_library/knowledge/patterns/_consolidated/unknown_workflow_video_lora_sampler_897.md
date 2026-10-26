---
name: unknown_workflow_video_lora_sampler_897
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9275
common_nodes: [CreateCFGScheduleFloatList, Display Any (rgthree), INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy globalSeed]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 图生视频_kj_多Lora加速版+画质调色_1965423072939491330.json, 视频生成/图生视频/wan2.2 KJ版图生视频-低显存工作流_1950109940024262657.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_897

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 图生视频_kj_多Lora加速版+画质调色_1965423072939491330.json、视频生成/图生视频/wan2.2 KJ版图生视频-低显存工作流_1950109940024262657.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `Display Any (rgthree)`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy globalSeed`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `ColorMatch` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `MathExpression_UTK` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `Wan22PromptSelector` —— 1/2 个有
- `WanVideoEnhanceAVideo` —— 1/2 个有
- `WanVideoLoraSelectMulti` —— 1/2 个有
- `WanVideoSLG` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
