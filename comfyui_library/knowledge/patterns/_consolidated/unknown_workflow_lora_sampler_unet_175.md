---
name: unknown_workflow_lora_sampler_unet_175
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.84625
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, QwenEditConfigPreparer, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEdit2509材质迁移_1989647500334256129.json, 图片生成/图生图/qwen-edit 多角度打光_2003346924235325441.json, 图片生成/图生图/动漫人物转真人单图编辑风格转换_2093628982968279041.json, 图片生成/图生图/动漫人物转真人单图编辑风格转换_2093899329370157058.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_175

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/QwenEdit2509材质迁移_1989647500334256129.json、图片生成/图生图/qwen-edit 多角度打光_2003346924235325441.json、图片生成/图生图/动漫人物转真人单图编辑风格转换_2093628982968279041.json、图片生成/图生图/动漫人物转真人单图编辑风格转换_2093899329370157058.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenEditConfigPreparer`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 3/4 个有
- `ImageScale` —— 2/4 个有
- `ColorMatch` —— 1/4 个有
- `ImageStitch` —— 1/4 个有
- `Is Mask Empty JK` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `SolidMask` —— 1/4 个有
- `easy ifElse` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1.25 | 1 - 1.5 | 4 | 80% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | beta57 | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.25，观测区间 1 - 1.5，4 个样本，取值集中（一致性 80%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 beta57，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
