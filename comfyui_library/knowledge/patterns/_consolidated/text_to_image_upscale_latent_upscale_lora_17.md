---
name: text_to_image_upscale_latent_upscale_lora_17
type: Text To Image
frequency: 4
level: strong
coverage: 0.9235
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/文戏不油武戏带感 MiniMax H3双采全能参考生视频V2_2104287266226139138.json, 视频生成/文生视频/文武双修均衡版｜MiniMax H3双采动漫短剧_2096624296683720706.json, 视频生成/文生视频/电影质感拉满｜MiniMax H3双采参考文武双修均衡_2096558764462792706.json, 视频生成/文生视频/高动态战斗专属｜BUNNY_H3双采放大FL2VA套件_2096632033136177153.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_17

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/文戏不油武戏带感 MiniMax H3双采全能参考生视频V2_2104287266226139138.json、视频生成/文生视频/文武双修均衡版｜MiniMax H3双采动漫短剧_2096624296683720706.json、视频生成/文生视频/电影质感拉满｜MiniMax H3双采参考文武双修均衡_2096558764462792706.json、视频生成/文生视频/高动态战斗专属｜BUNNY_H3双采放大FL2VA套件_2096632033136177153.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
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
- `ComfyMathExpression` —— 3/4 个有
- `ModelAttentionBackend` —— 3/4 个有
- `SolAttnMiniMax` —— 3/4 个有
- `VHS_VideoCombine` —— 3/4 个有
- `CR Prompt Text` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `CR Load LoRA` —— 1/4 个有
- `CreateVideo` —— 1/4 个有
- `FastGroupsBypassSwitch` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `SaveVideo` —— 1/4 个有

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
