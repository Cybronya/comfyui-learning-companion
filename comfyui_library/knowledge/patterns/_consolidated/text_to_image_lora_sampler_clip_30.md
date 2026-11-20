---
name: text_to_image_lora_sampler_clip_30
type: Text To Image
frequency: 23
level: strong
coverage: 0.78713
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/加速工作流多图参考短剧制作Minimax_H3图生视频_2088378063548669954.json, 视频生成/图生视频/动漫转真人指定人物｜H3图生视频一键生成直出_2093465253832126465.json, 视频生成/图生视频/单人加速版数字人MinimaxH3图生视频口播生成工作流_2088352533071876097.json, 视频生成/图生视频/单人加速版数字人图生视频｜MinimaxH3数字人工作流_2088319249872941058.json, 视频生成/图生视频/单图参考加参考音｜Minimax H3图生视频生成_2093782725252706305.json, 视频生成/图生视频/单图参考无参考音｜Minimax H3图生视频工作流_2094012813646852097.json, 视频生成/图生视频/单图参考无参考音｜Minimax H3图生视频直出_2093784039185543170.json, 视频生成/图生视频/参考图+参考音频｜MiniMax H3 4步生视频直出_2090936385749475330.json, 视频生成/图生视频/参考模式10步+3步｜H3 Latent Upscaler图生视频_2090888594817900545.json, 视频生成/图生视频/双图参考+1参考音｜Minimax H3批量管理系统api用_2094010898447945730.json, 视频生成/图生视频/双图参考+2参考音｜Minimax H3音画同参图生视频生成_2089444909353889793.json, 视频生成/图生视频/双图参考加参考音｜Minimax H3批量管理系统API版_2093778584715481089.json, 视频生成/图生视频/双图参考无音频｜Minimax H3图生视频一致性生成_2089443599820873730.json, 视频生成/图生视频/多参图生视频双采Latent放大｜Minimax-H3一键直出_2091672749377941505.json, 视频生成/图生视频/多参考图生视频｜MiniMax H3一键生成直出_2091663599461814274.json, 视频生成/图生视频/完美解决脸部崩坏｜MiniMax H3电影级人物特效图生视频_2090145072644976641.json, 视频生成/图生视频/小脸不崩动态不糊人物不油｜H3开源双模双采短剧漫剧图生视频_2092028224422371330.json, 视频生成/图生视频/小脸不崩漫剧必备｜Minimax H3双采样sigma强化图生视频_2090216685751066626.json, 视频生成/图生视频/强化二采放大工作流｜MiniMax H3自然去油画质提升_2096318365974491138.json, 视频生成/图生视频/海螺智能提示词双采样｜minimaxH3加速高清放大图生视频_2093734526240518145.json, 视频生成/文生视频/MINImax-H3单人音乐MV制作｜文生视频音乐生成_2094927265846091778.json, 视频生成/文生视频/单人音乐MV制作｜MINImax-H3三模视频生成工作流_2095106732040220673.json, 视频生成/文生视频/混合模型sigma强化潜空间放大｜minimaxH3高清直出不油腻_2091282726027616257.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_30

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/加速工作流多图参考短剧制作Minimax_H3图生视频_2088378063548669954.json、视频生成/图生视频/动漫转真人指定人物｜H3图生视频一键生成直出_2093465253832126465.json、视频生成/图生视频/单人加速版数字人MinimaxH3图生视频口播生成工作流_2088352533071876097.json、视频生成/图生视频/单人加速版数字人图生视频｜MinimaxH3数字人工作流_2088319249872941058.json、视频生成/图生视频/单图参考加参考音｜Minimax H3图生视频生成_2093782725252706305.json…）

- **类型**：Text To Image
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 23 个 workflow 都包含：
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
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 22/23 个有
- `BasicScheduler` —— 22/23 个有
- `KSamplerSelect` —— 22/23 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 20/23 个有
- `PrimitiveStringMultiline` —— 19/23 个有
- `VAEDecodeAudio` —— 19/23 个有
- `MiniMaxH3SigmaShift` —— 17/23 个有
- `ModelAttentionBackend` —— 13/23 个有
- `VHS_VideoCombine` —— 13/23 个有
- `CreateVideo` —— 11/23 个有
- `ModelPreviewOverrideKJ` —— 11/23 个有
- `SaveVideo` —— 11/23 个有
- `SplitSigmas` —— 11/23 个有
- `INTConstant` —— 10/23 个有
- `LTXVConcatAVLatent` —— 10/23 个有
- `LTXVSeparateAVLatent` —— 10/23 个有
- `LoadAudio` —— 10/23 个有
- `GetNode` —— 9/23 个有
- `H3SigmaRefiner` —— 9/23 个有
- `SetNode` —— 9/23 个有
- `MinimaxH3LatentUpscaler3D` —— 8/23 个有
- `SolAttnMiniMax` —— 7/23 个有
- `Fast Groups Bypasser (rgthree)` —— 4/23 个有
- `TrimAudioDuration` —— 4/23 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 4/23 个有
- `ResizeShortestToNode` —— 3/23 个有
- `easy float` —— 3/23 个有
- `ManualSigmas` —— 2/23 个有
- `MinimaxH3LatentUpscalerNode3D` —— 2/23 个有
- `PreviewAudio` —— 2/23 个有
- `SoundFlow_GetLength` —— 2/23 个有
- `CFGGuider` —— 1/23 个有
- `CR Text` —— 1/23 个有
- `ConditioningZeroOut` —— 1/23 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 1/23 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/23 个有
- `MiniMaxLowVRAMAttention` —— 1/23 个有
- `PathchSageAttentionKJ` —— 1/23 个有
- `PlaySound|pysssss` —— 1/23 个有
- `ShowText|pysssss` —— 1/23 个有
- `StariAI-MiniMaxH3-Skill` —— 1/23 个有
- `Text` —— 1/23 个有
- `easy cleanGpuUsed` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 23 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 23 | 100% |
| 采样算法 | er_sde | - | 23 | 100% |
| 调度器 | beta | - | 23 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |
| 宽度 | 80 | 80 - 80 | 23 | 100% |
| 高度 | 80 | 80 - 80 | 23 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，23 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，23 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，23 个样本，一致性 100%
- 调度器 最常用 beta，23 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 高发问题（24/23 个样本）：Steps较低可能导致细节不足
