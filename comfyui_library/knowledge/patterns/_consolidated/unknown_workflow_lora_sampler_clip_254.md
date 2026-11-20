---
name: unknown_workflow_lora_sampler_clip_254
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.987333
common_nodes: [BNK_CLIPTextEncodeAdvanced, CLIPSetLastLayer, CheckpointLoaderSimple, EmptyLatentImage, HyperLoRAApplyLoRA, HyperLoRAConfig, HyperLoRAFaceAttr, HyperLoRAGenerateIDLoRA, HyperLoRAIDCond, HyperLoRALoader, KSampler, LoadImage, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/【老金驿站】HyperLoRA-T2I换脸工作流_1916648677161766914.json, 平台全量/CG迷-HyperLORA换脸工作流_1927001686316056577.json, 平台全量/人物风格转绘hyperlora+ipadapter_1938425918673321985.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_254

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/【老金驿站】HyperLoRA-T2I换脸工作流_1916648677161766914.json、平台全量/CG迷-HyperLORA换脸工作流_1927001686316056577.json、平台全量/人物风格转绘hyperlora+ipadapter_1938425918673321985.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 3 个 workflow 都包含：
- `BNK_CLIPTextEncodeAdvanced`
- `CLIPSetLastLayer`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `HyperLoRAApplyLoRA`
- `HyperLoRAConfig`
- `HyperLoRAFaceAttr`
- `HyperLoRAGenerateIDLoRA`
- `HyperLoRAIDCond`
- `HyperLoRALoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ApplyInstantIDAdvanced` —— 2/3 个有
- `ControlNetLoader` —— 2/3 个有
- `ImpactMakeImageBatch` —— 2/3 个有
- `InstantIDFaceAnalysis` —— 2/3 个有
- `InstantIDModelLoader` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ApplyFBCacheOnModel` —— 1/3 个有
- `IPAdapterAdvanced` —— 1/3 个有
- `IPAdapterUnifiedLoader` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 896 - 1024 | 3 | 94% |
| 高度 | 1024 | 1024 - 1152 | 3 | 94% |
| 采样步数 | 25 | 8 - 30 | 3 | 55% |
| Prompt 约束强度(CFG) | 3 | 3 - 5 | 3 | 74% |
| 采样算法 | dpmpp_2m | - | 3 | 100% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 896 - 1024，3 个样本，取值集中（一致性 94%）
- 高度 中位数 1024，观测区间 1024 - 1152，3 个样本，取值集中（一致性 94%）
- 采样步数 中位数 25，观测区间 8 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 5，3 个样本
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
