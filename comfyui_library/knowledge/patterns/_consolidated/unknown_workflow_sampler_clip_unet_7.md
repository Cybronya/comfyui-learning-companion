---
name: unknown_workflow_sampler_clip_unet_7
type: Unknown Workflow
frequency: 28
level: strong
coverage: 0.893286
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, ModelPatchTorchSettings, PathchSageAttentionKJ, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux2-Klein-9B _ 4B 极速文生图，胶片质感_2012177114430181377.json, 图片生成/文生图/Flux2-Klein-9B 高性能文生图生成模型_2084850465476538369.json, 图片生成/文生图/Flux2-Klein-9B文生图2K直出_2013150879507030017.json, 图片生成/文生图/Flux2-Klein-9B文生图2k直出_2012016993716670466.json, 图片生成/文生图/Flux2-Klein-9B文生图_2059114128396079105.json, 图片生成/文生图/Flux2-Klein-9B文生图_2059269453438869505.json, 图片生成/文生图/Flux2-Klein-9B文生图_2059314653993463810.json, 图片生成/文生图/Flux2-Klein-9B文生图_2059319556044320770.json, 图片生成/文生图/Flux2-Klein-9B文生图_2059522181494820865.json, 图片生成/文生图/Flux2-Klein-9B文生图_2059536142109859842.json, 图片生成/文生图/Flux2-Klein-9B文生图_2059536321953226754.json, 图片生成/文生图/Flux2-Klein-9B文生图_2059539945018187778.json, 图片生成/文生图/Flux2-Klein-9B文生图_2059540088224313345.json, 图片生成/文生图/Flux2-Klein-9B文生图_2059879281945305089.json, 图片生成/文生图/Flux2-Klein-9B文生图_2063136844673536001.json, 图片生成/文生图/Flux2-Klein-9B文生图_2063148799211687937.json, 图片生成/文生图/Flux2-Klein-9B文生图_2066364752095432705.json, 图片生成/文生图/Flux2-Klein-9B文生图_2067979935930732545.json, 图片生成/文生图/Flux2-Klein-9B文生图_2067980166210609154.json, 图片生成/文生图/Flux2-Klein-9B文生图_2069735520573419522.json, 图片生成/文生图/Flux2-Klein-9B文生图_2078486441843322881.json, 图片生成/文生图/Flux2-Klein-9B文生图_2078522055611478017.json, 图片生成/文生图/Flux2-Klein-9B文生图_2084671748380905474.json, 图片生成/文生图/Flux2-Klein-文生图-9B版本-2k直出_2012182227475501058.json, 图片生成/文生图/Flux2-Klein反推图片提示词生图_2012302540993466370.json, 图片生成/文生图/Klein-9B 大模型 AI 文生图_2086324161999364098.json, 图片生成/文生图/Klein-9B 大模型文生图_2085747367650877442.json, 图片生成/文生图/转绘_2026876025988194306.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_7

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（图片生成/文生图/Flux2-Klein-9B _ 4B 极速文生图，胶片质感_2012177114430181377.json、图片生成/文生图/Flux2-Klein-9B 高性能文生图生成模型_2084850465476538369.json、图片生成/文生图/Flux2-Klein-9B文生图2K直出_2013150879507030017.json、图片生成/文生图/Flux2-Klein-9B文生图2k直出_2012016993716670466.json、图片生成/文生图/Flux2-Klein-9B文生图_2059114128396079105.json…）

- **类型**：Unknown Workflow
- **样本数**：28
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 28 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 27/28 个有
- `PrimitiveStringMultiline` —— 26/28 个有
- `LoadImage` —— 3/28 个有
- `RH_Captioner` —— 2/28 个有
- `Anything Everywhere` —— 1/28 个有
- `ImageScaleDownToSize` —— 1/28 个有
- `PreviewAny` —— 1/28 个有
- `QwenImageLatentAspectRatio` —— 1/28 个有
- `ShowText` —— 1/28 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 28 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 28 | 100% |
| 采样算法 | euler | - | 28 | 100% |
| 调度器 | simple | - | 28 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 28 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/28 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，28 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，28 个样本，一致性 100%
- 调度器 最常用 simple，28 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 高发问题（28/28 个样本）：Steps较低可能导致细节不足
