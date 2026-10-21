---
name: unknown_workflow_lora_sampler_clip_41
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.845286
common_nodes: [Anything Everywhere3, CLIPLoader, CLIPTextEncode, CR Prompt Text, CheckpointLoaderSimple, ColorMatch, Fast Groups Muter (rgthree), Image Comparer (rgthree), ImageScaleToTotalPixels, Int, KSamplerAdvanced, LatentSwitch, LoraLoaderModelOnly, PreviewImage, QwenImageLatentAspectRatio, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/文生图强强联合：Zimage构图+Klein高清修复_2019576100757704705.json, 图片生成/文生图/文生图：Zimage构图+Klein高清修复_2084922710471299074.json, 图片生成/文生图/文生图：Zimage构图+Klein高清修复_2084926999600128001.json, 图片生成/文生图/文生图：Zimage构图+Klein高清修复_2085256281174138881.json, 图片生成/文生图/文生图：Zimage构图+Klein高清修复_2085257479918804993.json, 图片生成/文生图/文生图：Zimage构图+Klein高清修复_2085259061586653186.json, 图片生成/文生图/超强文生图，极致细节：Zimage系列底图，Klein高清修复_2018129430551465986.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_41

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/文生图强强联合：Zimage构图+Klein高清修复_2019576100757704705.json、图片生成/文生图/文生图：Zimage构图+Klein高清修复_2084922710471299074.json、图片生成/文生图/文生图：Zimage构图+Klein高清修复_2084926999600128001.json、图片生成/文生图/文生图：Zimage构图+Klein高清修复_2085256281174138881.json、图片生成/文生图/文生图：Zimage构图+Klein高清修复_2085257479918804993.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `Fast Groups Muter (rgthree)`
- `Image Comparer (rgthree)`
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

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 7 | 100% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
