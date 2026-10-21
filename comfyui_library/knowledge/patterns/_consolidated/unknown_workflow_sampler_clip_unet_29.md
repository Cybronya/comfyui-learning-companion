---
name: unknown_workflow_sampler_clip_unet_29
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.835615
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, ModelPatchTorchSettings, PathchSageAttentionKJ, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, LayerUtility: PurgeVRAM]
members: [图片生成/文生图/(贞贞10000步 1批次)Flux Klein 9B文生图V1_2013675609699913730.json, 图片生成/文生图/(贞贞共16000步 4批次)Flux Klein 9B文生图V1_2013675619237761025.json, 图片生成/文生图/1986681179082551298.json, 图片生成/文生图/Flux2 Klein基础文生图工作流_2012173193552863233.json, 图片生成/文生图/Flux2-Klein 4B文生图2k版_2012059929259020289.json, 图片生成/文生图/Flux2-Klein 9B文生图2k版_2012059534927335425.json, 图片生成/文生图/Flux2-Klein-9B文生图 极速_2011995104159993858.json, 图片生成/文生图/Flux2-Klein-9B文生图 极速出图模型_2011995254534184961.json, 图片生成/文生图/Flux2-Klein-9B文生图+极速_2013513759398039554.json, 图片生成/文生图/极速文生图-flux 2 klein-4b_2014548009350074370.json, 图片生成/文生图/秒级文生图-Flux2-Klein 9B_2012169109827493890.json, 图片生成/文生图/秒级文生图-Flux2-Klein 9B版_2013822140604227585.json, 图片生成/文生图/秒级文生图—flux-2-klein-4b_2013130405263712257.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_29

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/(贞贞10000步 1批次)Flux Klein 9B文生图V1_2013675609699913730.json、图片生成/文生图/(贞贞共16000步 4批次)Flux Klein 9B文生图V1_2013675619237761025.json、图片生成/文生图/1986681179082551298.json、图片生成/文生图/Flux2 Klein基础文生图工作流_2012173193552863233.json、图片生成/文生图/Flux2-Klein 4B文生图2k版_2012059929259020289.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 11/13 个有
- `ConditioningZeroOut` —— 11/13 个有
- `LayerUtility: PurgeVRAM` —— 10/13 个有
- `PreviewImage` —— 7/13 个有
- `GetNode` —— 5/13 个有
- `SetNode` —— 5/13 个有
- `Int` —— 3/13 个有
- `LoraLoaderModelOnly` —— 3/13 个有
- `CR Prompt Text` —— 2/13 个有
- `JWInteger` —— 2/13 个有
- `LoadImage` —— 2/13 个有
- `easy promptLine` —— 2/13 个有
- `easy seed` —— 2/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 8 | 13 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 85% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 8，13 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 85%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、LayerUtility: PurgeVRAM
