---
name: text_to_image_lora_sampler_clip_123
type: Text To Image
frequency: 13
level: strong
coverage: 0.774154
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/开源版数字人 MiniMax-H3 视频文案一体全节点注释_2094256504005292034.json, 视频生成/图生视频/我自用的H3-w1_2094228023120846849.json, 视频生成/图生视频/战斗场面动态拉满｜Minimax H3最佳战斗版二代_2096534069990486018.json, 视频生成/图生视频/最佳动态战斗版V2｜Minimax H3图生视频高质量生成_2096318583386230785.json, 视频生成/图生视频/海螺MiniMax-H3开源版图片开口说话数字人-图像音频参考图生视频_2087385959053742082.json, 视频生成/图生视频/自然去油不磨皮｜MiniMax H3强化二采放大_2096579288177926145.json, 视频生成/文生视频/FL2VA首尾帧文生全能｜MiniMax H3视频生成工作流_2093069819640901634.json, 视频生成/文生视频/MiniMax H3 FL2VA文生首尾帧全能视频｜文生视频视频生视频图生视频_2090423722896347138.json, 视频生成/文生视频/MiniMax-H3 极限复杂大动态｜16G显存人脸去油腻方案_2096876860767563778.json, 视频生成/文生视频/MiniMax-H3疯狂测试工作流｜文生视频视频生视频_2095216174060630017.json, 视频生成/文生视频/疯狂测试全通过｜MiniMax H3三模输入全能出片_2096527562737541121.json, 视频生成/文生视频/疯狂测试工作流｜Aiden MiniMax-H3文生视频视频生视频_2095553065045807106.json, 视频生成/文生视频/疯狂测试工作流｜MiniMax H3文生视频图生视频多模式_2096295220886466562.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_123

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/开源版数字人 MiniMax-H3 视频文案一体全节点注释_2094256504005292034.json、视频生成/图生视频/我自用的H3-w1_2094228023120846849.json、视频生成/图生视频/战斗场面动态拉满｜Minimax H3最佳战斗版二代_2096534069990486018.json、视频生成/图生视频/最佳动态战斗版V2｜Minimax H3图生视频高质量生成_2096318583386230785.json、视频生成/图生视频/海螺MiniMax-H3开源版图片开口说话数字人-图像音频参考图生视频_2087385959053742082.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
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
- `BasicScheduler` —— 12/13 个有
- `LoadImage` —— 12/13 个有
- `孤海注释` —— 12/13 个有
- `CreateVideo` —— 11/13 个有
- `MiniMaxH3ReferenceToVideo` —— 11/13 个有
- `SaveVideo` —— 11/13 个有
- `ModelPreviewOverrideKJ` —— 10/13 个有
- `LTXVConcatAVLatent` —— 9/13 个有
- `LTXVSeparateAVLatent` —— 9/13 个有
- `MiniMaxH3SigmaShift` —— 8/13 个有
- `MinimaxH3LatentUpscaler3D` —— 8/13 个有
- `ModelAttentionBackend` —— 8/13 个有
- `PrimitiveStringMultiline` —— 8/13 个有
- `AudioCrop` —— 6/13 个有
- `GetNode` —— 6/13 个有
- `SetNode` —— 6/13 个有
- `SplitSigmas` —— 6/13 个有
- `ComfySwitchNode` —— 5/13 个有
- `LoadAudio` —— 5/13 个有
- `MiniMaxChunkFeedForward` —— 5/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/13 个有
- `VHS_LoadVideo` —— 5/13 个有
- `MiniMaxLowVRAMAttention` —— 4/13 个有
- `easy boolean` —— 4/13 个有
- `easy positive` —— 4/13 个有
- `忽略多组孤海` —— 4/13 个有
- `DisableNoise` —— 3/13 个有
- `ExtendIntermediateSigmas` —— 3/13 个有
- `H3SigmaRefiner` —— 3/13 个有
- `ManualSigmas` —— 3/13 个有
- `SplitSigmasDenoise` —— 3/13 个有
- `H3AudioRefineSampler` —— 2/13 个有
- `H3FrozenVideoCache` —— 2/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/13 个有
- `MiniMaxH3ImageToVideo` —— 2/13 个有
- `Seed (rgthree)` —— 2/13 个有
- `VHS_VideoCombine` —— 2/13 个有
- `AILab_QwenVL` —— 1/13 个有
- `CR Text` —— 1/13 个有
- `ConditioningZeroOut` —— 1/13 个有
- `JoinStrings` —— 1/13 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/13 个有
- `UniBlockSwap` —— 1/13 个有
- `VRAM_Debug` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有
- `布尔孤海` —— 1/13 个有

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
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
