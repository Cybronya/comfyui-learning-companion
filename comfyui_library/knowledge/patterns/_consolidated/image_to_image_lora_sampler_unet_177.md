---
name: image_to_image_lora_sampler_unet_177
type: Image To Image
frequency: 3
level: strong
coverage: 0.421
common_nodes: [CFGNorm, CLIPLoader, CR Prompt List, EmptyLatentImage, Fast Groups Muter (rgthree), FluxKontextMultiReferenceLatentMethod, GetImagesFromBatchIndexed, GetNode, INTConstant, ImageConcatFromBatch, ImageListToImageBatch, ImpactMakeImageList, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, PrimitiveString, PrimitiveStringMultiline, ReverseImageBatch, SaveImage, Seed (rgthree), SetNode, TextEncodeQwenImageEditPlus, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, VRAM_Debug, easy promptConcat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI短剧多视图角色卡生成_2027254982688378882.json, 图片生成/图生图/角色卡一键生成（qwen2511）_2020918936870588418.json, 图片生成/图生图/角色卡生成_2017594546737123330.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_177

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/AI短剧多视图角色卡生成_2027254982688378882.json、图片生成/图生图/角色卡一键生成（qwen2511）_2020918936870588418.json、图片生成/图生图/角色卡生成_2017594546737123330.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：42%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Prompt List`
- `EmptyLatentImage`
- `Fast Groups Muter (rgthree)`
- `FluxKontextMultiReferenceLatentMethod`
- `GetImagesFromBatchIndexed`
- `GetNode`
- `INTConstant`
- `ImageConcatFromBatch`
- `ImageListToImageBatch`
- `ImpactMakeImageList`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveString`
- `PrimitiveStringMultiline`
- `ReverseImageBatch`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VRAM_Debug`
- `easy promptConcat`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 720 - 720 | 3 | 100% |
| 高度 | 1280 | 1280 - 1280 | 3 | 100% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 720 - 720，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1280 - 1280，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
