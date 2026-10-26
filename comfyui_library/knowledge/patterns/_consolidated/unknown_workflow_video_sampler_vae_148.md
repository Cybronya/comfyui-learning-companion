---
name: unknown_workflow_video_sampler_vae_148
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.933333
common_nodes: [LoadWanVideoT5TextEncoder, WanVideoApplyNAG, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/Wan2.1 高质量文生图_1945360629114839041.json, 视频生成/文生视频/Wan2.1-文生视频_1949672954677862402.json, 视频生成/文生视频/Wan2.1_FusionX文生视频_1935147555195920385.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_148

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Wan2.1 高质量文生图_1945360629114839041.json、视频生成/文生视频/Wan2.1-文生视频_1949672954677862402.json、视频生成/文生视频/Wan2.1_FusionX文生视频_1935147555195920385.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `WanVideoApplyNAG`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 2/3 个有
- `WanVideoBlockSwap` —— 2/3 个有
- `WanVideoLoraSelect` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `FluxResolutionNode` —— 1/3 个有
- `Int` —— 1/3 个有
- `SaveImage` —— 1/3 个有
- `WanVideoExperimentalArgs` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
