---
name: text_to_image_video_lora_sampler_89
type: Text To Image
frequency: 10
level: strong
coverage: 0.6716
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MinimaxH3长视频生成｜高清不劣化图生视频_2095576583376556034.json, 视频生成/图生视频/TaoMate MiniMax H3加速3步采样视频生成处理工具_2101045862658043905.json, 视频生成/图生视频/minimax h3 i2v fastH3 图生视频快速生成方案_2108665137354862594.json, 视频生成/图生视频/minimax_h3_i2v_fastH3_v2_veda，图生视频极速版_2111247286016761857.json, 视频生成/图生视频/minimax_h3_rawmodel_veta注意力参考，图生视频方案_2111248740865634306.json, 视频生成/图生视频/minimax_h3_rawmodel参考生视频精品，数字人动作迁移_2111244078024323074.json, 视频生成/图生视频/minimax_h3多图快速参考生视频，文生图图生视频_2111236219102384130.json, 视频生成/图生视频/单采打戏流畅出片｜Minimax 图生视频动作拉满_2096266436170838018.json, 视频生成/图生视频/图生视频二采+1参考音｜Minimax H3批量API用_2094054081001250817.json, 视频生成/图生视频/长视频一键生成｜MinimaxH3图生视频续写_2095819929332314113.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_89

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3长视频生成｜高清不劣化图生视频_2095576583376556034.json、视频生成/图生视频/TaoMate MiniMax H3加速3步采样视频生成处理工具_2101045862658043905.json、视频生成/图生视频/minimax h3 i2v fastH3 图生视频快速生成方案_2108665137354862594.json、视频生成/图生视频/minimax_h3_i2v_fastH3_v2_veda，图生视频极速版_2111247286016761857.json、视频生成/图生视频/minimax_h3_rawmodel_veta注意力参考，图生视频方案_2111248740865634306.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 10 个 workflow 都包含：
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
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 9/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/10 个有
- `MiniMaxH3ReferenceToVideo` —— 8/10 个有
- `ResolutionSelector` —— 7/10 个有
- `BlockSparseAttention` —— 6/10 个有
- `MiniMaxH3SigmaShift` —— 6/10 个有
- `SaveImage` —— 6/10 个有
- `H3SigmaRefiner` —— 4/10 个有
- `PrimitiveInt` —— 4/10 个有
- `VedaSparseAttention` —— 4/10 个有
- `LayerColor: Brightness & Contrast` —— 3/10 个有
- `LayerUtility: PurgeVRAM V2` —— 3/10 个有
- `SolAttnPatch` —— 3/10 个有
- `TrimAudioDuration` —— 3/10 个有
- `FrameInterpolate` —— 2/10 个有
- `FrameInterpolationModelLoader` —— 2/10 个有
- `ImageFromBatch` —— 2/10 个有
- `MiniMaxH3AddGuide` —— 2/10 个有
- `MiniMaxH3ImageToVideo` —— 2/10 个有
- `ModelAttentionBackend` —— 2/10 个有
- `QwenH3PromptLocal` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `GetImageRangeFromBatch` —— 1/10 个有
- `LTXVSeparateAVLatent` —— 1/10 个有
- `LoadAudio` —— 1/10 个有
- `MiniMaxLowVRAMAttention` —— 1/10 个有
- `MinimaxH3LatentUpscaler3D` —— 1/10 个有
- `PT_H3ConcatAVLatent` —— 1/10 个有
- `RTXVideoSuperResolution` —— 1/10 个有
- `SplitSigmas` —— 1/10 个有

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
