---
name: text_to_image_video_upscale_lora_9
type: Text To Image
frequency: 2
level: weak
coverage: 0.918
common_nodes: [BasicScheduler, BlockSparseAttention, CLIPLoader, CLIPTextEncode, EmptyLatentImage, ExtendIntermediateSigmas, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3Director, MiniMaxH3DirectorFaceRefine, MiniMaxH3DirectorGroupsCombine, MiniMaxH3DirectorRefine, MiniMaxH3DirectorSelfLift, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, ModelAttentionBackend, PathchSageAttentionKJ, PreviewAny, PrimitiveStringMultiline, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/允希V8.2闭唇正脸一秒轻触首尾帧｜单图外接口播版_2111330532469600258.json, 视频生成/图生视频/允希V8.2闭唇正脸主体参考版｜单图外接一秒轻触_2111335218408943617.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_lora_9

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/允希V8.2闭唇正脸一秒轻触首尾帧｜单图外接口播版_2111330532469600258.json、视频生成/图生视频/允希V8.2闭唇正脸主体参考版｜单图外接一秒轻触_2111335218408943617.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ExtendIntermediateSigmas`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `MiniMaxH3DirectorFaceRefine`
- `MiniMaxH3DirectorGroupsCombine`
- `MiniMaxH3DirectorRefine`
- `MiniMaxH3DirectorSelfLift`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 1/2 个有
- `MiniMaxH3DirectorGroupImageToVideo` —— 1/2 个有
- `MiniMaxH3DirectorGroupReferenceToVideo` —— 1/2 个有
- `ModelPreviewOverrideKJ` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `Video Slice` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
