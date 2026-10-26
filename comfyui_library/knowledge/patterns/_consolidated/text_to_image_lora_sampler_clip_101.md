---
name: text_to_image_lora_sampler_clip_101
type: Text To Image
frequency: 13
level: strong
coverage: 0.797462
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MiniMax H3终极篇文武双全｜战斗特效打斗场面一步到位_2111056774492147714.json, 图片生成/图生图/MiniMax H3终极篇，文武双全战斗特效_2111257793977217026.json, 图片生成/图生图/Minimax h3高一致性工作流｜多镜头音频参考视频生成_2097838671696318466.json, 图片生成/文生图/H3fast-v2全参加速方案，文生图图生图双模快跑_2111585524942204929.json, 图片生成/文生图/H3单采工作流兼顾效果和速度，文生图反推提示词图生图处理方案_2107334378736144385.json, 图片生成/文生图/H3单采工作流兼顾效果和速度，文生图反推提示词图生图处理方案_2107445023326429185.json, 图片生成/文生图/H3官流终极版工作流，文生视频图生视频全覆盖方案_2106884457763532802.json, 数字人/数字人/HaoAGI1016 MiniMaxH3文武线程｜数字人文戏武戏双路并跑_2112929068525121537.json, 数字人/数字人/MiniMax H3多模态数字人 图生视频多模态处理生成工具_2113063208369082370.json, 视频生成/图生视频/H3 SelfLift参考生视频，双采单采加速任选模式_2110850789378977793.json, 视频生成/图生视频/MiniMax H3 SelfLift加速双采加单采参考生视频 视频生成加速_2109348613032861697.json, 视频生成/图生视频/MiniMax H3 SelfLift加速双采单采，参考生视频提速版_2110810539428499457.json, 视频生成/文生视频/H3双采参考视频生成 文生视频图生视频多模态_2098274586579263490.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_101

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/MiniMax H3终极篇文武双全｜战斗特效打斗场面一步到位_2111056774492147714.json、图片生成/图生图/MiniMax H3终极篇，文武双全战斗特效_2111257793977217026.json、图片生成/图生图/Minimax h3高一致性工作流｜多镜头音频参考视频生成_2097838671696318466.json、图片生成/文生图/H3fast-v2全参加速方案，文生图图生图双模快跑_2111585524942204929.json、图片生成/文生图/H3单采工作流兼顾效果和速度，文生图反推提示词图生图处理方案_2107334378736144385.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicScheduler`
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
- `PrimitiveFloat`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ModelPreviewOverrideKJ` —— 11/13 个有
- `SaveImage` —— 11/13 个有
- `VHS_LoadVideo` —— 11/13 个有
- `孤海注释` —— 11/13 个有
- `BlockSparseAttention` —— 10/13 个有
- `LoadAudio` —— 10/13 个有
- `BasicGuider` —— 9/13 个有
- `RandomNoise` —— 9/13 个有
- `SamplerCustomAdvanced` —— 9/13 个有
- `ConditioningZeroOut` —— 8/13 个有
- `SelfLiftH3Sampler` —— 8/13 个有
- `PrimitiveStringMultiline` —— 7/13 个有
- `VHS_VideoCombine` —— 7/13 个有
- `SaveVideo` —— 6/13 个有
- `CreateVideo` —— 5/13 个有
- `GetNode` —— 5/13 个有
- `MiniMaxChunkFeedForward` —— 5/13 个有
- `MiniMaxH3SigmaShift` —— 5/13 个有
- `SetNode` —— 5/13 个有
- `Any Switch (rgthree)` —— 4/13 个有
- `ExtendIntermediateSigmas` —— 4/13 个有
- `Fast Groups Muter (rgthree)` —— 4/13 个有
- `GoohaiUniversalSlider` —— 4/13 个有
- `ManualSigmas` —— 4/13 个有
- `MiniMaxLowVRAMAttention` —— 4/13 个有
- `Text` —— 4/13 个有
- `EmptyImage` —— 2/13 个有
- `ImageScale` —— 2/13 个有
- `PreviewImage` —— 2/13 个有
- `easy showAnything` —— 2/13 个有
- `LoraLoaderBypassModelOnly` —— 1/13 个有
- `MiniMaxH3AddGuide` —— 1/13 个有
- `PainterVRAM` —— 1/13 个有
- `VideoCombineV2` —— 1/13 个有
- `easy positive` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
