---
name: unknown_workflow_video_lora_sampler_953
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.818
common_nodes: [Anything Everywhere, FantasyPortraitModelLoader, FantasyTalkingModelLoader, MultiTalkModelLoader, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/wan 2.1 文生视频 （综合拆分）_2001587510151114753.json, 视频生成/文生视频/wan2.1+2.2 基础综合版_2001569276173664257.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_953

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/wan 2.1 文生视频 （综合拆分）_2001587510151114753.json、视频生成/文生视频/wan2.1+2.2 基础综合版_2001569276173664257.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `FantasyPortraitModelLoader`
- `FantasyTalkingModelLoader`
- `MultiTalkModelLoader`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTeaCache`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `CreateCFGScheduleFloatList` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `WanVideoClipVisionEncode` —— 1/2 个有
- `WanVideoImageToVideoEncode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
