---
name: unknown_workflow_sampler_clip_unet_30
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.861846
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, easy cleanGpuUsed, CR SDXL Aspect Ratio, CR Text Concatenate, LayerUtility: PurgeVRAM V2]
members: [图片生成/文生图/1952908666094743554.json, 图片生成/文生图/1953001917527093249.json, 图片生成/文生图/1953019372622311426.json, 图片生成/文生图/1953283718866792449.json, 图片生成/文生图/1953303428673040385.json, 图片生成/文生图/1953307722135572481.json, 图片生成/文生图/1953318467875295234.json, 图片生成/文生图/1953742275262251009.json, 图片生成/文生图/1954707955675480065.json, 图片生成/文生图/1958431884814479361.json, 图片生成/文生图/1967092738313293826.json, 图片生成/文生图/1976891524531339266.json, 图片生成/文生图/1981195188544634881.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_30

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/1952908666094743554.json、图片生成/文生图/1953001917527093249.json、图片生成/文生图/1953019372622311426.json、图片生成/文生图/1953283718866792449.json、图片生成/文生图/1953303428673040385.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 12/13 个有
- `LoraLoaderModelOnly` —— 11/13 个有
- `LoadImage` —— 7/13 个有
- `PreviewImage` —— 7/13 个有
- `CR Text` —— 5/13 个有
- `easy cleanGpuUsed` —— 5/13 个有
- `CR Text Concatenate` —— 2/13 个有
- `ShowText` —— 2/13 个有
- `String` —— 2/13 个有
- `AILab_QwenVL` —— 1/13 个有
- `CR SDXL Aspect Ratio` —— 1/13 个有
- `Florence2ModelLoader` —— 1/13 个有
- `Florence2Run` —— 1/13 个有
- `LayerUtility: PurgeVRAM V2` —— 1/13 个有
- `PrimitiveInt` —— 1/13 个有
- `RH_Translator` —— 1/13 个有
- `ShowText|pysssss` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 20 | 13 | 55% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 13 | 28% |
| 采样算法 | euler | - | 13 | 85% |
| 调度器 | simple | - | 13 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 20，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，13 个样本，取值分散，一致性仅 28%
- 采样算法 最常用 euler，13 个样本，一致性 85%
- 调度器 最常用 simple，13 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、easy cleanGpuUsed、CR SDXL Aspect Ratio、CR Text Concatenate、LayerUtility: PurgeVRAM V2
