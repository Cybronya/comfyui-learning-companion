---
name: text_to_image_sampler_clip_unet_136
type: Text To Image
frequency: 5
level: moderate
coverage: 0.7332
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/2-图像生成 (T2I+I2I) Z-Image Turbo 工作流_2053397476975104001.json, 图片生成/文生图/Z-image 文生图+反推洗图_1993920304986652673.json, 图片生成/文生图/boogu全自动文生图工作流_2071823346756575234.json, 图片生成/文生图/krea2全自动文生图工作流_2071823380147425281.json, 图片生成/文生图/krea2全自动文生图工作流_2095743937389621250.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_136

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/2-图像生成 (T2I+I2I) Z-Image Turbo 工作流_2053397476975104001.json、图片生成/文生图/Z-image 文生图+反推洗图_1993920304986652673.json、图片生成/文生图/boogu全自动文生图工作流_2071823346756575234.json、图片生成/文生图/krea2全自动文生图工作流_2071823380147425281.json、图片生成/文生图/krea2全自动文生图工作流_2095743937389621250.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 5 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `ConditioningZeroOut` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `ResolutionSelector` —— 3/5 个有
- `llama_cpp_instruct_adv` —— 3/5 个有
- `llama_cpp_model_loader` —— 3/5 个有
- `llama_cpp_parameters` —— 3/5 个有
- `ConditioningKrea2Rebalance` —— 2/5 个有
- `VAEEncode` —— 2/5 个有
- `AILab_QwenVL` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `Resize Image for SDXL` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 10 | 5 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 512 | 512 - 1344 | 5 | 56% |
| 高度 | 512 | 512 - 1024 | 5 | 69% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 10，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 1344，5 个样本
- 高度 中位数 512，观测区间 512 - 1024，5 个样本
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
