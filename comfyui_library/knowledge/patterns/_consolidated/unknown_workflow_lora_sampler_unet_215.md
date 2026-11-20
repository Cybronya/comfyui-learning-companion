---
name: unknown_workflow_lora_sampler_unet_215
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.948667
common_nodes: [CFGNorm, CLIPLoader, EmptyLatentImage, FluxKontextMultiReferenceLatentMethod, FluxResolutionNode, GetImageSizeRatio, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveBoolean, SaveImage, TextEncodeQwenImageEditPlus, TextInput_, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image-edit-2511 可视化灯光调节_2011078611016617985.json, 图片生成/图生图/Qwen-image-edit-2511 可视化角度编辑_2009970399672541185.json, 图片生成/图生图/动漫与现实的融合_2012002444644978689.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_215

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen-image-edit-2511 可视化灯光调节_2011078611016617985.json、图片生成/图生图/Qwen-image-edit-2511 可视化角度编辑_2009970399672541185.json、图片生成/图生图/动漫与现实的融合_2012002444644978689.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptyLatentImage`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxResolutionNode`
- `GetImageSizeRatio`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PrimitiveBoolean`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleDownToSize` —— 2/3 个有
- `PreviewAny` —— 1/3 个有
- `QwenMultiangleCameraNode` —— 1/3 个有
- `QwenMultiangleLightningNode` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `easy promptList` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
