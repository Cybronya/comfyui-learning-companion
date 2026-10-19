---
name: unknown_workflow_video_sampler_vae_167
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.908
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/1946120056569774081.json, 视频生成/文生视频/1933749868416389122.json, 视频生成/文生视频/1934524446843568130.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_167

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/1946120056569774081.json、视频生成/文生视频/1933749868416389122.json、视频生成/文生视频/1934524446843568130.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
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
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 2/3 个有
- `Primitive integer [Crystools]` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `DualCLIPLoader` —— 1/3 个有
- `WanVideoLoraSelectMulti` —— 1/3 个有
- `WanVideoTorchCompileSettings` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
