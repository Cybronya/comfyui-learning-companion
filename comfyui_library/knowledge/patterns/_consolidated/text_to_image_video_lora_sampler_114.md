---
name: text_to_image_video_lora_sampler_114
type: Text To Image
frequency: 6
level: strong
coverage: 0.826667
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3视频蒸馏复刻采样工作流拆解系列，风格迁移与动作迁移十集教程_2105121681349103617.json, 视频生成/图生视频/MiniMax_H3导演Skill加双采2K直出工作流，文生视频视频生视频图生视频_2109823268537585666.json, 视频生成/文生视频/MiniMax H3导演Skill加双采2K直出工作流，文生视频视频生视频图生视频_2106862808569827330.json, 视频生成/文生视频/MiniMax H3导演skill加持｜双采样2K直出高质感视频_2104492093019353089.json, 视频生成/文生视频/导演skill加持双采2K直出 MiniMax H3高质量视频生成_2104764024637444098.json, 视频生成/文生视频/导演skill加持双采2K直出 MiniMax H3高质量视频生成_2105437067290431490.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_114

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/H3视频蒸馏复刻采样工作流拆解系列，风格迁移与动作迁移十集教程_2105121681349103617.json、视频生成/图生视频/MiniMax_H3导演Skill加双采2K直出工作流，文生视频视频生视频图生视频_2109823268537585666.json、视频生成/文生视频/MiniMax H3导演Skill加双采2K直出工作流，文生视频视频生视频图生视频_2106862808569827330.json、视频生成/文生视频/MiniMax H3导演skill加持｜双采样2K直出高质感视频_2104492093019353089.json、视频生成/文生视频/导演skill加持双采2K直出 MiniMax H3高质量视频生成_2104764024637444098.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3SigmaShift` —— 5/6 个有
- `MiniMaxH3Unified` —— 5/6 个有
- `SaveImage` —— 5/6 个有
- `VAEDecodeAudio` —— 5/6 个有
- `孤海注释` —— 4/6 个有
- `EmptyImage` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `Display Any (rgthree)` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `LoadAudio` —— 1/6 个有
- `MiniMaxH3AVDecodeT8` —— 1/6 个有
- `RandomNoise` —— 1/6 个有
- `Seed (rgthree)` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有
- `easy getNode` —— 1/6 个有
- `easy setNode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
