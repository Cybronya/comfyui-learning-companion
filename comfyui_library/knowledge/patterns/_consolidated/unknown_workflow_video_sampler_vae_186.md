---
name: unknown_workflow_video_sampler_vae_186
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.755
common_nodes: [ColorMatch, DownloadAndLoadHyVideoTextEncoder, HyVideoBlockSwap, HyVideoCFG, HyVideoDecode, HyVideoEncode, HyVideoEnhanceAVideo, HyVideoModelLoader, HyVideoSampler, HyVideoTextEncode, HyVideoTorchCompileSettings, HyVideoVAELoader, ImageResizeKJ, Int, LoadImage, MathExpression|pysssss, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/图生视频，SkyReels_1892222949557243905.json, 视频生成/图生视频/混元_SkyReels_图生视频，对标可灵与海螺等！_1892126522352820225.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_186

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/图生视频，SkyReels_1892222949557243905.json、视频生成/图生视频/混元_SkyReels_图生视频，对标可灵与海螺等！_1892126522352820225.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `ColorMatch`
- `DownloadAndLoadHyVideoTextEncoder`
- `HyVideoBlockSwap`
- `HyVideoCFG`
- `HyVideoDecode`
- `HyVideoEncode`
- `HyVideoEnhanceAVideo`
- `HyVideoModelLoader`
- `HyVideoSampler`
- `HyVideoTextEncode`
- `HyVideoTorchCompileSettings`
- `HyVideoVAELoader`
- `ImageResizeKJ`
- `Int`
- `LoadImage`
- `MathExpression|pysssss`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `Float` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
