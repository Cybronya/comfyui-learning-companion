---
name: image_to_image_sampler_clip_unet_126
type: Image To Image
frequency: 5
level: weak
coverage: 0.98
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-IMAGE-BASE-真人转动漫_2030265707363045378.json, 图片生成/图生图/一键通道图(klein2)_2077597343460978690.json, 图片生成/图生图/一键通道图(klein2)_2081910991482343426.json, 图片生成/图生图/最强Qwan中文图像洗图工作流_1954158265661833217.json, 图片生成/图生图/添加人物（klein2）_2077587992918712321.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_126

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Z-IMAGE-BASE-真人转动漫_2030265707363045378.json、图片生成/图生图/一键通道图(klein2)_2077597343460978690.json、图片生成/图生图/一键通道图(klein2)_2081910991482343426.json、图片生成/图生图/最强Qwan中文图像洗图工作流_1954158265661833217.json、图片生成/图生图/添加人物（klein2）_2077587992918712321.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `ReferenceLatent` —— 3/5 个有
- `ModelSamplingAuraFlow` —— 2/5 个有
- `RH_Captioner` —— 2/5 个有
- `CR Text Concatenate` —— 1/5 个有
- `GrowMaskWithBlur` —— 1/5 个有
- `InpaintModelConditioning` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `easy imageConcat` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 20 | 5 | 37% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 5 | 43% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 0.5 - 1 | 5 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 20，5 个样本，取值分散，一致性仅 37%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，5 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，5 个样本
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
