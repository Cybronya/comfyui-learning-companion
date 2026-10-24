---
name: image_to_image_lora_sampler_unet_124
type: Image To Image
frequency: 5
level: moderate
coverage: 0.6774
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image Edit图片编辑_1958360119752998914.json, 图片生成/图生图/Qwen image Edit 2511图像编辑工作流_2003529388635398145.json, 图片生成/图生图/Qwen image edit 2511 图像编辑基础通用工作流_2003707894862364674.json, 图片生成/图生图/Qwen图片编辑模型Plus版本_1970454036820488193.json, 图片生成/图生图/qwen_image_edit多图编辑_1970660738824105985.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_124

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen Image Edit图片编辑_1958360119752998914.json、图片生成/图生图/Qwen image Edit 2511图像编辑工作流_2003529388635398145.json、图片生成/图生图/Qwen image edit 2511 图像编辑基础通用工作流_2003707894862364674.json、图片生成/图生图/Qwen图片编辑模型Plus版本_1970454036820488193.json、图片生成/图生图/qwen_image_edit多图编辑_1970660738824105985.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `TextEncodeQwenImageEdit` —— 4/5 个有
- `TextEncodeQwenImageEditPlus` —— 4/5 个有
- `DWPreprocessor` —— 2/5 个有
- `EmptySD3LatentImage` —— 2/5 个有
- `Fast Groups Muter (rgthree)` —— 2/5 个有
- `Any Switch (rgthree)` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `DF_Get_image_size` —— 1/5 个有
- `EmptyLatentImage` —— 1/5 个有
- `Fast Bypasser (rgthree)` —— 1/5 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/5 个有
- `ImageStitch` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 8 | 5 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 5 | 54% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 512 | - | 1 | 100% |
| 高度 | 512 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
