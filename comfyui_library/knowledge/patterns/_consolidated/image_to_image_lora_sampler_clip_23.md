---
name: image_to_image_lora_sampler_clip_23
type: Image To Image
frequency: 9
level: moderate
coverage: 0.941
common_nodes: [CLIPTextEncode, CR Text, CR Text Concatenate, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux相似图生成工作流--YIHANG_1958430969332133889.json, 图片生成/图生图/Wan2.2-最强洗图工作流_1982478793510141953.json, 图片生成/图生图/Wan2.2最强写实洗图工作流_1949488940486664194.json, 图片生成/图生图/Wan2.2最强写实洗图工作流_2009509806486327298.json, 图片生成/图生图/Wan2.2（写实修复）_1962173423302676481.json, 图片生成/图生图/啊癫 wan2.2人像写实洗图_1954212582670397441.json, 图片生成/图生图/图片写实修复_1968563258640740354.json, 图片生成/文生图/啊癫 Wan2.2 人像写实 超真实_1952340994471735297.json, 图片生成/文生图/通义万相图生图洗图工作流_1949727235787366402.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Flux相似图生成工作流--YIHANG_1958430969332133889.json、图片生成/图生图/Wan2.2-最强洗图工作流_1982478793510141953.json、图片生成/图生图/Wan2.2最强写实洗图工作流_1949488940486664194.json、图片生成/图生图/Wan2.2最强写实洗图工作流_2009509806486327298.json、图片生成/图生图/Wan2.2（写实修复）_1962173423302676481.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 8/9 个有
- `RH_Captioner` —— 8/9 个有
- `ModelSamplingSD3` —— 7/9 个有
- `PathchSageAttentionKJ` —— 7/9 个有
- `easy showAnything` —— 7/9 个有
- `LayerUtility: ImageReel` —— 6/9 个有
- `LayerUtility: ImageReelComposit` —— 6/9 个有
- `CFGZeroStarAndInit` —— 5/9 个有
- `Image Comparer (rgthree)` —— 3/9 个有
- `DualCLIPLoader` —— 1/9 个有
- `JC` —— 1/9 个有
- `LayerUtility: CropByMask V2` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `SaveLatent` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.7 | 0.4 - 1 | 9 | 79% |
| LoRA 文本强度 | 0.7 | 0.4 - 1 | 9 | 79% |
| 采样步数 | 20 | 8 - 20 | 9 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | res_2s | - | 9 | 89% |
| 调度器 | bong_tangent | - | 9 | 89% |
| 重绘幅度 | 0.4 | 0.15 - 0.7 | 9 | 58% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 0.7，观测区间 0.4 - 1，9 个样本
- LoRA 文本强度 中位数 0.7，观测区间 0.4 - 1，9 个样本
- 采样步数 中位数 20，观测区间 8 - 20，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，9 个样本，一致性 89%
- 调度器 最常用 bong_tangent，9 个样本，一致性 89%
- 重绘幅度 中位数 0.4，观测区间 0.15 - 0.7，9 个样本
