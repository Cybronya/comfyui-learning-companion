---
name: unknown_workflow_lora_clip_unet_2
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.854286
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, ImpactInt, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text, CR Text Concatenate, Note Plus (mtb)]
members: [图片生成/文生图/1951984559229489154.json, 图片生成/文生图/1953833112910352386.json, 图片生成/文生图/1955849490886479874.json, 图片生成/文生图/1958332452488024065.json, 图片生成/文生图/1961625719518511105.json, 图片生成/文生图/1964175572664467458.json, 视频生成/文生视频/1951984559229489154.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_2

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1951984559229489154.json、图片生成/文生图/1953833112910352386.json、图片生成/文生图/1955849490886479874.json、图片生成/文生图/1958332452488024065.json、图片生成/文生图/1961625719518511105.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `ImpactInt`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 6/7 个有
- `CR Text` —— 5/7 个有
- `PathchSageAttentionKJ` —— 5/7 个有
- `CR Text Concatenate` —— 4/7 个有
- `Image Comparer (rgthree)` —— 4/7 个有
- `ModelSamplingSD3` —— 4/7 个有
- `CFGZeroStarAndInit` —— 3/7 个有
- `RH_LLMAPI_NODE` —— 3/7 个有
- `easy showAnything` —— 3/7 个有
- `ConditioningZeroOut` —— 2/7 个有
- `SeedVR2BlockSwap` —— 2/7 个有
- `SeedVR2GGUF` —— 2/7 个有
- `Note Plus (mtb)` —— 1/7 个有
- `WanMoeKSampler` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 100% |
| Prompt 约束强度(CFG) | 10 | 10 - 12 | 7 | 91% |
| 采样算法 | 1 | 1 - 3 | 7 | 46% |
| 调度器 | euler | - | 7 | 43% |
| 重绘幅度 | beta | - | 7 | 43% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 10 - 12，7 个样本，取值集中（一致性 91%）
- 采样算法 中位数 1，观测区间 1 - 3，7 个样本，取值分散，一致性仅 46%
- 调度器 最常用 euler，7 个样本，一致性 43%
- 重绘幅度 最常用 beta，7 个样本，一致性 43%
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Concatenate、Note Plus (mtb)
