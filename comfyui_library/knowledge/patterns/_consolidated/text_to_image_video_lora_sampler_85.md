---
name: text_to_image_video_lora_sampler_85
type: Text To Image
frequency: 10
level: strong
coverage: 0.6989
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/MiniMax H3数字人与MV视频制作工作流，虚拟形象演唱表演一键生成_2114421903237668865.json, 数字人/数字人/MinimaxH3数字人&MV工作流｜数字人唱歌表演一站搞定_2114251983816314882.json, 数字人/数字人/全行业广告制作加音频驱动加提示词生成器辅助扩写，数字人电商产品方案_2107226505611923457.json, 数字人/数字人/全行业广告制作助手｜音频驱动加提示词生成器辅助扩写_2106927316462039041.json, 视频生成/图生视频/Minimax H3参考生视频+高动态｜图生视频生成_2095268329618497537.json, 视频生成/图生视频/Minimax H3参考生视频自用版｜高动态可出20s长片_2107687775708475394.json, 视频生成/图生视频/Minimax H3参考生视频高动态自用版可生成20秒以上视频工作流，图生视频方案_2107905533574471681.json, 视频生成/图生视频/二采首尾帧+参考音｜Minimax H3图生视频生成_2092586326188191745.json, 视频生成/图生视频/二采首尾帧参考音｜Minimax H3图生视频直出_2092337325798940674.json, 视频生成/图生视频/全行业广告制作助手｜音频驱动加提示词生成器辅助扩写_2107981763464220673.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_85

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（数字人/数字人/MiniMax H3数字人与MV视频制作工作流，虚拟形象演唱表演一键生成_2114421903237668865.json、数字人/数字人/MinimaxH3数字人&MV工作流｜数字人唱歌表演一站搞定_2114251983816314882.json、数字人/数字人/全行业广告制作加音频驱动加提示词生成器辅助扩写，数字人电商产品方案_2107226505611923457.json、数字人/数字人/全行业广告制作助手｜音频驱动加提示词生成器辅助扩写_2106927316462039041.json、视频生成/图生视频/Minimax H3参考生视频+高动态｜图生视频生成_2095268329618497537.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 9/10 个有
- `孤海注释` —— 9/10 个有
- `H3SigmaRefiner` —— 7/10 个有
- `LayerUtility: PurgeVRAM V2` —— 7/10 个有
- `MiniMaxH3SigmaShift` —— 7/10 个有
- `MinimaxH3LatentUpscaler3D` —— 7/10 个有
- `PT_H3ConcatAVLatent` —— 7/10 个有
- `PrimitiveFloat` —— 7/10 个有
- `PrimitiveInt` —— 7/10 个有
- `PrimitiveStringMultiline` —— 7/10 个有
- `ResolutionSelector` —— 7/10 个有
- `VAEDecodeAudio` —— 7/10 个有
- `easy showAnything` —— 6/10 个有
- `LTXVAudioVAEEncode` —— 5/10 个有
- `LTXVConcatAVLatent` —— 5/10 个有
- `MiniMaxLowVRAMAttention` —— 5/10 个有
- `SetLatentNoiseMask` —— 5/10 个有
- `SolidMask` —— 5/10 个有
- `SoundFlow_GetLength` —— 5/10 个有
- `BlockSparseAttention` —— 4/10 个有
- `Fast Groups Bypasser (rgthree)` —— 4/10 个有
- `CR Text` —— 3/10 个有
- `INTConstant` —— 3/10 个有
- `LayerColor: Brightness & Contrast` —— 3/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/10 个有
- `MultiTextConcatenate` —— 3/10 个有
- `MuyeTextEditOutput` —— 3/10 个有
- `RHLLMChatNode` —— 3/10 个有
- `SaveImage` —— 3/10 个有
- `Any Switch (rgthree)` —— 2/10 个有
- `MiniMaxChunkFeedForward` —— 2/10 个有
- `SplitSigmas` —— 2/10 个有
- `EmptyImage` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `SolAttnPatch` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
