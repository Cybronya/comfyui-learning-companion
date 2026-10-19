---
name: text_to_image_lora_sampler_clip_61
type: Text To Image
frequency: 13
level: strong
coverage: 0.886231
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3Director, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3视频生成 导演台 10.9 优化乱说对白方案_2100106257972678658.json, 视频生成/图生视频/MiniMax H3视频生成导演台10.9优化乱说对白方案 数字人口播优化_2109031622308880385.json, 视频生成/图生视频/MiniMax导演台全能工作流-图生视频工作流_2087382195718676481.json, 视频生成/图生视频/MinimaxH3导演台优化二采 图生视频增强方案_2110355752249548801.json, 视频生成/图生视频/fl2v图生视频｜MiniMax H3导演台全能工作流_2092914595471126529.json, 视频生成/图生视频/fl2v导演台全能｜MiniMax H3人物类特效图生视频_2092576351906787329.json, 视频生成/图生视频/fl2v导演台全能｜MiniMax H3图生视频生成_2091763159051890689.json, 视频生成/图生视频/fl2v导演台全能｜MiniMax H3图生视频生成_2092064759645564929.json, 视频生成/图生视频/ref2va全能参考｜MiniMax H3导演台全能工作流_2092704060947386370.json, 视频生成/图生视频/ref2va全能参考｜MiniMax H3导演台图生视频生视频_2092892930460708865.json, 视频生成/图生视频/ref2va全能参考｜MiniMax H3导演台工作流_2091198014990934017.json, 视频生成/图生视频/允希V8.2闭唇正脸一秒轻触首尾帧｜单图外接口播版_2111330532469600258.json, 视频生成/图生视频/允希V8.2闭唇正脸主体参考版｜单图外接一秒轻触_2111335218408943617.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_61

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3视频生成 导演台 10.9 优化乱说对白方案_2100106257972678658.json、视频生成/图生视频/MiniMax H3视频生成导演台10.9优化乱说对白方案 数字人口播优化_2109031622308880385.json、视频生成/图生视频/MiniMax导演台全能工作流-图生视频工作流_2087382195718676481.json、视频生成/图生视频/MinimaxH3导演台优化二采 图生视频增强方案_2110355752249548801.json、视频生成/图生视频/fl2v图生视频｜MiniMax H3导演台全能工作流_2092914595471126529.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 12/13 个有
- `VHS_VideoCombine` —— 11/13 个有
- `MiniMaxH3DirectorRefine` —— 10/13 个有
- `PreviewAny` —— 10/13 个有
- `UpscaleModelLoader` —— 9/13 个有
- `PathchSageAttentionKJ` —— 5/13 个有
- `LoadImage` —— 4/13 个有
- `BasicScheduler` —— 3/13 个有
- `CreateVideo` —— 3/13 个有
- `SaveImage` —— 3/13 个有
- `SaveVideo` —— 3/13 个有
- `BlockSparseAttention` —— 2/13 个有
- `ExtendIntermediateSigmas` —— 2/13 个有
- `MiniMaxH3DirectorFaceRefine` —— 2/13 个有
- `MiniMaxH3DirectorGroupsCombine` —— 2/13 个有
- `MiniMaxH3DirectorSelfLift` —— 2/13 个有
- `MiniMaxH3SigmaShift` —— 2/13 个有
- `ModelAttentionBackend` —— 2/13 个有
- `PrimitiveStringMultiline` —— 2/13 个有
- `MiniMaxH3DirectorGroupImageToVideo` —— 1/13 个有
- `MiniMaxH3DirectorGroupReferenceToVideo` —— 1/13 个有
- `ModelPreviewOverrideKJ` —— 1/13 个有
- `Video Slice` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（15/13 个样本）：Steps较低可能导致细节不足
