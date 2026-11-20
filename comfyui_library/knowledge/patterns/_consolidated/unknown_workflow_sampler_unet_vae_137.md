---
name: unknown_workflow_sampler_unet_vae_137
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.809778
common_nodes: [CLIPLoader, KSampler, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/fibo2-dev-文生图_2112890953806733313.json, 图片生成/文生图/fibo2-edit-turbo-文生图_2114716474584686593.json, 图片生成/文生图/image_qwen_image_2_1_t2i_2102665438198059010.json, 图片生成/文生图/qwen image 2.1 文生图提示词扩写_2102006301646745601.json, 图片生成/文生图/qwen image 2.1文生图_2094967170106216450.json, 图片生成/文生图/qwen-image 2.1文生图_2101776581311156225.json, 图片生成/文生图/qwen-image2.1-文生图_2101865085642825729.json, 图片生成/文生图/qwen-image2.1文生图_2115022402173358081.json, 图片生成/文生图/qwen2.1 文生图_2102025901952299009.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_137

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/fibo2-dev-文生图_2112890953806733313.json、图片生成/文生图/fibo2-edit-turbo-文生图_2114716474584686593.json、图片生成/文生图/image_qwen_image_2_1_t2i_2102665438198059010.json、图片生成/文生图/qwen image 2.1 文生图提示词扩写_2102006301646745601.json、图片生成/文生图/qwen image 2.1文生图_2094967170106216450.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 7/9 个有
- `TextEncodeQwenImage21` —— 7/9 个有
- `PrimitiveStringMultiline` —— 4/9 个有
- `TextGenerateLTX2Prompt` —— 3/9 个有
- `easy showAnything` —— 3/9 个有
- `ComfySwitchNode` —— 2/9 个有
- `PreviewAny` —— 2/9 个有
- `TextEncodeFibo2` —— 2/9 个有
- `TextGenerate` —— 2/9 个有
- `RH_LLMAPI_Pro_Node` —— 1/9 个有
- `Text Multiline` —— 1/9 个有
- `TextInputNode` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 8 - 50 | 9 | 59% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 9 | 39% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1024 | 768 - 1024 | 7 | 91% |
| 高度 | 1024 | 1024 - 1024 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 8 - 50，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，9 个样本，取值分散，一致性仅 39%
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 768 - 1024，7 个样本，取值集中（一致性 91%）
- 高度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
