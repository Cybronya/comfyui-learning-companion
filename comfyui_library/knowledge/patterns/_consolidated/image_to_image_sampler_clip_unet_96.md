---
name: image_to_image_sampler_clip_unet_96
type: Image To Image
frequency: 5
level: weak
coverage: 0.8926
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWen-Image图生图中文渲染-ComfyUI_1953102878534791169.json, 图片生成/图生图/Z-image-base-洗图_2016877440781524993.json, 图片生成/图生图/ZImage+LoRA图生图_1995169009526038529.json, 图片生成/图生图/最强Qwan中文图像洗图工作流_1954158265661833217.json, 图片生成/图生图/洗图+细节增强【WAN2.1】_1946052911623270402.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_96

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/QWen-Image图生图中文渲染-ComfyUI_1953102878534791169.json、图片生成/图生图/Z-image-base-洗图_2016877440781524993.json、图片生成/图生图/ZImage+LoRA图生图_1995169009526038529.json、图片生成/图生图/最强Qwan中文图像洗图工作流_1954158265661833217.json、图片生成/图生图/洗图+细节增强【WAN2.1】_1946052911623270402.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 4/5 个有
- `RH_Captioner` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `Text Concatenate` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `Text Multiline` —— 2/5 个有
- `AILab_QwenVL` —— 1/5 个有
- `Anything Everywhere3` —— 1/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `LayerUtility: ImageScaleRestore` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `easy stylesSelector` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 9 - 30 | 5 | 57% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 3 | 5 | 58% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 0.2 - 1 | 5 | 60% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 9 - 30，5 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 3，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，5 个样本
