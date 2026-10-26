---
name: text_to_image_video_lora_sampler_165
type: Text To Image
frequency: 4
level: strong
coverage: 0.85475
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PT_H3ConcatAVLatent, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/加速放大Minimax参考生视频图生视频高清采样工作流_2088400575028355073.json, 视频生成/图生视频/参考生视频加速放大｜Minimax图生视频工作流_2088379811487113218.json, 视频生成/图生视频/极速高清直出｜H3文生视频角色一致性视频超分_2089486697900888065.json, 视频生成/图生视频/清晰度天花板超级加强v3｜minimax h3数字人图生视频_2089034956130570241.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_165

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/加速放大Minimax参考生视频图生视频高清采样工作流_2088400575028355073.json、视频生成/图生视频/参考生视频加速放大｜Minimax图生视频工作流_2088379811487113218.json、视频生成/图生视频/极速高清直出｜H3文生视频角色一致性视频超分_2089486697900888065.json、视频生成/图生视频/清晰度天花板超级加强v3｜minimax h3数字人图生视频_2089034956130570241.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PT_H3ConcatAVLatent`
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
- `LoadAudio` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `VAEEncode` —— 3/4 个有
- `CR Prompt Text` —— 2/4 个有
- `CreateVideo` —— 2/4 个有
- `ImpactConditionalBranch` —— 2/4 个有
- `Int` —— 2/4 个有
- `MathExpression_UTK` —— 2/4 个有
- `RIFE VFI` —— 2/4 个有
- `ResizeShortestToNode` —— 2/4 个有
- `VAEEncodeAudio` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `easy clearCacheAll` —— 2/4 个有
- `获取视频信息` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `ExtendIntermediateSigmas` —— 1/4 个有
- `H3SigmaRefiner` —— 1/4 个有
- `ModelAttentionBackend` —— 1/4 个有
- `VAEEncodeTiled` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
