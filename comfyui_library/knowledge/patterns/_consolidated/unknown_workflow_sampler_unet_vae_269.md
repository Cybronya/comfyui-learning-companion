---
name: unknown_workflow_sampler_unet_vae_269
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.730667
common_nodes: [Any Switch (rgthree), CLIPLoader, CR Prompt Text, EmptyLatentImage, KSampler, LoadImage, PathchSageAttentionKJ, PrimitiveString, QwenImage21Cache, QwenPERewriteT8, SaveImage, ShowText|pysssss, StringToInt, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen image 2.1图片编辑-2_2112555622364438530.json, 图片生成/图生图/Qwen image 2.1图片编辑-3_2112623085848449026.json, 图片生成/图生图/Qwen image 2.1图片编辑-4_2112629999802085378.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_269

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen image 2.1图片编辑-2_2112555622364438530.json、图片生成/图生图/Qwen image 2.1图片编辑-3_2112623085848449026.json、图片生成/图生图/Qwen image 2.1图片编辑-4_2112629999802085378.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CR Prompt Text`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PathchSageAttentionKJ`
- `PrimitiveString`
- `QwenImage21Cache`
- `QwenPERewriteT8`
- `SaveImage`
- `ShowText|pysssss`
- `StringToInt`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 16 | 16 - 16 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | 40 | 40 - 40 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 16，观测区间 16 - 16，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 40 - 40，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
