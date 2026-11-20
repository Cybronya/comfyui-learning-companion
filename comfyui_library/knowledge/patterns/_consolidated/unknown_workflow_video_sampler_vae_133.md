---
name: unknown_workflow_video_sampler_vae_133
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9342
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Self Forcing 超快文生视频_1932781560670081026.json, 视频生成/文生视频/VACE 14b 文生视频（WAN2.1）稳定版_1922872818927812610.json, 视频生成/文生视频/Wan2.1(KJ)文本到视频基础工作流_1946120056569774081.json, 视频生成/文生视频/Wan2.1-FusionX文生视频加速工作流_1933749868416389122.json, 视频生成/文生视频/高清FusionX最强文生视频双倍加速版_1934524446843568130.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_133

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/Self Forcing 超快文生视频_1932781560670081026.json、视频生成/文生视频/VACE 14b 文生视频（WAN2.1）稳定版_1922872818927812610.json、视频生成/文生视频/Wan2.1(KJ)文本到视频基础工作流_1946120056569774081.json、视频生成/文生视频/Wan2.1-FusionX文生视频加速工作流_1933749868416389122.json、视频生成/文生视频/高清FusionX最强文生视频双倍加速版_1934524446843568130.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoEmptyEmbeds` —— 4/5 个有
- `WanVideoTeaCache` —— 4/5 个有
- `JWInteger` —— 3/5 个有
- `Primitive integer [Crystools]` —— 2/5 个有
- `Text Multiline` —— 2/5 个有
- `DualCLIPLoader` —— 1/5 个有
- `TextInput_` —— 1/5 个有
- `WanVideoLoraSelectMulti` —— 1/5 个有
- `WanVideoTorchCompileSettings` —— 1/5 个有
- `WanVideoVACEEncode` —— 1/5 个有
- `WanVideoVACEModelSelect` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
