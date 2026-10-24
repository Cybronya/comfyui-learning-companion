---
name: unknown_workflow_lora_sampler_unet_176
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.9115
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEditPlus任意控图多图编辑人物一致性_1971932971102105602.json, 图片生成/图生图/qwen编辑plus_1957721637841989634.json, 图片生成/图生图/单图直出多视角，背面也可以，超强一致性_1986710528087240705.json, 图片生成/图生图/🦖QwenEdit Plus单图文字修改_1971088622319505410.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_176

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/QwenEditPlus任意控图多图编辑人物一致性_1971932971102105602.json、图片生成/图生图/qwen编辑plus_1957721637841989634.json、图片生成/图生图/单图直出多视角，背面也可以，超强一致性_1986710528087240705.json、图片生成/图生图/🦖QwenEdit Plus单图文字修改_1971088622319505410.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 3/4 个有
- `ImageStitch` —— 3/4 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 3/4 个有
- `CR Prompt Text` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `QwenEditConfigPreparer` —— 1/4 个有
- `QwenEditOutputExtractor` —— 1/4 个有
- `Text Multiline` —— 1/4 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 9 | 4 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 9，4 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
