---
name: text_to_image_video_lora_sampler_22
type: Text To Image
frequency: 20
level: strong
coverage: 0.8934
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, ResolutionSelector, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Minimax H3 self-lift双采 sage加速二十五步最高质量版_2098297223221178370.json, 视频生成/文生视频/SelfLift双采BF16max多宫格单图专用三音色参考工作流，图生视频方案_2106481893637181442.json, 视频生成/文生视频/SelfLift双采BF16max多宫格单图专用双音色参考工作流，图生视频方案_2106512263355125761.json, 视频生成/文生视频/sage无损加速双bf16满血版MinimaxH3文生视频图生视频极致清晰_2088396155074990082.json, 视频生成/文生视频/sage无损加速｜MinimaxH3双bf16满血版文生图生视频全能_2089463275493875714.json, 视频生成/文生视频/selfift双采BF16max多宫格单图专用｜三音色参考自由切换_2106225447443984385.json, 视频生成/文生视频/二采高清放大minimaxH3工作流ENG_2087133080908816386.json, 视频生成/文生视频/低显存高速Minimax H3双采 self-lift模式lora加速质量版_2098116326828105730.json, 视频生成/文生视频/剪枝版BF16微表情｜Minimax H3 10秒768P模板_2090578253928034305.json, 视频生成/文生视频/剪枝版BF16高动态5秒｜Minimax H3 768P视频模板_2090576848353849345.json, 视频生成/文生视频/剪枝版BF16高动态｜Minimax H3 15秒768P模板_2090575450929188866.json, 视频生成/文生视频/剪枝版BF16高动态｜Minimax H3 15秒768P视频模板_2090889192581713922.json, 视频生成/文生视频/剪枝版高动态5秒模板｜Minimax H3 BF16 768P视频生成_2090892022604455938.json, 视频生成/文生视频/多参考打斗视频生成｜MiniMax H3 BF16 768P lora_2095944735889383425.json, 视频生成/文生视频/多参考真实打斗生成｜MiniMax H3 Dasiwa 768P lora_2095940373528014850.json, 视频生成/文生视频/微表情10秒768P模板｜Minimax H3剪枝版BF16视频_2090893466330030082.json, 视频生成/文生视频/极致满血1K 10秒模板｜Minimax H3多参双bf16加sage加速25步_2088754648592248834.json, 视频生成/文生视频/真实打斗多参考生成｜MiniMax H3 B25-49 768P lora_2095941865878147073.json, 视频生成/文生视频/高画质BF16剪枝版｜Minimax H3采样器调度器无加速_2093808070471282690.json, 视频生成/文生视频/高速运动BF16剪枝版｜Minimax H3采样器调度器无加速_2093806594449563650.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_22

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/文生视频/Minimax H3 self-lift双采 sage加速二十五步最高质量版_2098297223221178370.json、视频生成/文生视频/SelfLift双采BF16max多宫格单图专用三音色参考工作流，图生视频方案_2106481893637181442.json、视频生成/文生视频/SelfLift双采BF16max多宫格单图专用双音色参考工作流，图生视频方案_2106512263355125761.json、视频生成/文生视频/sage无损加速双bf16满血版MinimaxH3文生视频图生视频极致清晰_2088396155074990082.json、视频生成/文生视频/sage无损加速｜MinimaxH3双bf16满血版文生图生视频全能_2089463275493875714.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 20 个 workflow 都包含：
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
- `LayerUtility: PurgeVRAM V2` —— 17/20 个有
- `BasicGuider` —— 15/20 个有
- `RandomNoise` —— 15/20 个有
- `SamplerCustomAdvanced` —— 15/20 个有
- `CR Prompt Text` —— 14/20 个有
- `ConditioningZeroOut` —— 5/20 个有
- `H3SigmaRefiner` —— 5/20 个有
- `PrimitiveStringMultiline` —— 5/20 个有
- `SelfLiftH3Sampler` —— 5/20 个有
- `SaveImage` —— 4/20 个有
- `LoadAudio` —— 3/20 个有
- `ImageResizeKJv2` —— 1/20 个有
- `LoraLoaderBypassModelOnly` —— 1/20 个有
- `MiniMaxChunkFeedForward` —— 1/20 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/20 个有
- `MiniMaxLowVRAMAttention` —— 1/20 个有
- `PT_H3ConcatAVLatent` —— 1/20 个有
- `Text Multiline` —— 1/20 个有
- `VAEEncode` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 20 | 100% |
| 采样算法 | er_sde | - | 20 | 100% |
| 调度器 | beta | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |
| 宽度 | 80 | 80 - 80 | 20 | 100% |
| 高度 | 80 | 80 - 80 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 100%
- 调度器 最常用 beta，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高发问题（20/20 个样本）：Steps较低可能导致细节不足
