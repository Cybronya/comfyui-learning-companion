---
name: unknown_workflow_sampler_clip_unet_42
type: Unknown Workflow
frequency: 17
level: strong
coverage: 0.877294
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-Klein文生图_2012139649845698562.json, 图片生成/文生图/(贞贞10000步 1批次)Flux Klein 9B文生图V1_2013675609699913730.json, 图片生成/文生图/(贞贞共16000步 4批次)Flux Klein 9B文生图V1_2013675619237761025.json, 图片生成/文生图/Ernie-Image-Turbo_2054569121966247938.json, 图片生成/文生图/Flux-Klein文生图_2110216204848820226.json, 图片生成/文生图/Flux-Klein文生图_2110287496109187074.json, 图片生成/文生图/Flux2 Klein基础文生图工作流_2012173193552863233.json, 图片生成/文生图/Flux2-Klein 4B文生图2k版_2012059929259020289.json, 图片生成/文生图/Flux2-Klein 9B文生图2k版_2012059534927335425.json, 图片生成/文生图/Flux2-Klein-9B文生图 极速_1986681179082551298.json, 图片生成/文生图/Flux2-Klein-9B文生图 极速_2011995104159993858.json, 图片生成/文生图/Flux2-Klein-9B文生图 极速出图模型_2011995254534184961.json, 图片生成/文生图/Flux2-Klein-9B文生图+极速_2013513759398039554.json, 图片生成/文生图/极速文生图-flux 2 klein-4b_2014548009350074370.json, 图片生成/文生图/秒级文生图-Flux2-Klein 9B_2012169109827493890.json, 图片生成/文生图/秒级文生图-Flux2-Klein 9B版_2013822140604227585.json, 图片生成/文生图/秒级文生图—flux-2-klein-4b_2013130405263712257.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_42

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein文生图_2012139649845698562.json、图片生成/文生图/(贞贞10000步 1批次)Flux Klein 9B文生图V1_2013675609699913730.json、图片生成/文生图/(贞贞共16000步 4批次)Flux Klein 9B文生图V1_2013675619237761025.json、图片生成/文生图/Ernie-Image-Turbo_2054569121966247938.json、图片生成/文生图/Flux-Klein文生图_2110216204848820226.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelPatchTorchSettings` —— 16/17 个有
- `PathchSageAttentionKJ` —— 16/17 个有
- `CR Text` —— 13/17 个有
- `ConditioningZeroOut` —— 13/17 个有
- `LayerUtility: PurgeVRAM` —— 10/17 个有
- `PreviewImage` —— 7/17 个有
- `GetNode` —— 5/17 个有
- `SetNode` —— 5/17 个有
- `JWInteger` —— 4/17 个有
- `Int` —— 3/17 个有
- `LoraLoaderModelOnly` —— 3/17 个有
- `CR Prompt Text` —— 2/17 个有
- `LoadImage` —— 2/17 个有
- `easy promptLine` —— 2/17 个有
- `easy seed` —— 2/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 8 | 17 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.1 | 17 | 98% |
| 采样算法 | euler | - | 17 | 100% |
| 调度器 | simple | - | 17 | 82% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 8，17 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.1，17 个样本，取值集中（一致性 98%）
- 采样算法 最常用 euler，17 个样本，一致性 100%
- 调度器 最常用 simple，17 个样本，一致性 82%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（17/17 个样本）：Steps较低可能导致细节不足
