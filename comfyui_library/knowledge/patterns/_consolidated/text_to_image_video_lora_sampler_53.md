---
name: text_to_image_video_lora_sampler_53
type: Text To Image
frequency: 13
level: strong
coverage: 0.878923
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/图生视频Minimax_H3_ENG海螺_2087149189619863554.json, 视频生成/图生视频/图生视频基础版｜海螺Minimax_H3一键生成_2092175596649537537.json, 视频生成/图生视频/图生视频工作流｜MINIMAX-H3多功能视频生成_2090564776375185409.json, 视频生成/图生视频/多主体生视Minimax_H3频ENG海螺_2087146580276244481.json, 视频生成/图生视频/多主体生视频｜海螺Minimax_H3图生视频生成_2092178321030336513.json, 视频生成/图生视频/多参工作流｜minimax h3图生视频一键生成_2095085442826850306.json, 视频生成/图生视频/开源参考生视频｜Minimax-H3短剧漫剧创意视频_2092025540294303746.json, 视频生成/图生视频/开源参考生视频｜Minimax-H3短剧漫剧角色设计生成_2094785389037965314.json, 视频生成/图生视频/开源版Minimax H3视频全功能加速-turbo4步图片参考短视频生成_2087388416773283842.json, 视频生成/图生视频/极速高清直出｜H3文生视频角色一致性视频超分_2089486697900888065.json, 视频生成/图生视频/清晰度天花板超级加强v3｜minimax h3数字人图生视频_2089034956130570241.json, 视频生成/文生视频/MINIMAX-H3导演台工作流｜文生图生视频三合一_2092335889228853249.json, 视频生成/文生视频/MiniMax-H3全自动工作流｜文生图文生视频图生视频三合一_2089689168518664193.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_53

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/图生视频Minimax_H3_ENG海螺_2087149189619863554.json、视频生成/图生视频/图生视频基础版｜海螺Minimax_H3一键生成_2092175596649537537.json、视频生成/图生视频/图生视频工作流｜MINIMAX-H3多功能视频生成_2090564776375185409.json、视频生成/图生视频/多主体生视Minimax_H3频ENG海螺_2087146580276244481.json、视频生成/图生视频/多主体生视频｜海螺Minimax_H3图生视频生成_2092178321030336513.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 12/13 个有
- `MiniMaxH3DualClockSamplerT8` —— 11/13 个有
- `ModelAttentionBackend` —— 6/13 个有
- `PrimitiveStringMultiline` —— 5/13 个有
- `BasicScheduler` —— 3/13 个有
- `ImageResizeKJv2` —— 3/13 个有
- `KSamplerSelect` —— 3/13 个有
- `PT_H3ConcatAVLatent` —— 3/13 个有
- `Text` —— 3/13 个有
- `CR Prompt Text` —— 2/13 个有
- `CR Text` —— 2/13 个有
- `H3SigmaRefiner` —— 2/13 个有
- `LoadAudio` —— 2/13 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/13 个有
- `RH_LLMAPI_Pro_Node` —— 2/13 个有
- `SolAttnMiniMax` —— 2/13 个有
- `VAEEncode` —— 2/13 个有
- `ExtendIntermediateSigmas` —— 1/13 个有
- `Fast Groups Bypasser (rgthree)` —— 1/13 个有
- `GetImageSize` —— 1/13 个有
- `PreviewAny` —— 1/13 个有
- `VAEEncodeTiled` —— 1/13 个有

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
