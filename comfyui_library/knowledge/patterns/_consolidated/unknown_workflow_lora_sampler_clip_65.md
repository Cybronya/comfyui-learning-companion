---
name: unknown_workflow_lora_sampler_clip_65
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9036
common_nodes: [ApplyFBCacheOnModel, BNK_CLIPTextEncodeAdvanced, CLIPSetLastLayer, CheckpointLoaderSimple, EmptyLatentImage, HyperLoRAApplyLoRA, HyperLoRAConfig, HyperLoRAFaceAttr, HyperLoRAGenerateIDLoRA, HyperLoRAIDCond, HyperLoRALoader, ImpactMakeImageBatch, JWInteger, KSampler, LoadImage, SaveImage, VAEDecode]
problems: []
missing: [LayerUtility: PurgeVRAM V2, Note Plus (mtb), CR Prompt Text]
members: [图片生成/文生图/1915751964595130369.json, 图片生成/文生图/1915753672788082690.json, 图片生成/文生图/1915754672240394242.json, 图片生成/文生图/1915755901133717506.json, 图片生成/文生图/1916009861518131201.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_65

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1915751964595130369.json、图片生成/文生图/1915753672788082690.json、图片生成/文生图/1915754672240394242.json、图片生成/文生图/1915755901133717506.json、图片生成/文生图/1916009861518131201.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `ApplyFBCacheOnModel`
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
- `ImpactMakeImageBatch`
- `JWInteger`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 4/5 个有
- `LayerUtility: PurgeVRAM V2` —— 4/5 个有
- `Note Plus (mtb)` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `ControlNetLoader` —— 3/5 个有
- `ControlNetApplyAdvanced` —— 2/5 个有
- `OpenposePreprocessor` —— 2/5 个有
- `ApplyInstantIDAdvanced` —— 1/5 个有
- `CR Prompt Text` —— 1/5 个有
- `FaceDetailer` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `ImageUpscaleWithModel` —— 1/5 个有
- `InstantIDFaceAnalysis` —— 1/5 个有
- `InstantIDModelLoader` —— 1/5 个有
- `UltralyticsDetectorProvider` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 5 | 3 - 5 | 5 | 83% |
| 采样算法 | dpmpp_2m | - | 5 | 100% |
| 调度器 | karras | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| ControlNet 权重 | 0.7 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 3 - 5，5 个样本，取值集中（一致性 83%）
- 采样算法 最常用 dpmpp_2m，5 个样本，一致性 100%
- 调度器 最常用 karras，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM V2、Note Plus (mtb)、CR Prompt Text
