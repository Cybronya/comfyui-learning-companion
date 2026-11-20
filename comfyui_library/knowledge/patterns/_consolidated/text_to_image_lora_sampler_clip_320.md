---
name: text_to_image_lora_sampler_clip_320
type: Text To Image
frequency: 7
level: strong
coverage: 0.851857
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/简单易用全能生成｜文生视频图生视频一站式工作流_2096713688211345409.json, 视频生成/文生视频/超级加速文生视频｜Minimax_h3角色一致性表演生成_2093781650823012354.json, 视频生成/文生视频/超级加速文生视频｜Minimax_h3角色表演一致性_2093447912754860034.json, 视频生成/文生视频/首尾帧生视频｜MiniMax-H3文生视频图生视频全能_2089683499384135682.json, 视频生成/文生视频/高画质BF16剪枝版｜Minimax H3采样器调度器无加速_2093808070471282690.json, 视频生成/文生视频/高速运动BF16剪枝版｜Minimax H3采样器调度器无加速_2093806594449563650.json, 视频生成/视频生视频/参考视频驱动动作迁移 MiniMax_H3 Ref2VA视频生视频工作流_2106160686563942401.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_320

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/简单易用全能生成｜文生视频图生视频一站式工作流_2096713688211345409.json、视频生成/文生视频/超级加速文生视频｜Minimax_h3角色一致性表演生成_2093781650823012354.json、视频生成/文生视频/超级加速文生视频｜Minimax_h3角色表演一致性_2093447912754860034.json、视频生成/文生视频/首尾帧生视频｜MiniMax-H3文生视频图生视频全能_2089683499384135682.json、视频生成/文生视频/高画质BF16剪枝版｜Minimax H3采样器调度器无加速_2093808070471282690.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 6/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/7 个有
- `PrimitiveFloat` —— 6/7 个有
- `VHS_VideoCombine` —— 6/7 个有
- `CR Prompt Text` —— 4/7 个有
- `LoadImage` —— 4/7 个有
- `VAEDecodeAudio` —— 4/7 个有
- `CR Text` —— 3/7 个有
- `MiniMaxH3AVDecodeT8` —— 3/7 个有
- `MiniMaxH3AudioConditioningT8` —— 3/7 个有
- `MiniMaxH3ImageToVideo` —— 3/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `PainterVRAM` —— 2/7 个有
- `PathchSageAttentionKJ` —— 2/7 个有
- `CreateVideo` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `GetNode` —— 1/7 个有
- `MiniMaxH3Unified` —— 1/7 个有
- `SaveVideo` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有
- `VideoCombineV2` —— 1/7 个有

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
