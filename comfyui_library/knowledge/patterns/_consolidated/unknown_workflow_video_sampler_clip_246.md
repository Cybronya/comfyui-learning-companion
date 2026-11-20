---
name: unknown_workflow_video_sampler_clip_246
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, Fast Groups Bypasser (rgthree), GetNode, HunyuanVideoFoley, ImageResizeKJv2, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, QZ_ResolutionPreset, Qwen3_VQA, RIFE VFI, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, WanMoeKSampler, easy cleanGpuUsed, easy promptLine, easy showAnything, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.2+Qwen3VL+Foley_全自动自配音效图生视频_2043951609989828610.json, 视频生成/图生视频/WAN2.2+Qwen3VL+Foley音效 全自动图生视频配音_1986984550565916673.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_246

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/WAN2.2+Qwen3VL+Foley_全自动自配音效图生视频_2043951609989828610.json、视频生成/图生视频/WAN2.2+Qwen3VL+Foley音效 全自动图生视频配音_1986984550565916673.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：50%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `HunyuanVideoFoley`
- `ImageResizeKJv2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `QZ_ResolutionPreset`
- `Qwen3_VQA`
- `RIFE VFI`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `WanMoeKSampler`
- `easy cleanGpuUsed`
- `easy promptLine`
- `easy showAnything`
- `wanBlockSwap`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | 1 | - | 2 | 100% |
| 重绘幅度 | euler | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
