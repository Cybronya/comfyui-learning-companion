---
name: text_to_image_video_lora_sampler_116
type: Text To Image
frequency: 8
level: strong
coverage: 0.765875
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SaveImage, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3视频蒸馏复刻采样工作流拆解系列，风格迁移与动作迁移十集教程_2105121681349103617.json, 视频生成/图生视频/MiniMax H3 Singularity V2 R2VA 去油抗飘图生视频工具_2114080323918192641.json, 视频生成/图生视频/MiniMax H3 Singularity V2面部精修 高清图生视频工具_2114081864469278722.json, 视频生成/图生视频/MiniMax_H3导演Skill加双采2K直出工作流，文生视频视频生视频图生视频_2109823268537585666.json, 视频生成/图生视频/Minimax H3 Singularity V2八步加速工作流，人脸修复细节清晰_2114464058652053505.json, 视频生成/图生视频/Minimax_H3_Singularity_V2八步加速工作流，人脸修复细节清晰_2117102149187493890.json, 视频生成/文生视频/导演skill加持双采2K直出 MiniMax H3高质量视频生成_2104764024637444098.json, 视频生成/文生视频/导演skill加持双采2K直出 MiniMax H3高质量视频生成_2105437067290431490.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_116

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/H3视频蒸馏复刻采样工作流拆解系列，风格迁移与动作迁移十集教程_2105121681349103617.json、视频生成/图生视频/MiniMax H3 Singularity V2 R2VA 去油抗飘图生视频工具_2114080323918192641.json、视频生成/图生视频/MiniMax H3 Singularity V2面部精修 高清图生视频工具_2114081864469278722.json、视频生成/图生视频/MiniMax_H3导演Skill加双采2K直出工作流，文生视频视频生视频图生视频_2109823268537585666.json、视频生成/图生视频/Minimax H3 Singularity V2八步加速工作流，人脸修复细节清晰_2114464058652053505.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 8 个 workflow 都包含：
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
- `VAEDecodeAudio` —— 7/8 个有
- `MiniMaxH3SigmaShift` —— 6/8 个有
- `孤海注释` —— 5/8 个有
- `BlockSparseAttention` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `H3SigmaRefiner` —— 4/8 个有
- `ImageScaleToTotalPixels` —— 4/8 个有
- `ModelPreviewOverrideKJ` —— 4/8 个有
- `GetNode` —— 3/8 个有
- `H3FaceStitch` —— 3/8 个有
- `H3FaceTrackCrop` —— 3/8 个有
- `MiniMaxH3Unified` —— 3/8 个有
- `PreviewAny` —— 3/8 个有
- `SetNode` —— 3/8 个有
- `VOSR2ModelLoader` —— 3/8 个有
- `VOSR2Upscale` —— 3/8 个有
- `EmptyImage` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `Display Any (rgthree)` —— 1/8 个有
- `LoadAudio` —— 1/8 个有
- `MiniMaxH3AVDecodeT8` —— 1/8 个有
- `RandomNoise` —— 1/8 个有
- `Seed (rgthree)` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有
- `easy getNode` —— 1/8 个有
- `easy setNode` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
