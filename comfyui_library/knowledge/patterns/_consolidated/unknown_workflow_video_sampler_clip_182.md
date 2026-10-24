---
name: unknown_workflow_video_sampler_clip_182
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.944667
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetImageSizeAndCount, ImageFromBatch, ImpactInt, KSampler, LoadImage, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, TorchCompileModelWanVideo, UNETLoader, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, WanVideoTeaCacheKJ]
problems: []
missing: []
members: [视频生成/图生视频/For循环不限时长图生视频_1901121776833675266.json, 视频生成/图生视频/Wan2.1-15秒图生视频3段扩展_1899668266204221441.json, 视频生成/图生视频/图生视频—15秒视频生成_1899809388968685570.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_182

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/For循环不限时长图生视频_1901121776833675266.json、视频生成/图生视频/Wan2.1-15秒图生视频3段扩展_1899668266204221441.json、视频生成/图生视频/图生视频—15秒视频生成_1899809388968685570.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `ImageFromBatch`
- `ImpactInt`
- `KSampler`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `TorchCompileModelWanVideo`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `WanVideoTeaCacheKJ`

**可变部分**（部分 workflow 才有）：
- `ImageBatch` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `String Literal` —— 1/3 个有
- `Text Load Line From File` —— 1/3 个有
- `easy batchAnything` —— 1/3 个有
- `easy forLoopEnd` —— 1/3 个有
- `easy forLoopStart` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
