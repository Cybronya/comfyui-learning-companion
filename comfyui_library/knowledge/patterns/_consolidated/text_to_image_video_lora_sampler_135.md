---
name: text_to_image_video_lora_sampler_135
type: Text To Image
frequency: 5
level: strong
coverage: 0.9216
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, H3SigmaRefiner, Int, JjkText, KSampler, KSamplerSelect, List of strings [Crystools], LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3VDNRuntimeAuditT8Advanced, ModelAttentionBackend, PrimitiveStringMultiline, RH_Screenwriter, ResolutionSelector, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WujiCleaner, WujiH3PromptEnhancer, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/H3极速高动态武戏文戏视频生成 多重加速方案_2098865474892288001.json, 视频生成/文生视频/MIniMax H3+DSW+LMS+SelfLift+VDN+SLA极速高动态武戏文戏视频生成方案_2105105571027443713.json, 视频生成/文生视频/MIniMax-H3+DSW+LMS+SelfLift+VDN+SLA｜极速高动态武戏文戏生成_2106954882283560961.json, 视频生成/文生视频/MIniMax-H3多插件合体｜武戏文戏极速生成高动态视频｜文生图生视频_2099090254283231234.json, 视频生成/文生视频/MiniMax H3极速高动态武戏文戏视频生成，文生视频分镜生成图生视频方案_2107169174538776577.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_135

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/H3极速高动态武戏文戏视频生成 多重加速方案_2098865474892288001.json、视频生成/文生视频/MIniMax H3+DSW+LMS+SelfLift+VDN+SLA极速高动态武戏文戏视频生成方案_2105105571027443713.json、视频生成/文生视频/MIniMax-H3+DSW+LMS+SelfLift+VDN+SLA｜极速高动态武戏文戏生成_2106954882283560961.json、视频生成/文生视频/MIniMax-H3多插件合体｜武戏文戏极速生成高动态视频｜文生图生视频_2099090254283231234.json、视频生成/文生视频/MiniMax H3极速高动态武戏文戏视频生成，文生视频分镜生成图生视频方案_2107169174538776577.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `H3SigmaRefiner`
- `Int`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `List of strings [Crystools]`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3VDNRuntimeAuditT8Advanced`
- `ModelAttentionBackend`
- `PrimitiveStringMultiline`
- `RH_Screenwriter`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WujiCleaner`
- `WujiH3PromptEnhancer`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BlockSparseAttention` —— 3/5 个有
- `CM_IntToFloat` —— 3/5 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 3/5 个有
- `MiniMaxH3HyperVAE2xLoaderEXPT8` —— 3/5 个有
- `MiniMaxH3OutputTrimT8` —— 3/5 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 3/5 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 3/5 个有
- `SaveImage` —— 3/5 个有
- `SelfLiftAvatarH3Sampler` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `MiniMaxH3SigmaShift` —— 2/5 个有
- `SelfLiftH3Sampler` —— 2/5 个有
- `SolAttnMiniMax` —— 2/5 个有

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
