---
name: unknown_workflow_lora_sampler_clip_49
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.945
common_nodes: [BNK_CLIPTextEncodeAdvanced, CheckpointLoaderSimple, EmptyLatentImage, HyperLoRAApplyLoRA, HyperLoRAConfig, HyperLoRAFaceAttr, HyperLoRAGenerateIDLoRA, HyperLoRAIDCond, HyperLoRALoader, ImpactMakeImageBatch, KSampler, LoadImage, SaveImage, VAEDecode]
problems: []
missing: [LayerUtility: PurgeVRAM V2, CR Text]
members: [图片生成/文生图/1915931428176203777.json, 图片生成/文生图/1916648677161766914.json, 图片生成/文生图/1918130332774629377.json, 图片生成/文生图/1918136035447083009.json, 图片生成/文生图/1973749895905587201.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_49

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1915931428176203777.json、图片生成/文生图/1916648677161766914.json、图片生成/文生图/1918130332774629377.json、图片生成/文生图/1918136035447083009.json、图片生成/文生图/1973749895905587201.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `BNK_CLIPTextEncodeAdvanced`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `HyperLoRAApplyLoRA`
- `HyperLoRAConfig`
- `HyperLoRAFaceAttr`
- `HyperLoRAGenerateIDLoRA`
- `HyperLoRAIDCond`
- `HyperLoRALoader`
- `ImpactMakeImageBatch`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ApplyFBCacheOnModel` —— 3/5 个有
- `CLIPSetLastLayer` —— 3/5 个有
- `ApplyInstantIDAdvanced` —— 2/5 个有
- `ControlNetLoader` —— 2/5 个有
- `InstantIDFaceAnalysis` —— 2/5 个有
- `InstantIDModelLoader` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `DeepTranslatorTextNode` —— 1/5 个有
- `FloatConstant` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `Int` —— 1/5 个有
- `JWInteger` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `Video_Upscale_With_Model` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 896 - 1024 | 5 | 95% |
| 高度 | 1024 | 1024 - 1152 | 5 | 95% |
| 采样步数 | 20 | 20 - 30 | 5 | 82% |
| Prompt 约束强度(CFG) | 5 | 3 - 5 | 5 | 77% |
| 采样算法 | dpmpp_2m | - | 5 | 100% |
| 调度器 | karras | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 896 - 1024，5 个样本，取值集中（一致性 95%）
- 高度 中位数 1024，观测区间 1024 - 1152，5 个样本，取值集中（一致性 95%）
- 采样步数 中位数 20，观测区间 20 - 30，5 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 3 - 5，5 个样本
- 采样算法 最常用 dpmpp_2m，5 个样本，一致性 100%
- 调度器 最常用 karras，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM V2、CR Text
