---
name: unknown_workflow_lora_sampler_unet_172
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.92375
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlusPro_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-edit-2511 multianglelighting重打光工作流_2011415104608276481.json, 图片生成/图生图/anime2real-2511动漫转真人工作流alpha_2008554085934440450.json, 图片生成/图生图/anime2real-2511动漫转真人工作流正式版_2008849773113118722.json, 图片生成/图生图/anime2real-2511动漫转真人工作流正式版_2019037044483301378.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_172

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-edit-2511 multianglelighting重打光工作流_2011415104608276481.json、图片生成/图生图/anime2real-2511动漫转真人工作流alpha_2008554085934440450.json、图片生成/图生图/anime2real-2511动漫转真人工作流正式版_2008849773113118722.json、图片生成/图生图/anime2real-2511动漫转真人工作流正式版_2019037044483301378.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlusPro_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 3/4 个有
- `ImageConcatMulti` —— 3/4 个有
- `Label (rgthree)` —— 3/4 个有
- `Textbox` —— 2/4 个有
- `QwenMultiangleLightningNode` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `SynVowColorPicker` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 4 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，4 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
