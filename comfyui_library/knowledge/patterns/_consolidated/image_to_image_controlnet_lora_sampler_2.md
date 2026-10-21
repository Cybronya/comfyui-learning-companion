---
name: image_to_image_controlnet_lora_sampler_2
type: Image To Image
frequency: 4
level: strong
coverage: 0.79
common_nodes: [AIO_Preprocessor, CLIPLoader, ControlNetLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SetUnionControlNetType, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/文生图/1962818248989360130.json, 图片生成/文生图/1963114897561333762.json, 图片生成/文生图/controlnet—千问教学工作流_1994239870906417154.json, 图片生成/文生图/qwen-毛坯房一键精装图_1994410356925665282.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1962818248989360130.json、图片生成/文生图/1963114897561333762.json、图片生成/文生图/controlnet—千问教学工作流_1994239870906417154.json、图片生成/文生图/qwen-毛坯房一键精装图_1994410356925665282.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `ControlNetLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/4 个有
- `CFGNorm` —— 2/4 个有
- `CLIPTextEncode` —— 2/4 个有
- `ControlNetApplyAdvanced` —— 2/4 个有
- `ControlNetApplySD3` —— 2/4 个有
- `EmptyLatentImage` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `OpenposePreprocessor` —— 2/4 个有
- `TextEncodeQwenImageEdit` —— 2/4 个有
- `DWPreprocessor` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | - | 2 | 100% |
| 高度 | 720 | - | 2 | 100% |
| 采样步数 | 4 | 4 - 10 | 4 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| ControlNet 权重 | 1 | 0.75 - 1.8 | 4 | 63% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 720，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 0.75 - 1.8，4 个样本
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2
