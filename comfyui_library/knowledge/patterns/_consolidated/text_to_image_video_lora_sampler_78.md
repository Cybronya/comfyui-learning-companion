---
name: text_to_image_video_lora_sampler_78
type: Text To Image
frequency: 11
level: strong
coverage: 0.887727
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/反推提示词极速二次采样高质量图文生视频｜MiniMax_H3视频超分写实图生视频_2088172964058587138.json, 视频生成/图生视频/反推提示词极速二采高质量｜MiniMax H3文生视频写实_2097527914727305218.json, 视频生成/图生视频/反推提示词极速二采｜MiniMax_H3写实图文生视频超分_2091790249075761153.json, 视频生成/图生视频/图生·首尾帧·多参一体化（H38步双时钟）极速导演台ENG_2087117508317900801.json, 视频生成/图生视频/图生视频Minimax_H3_ENG海螺_2087149189619863554.json, 视频生成/图生视频/图生视频基础版｜海螺Minimax_H3一键生成_2092175596649537537.json, 视频生成/图生视频/多参工作流｜minimax h3图生视频一键生成_2095085442826850306.json, 视频生成/图生视频/极速高清直出｜H3文生视频角色一致性视频超分_2089486697900888065.json, 视频生成/图生视频/海螺H3图生视频｜8步极速加速优化t8版，角色表演流畅_2099887065814093826.json, 视频生成/图生视频/清晰度天花板超级加强v3｜minimax h3数字人图生视频_2089034956130570241.json, 视频生成/文生视频/二采高清放大minimaxH3工作流ENG_2087133080908816386.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_78

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/反推提示词极速二次采样高质量图文生视频｜MiniMax_H3视频超分写实图生视频_2088172964058587138.json、视频生成/图生视频/反推提示词极速二采高质量｜MiniMax H3文生视频写实_2097527914727305218.json、视频生成/图生视频/反推提示词极速二采｜MiniMax_H3写实图文生视频超分_2091790249075761153.json、视频生成/图生视频/图生·首尾帧·多参一体化（H38步双时钟）极速导演台ENG_2087117508317900801.json、视频生成/图生视频/图生视频Minimax_H3_ENG海螺_2087149189619863554.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
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
- `MiniMaxH3DualClockSamplerT8`
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
- `LoadImage` —— 10/11 个有
- `ImageResizeKJv2` —— 7/11 个有
- `BasicScheduler` —— 6/11 个有
- `KSamplerSelect` —— 6/11 个有
- `PT_H3ConcatAVLatent` —— 6/11 个有
- `CR Text` —— 5/11 个有
- `VAEEncode` —— 5/11 个有
- `Dapao_LlamaCaption` —— 3/11 个有
- `Dapao_LlamaCaptionOptions` —— 3/11 个有
- `Fast Groups Bypasser (rgthree)` —— 3/11 个有
- `RegexReplace` —— 3/11 个有
- `easy promptConcat` —— 3/11 个有
- `easy showAnything` —— 3/11 个有
- `CR Prompt Text` —— 2/11 个有
- `ModelAttentionBackend` —— 2/11 个有
- `Text` —— 2/11 个有
- `ExtendIntermediateSigmas` —— 1/11 个有
- `GetImageSize` —— 1/11 个有
- `H3SigmaRefiner` —— 1/11 个有
- `LoadAudio` —— 1/11 个有
- `Text Multiline` —— 1/11 个有
- `VAEEncodeTiled` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
