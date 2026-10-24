---
name: unknown_workflow_video_sampler_vae_122
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9096
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Self Forcing 30秒81帧文生视频_1932675120529821697.json, 视频生成/文生视频/Self Forcing 超快文生视频_1932781560670081026.json, 视频生成/文生视频/Wan2.1 FusionX文生视频工作流_1961757456491810818.json, 视频生成/文生视频/Wan2.1(KJ)文本到视频基础工作流_1946120056569774081.json, 视频生成/文生视频/Wan21 FusionX 文生图-极速版本_1940772323597434882.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_122

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/Self Forcing 30秒81帧文生视频_1932675120529821697.json、视频生成/文生视频/Self Forcing 超快文生视频_1932781560670081026.json、视频生成/文生视频/Wan2.1 FusionX文生视频工作流_1961757456491810818.json、视频生成/文生视频/Wan2.1(KJ)文本到视频基础工作流_1946120056569774081.json、视频生成/文生视频/Wan21 FusionX 文生图-极速版本_1940772323597434882.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTextEncode` —— 4/5 个有
- `Int` —— 3/5 个有
- `WanVideoExperimentalArgs` —— 3/5 个有
- `WanVideoTeaCache` —— 3/5 个有
- `WanVideoTorchCompileSettings` —— 3/5 个有
- `SimpleMath+` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `DualCLIPLoader` —— 1/5 个有
- `JWInteger` —— 1/5 个有
- `WanVideoApplyNAG` —— 1/5 个有
- `WanVideoLoraSelectMulti` —— 1/5 个有
- `WanVideoTextEncodeSingle` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
