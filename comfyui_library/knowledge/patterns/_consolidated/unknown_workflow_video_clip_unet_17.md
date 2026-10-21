---
name: unknown_workflow_video_clip_unet_17
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.68025
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageResizeKJv2, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/2008338677897895938.json, 视频生成/图生视频/1983512316119588865.json, 视频生成/图生视频/1979526029473648642.json, 视频生成/图生视频/2050914662958542849.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_17

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2008338677897895938.json、视频生成/图生视频/1983512316119588865.json、视频生成/图生视频/1979526029473648642.json、视频生成/图生视频/2050914662958542849.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 3/4 个有
- `ImpactInt` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `KSamplerAdvanced` —— 2/4 个有
- `ModelSamplingSD3` —— 2/4 个有
- `WanFirstLastFrameToVideo` —— 2/4 个有
- `WanImageToVideo` —— 2/4 个有
- `WanMoeKSampler` —— 2/4 个有
- `Anything Everywhere` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `YANC.MultilineString` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 7 | 6 - 8 | 4 | 86% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | 1 | - | 2 | 100% |
| 重绘幅度 | euler_ancestral | - | 4 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 7，观测区间 6 - 8，4 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，4 个样本，一致性 50%
