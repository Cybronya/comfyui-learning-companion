---
name: image_to_image_lora_sampler_clip_5
type: Image To Image
frequency: 4
level: weak
coverage: 0.86675
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [easy imagePixelPerfect]
members: [图片生成/图生图/2101865451822338049.json, 图片生成/文生图/1959874321042845698.json, 图片生成/文生图/Qwen-Image-Layered图生分层提示词优化工作流_2002275313906270210.json, 图片生成/文生图/千问分层模型Qwen Image Layered_2002295276218007554.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_5

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2101865451822338049.json、图片生成/文生图/1959874321042845698.json、图片生成/文生图/Qwen-Image-Layered图生分层提示词优化工作流_2002275313906270210.json、图片生成/文生图/千问分层模型Qwen Image Layered_2002295276218007554.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 3/4 个有
- `ReferenceLatent` —— 3/4 个有
- `AILab_QwenVL` —— 2/4 个有
- `EmptyHunyuanLatentVideo` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `LatentCutToBatch` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `PreviewAny` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `AIO_Preprocessor` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有
- `easy imagePixelPerfect` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 4 | 2% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 4 | 26% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 0.5 - 1 | 4 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，4 个样本，取值分散，一致性仅 2%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，4 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，4 个样本
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：easy imagePixelPerfect
