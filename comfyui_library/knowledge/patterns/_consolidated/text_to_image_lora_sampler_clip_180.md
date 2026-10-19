---
name: text_to_image_lora_sampler_clip_180
type: Text To Image
frequency: 5
level: strong
coverage: 0.8986
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 Ref顶级多参不偏色不油光图生视频处理工具_2102134491904036866.json, 视频生成/图生视频/MiniMax H3 Semantic Bridge LCM高清图生视频文戏专用工作流，图生视频方案_2107901152405835778.json, 视频生成/图生视频/MiniMaxH3+Semantic Bridge+LCM｜高清图生视频文戏_2107683302575534082.json, 视频生成/图生视频/MiniMaxH3+Semantic Bridge+LCM｜高清图生视频文戏专用工作流_2101857846328651777.json, 视频生成/文生视频/参考加速工作流｜Minmax H3文生图生视频直出_2091671424758009858.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_180

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 Ref顶级多参不偏色不油光图生视频处理工具_2102134491904036866.json、视频生成/图生视频/MiniMax H3 Semantic Bridge LCM高清图生视频文戏专用工作流，图生视频方案_2107901152405835778.json、视频生成/图生视频/MiniMaxH3+Semantic Bridge+LCM｜高清图生视频文戏_2107683302575534082.json、视频生成/图生视频/MiniMaxH3+Semantic Bridge+LCM｜高清图生视频文戏专用工作流_2101857846328651777.json、视频生成/文生视频/参考加速工作流｜Minmax H3文生图生视频直出_2091671424758009858.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3SigmaShift`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 4/5 个有
- `ImageResizeKJv2` —— 4/5 个有
- `Int` —— 4/5 个有
- `MiniMaxH3ReferenceToVideo` —— 3/5 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 3/5 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 3/5 个有
- `RH_Screenwriter` —— 3/5 个有
- `VHS_VideoCombine` —— 3/5 个有
- `WujiCleaner` —— 3/5 个有
- `WujiH3PromptEnhancer` —— 3/5 个有
- `easy promptConcat` —— 3/5 个有
- `CreateVideo` —— 2/5 个有
- `MiniMaxH3AudioConditioningT8` —— 2/5 个有
- `PrimitiveFloat` —— 2/5 个有
- `SaveImage` —— 2/5 个有
- `SaveVideo` —— 2/5 个有
- `BasicGuider` —— 1/5 个有
- `ModelAttentionBackend` —— 1/5 个有
- `QwenH3PromptLocal` —— 1/5 个有
- `SigmasPreview` —— 1/5 个有
- `YC_ShowText` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
