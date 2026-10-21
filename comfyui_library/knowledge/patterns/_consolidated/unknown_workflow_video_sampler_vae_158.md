---
name: unknown_workflow_video_sampler_vae_158
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.808
common_nodes: [INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1949705582357422081.json, 视频生成/图生视频/1949690915247017986.json, 视频生成/图生视频/1934266814887063554.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_158

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1949705582357422081.json、视频生成/图生视频/1949690915247017986.json、视频生成/图生视频/1934266814887063554.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoPhantomEmbeds`
- `WanVideoSampler`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImageFromUrl` —— 2/3 个有
- `Note Plus (mtb)` —— 2/3 个有
- `WanVideoApplyNAG` —— 2/3 个有
- `WanVideoLoraSelect` —— 2/3 个有
- `WanVideoTextEncodeSingle` —— 2/3 个有
- `WanVideoEnhanceAVideo` —— 1/3 个有
- `WanVideoSLG` —— 1/3 个有
- `WanVideoTextEncode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
