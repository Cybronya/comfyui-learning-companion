---
name: unknown_workflow_sampler_clip_vae_41
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.852167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, PathchSageAttentionKJ, SaveImage, Text Multiline, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image-base_Turbo文生图+提示词生成器_2017665006296371201.json, 图片生成/文生图/Zimage base BF16 一键出模特大片自动生成提示词_2016369219578892289.json, 图片生成/文生图/Zimage base BF16一键出模特大片_2016359000308195330.json, 图片生成/文生图/Zimage base FP8 一键出模特大片自动生成提示词_2016377462980091905.json, 图片生成/文生图/Zimage base GGUF 一键出模特大片自动生成提示词_2016452786682073089.json, 图片生成/文生图/Zimage base GGUF一键出模特大片_2016452734408462338.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_41

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Z-image-base_Turbo文生图+提示词生成器_2017665006296371201.json、图片生成/文生图/Zimage base BF16 一键出模特大片自动生成提示词_2016369219578892289.json、图片生成/文生图/Zimage base BF16一键出模特大片_2016359000308195330.json、图片生成/文生图/Zimage base FP8 一键出模特大片自动生成提示词_2016377462980091905.json、图片生成/文生图/Zimage base GGUF 一键出模特大片自动生成提示词_2016452786682073089.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `SaveImage`
- `Text Multiline`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 4/6 个有
- `PrimitiveStringMultiline` —— 3/6 个有
- `RH_LLMAPI_NODE` —— 3/6 个有
- `UnetLoaderGGUF` —— 2/6 个有
- `> Text Replace` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `Qwen2.5` —— 1/6 个有
- `ShowText` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 6 | 100% |
| Prompt 约束强度(CFG) | 4 | 3 - 4 | 6 | 90% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 3 - 4，6 个样本，取值集中（一致性 90%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
