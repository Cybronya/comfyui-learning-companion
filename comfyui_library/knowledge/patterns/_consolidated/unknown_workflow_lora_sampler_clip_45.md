---
name: unknown_workflow_lora_sampler_clip_45
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.845444
common_nodes: [Anything Everywhere3, CLIPLoader, CLIPTextEncode, CR Prompt Text, CheckpointLoaderSimple, ColorMatch, Fast Groups Muter (rgthree), ImageScaleToTotalPixels, Int, KSamplerAdvanced, LatentSwitch, LoraLoaderModelOnly, PreviewImage, QwenImageLatentAspectRatio, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/AI视频文生图_2042991324063866882.json, 图片生成/文生图/Zimage构图+Klein高清修复_2037766497598181377.json, 图片生成/文生图/文生图强强联合：Zimage构图+Klein高清修复_2019576100757704705.json, 图片生成/文生图/文生图：Zimage构图+Klein高清修复_2084922710471299074.json, 图片生成/文生图/文生图：Zimage构图+Klein高清修复_2084926999600128001.json, 图片生成/文生图/文生图：Zimage构图+Klein高清修复_2085256281174138881.json, 图片生成/文生图/文生图：Zimage构图+Klein高清修复_2085257479918804993.json, 图片生成/文生图/文生图：Zimage构图+Klein高清修复_2085259061586653186.json, 图片生成/文生图/超强文生图，极致细节：Zimage系列底图，Klein高清修复_2018129430551465986.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_45

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/AI视频文生图_2042991324063866882.json、图片生成/文生图/Zimage构图+Klein高清修复_2037766497598181377.json、图片生成/文生图/文生图强强联合：Zimage构图+Klein高清修复_2019576100757704705.json、图片生成/文生图/文生图：Zimage构图+Klein高清修复_2084922710471299074.json、图片生成/文生图/文生图：Zimage构图+Klein高清修复_2084926999600128001.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 9 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `Fast Groups Muter (rgthree)`
- `ImageScaleToTotalPixels`
- `Int`
- `KSamplerAdvanced`
- `LatentSwitch`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `QwenImageLatentAspectRatio`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 8/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 89% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 9 | 100% |
| 采样算法 | 1 | 1 - 1 | 9 | 100% |
| 调度器 | euler | - | 9 | 100% |
| 重绘幅度 | simple | - | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 89%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，9 个样本，一致性 100%
- 重绘幅度 最常用 simple，9 个样本，一致性 100%
