---
name: text_to_image_lora_sampler_clip_35
type: Text To Image
frequency: 18
level: strong
coverage: 0.897222
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/加速工作流多图参考短剧制作Minimax_H3图生视频_2088378063548669954.json, 视频生成/图生视频/动漫转真人指定人物｜H3图生视频一键生成直出_2093465253832126465.json, 视频生成/图生视频/单人加速版数字人MinimaxH3图生视频口播生成工作流_2088352533071876097.json, 视频生成/图生视频/单人加速版数字人图生视频｜MinimaxH3数字人工作流_2088319249872941058.json, 视频生成/图生视频/单图参考加参考音｜Minimax H3图生视频生成_2093782725252706305.json, 视频生成/图生视频/单图参考无参考音｜Minimax H3图生视频工作流_2094012813646852097.json, 视频生成/图生视频/单图参考无参考音｜Minimax H3图生视频直出_2093784039185543170.json, 视频生成/图生视频/参考图+参考音频｜MiniMax H3 4步生视频直出_2090936385749475330.json, 视频生成/图生视频/参考模式10步+3步｜H3 Latent Upscaler图生视频_2090888594817900545.json, 视频生成/图生视频/双图参考+1参考音｜Minimax H3批量管理系统api用_2094010898447945730.json, 视频生成/图生视频/双图参考+2参考音｜Minimax H3音画同参图生视频生成_2089444909353889793.json, 视频生成/图生视频/双图参考加参考音｜Minimax H3批量管理系统API版_2093778584715481089.json, 视频生成/图生视频/多图参考短剧制作加速工作流｜Minimax_H3图生视频_2088347597277843458.json, 视频生成/图生视频/润哥教育IP数字人H3参考生视频｜声音克隆口型自动对齐_2111277682607607809.json, 视频生成/图生视频/高动态打斗模型生成｜Minimax H3更稳更有冲击力图生视频_2096705144170835969.json, 视频生成/文生视频/H3多图参考加速工作流 单采不油腻不破音_2099563905008889858.json, 视频生成/文生视频/MiniMax H3多图参考加速工作流 单采不油腻不破音_2099185147278090242.json, 视频生成/文生视频/Minimax_H3多图参考加速版｜文图视频都能喂，出视频又快又稳_2099527126897745922.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_35

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/加速工作流多图参考短剧制作Minimax_H3图生视频_2088378063548669954.json、视频生成/图生视频/动漫转真人指定人物｜H3图生视频一键生成直出_2093465253832126465.json、视频生成/图生视频/单人加速版数字人MinimaxH3图生视频口播生成工作流_2088352533071876097.json、视频生成/图生视频/单人加速版数字人图生视频｜MinimaxH3数字人工作流_2088319249872941058.json、视频生成/图生视频/单图参考加参考音｜Minimax H3图生视频生成_2093782725252706305.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 17/18 个有
- `VHS_VideoCombine` —— 17/18 个有
- `KSamplerSelect` —— 16/18 个有
- `VAEDecodeAudio` —— 16/18 个有
- `BasicScheduler` —— 15/18 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 15/18 个有
- `PrimitiveStringMultiline` —— 15/18 个有
- `BasicGuider` —— 13/18 个有
- `LoadAudio` —— 13/18 个有
- `MiniMaxH3SigmaShift` —— 12/18 个有
- `ModelAttentionBackend` —— 8/18 个有
- `INTConstant` —— 6/18 个有
- `CFGGuider` —— 5/18 个有
- `ConditioningZeroOut` —— 5/18 个有
- `H3AudioRefineSampler` —— 3/18 个有
- `H3FrozenVideoCache` —— 3/18 个有
- `MiniMaxH3TurboSampler` —— 3/18 个有
- `ModelPreviewOverrideKJ` —— 3/18 个有
- `SolAttnPatch` —— 3/18 个有
- `CreateVideo` —— 2/18 个有
- `ManualSigmas` —— 2/18 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/18 个有
- `SaveImage` —— 2/18 个有
- `SaveVideo` —— 2/18 个有
- `TrimAudioDuration` —— 2/18 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/18 个有
- `BlockSparseAttention` —— 1/18 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 1/18 个有
- `PlaySound|pysssss` —— 1/18 个有
- `SplitSigmas` —— 1/18 个有
- `Text` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 18 | 100% |
| 采样算法 | er_sde | - | 18 | 100% |
| 调度器 | beta | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 80 | 80 - 80 | 18 | 100% |
| 高度 | 80 | 80 - 80 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高发问题（18/18 个样本）：Steps较低可能导致细节不足
