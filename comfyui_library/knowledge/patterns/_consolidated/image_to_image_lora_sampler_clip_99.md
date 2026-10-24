---
name: image_to_image_lora_sampler_clip_99
type: Image To Image
frequency: 3
level: moderate
coverage: 0.835
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-IMAGE-BASE-真人转动漫_2030265707363045378.json, 图片生成/图生图/qwen编辑线稿转效果图_1958881314973888513.json, 图片生成/图生图/wan2.1图生图_洗图_1952652175081160705.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_99

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Z-IMAGE-BASE-真人转动漫_2030265707363045378.json、图片生成/图生图/qwen编辑线稿转效果图_1958881314973888513.json、图片生成/图生图/wan2.1图生图_洗图_1952652175081160705.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `easy imageConcat` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ModelSamplingSD3` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `TextEncodeQwenImageEditPlus` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 8 - 20 | 3 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 33% |
| 重绘幅度 | 0.5 | 0.43 - 1 | 3 | 61% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 33%
- 重绘幅度 中位数 0.5，观测区间 0.43 - 1，3 个样本
