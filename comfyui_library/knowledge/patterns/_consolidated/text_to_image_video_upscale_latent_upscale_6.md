---
name: text_to_image_video_upscale_latent_upscale_6
type: Text To Image
frequency: 11
level: strong
coverage: 0.916455
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyModelAdapter, MiniMaxH3EasyOutput, MiniMaxH3EasySecondPassConditioning, MinimaxH3LatentUpscaler3D, RandomNoise, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/高质量数字人MiniMax H3工作流，数字人生成处理方案_2106903069106720770.json, 视频生成/图生视频/H3 Easy工作台双采样｜提示词增强图生视频生成_2097078423951859713.json, 视频生成/图生视频/H3 最强去油双采样｜提示词全自动优化一步到位｜图生视频_2096829872772575233.json, 视频生成/图生视频/MINIMAX-H3去油精简流独立双采样｜角色一致性_2095589274757451777.json, 视频生成/图生视频/MINIMAX-H3开源最强去油全模式精简流｜双采样_2095579769827057666.json, 视频生成/图生视频/Mnimaxh3极简流分块二采｜支持种子固定可复现｜图生视频稳定输出_2104772144688361474.json, 视频生成/图生视频/minimaxh3高质量数字人_口播视频生成省时省力_2106603151494303745.json, 视频生成/图生视频/最强去油双采样工作流｜H3提示词全自动优化图生视频_2096682501061300226.json, 视频生成/图生视频/高质量数字人MiniMax_H3工作流，数字人生成处理方案_2108732703087616001.json, 视频生成/图生视频/高质量数字人minimax h3 数字人视频生成方案_2105028607759446018.json, 视频生成/文生视频/Mnimaxh3极简流分块二采｜种子固定方便复刻同款_2103076631169556482.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_6

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（数字人/数字人/高质量数字人MiniMax H3工作流，数字人生成处理方案_2106903069106720770.json、视频生成/图生视频/H3 Easy工作台双采样｜提示词增强图生视频生成_2097078423951859713.json、视频生成/图生视频/H3 最强去油双采样｜提示词全自动优化一步到位｜图生视频_2096829872772575233.json、视频生成/图生视频/MINIMAX-H3去油精简流独立双采样｜角色一致性_2095589274757451777.json、视频生成/图生视频/MINIMAX-H3开源最强去油全模式精简流｜双采样_2095579769827057666.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyModelAdapter`
- `MiniMaxH3EasyOutput`
- `MiniMaxH3EasySecondPassConditioning`
- `MinimaxH3LatentUpscaler3D`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 10/11 个有
- `LoadImage` —— 8/11 个有
- `VAEDecodeAudio` —— 7/11 个有
- `GoohaiMinimaxH3TiledSampler` —— 6/11 个有
- `ModelAttentionBackend` —— 6/11 个有
- `Seed (rgthree)` —— 6/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/11 个有
- `LTXVAudioVAEEncode` —— 4/11 个有
- `SaveImage` —— 4/11 个有
- `SetLatentNoiseMask` —— 4/11 个有
- `SolidMask` —— 4/11 个有
- `TrimAudioDuration` —— 4/11 个有
- `VHS_LoadVideo` —— 4/11 个有
- `CR Prompt Text` —— 3/11 个有
- `Int` —— 3/11 个有
- `MiniMaxH3PromptEnhancerT8` —— 3/11 个有
- `PreviewAny` —— 3/11 个有
- `RH_Translator` —— 3/11 个有
- `easy saveText` —— 3/11 个有
- `easy showAnything` —— 3/11 个有
- `EmptyImage` —— 1/11 个有
- `MiniMaxH3EasyMediaLoader` —— 1/11 个有
- `PreviewImage` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
