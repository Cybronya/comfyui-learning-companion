---
name: text_to_image_video_lora_sampler_93
type: Text To Image
frequency: 8
level: strong
coverage: 0.70275
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3数字人对口型｜视频生视频图生视频生成_2092934748694990850.json, 视频生成/图生视频/H3质变音频驱动数字人｜全能参考升级版｜精准可控说话表演_2104819764299386881.json, 视频生成/图生视频/H3超级打戏无损工作流｜战斗特效分镜出图图生视频_2110709132494991362.json, 视频生成/图生视频/H3长视频衔接尾帧22帧锚点 视频生成连贯性优化_2109025859695890434.json, 视频生成/图生视频/H3高清快速出视频工作流，图生视频高效创作工具_2106126711132876801.json, 视频生成/图生视频/MiniMax H3角色替换｜单人指定角色+视频编辑多合一_2110716972131512322.json, 视频生成/图生视频/数字人对口型生成｜H3视频生视频图生视频直出_2092730251368558593.json, 视频生成/图生视频/最强单采V2加特林版，10步极速战斗特效出片_2111231473561989122.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_93

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/H3数字人对口型｜视频生视频图生视频生成_2092934748694990850.json、视频生成/图生视频/H3质变音频驱动数字人｜全能参考升级版｜精准可控说话表演_2104819764299386881.json、视频生成/图生视频/H3超级打戏无损工作流｜战斗特效分镜出图图生视频_2110709132494991362.json、视频生成/图生视频/H3长视频衔接尾帧22帧锚点 视频生成连贯性优化_2109025859695890434.json、视频生成/图生视频/H3高清快速出视频工作流，图生视频高效创作工具_2106126711132876801.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 7/8 个有
- `LoadAudio` —— 7/8 个有
- `ModelPreviewOverrideKJ` —— 7/8 个有
- `PrimitiveFloat` —— 6/8 个有
- `GetNode` —— 5/8 个有
- `PrimitiveStringMultiline` —— 5/8 个有
- `SetNode` —— 5/8 个有
- `VAEDecodeAudio` —— 5/8 个有
- `VHS_LoadVideo` —— 5/8 个有
- `BlockSparseAttention` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `ManualSigmas` —— 4/8 个有
- `CR Prompt Text` —— 3/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/8 个有
- `MiniMaxH3SigmaShift` —— 3/8 个有
- `SaveImage` —— 3/8 个有
- `SoundFlow_GetLength` —— 3/8 个有
- `TrimAudioDuration` —— 3/8 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 3/8 个有
- `ShowAnything|Mie` —— 2/8 个有
- `AudioCrop` —— 1/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `GetImageRangeFromBatch` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `MiniMaxChunkFeedForward` —— 1/8 个有
- `MiniMaxH3AddGuide` —— 1/8 个有
- `MiniMaxH3Unified` —— 1/8 个有
- `MiniMaxLowVRAMAttention` —— 1/8 个有
- `PreviewAudio` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
