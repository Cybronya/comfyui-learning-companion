---
name: unknown_workflow_video_sampler_vae_236
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8905
common_nodes: [CR Prompt Text, JWInteger, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/FusionX Nag版双重加速文生视频V1（支持负面词禁用）_1933931993669525506.json, 视频生成/文生视频/Self Forcing 30秒81帧文生视频_1932675120529821697.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_236

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/FusionX Nag版双重加速文生视频V1（支持负面词禁用）_1933931993669525506.json、视频生成/文生视频/Self Forcing 30秒81帧文生视频_1932675120529821697.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Float` —— 1/2 个有
- `Int` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `Primitive integer [Crystools]` —— 1/2 个有
- `WanVideoApplyNAG` —— 1/2 个有
- `WanVideoMagCache` —— 1/2 个有
- `WanVideoTextEncode` —— 1/2 个有
- `WanVideoTextEncodeSingle` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
