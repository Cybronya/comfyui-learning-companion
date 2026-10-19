---
name: text_to_image_lora_sampler_clip_45
type: Text To Image
frequency: 15
level: strong
coverage: 0.720267
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/H3单采工作流兼顾效果和速度，文生图反推提示词图生图处理方案_2107241699616575490.json, 图片生成/反推提示词/H3单采工作流｜反推提示词图生图快速上手版_2106964960260739074.json, 图片生成/图生图/MiniMax H3多参考生视频666版｜多图参考融合生成，一致性拉满_2107319483974111233.json, 图片生成/文生图/H3单采工作流兼顾效果和速度，文生图反推提示词图生图处理方案_2107334378736144385.json, 图片生成/文生图/H3单采工作流兼顾效果和速度，文生图反推提示词图生图处理方案_2107445023326429185.json, 图片生成/文生图/H3官流终极版工作流，文生视频图生视频全覆盖方案_2106884457763532802.json, 数字人/数字人/Minimax H3多参考口播｜数字人口播素材多路喂｜口型和画面都对得上_2102653513489805313.json, 数字人/数字人/优化版本新版口播方案，数字人视频生视频制作_2111284544136630274.json, 数字人/数字人/新版口播数字人视频生成工作流｜视频生视频一键出片_2108369479599218690.json, 数字人/数字人/老王房产专用流｜Minimax+H3双模双采数字人_2097974073354702849.json, 视频生成/图生视频/2采五段加速流 视频生成加速方案高效出片_2104985692295229442.json, 视频生成/图生视频/H3参考生视频提示词优化二阶高清处理工具_2100427862649171970.json, 视频生成/图生视频/H3视频衔接工作流｜多段视频无缝拼接生成_2095211983237894146.json, 视频生成/图生视频/MiniMax H3多参考生视频无限流五段二采串联处理工具_2102166646034100225.json, 视频生成/图生视频/五段式加速二采工作流｜角色表演视频一次成型｜图生视频高效出片_2104743299977400322.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_45

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/反推提示词/H3单采工作流兼顾效果和速度，文生图反推提示词图生图处理方案_2107241699616575490.json、图片生成/反推提示词/H3单采工作流｜反推提示词图生图快速上手版_2106964960260739074.json、图片生成/图生图/MiniMax H3多参考生视频666版｜多图参考融合生成，一致性拉满_2107319483974111233.json、图片生成/文生图/H3单采工作流兼顾效果和速度，文生图反推提示词图生图处理方案_2107334378736144385.json、图片生成/文生图/H3单采工作流兼顾效果和速度，文生图反推提示词图生图处理方案_2107445023326429185.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
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
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 13/15 个有
- `VHS_VideoCombine` —— 13/15 个有
- `ModelAttentionBackend` —— 12/15 个有
- `VHS_LoadVideo` —— 12/15 个有
- `孤海注释` —— 12/15 个有
- `GetNode` —— 9/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/15 个有
- `SetNode` —— 9/15 个有
- `ModelPreviewOverrideKJ` —— 8/15 个有
- `PrimitiveStringMultiline` —— 8/15 个有
- `SaveImage` —— 8/15 个有
- `BlockSparseAttention` —— 7/15 个有
- `LTXVConcatAVLatent` —— 7/15 个有
- `LTXVSeparateAVLatent` —— 7/15 个有
- `MiniMaxH3AddGuide` —— 7/15 个有
- `MinimaxH3LatentUpscaler3D` —— 7/15 个有
- `SplitSigmas` —— 7/15 个有
- `Text` —— 7/15 个有
- `ManualSigmas` —— 6/15 个有
- `MiniMaxH3SigmaShift` —— 5/15 个有
- `GetImageRangeFromBatch` —— 4/15 个有
- `PreviewImage` —— 4/15 个有
- `easy float` —— 4/15 个有
- `AudioConcat` —— 3/15 个有
- `CreateVideo` —— 3/15 个有
- `EmptyImage` —— 3/15 个有
- `ImageBatchMulti` —— 3/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/15 个有
- `MiniMaxLowVRAMAttention` —— 3/15 个有
- `SaveAudio` —— 3/15 个有
- `SaveVideo` —— 3/15 个有
- `TrimAudioDuration` —— 3/15 个有
- `Fast Groups Bypasser (rgthree)` —— 2/15 个有
- `H3SigmaRefiner` —— 2/15 个有
- `MiniMaxChunkFeedForward` —— 2/15 个有
- `PrimitiveInt` —— 2/15 个有
- `ComfySwitchNode` —— 1/15 个有
- `FL_UnloadAllModels` —— 1/15 个有
- `LayerColor: ColorAdapter` —— 1/15 个有
- `PathchSageAttentionKJ` —— 1/15 个有
- `PrimitiveBoolean` —— 1/15 个有
- `SpectrumApplyMiniMaxH3` —— 1/15 个有
- `easy cleanGpuUsed` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
