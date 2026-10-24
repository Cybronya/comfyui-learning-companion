---
name: text_to_image_video_lora_sampler_107
type: Text To Image
frequency: 7
level: strong
coverage: 0.858429
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PT_H3ConcatAVLatent, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/加速放大Minimax参考生视频图生视频高清采样工作流_2088400575028355073.json, 视频生成/图生视频/参考生视频加速放大｜Minimax图生视频工作流_2088379811487113218.json, 视频生成/图生视频/双采加速图生视频｜MINIMAX-H3视频生成工作流_2088326770620715010.json, 视频生成/图生视频/双采加速工作流MINIMAX H3图生视频风扇变装模板_2088358447304761345.json, 视频生成/图生视频/反推提示词极速二次采样高质量图文生视频｜MiniMax_H3视频超分写实图生视频_2088172964058587138.json, 视频生成/图生视频/反推提示词极速二采高质量｜MiniMax H3文生视频写实_2097527914727305218.json, 视频生成/图生视频/反推提示词极速二采｜MiniMax_H3写实图文生视频超分_2091790249075761153.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_107

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/加速放大Minimax参考生视频图生视频高清采样工作流_2088400575028355073.json、视频生成/图生视频/参考生视频加速放大｜Minimax图生视频工作流_2088379811487113218.json、视频生成/图生视频/双采加速图生视频｜MINIMAX-H3视频生成工作流_2088326770620715010.json、视频生成/图生视频/双采加速工作流MINIMAX H3图生视频风扇变装模板_2088358447304761345.json、视频生成/图生视频/反推提示词极速二次采样高质量图文生视频｜MiniMax_H3视频超分写实图生视频_2088172964058587138.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
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
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 5/7 个有
- `ImageResizeKJv2` —— 5/7 个有
- `CR Text` —— 3/7 个有
- `Dapao_LlamaCaption` —— 3/7 个有
- `Dapao_LlamaCaptionOptions` —— 3/7 个有
- `RegexReplace` —— 3/7 个有
- `easy promptConcat` —— 3/7 个有
- `easy showAnything` —— 3/7 个有
- `CR Prompt Text` —— 2/7 个有
- `CreateVideo` —— 2/7 个有
- `ImpactConditionalBranch` —— 2/7 个有
- `Int` —— 2/7 个有
- `LoadAudio` —— 2/7 个有
- `MathExpression_UTK` —— 2/7 个有
- `PrimitiveStringMultiline` —— 2/7 个有
- `RIFE VFI` —— 2/7 个有
- `ResizeShortestToNode` —— 2/7 个有
- `VAEEncodeAudio` —— 2/7 个有
- `VHS_LoadVideo` —— 2/7 个有
- `easy clearCacheAll` —— 2/7 个有
- `获取视频信息` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
