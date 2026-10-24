---
name: image_to_image_sampler_vae_10
type: Image To Image
frequency: 11
level: moderate
coverage: 0.719818
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_Nunchaku_任意姿势参考迁移_1995464356798377986.json, 图片生成/图生图/Qwen_一键双人合影工作流_1994794472980537346.json, 图片生成/图生图/Qwen光线迁移_1998591999689261058.json, 图片生成/图生图/WH-AI-Studio换装Qwen版_2022569512205295617.json, 图片生成/图生图/WH-AI-Studio电商模特换姿势-动作迁移完美版（保持人物服装细节一致）_2022561416414240770.json, 图片生成/图生图/【推荐，动漫转真人快速版】动漫转写实真人2511-高还原_2017655194384867330.json, 图片生成/图生图/万物转厚涂梦幻动漫风格_2511（风格重绘）_2012103777167347714.json, 图片生成/图生图/动漫转真人高还原_2067296922406313986.json, 图片生成/图生图/史上最强-动漫转写实真人2511AnythingtoRealCharacters正式版-高还原_2088249983240851458.json, 图片生成/图生图/效果最好-动漫转写实真人2511（高还原）_2014551974833819650.json, 图片生成/图生图/（网页）千问换姿势工作流_2037509543676088321.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_10

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen_Nunchaku_任意姿势参考迁移_1995464356798377986.json、图片生成/图生图/Qwen_一键双人合影工作流_1994794472980537346.json、图片生成/图生图/Qwen光线迁移_1998591999689261058.json、图片生成/图生图/WH-AI-Studio换装Qwen版_2022569512205295617.json、图片生成/图生图/WH-AI-Studio电商模特换姿势-动作迁移完美版（保持人物服装细节一致）_2022561416414240770.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 10/11 个有
- `UNETLoader` —— 10/11 个有
- `GetNode` —— 8/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/11 个有
- `SetNode` —— 8/11 个有
- `TextEncodeQwenImageEdit` —— 7/11 个有
- `ImageScaleToTotalPixels` —— 6/11 个有
- `FluxKontextMultiReferenceLatentMethod` —— 5/11 个有
- `Image Comparer (rgthree)` —— 4/11 个有
- `easy imageConcat` —— 4/11 个有
- `Anything Everywhere3` —— 3/11 个有
- `DWPreprocessor` —— 3/11 个有
- `LatentUpscaleBy` —— 3/11 个有
- `GetImageSize` —— 2/11 个有
- `NunchakuQwenImageDiTLoader` —— 1/11 个有
- `ReferenceLatent` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 11 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 0.5 - 1 | 11 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，11 个样本
- 高发问题（14/11 个样本）：Steps较低可能导致细节不足
