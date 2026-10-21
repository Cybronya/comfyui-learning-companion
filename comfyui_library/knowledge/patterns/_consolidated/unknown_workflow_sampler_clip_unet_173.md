---
name: unknown_workflow_sampler_clip_unet_173
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.91575
common_nodes: [ApplySageAttention, CFGZeroStar, CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyHunyuanLatentVideo, JWInteger, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, ModelSamplingSD3, SaveImage, SaveLatent, UNETLoader, UNetTemporalAttentionMultiply]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: [LayerUtility: PurgeVRAM V2, CR Prompt Text]
members: [视频生成/文生视频/1930947549484789761.json, 视频生成/文生视频/1937509821795209217.json, 视频生成/文生视频/1939614536154660866.json, 视频生成/文生视频/1931163021429637122.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_173

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/1930947549484789761.json、视频生成/文生视频/1937509821795209217.json、视频生成/文生视频/1939614536154660866.json、视频生成/文生视频/1931163021429637122.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `ApplySageAttention`
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyHunyuanLatentVideo`
- `JWInteger`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `ModelSamplingSD3`
- `SaveImage`
- `SaveLatent`
- `UNETLoader`
- `UNetTemporalAttentionMultiply`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/4 个有
- `LoadLatent` —— 2/4 个有
- `VHS_VideoCombine` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `TeaCache` —— 1/4 个有
- `VAEDecode` —— 1/4 个有
- `VAELoader` —— 1/4 个有
- `WanVideoDecode` —— 1/4 个有
- `WanVideoVAELoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 5 - 20 | 4 | 60% |
| Prompt 约束强度(CFG) | 5 | 1 - 5 | 4 | 57% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | normal | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 3/4 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 5 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 5，观测区间 1 - 5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 normal，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：发现KSampler但没有VAEDecode
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM V2、CR Prompt Text
