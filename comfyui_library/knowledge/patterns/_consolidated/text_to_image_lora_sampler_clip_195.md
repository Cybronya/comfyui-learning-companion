---
name: text_to_image_lora_sampler_clip_195
type: Text To Image
frequency: 10
level: strong
coverage: 0.8364
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/fl2v_turbo加速｜MiniMax-H3图生视频文生视频提速_2089412676161204225.json, 视频生成/文生视频/h3文生_首尾帧视频_2087479552833576961.json, 视频生成/文生视频/lightx2v文生图生首尾帧加速-minimax_h3工作流_2087348521795153921.json, 视频生成/文生视频/minmaxH3单采加速｜文生视频图生视频 极速出片小钢炮_2105529286273880065.json, 视频生成/文生视频/一键工作流战斗特效｜文生视频图生视频工作流_2088376043441844226.json, 视频生成/文生视频/两步生成768P视频｜Minimax H3 多参数加速LoRA_2096256232272257025.json, 视频生成/文生视频/多参数视频生成768p｜Minimax H3加速LoRA两步_2095964673219846146.json, 视频生成/文生视频/文生+首尾帧全能｜MiniMax H3 FL2VA视频生成_2093227972433104897.json, 视频生成/文生视频/极速版二采潜空间直接放大 minimaxh3 去油画质提升_2094233661909585921.json, 视频生成/文生视频/高清人脸｜海螺H3 sigma强化潜空间放大视频生成_2089812873718624257.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_195

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/fl2v_turbo加速｜MiniMax-H3图生视频文生视频提速_2089412676161204225.json、视频生成/文生视频/h3文生_首尾帧视频_2087479552833576961.json、视频生成/文生视频/lightx2v文生图生首尾帧加速-minimax_h3工作流_2087348521795153921.json、视频生成/文生视频/minmaxH3单采加速｜文生视频图生视频 极速出片小钢炮_2105529286273880065.json、视频生成/文生视频/一键工作流战斗特效｜文生视频图生视频工作流_2088376043441844226.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 9/10 个有
- `PrimitiveFloat` —— 9/10 个有
- `ResolutionSelector` —— 9/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/10 个有
- `MiniMaxH3SigmaShift` —— 6/10 个有
- `PrimitiveStringMultiline` —— 6/10 个有
- `LTXVConcatAVLatent` —— 5/10 个有
- `LTXVSeparateAVLatent` —— 5/10 个有
- `MiniMaxH3ImageToVideo` —— 5/10 个有
- `MiniMaxH3ReferenceToVideo` —— 5/10 个有
- `ModelAttentionBackend` —— 5/10 个有
- `ModelPreviewOverrideKJ` —— 5/10 个有
- `MinimaxH3LatentUpscaler3D` —— 4/10 个有
- `H3SigmaRefiner` —— 3/10 个有
- `SplitSigmas` —— 3/10 个有
- `GetNode` —— 2/10 个有
- `GetVideoComponents` —— 2/10 个有
- `LoadVideo` —— 2/10 个有
- `PathchSageAttentionKJ` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `ExtendIntermediateSigmas` —— 1/10 个有
- `LoadAudio` —— 1/10 个有
- `MiniMaxH3TurboLoRA` —— 1/10 个有
- `MiniMaxH3TurboSampler` —— 1/10 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/10 个有
- `PixaromaDuration` —— 1/10 个有
- `PixaromaSizes` —— 1/10 个有
- `SolAttnMiniMax` —— 1/10 个有
- `忽略多组孤海` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
