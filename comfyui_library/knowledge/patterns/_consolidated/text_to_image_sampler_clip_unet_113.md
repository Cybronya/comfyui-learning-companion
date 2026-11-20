---
name: text_to_image_sampler_clip_unet_113
type: Text To Image
frequency: 6
level: weak
coverage: 0.892167
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/RealQwenImage V2真人短剧_漫剧角色自动反推生图_2014230476336140290.json, 图片生成/图生图/Z-image 最新模型 图生图工作流V1.0_1993877826990522370.json, 图片生成/图生图/z-image-turbo-图反推提示词_2033467521940066305.json, 图片生成/图生图/z-image图生图(qwen3VL) - 适合新手研究学习的工作流_1997880728690024449.json, 图片生成/图生图/z-image图生图+FlashVSR超清放大-适合新手研究学习_1997896264995995649.json, 图片生成/文生图/Qwen2512反推提示词-出图_2012715450945245186.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_113

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/RealQwenImage V2真人短剧_漫剧角色自动反推生图_2014230476336140290.json、图片生成/图生图/Z-image 最新模型 图生图工作流V1.0_1993877826990522370.json、图片生成/图生图/z-image-turbo-图反推提示词_2033467521940066305.json、图片生成/图生图/z-image图生图(qwen3VL) - 适合新手研究学习的工作流_1997880728690024449.json、图片生成/图生图/z-image图生图+FlashVSR超清放大-适合新手研究学习_1997896264995995649.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/6 个有
- `PreviewAny` —— 4/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `ModelSamplingAuraFlow` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `DF_Get_image_size` —— 1/6 个有
- `FlashVSRNode` —— 1/6 个有
- `ImageScaleDownToSize` —— 1/6 个有
- `MemoryCleaner` —— 1/6 个有
- `Seed (rgthree)` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1052 | 512 - 1920 | 6 | 58% |
| 高度 | 1372 | 512 - 1920 | 6 | 63% |
| 采样步数 | 9.5 | 4 - 20 | 6 | 45% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 6 | 0% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1052，观测区间 512 - 1920，6 个样本
- 高度 中位数 1372，观测区间 512 - 1920，6 个样本
- 采样步数 中位数 9.5，观测区间 4 - 20，6 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，6 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
