---
name: text_to_image_video_lora_sampler_67
type: Text To Image
frequency: 11
level: strong
coverage: 0.893
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, ResolutionSelector, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/SelfLift双采BF16max多宫格单图专用三音色参考工作流，图生视频方案_2106481893637181442.json, 视频生成/图生视频/SelfLift双采BF16max多宫格单图专用双音色参考工作流，图生视频方案_2106512263355125761.json, 视频生成/图生视频/h3开源加速版MINIMAX-H3合集｜单图生多图参考4步lora加速_2097965293799825409.json, 视频生成/图生视频/minimax h3多参工作流｜多参考图生视频高质量生成_2097060954776367106.json, 视频生成/图生视频/minimax h3多参工作流｜多图参考图生视频生成_2094887223530450946.json, 视频生成/图生视频/selfift双采BF16max多宫格单图专用｜三音色参考自由切换_2106225447443984385.json, 视频生成/图生视频/双采加速图生视频｜MINIMAX-H3视频生成工作流_2088326770620715010.json, 视频生成/图生视频/双采加速工作流MINIMAX H3图生视频风扇变装模板_2088358447304761345.json, 视频生成/图生视频/反推提示词极速二次采样高质量图文生视频｜MiniMax_H3视频超分写实图生视频_2088172964058587138.json, 视频生成/图生视频/反推提示词极速二采高质量｜MiniMax H3文生视频写实_2097527914727305218.json, 视频生成/图生视频/反推提示词极速二采｜MiniMax_H3写实图文生视频超分_2091790249075761153.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_67

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/SelfLift双采BF16max多宫格单图专用三音色参考工作流，图生视频方案_2106481893637181442.json、视频生成/图生视频/SelfLift双采BF16max多宫格单图专用双音色参考工作流，图生视频方案_2106512263355125761.json、视频生成/图生视频/h3开源加速版MINIMAX-H3合集｜单图生多图参考4步lora加速_2097965293799825409.json、视频生成/图生视频/minimax h3多参工作流｜多参考图生视频高质量生成_2097060954776367106.json、视频生成/图生视频/minimax h3多参工作流｜多图参考图生视频生成_2094887223530450946.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 8/11 个有
- `BasicScheduler` —— 8/11 个有
- `KSamplerSelect` —— 8/11 个有
- `LoraLoaderBypassModelOnly` —— 8/11 个有
- `RandomNoise` —— 8/11 个有
- `SamplerCustomAdvanced` —— 8/11 个有
- `MiniMaxH3DualClockSamplerT8` —— 7/11 个有
- `Fast Groups Bypasser (rgthree)` —— 6/11 个有
- `PrimitiveStringMultiline` —— 6/11 个有
- `CR Text` —— 5/11 个有
- `LoadAudio` —— 5/11 个有
- `PT_H3ConcatAVLatent` —— 5/11 个有
- `VAEEncode` —— 5/11 个有
- `ImageResizeKJv2` —— 4/11 个有
- `ConditioningZeroOut` —— 3/11 个有
- `Dapao_LlamaCaption` —— 3/11 个有
- `Dapao_LlamaCaptionOptions` —— 3/11 个有
- `H3SigmaRefiner` —— 3/11 个有
- `LayerUtility: PurgeVRAM V2` —— 3/11 个有
- `RegexReplace` —— 3/11 个有
- `SaveImage` —— 3/11 个有
- `SelfLiftH3Sampler` —— 3/11 个有
- `easy promptConcat` —— 3/11 个有
- `easy showAnything` —— 3/11 个有
- `GetImageSize` —— 1/11 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/11 个有
- `UniBlockSwap` —— 1/11 个有
- `VHS_LoadVideo` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
