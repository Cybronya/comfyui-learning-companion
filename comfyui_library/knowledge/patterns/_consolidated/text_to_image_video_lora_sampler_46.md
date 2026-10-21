---
name: text_to_image_video_lora_sampler_46
type: Text To Image
frequency: 13
level: strong
coverage: 0.735462
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/H3单采工作流兼顾效果和速度，文生图反推提示词图生图处理方案_2107241699616575490.json, 图片生成/反推提示词/H3单采工作流｜反推提示词图生图快速上手版_2106964960260739074.json, 图片生成/图生图/MiniMax H3多参考生视频666版｜多图参考融合生成，一致性拉满_2107319483974111233.json, 图片生成/文生图/8.31最佳多参考｜MiniMax H3反推提示词生视频_2094730905653956609.json, 图片生成/文生图/H3单采工作流兼顾效果和速度，文生图反推提示词图生图处理方案_2107334378736144385.json, 图片生成/文生图/H3单采工作流兼顾效果和速度，文生图反推提示词图生图处理方案_2107445023326429185.json, 图片生成/文生图/H3官流终极版工作流，文生视频图生视频全覆盖方案_2106884457763532802.json, 图片生成/文生图/MiniMax H3多参考生视频工作流，文生图图生图多参考视频生成方案_2107562264558653442.json, 图片生成/文生图/MiniMax H3多参考生视频工作流，文生图图生图多参考视频生成方案_2107940300458119170.json, 图片生成/文生图/真人一致性｜人物一致、细节升级_2098733105417908225.json, 数字人/数字人/shuzirenzhufu数字人祝福｜口播祝福视频自动生成_2103102956919939074.json, 视频生成/文生视频/参考音视频数字人｜MiniMax H3图生视频生成_2094475690098909186.json, 视频生成/文生视频/视频参考编辑替换｜MiniMax H3三模视频工作流_2094365213192712193.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_46

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/反推提示词/H3单采工作流兼顾效果和速度，文生图反推提示词图生图处理方案_2107241699616575490.json、图片生成/反推提示词/H3单采工作流｜反推提示词图生图快速上手版_2106964960260739074.json、图片生成/图生图/MiniMax H3多参考生视频666版｜多图参考融合生成，一致性拉满_2107319483974111233.json、图片生成/文生图/8.31最佳多参考｜MiniMax H3反推提示词生视频_2094730905653956609.json、图片生成/文生图/H3单采工作流兼顾效果和速度，文生图反推提示词图生图处理方案_2107334378736144385.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 13 个 workflow 都包含：
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
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 12/13 个有
- `PrimitiveFloat` —— 10/13 个有
- `VHS_LoadVideo` —— 10/13 个有
- `孤海注释` —— 10/13 个有
- `ModelAttentionBackend` —— 9/13 个有
- `ModelPreviewOverrideKJ` —— 9/13 个有
- `LTXVConcatAVLatent` —— 8/13 个有
- `LTXVSeparateAVLatent` —— 8/13 个有
- `MinimaxH3LatentUpscaler3D` —— 8/13 个有
- `SplitSigmas` —— 8/13 个有
- `GetNode` —— 7/13 个有
- `SetNode` —— 7/13 个有
- `Text` —— 7/13 个有
- `easy float` —— 7/13 个有
- `PreviewImage` —— 6/13 个有
- `PrimitiveStringMultiline` —— 6/13 个有
- `SaveImage` —— 6/13 个有
- `BlockSparseAttention` —— 5/13 个有
- `ManualSigmas` —— 5/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/13 个有
- `H3SigmaRefiner` —— 4/13 个有
- `ApplyFaceProcessor` —— 3/13 个有
- `AudioCrop` —— 3/13 个有
- `EasyCache` —— 3/13 个有
- `FaceProcessorLoader` —— 3/13 个有
- `PathchSageAttentionKJ` —— 3/13 个有
- `PrimitiveString` —— 3/13 个有
- `SeedVR2` —— 3/13 个有
- `SeedVR2BlockSwap` —— 3/13 个有
- `SoundFlow_GetLength` —— 3/13 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 3/13 个有
- `EmptyImage` —— 2/13 个有
- `AILab_QwenVL` —— 1/13 个有
- `ImageScale` —— 1/13 个有
- `MiniMaxH3SigmaShift` —— 1/13 个有
- `ZML_MergeText` —— 1/13 个有

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
| Steps较低可能导致细节不足 | 14/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（14/13 个样本）：Steps较低可能导致细节不足
