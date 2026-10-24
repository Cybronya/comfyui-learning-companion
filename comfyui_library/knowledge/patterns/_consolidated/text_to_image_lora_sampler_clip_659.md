---
name: text_to_image_lora_sampler_clip_659
type: Text To Image
frequency: 2
level: weak
coverage: 0.887
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3Director, ModelAttentionBackend, PlaySound|pysssss, PreviewAny, SaveImage, SaveVideo, UNETLoader, VAEDecode, VAELoader, easy imageChooser, kkVideoFirstLastFrames, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/SelfLift导演台｜MiniMax H3全能工作流一键直出1080P画质_2103019595601891330.json, 视频生成/图生视频/minmax h3导演台单采直出，rh upscale竖屏出片_2110832227595673602.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_659

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/SelfLift导演台｜MiniMax H3全能工作流一键直出1080P画质_2103019595601891330.json、视频生成/图生视频/minmax h3导演台单采直出，rh upscale竖屏出片_2110832227595673602.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `ModelAttentionBackend`
- `PlaySound|pysssss`
- `PreviewAny`
- `SaveImage`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageChooser`
- `kkVideoFirstLastFrames`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 1/2 个有
- `BlockSparseAttention` —— 1/2 个有
- `ExtendIntermediateSigmas` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `LoraLoaderBypassModelOnly` —— 1/2 个有
- `MiniMaxH3DirectorFaceRefine` —— 1/2 个有
- `MiniMaxH3DirectorGroupReferenceToVideo` —— 1/2 个有
- `MiniMaxH3DirectorGroupsCombine` —— 1/2 个有
- `MiniMaxH3DirectorSelfLift` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `RH_Upscale` —— 1/2 个有

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
