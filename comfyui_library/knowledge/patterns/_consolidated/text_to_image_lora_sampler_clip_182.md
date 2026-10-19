---
name: text_to_image_lora_sampler_clip_182
type: Text To Image
frequency: 5
level: strong
coverage: 0.8624
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelAttentionBackend, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SaveVideo, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/H3 TaoMate 3步加速Lora 视频生成处理工具_2100654393346576385.json, 视频生成/文生视频/H3加速双采SelfLift工作流 图生视频高效生成_2099944178082992130.json, 视频生成/文生视频/H3双采参考视频生成 文生视频图生视频多模态_2098274586579263490.json, 视频生成/文生视频/MiniMax H3 SelfLift加速双采文戏武戏参考生视频处理工具_2101730945995993089.json, 视频生成/文生视频/MiniMax H3-SelfLift加速双采｜文戏不油武戏动态强_2101550350955270145.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_182

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/H3 TaoMate 3步加速Lora 视频生成处理工具_2100654393346576385.json、视频生成/文生视频/H3加速双采SelfLift工作流 图生视频高效生成_2099944178082992130.json、视频生成/文生视频/H3双采参考视频生成 文生视频图生视频多模态_2098274586579263490.json、视频生成/文生视频/MiniMax H3 SelfLift加速双采文戏武戏参考生视频处理工具_2101730945995993089.json、视频生成/文生视频/MiniMax H3-SelfLift加速双采｜文戏不油武戏动态强_2101550350955270145.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveVideo`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxChunkFeedForward` —— 4/5 个有
- `MiniMaxH3ReferenceToVideo` —— 4/5 个有
- `MiniMaxLowVRAMAttention` —— 4/5 个有
- `ModelPreviewOverrideKJ` —— 4/5 个有
- `SaveImage` —— 4/5 个有
- `BasicGuider` —— 3/5 个有
- `ExtendIntermediateSigmas` —— 3/5 个有
- `RandomNoise` —— 3/5 个有
- `SamplerCustomAdvanced` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `LoadAudio` —— 2/5 个有
- `LoraLoaderBypassModelOnly` —— 2/5 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/5 个有
- `SolAttnMiniMax` —— 2/5 个有
- `Any Switch (rgthree)` —— 1/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `H3SigmaRefiner` —— 1/5 个有
- `LTXVSeparateAVLatent` —— 1/5 个有
- `LoraLoader` —— 1/5 个有
- `ManualSigmas` —— 1/5 个有
- `MiniMaxH3AudioConditioningT8` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.75 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
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
