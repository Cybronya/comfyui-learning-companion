---
name: text_to_image_lora_sampler_clip_67
type: Text To Image
frequency: 16
level: strong
coverage: 0.882812
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3AudioConditioningT8, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/图生视频高质量生成｜MiniMax H3画面细节增强_2096700949896196098.json, 视频生成/图生视频/多主体生视Minimax_H3频ENG海螺_2087146580276244481.json, 视频生成/图生视频/多主体生视频｜海螺Minimax_H3图生视频生成_2092178321030336513.json, 视频生成/图生视频/多参工作流｜minimax h3图生视频一键生成_2095085442826850306.json, 视频生成/图生视频/开源参考生视频｜Minimax-H3短剧漫剧创意视频_2092025540294303746.json, 视频生成/图生视频/开源参考生视频｜Minimax-H3短剧漫剧角色设计生成_2094785389037965314.json, 视频生成/图生视频/开源版Minimax H3视频全功能加速-turbo4步图片参考短视频生成_2087388416773283842.json, 视频生成/图生视频/海螺H3图生视频｜8步极速加速优化t8版，角色表演流畅_2099887065814093826.json, 视频生成/图生视频/海螺h3开源版H3数字人加速四倍MiniMax图生视频口播数字宫格图片_2086452080943919106.json, 视频生成/图生视频/稳定加速5参考图版｜MiniMax H3全能参考自定义音频_2091200766919925762.json, 视频生成/图生视频/稳定加速版全能参考｜MiniMax H3五参考图音频自定义_2090900087277973505.json, 视频生成/图生视频/稳定加速版全能参考｜MiniMax H3开源支持自定义音频_2091271985484623874.json, 视频生成/图生视频/稳定加速版全能参考｜MiniMax H3支持自定义音频_2092396498217689090.json, 视频生成/图生视频/稳定加速版｜MiniMax H3 全能参考4步加速_2089295207438307330.json, 视频生成/文生视频/4步lora 1.0+sage双重加速｜MinimaxH3双bf16满血版视频生成_2089461776118280193.json, 视频生成/文生视频/minimax开源版中文锁定语音H3稳定4步lora加速版优化版图生视频_2086411021345972225.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_67

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/图生视频高质量生成｜MiniMax H3画面细节增强_2096700949896196098.json、视频生成/图生视频/多主体生视Minimax_H3频ENG海螺_2087146580276244481.json、视频生成/图生视频/多主体生视频｜海螺Minimax_H3图生视频生成_2092178321030336513.json、视频生成/图生视频/多参工作流｜minimax h3图生视频一键生成_2095085442826850306.json、视频生成/图生视频/开源参考生视频｜Minimax-H3短剧漫剧创意视频_2092025540294303746.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：88%

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

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 15/16 个有
- `VHS_VideoCombine` —— 15/16 个有
- `孤海注释` —— 14/16 个有
- `LoraLoaderBypassModelOnly` —— 13/16 个有
- `MiniMaxH3DualClockSamplerT8` —— 12/16 个有
- `MiniMaxH3AVDecodeT8` —— 10/16 个有
- `PrimitiveStringMultiline` —— 10/16 个有
- `BasicScheduler` —— 7/16 个有
- `CreateVideo` —— 7/16 个有
- `SaveVideo` —— 7/16 个有
- `KSamplerSelect` —— 6/16 个有
- `VAEDecodeAudio` —— 6/16 个有
- `CR Prompt Text` —— 5/16 个有
- `LoadAudio` —— 5/16 个有
- `ModelAttentionBackend` —— 3/16 个有
- `SolAttnMiniMax` —— 3/16 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/16 个有
- `CR Text` —— 1/16 个有
- `GetImageSize` —— 1/16 个有
- `ImageResizeKJv2` —— 1/16 个有
- `Label (rgthree)` —— 1/16 个有
- `MiniMaxH3VDNExecutionPlanT8Advanced` —— 1/16 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/16 个有

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
