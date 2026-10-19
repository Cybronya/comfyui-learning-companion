---
name: text_to_image_lora_sampler_clip_69
type: Text To Image
frequency: 12
level: strong
coverage: 0.89875
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Minimax_H3单人极速人物替换，角色一致性动作迁移_2110892482811744258.json, 视频生成/图生视频/lightx2v正式版参考模式｜minimax_h3视频生视频图生视频工作流_2088211325951504385.json, 视频生成/图生视频/minimaxH3 多参考视频PV工作流｜备用方案图生视频更稳妥_2097504953928605697.json, 视频生成/图生视频/minimax_h3_turbo_v4_step600_ema图生视频加速模型_2105146341893693442.json, 视频生成/图生视频/三图参考无参考音｜Minimax H3图生视频人物一致性生成_2089442281551130625.json, 视频生成/图生视频/单图参考加参考音｜Minimax H3图生视频生成_2093782725252706305.json, 视频生成/图生视频/单图参考无参考音｜Minimax H3图生视频工作流_2094012813646852097.json, 视频生成/图生视频/单图参考无参考音｜Minimax H3图生视频直出_2093784039185543170.json, 视频生成/图生视频/参考图+参考音频｜MiniMax H3 4步生视频直出_2090936385749475330.json, 视频生成/图生视频/参考模式10步+3步｜H3 Latent Upscaler图生视频_2090888594817900545.json, 视频生成/文生视频/minmaxH3单采加速三连发｜文生视频图生视频 又快又稳出片神器_2105532532883283969.json, 视频生成/文生视频/minmaxH3单采加速多场景｜文生视频视频生视频图生视频全支持_2105530783984340993.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_69

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/Minimax_H3单人极速人物替换，角色一致性动作迁移_2110892482811744258.json、视频生成/图生视频/lightx2v正式版参考模式｜minimax_h3视频生视频图生视频工作流_2088211325951504385.json、视频生成/图生视频/minimaxH3 多参考视频PV工作流｜备用方案图生视频更稳妥_2097504953928605697.json、视频生成/图生视频/minimax_h3_turbo_v4_step600_ema图生视频加速模型_2105146341893693442.json、视频生成/图生视频/三图参考无参考音｜Minimax H3图生视频人物一致性生成_2089442281551130625.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 12 个 workflow 都包含：
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
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 11/12 个有
- `PrimitiveStringMultiline` —— 11/12 个有
- `孤海注释` —— 11/12 个有
- `MiniMaxH3SigmaShift` —— 9/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/12 个有
- `CreateVideo` —— 7/12 个有
- `VHS_VideoCombine` —— 7/12 个有
- `LoadAudio` —— 6/12 个有
- `SaveVideo` —— 6/12 个有
- `INTConstant` —— 4/12 个有
- `ModelAttentionBackend` —— 4/12 个有
- `VHS_LoadVideo` —— 4/12 个有
- `ExtendIntermediateSigmas` —— 3/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/12 个有
- `ModelPreviewOverrideKJ` —— 2/12 个有
- `PreviewImage` —— 2/12 个有
- `EmptyImage` —— 1/12 个有
- `Fast Groups Bypasser (rgthree)` —— 1/12 个有
- `ManualSigmas` —— 1/12 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 1/12 个有
- `MuyeTextEditOutput` —— 1/12 个有
- `SaveImage` —— 1/12 个有
- `SplitSigmas` —— 1/12 个有
- `VHS_SelectImages` —— 1/12 个有
- `VHS_VideoInfoLoaded` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
