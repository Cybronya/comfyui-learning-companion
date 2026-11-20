---
name: text_to_image_sampler_clip_unet_156
type: Text To Image
frequency: 4
level: moderate
coverage: 0.89025
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWEN-EDIT-PLUS 换脸和可控姿势的OOTD工作流_1970783578869145601.json, 图片生成/图生图/Qwen Edit 2509  MultipleAngles -转换视角_1993290281585934338.json, 图片生成/图生图/[1月] 最强视角切换(Qwen 96视角)_2009597776102952961.json, 图片生成/图生图/qwen_image_多图合一-图片编辑_1970819754611118082.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_156

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/QWEN-EDIT-PLUS 换脸和可控姿势的OOTD工作流_1970783578869145601.json、图片生成/图生图/Qwen Edit 2509  MultipleAngles -转换视角_1993290281585934338.json、图片生成/图生图/[1月] 最强视角切换(Qwen 96视角)_2009597776102952961.json、图片生成/图生图/qwen_image_多图合一-图片编辑_1970819754611118082.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `AIO_Preprocessor` —— 2/4 个有
- `CR Text` —— 2/4 个有
- `DF_Get_image_size` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `FluxGuidance` —— 1/4 个有
- `Image Stitch` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `Int` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1680 | 1280 - 1920 | 4 | 83% |
| 高度 | 1080 | 720 - 1920 | 4 | 63% |
| 采样步数 | 14 | 8 - 20 | 4 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 4 | 81% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1680，观测区间 1280 - 1920，4 个样本，取值集中（一致性 83%）
- 高度 中位数 1080，观测区间 720 - 1920，4 个样本
- 采样步数 中位数 14，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，4 个样本，取值集中（一致性 81%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
