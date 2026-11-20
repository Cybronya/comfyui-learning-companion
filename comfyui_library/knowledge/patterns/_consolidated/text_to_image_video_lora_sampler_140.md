---
name: text_to_image_video_lora_sampler_140
type: Text To Image
frequency: 5
level: strong
coverage: 0.6958
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SaveImage, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3视频蒸馏复刻采样工作流拆解系列，风格迁移与动作迁移十集教程_2105121681349103617.json, 视频生成/图生视频/MiniMax H3 Singularity V2 R2VA 去油抗飘图生视频工具_2114080323918192641.json, 视频生成/图生视频/MiniMax H3 Singularity V2面部精修 高清图生视频工具_2114081864469278722.json, 视频生成/图生视频/MiniMax_H3导演Skill加双采2K直出工作流，文生视频视频生视频图生视频_2109823268537585666.json, 视频生成/图生视频/Minimax H3 Singularity V2八步加速工作流，人脸修复细节清晰_2114464058652053505.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_140

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/H3视频蒸馏复刻采样工作流拆解系列，风格迁移与动作迁移十集教程_2105121681349103617.json、视频生成/图生视频/MiniMax H3 Singularity V2 R2VA 去油抗飘图生视频工具_2114080323918192641.json、视频生成/图生视频/MiniMax H3 Singularity V2面部精修 高清图生视频工具_2114081864469278722.json、视频生成/图生视频/MiniMax_H3导演Skill加双采2K直出工作流，文生视频视频生视频图生视频_2109823268537585666.json、视频生成/图生视频/Minimax H3 Singularity V2八步加速工作流，人脸修复细节清晰_2114464058652053505.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `VAEDecodeAudio` —— 4/5 个有
- `BlockSparseAttention` —— 3/5 个有
- `GetNode` —— 3/5 个有
- `ImageScaleToTotalPixels` —— 3/5 个有
- `MiniMaxH3SigmaShift` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `孤海注释` —— 3/5 个有
- `EmptyImage` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `H3FaceStitch` —— 2/5 个有
- `H3FaceTrackCrop` —— 2/5 个有
- `H3SigmaRefiner` —— 2/5 个有
- `ModelPreviewOverrideKJ` —— 2/5 个有
- `PreviewAny` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `VOSR2ModelLoader` —— 2/5 个有
- `VOSR2Upscale` —— 2/5 个有
- `Display Any (rgthree)` —— 1/5 个有
- `LoadAudio` —— 1/5 个有
- `MiniMaxH3AVDecodeT8` —— 1/5 个有
- `MiniMaxH3Unified` —— 1/5 个有
- `RandomNoise` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有
- `easy getNode` —— 1/5 个有
- `easy setNode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
