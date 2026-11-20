---
name: text_to_image_lora_sampler_clip_76
type: Text To Image
frequency: 16
level: strong
coverage: 0.867
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3AudioConditioningT8, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/图生视频工作流｜MINIMAX-H3多功能视频生成_2090564776375185409.json, 视频生成/图生视频/图生视频高质量生成｜MiniMax H3画面细节增强_2096700949896196098.json, 视频生成/图生视频/多主体生视Minimax_H3频ENG海螺_2087146580276244481.json, 视频生成/图生视频/多主体生视频｜海螺Minimax_H3图生视频生成_2092178321030336513.json, 视频生成/图生视频/开源参考生视频｜Minimax-H3短剧漫剧创意视频_2092025540294303746.json, 视频生成/图生视频/开源参考生视频｜Minimax-H3短剧漫剧角色设计生成_2094785389037965314.json, 视频生成/图生视频/开源版Minimax H3视频全功能加速-turbo4步图片参考短视频生成_2087388416773283842.json, 视频生成/图生视频/开源稳定加速版全能参考｜MiniMax H3支持自定义音频图生视频_2091285576120102913.json, 视频生成/图生视频/打斗专用全自动｜MINIMAX-H3战斗特效图生视频一键直出_2089424199805915137.json, 视频生成/图生视频/打斗视频专用全自动模版｜MINIMAX-H3战斗特效图生视频_2091649091871789058.json, 视频生成/图生视频/打斗视频全自动模版｜MINIMAX-H3 战斗特效图生视频_2089268317403049986.json, 视频生成/图生视频/打斗视频全自动模版｜MINIMAX-H3战斗特效图生视频_2091811960156418049.json, 视频生成/图生视频/音频驱动音乐MV｜MiniMax H3数字人加速版V1出片快_2100122889331765250.json, 视频生成/图生视频/高质量自动化多参视频流｜动漫人物特效图生视频_2092738709815906306.json, 视频生成/文生视频/H3多图参考打斗全自动工作流 文生视频图生视频_2100307233627262978.json, 视频生成/文生视频/MiniMax-H3全自动工作流｜文生图文生视频图生视频三合一_2089689168518664193.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_76

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/图生视频工作流｜MINIMAX-H3多功能视频生成_2090564776375185409.json、视频生成/图生视频/图生视频高质量生成｜MiniMax H3画面细节增强_2096700949896196098.json、视频生成/图生视频/多主体生视Minimax_H3频ENG海螺_2087146580276244481.json、视频生成/图生视频/多主体生视频｜海螺Minimax_H3图生视频生成_2092178321030336513.json、视频生成/图生视频/开源参考生视频｜Minimax-H3短剧漫剧创意视频_2092025540294303746.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AudioConditioningT8`
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
- `LoraLoaderBypassModelOnly` —— 15/16 个有
- `MiniMaxH3AVDecodeT8` —— 15/16 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 15/16 个有
- `VHS_VideoCombine` —— 15/16 个有
- `MiniMaxH3DualClockSamplerT8` —— 12/16 个有
- `PrimitiveStringMultiline` —— 12/16 个有
- `LoadAudio` —— 9/16 个有
- `RH_LLMAPI_Pro_Node` —— 8/16 个有
- `BasicScheduler` —— 7/16 个有
- `KSamplerSelect` —— 7/16 个有
- `PreviewAny` —— 7/16 个有
- `Fast Groups Bypasser (rgthree)` —— 6/16 个有
- `PT_H3ConcatAVLatent` —— 6/16 个有
- `VAEEncode` —— 6/16 个有
- `CR Prompt Text` —— 4/16 个有
- `ModelAttentionBackend` —— 4/16 个有
- `SolAttnMiniMax` —— 4/16 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 3/16 个有
- `CreateVideo` —— 2/16 个有
- `SaveVideo` —— 2/16 个有
- `H3SigmaRefiner` —— 1/16 个有
- `MemoryCleaner` —— 1/16 个有
- `MiniMaxH3VDNExecutionPlanT8Advanced` —— 1/16 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/16 个有
- `SaveImage` —— 1/16 个有
- `VAEDecodeAudio` —— 1/16 个有
- `VHS_LoadVideo` —— 1/16 个有
- `WujiCleaner` —— 1/16 个有
- `XB_ROCmMemCleaner` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足
