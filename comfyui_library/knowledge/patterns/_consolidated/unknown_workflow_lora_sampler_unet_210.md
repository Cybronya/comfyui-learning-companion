---
name: unknown_workflow_lora_sampler_unet_210
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.943
common_nodes: [CFGNorm, CLIPLoader, EmptyLatentImage, FluxKontextMultiReferenceLatentMethod, FluxResolutionNode, GetImageSizeRatio, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveBoolean, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image-edit-2511 可视化灯光调节_2011078611016617985.json, 图片生成/图生图/Qwen-image-edit-2511 可视化角度编辑_2009970399672541185.json, 图片生成/图生图/动漫与现实的融合_2012002444644978689.json, 平台全量/Qwen-image-edit-2511 Anypose  动作迁移_2007289280091136001.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_210

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-image-edit-2511 可视化灯光调节_2011078611016617985.json、图片生成/图生图/Qwen-image-edit-2511 可视化角度编辑_2009970399672541185.json、图片生成/图生图/动漫与现实的融合_2012002444644978689.json、平台全量/Qwen-image-edit-2511 Anypose  动作迁移_2007289280091136001.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
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
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextInput_` —— 3/4 个有
- `ImageScaleDownToSize` —— 2/4 个有
- `RHHiddenNodes` —— 2/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `QwenMultiangleCameraNode` —— 1/4 个有
- `QwenMultiangleLightningNode` —— 1/4 个有
- `easy promptList` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
