---
name: unknown_workflow_video_sampler_vae_168
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.933333
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.1-NAG反向应用_2072999737776971776.json, 视频生成/文生视频/1949672954677862402.json, 视频生成/文生视频/1935147555195920385.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_168

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/Wan2.1-NAG反向应用_2072999737776971776.json、视频生成/文生视频/1949672954677862402.json、视频生成/文生视频/1935147555195920385.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `Int` —— 1/3 个有
- `String Literal` —— 1/3 个有
- `WanVideoEnhanceAVideo` —— 1/3 个有
- `WanVideoExperimentalArgs` —— 1/3 个有
- `WanVideoLoraSelect` —— 1/3 个有
- `WanVideoTeaCache` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
