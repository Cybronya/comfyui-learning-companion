---
name: image_to_image_lora_sampler_unet_100
type: Image To Image
frequency: 6
level: strong
coverage: 0.877167
common_nodes: [CLIPLoader, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/8步加速-QwenEdit位置偏移解决方案_1968478135140397058.json, 图片生成/图生图/Qwen Image Edit 2511图生图_2026496059094077441.json, 图片生成/图生图/Qwen-edit-2511-去水印_2005123694177517569.json, 图片生成/图生图/Qwen-edit-2511-无限扩图（简化版）_2005999334229495810.json, 图片生成/图生图/Qwen2511 细节一致性修复工作流_2017865949512208386.json, 图片生成/图生图/QwenEdit偏移问题解决方案_1965093253525684225.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_100

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/8步加速-QwenEdit位置偏移解决方案_1968478135140397058.json、图片生成/图生图/Qwen Image Edit 2511图生图_2026496059094077441.json、图片生成/图生图/Qwen-edit-2511-去水印_2005123694177517569.json、图片生成/图生图/Qwen-edit-2511-无限扩图（简化版）_2005999334229495810.json、图片生成/图生图/Qwen2511 细节一致性修复工作流_2017865949512208386.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 5/6 个有
- `TextEncodeQwenImageEditPlus` —— 4/6 个有
- `CFGNorm` —— 3/6 个有
- `ModelSamplingAuraFlow` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `ReferenceLatent` —— 3/6 个有
- `Text Multiline` —— 2/6 个有
- `TextEncodeQwenImageEdit` —— 2/6 个有
- `TextEncodeQwenImageEdit_lrzjason` —— 2/6 个有
- `CLIPTextEncode` —— 1/6 个有
- `DapaoImagePadDirectionNode` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `NunchakuQwenImageDiTLoader` —— 1/6 个有
- `RH_LLMAPI_NODE` —— 1/6 个有
- `easy showAnything` —— 1/6 个有
- `seed _O` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 8 | 6 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（22/6 个样本）：Steps较低可能导致细节不足
