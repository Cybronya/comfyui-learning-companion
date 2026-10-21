---
name: text_to_image_sampler_clip_unet_48
type: Text To Image
frequency: 9
level: moderate
coverage: 0.817556
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/2-图像生成 (T2I+I2I) Z-Image Turbo 工作流_2053397476975104001.json, 图片生成/文生图/Z-image 文生图+反推洗图_1993920304986652673.json, 图片生成/文生图/boogu turbo反推文生图_2070395337566679041.json, 图片生成/文生图/boogu turbo反推文生图_2070430959291428865.json, 图片生成/文生图/boogu turbo反推文生图无需提示词_2070351358628294658.json, 图片生成/文生图/boogu turbo反推文生图无需提示词_2070418685847760898.json, 图片生成/文生图/boogu全自动文生图工作流_2071823346756575234.json, 图片生成/文生图/krea2全自动文生图工作流_2071823380147425281.json, 图片生成/文生图/krea2全自动文生图工作流_2095743937389621250.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_48

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/2-图像生成 (T2I+I2I) Z-Image Turbo 工作流_2053397476975104001.json、图片生成/文生图/Z-image 文生图+反推洗图_1993920304986652673.json、图片生成/文生图/boogu turbo反推文生图_2070395337566679041.json、图片生成/文生图/boogu turbo反推文生图_2070430959291428865.json、图片生成/文生图/boogu turbo反推文生图无需提示词_2070351358628294658.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 9 个 workflow 都包含：
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
- `CR Text` —— 8/9 个有
- `ConditioningZeroOut` —— 8/9 个有
- `AILab_QwenVL` —— 5/9 个有
- `Any Switch (rgthree)` —— 5/9 个有
- `Fast Groups Bypasser (rgthree)` —— 5/9 个有
- `easy showAnything` —— 4/9 个有
- `ResolutionSelector` —— 3/9 个有
- `llama_cpp_instruct_adv` —— 3/9 个有
- `llama_cpp_model_loader` —— 3/9 个有
- `llama_cpp_parameters` —— 3/9 个有
- `ConditioningKrea2Rebalance` —— 2/9 个有
- `VAEEncode` —— 2/9 个有
- `PrimitiveFloat` —— 1/9 个有
- `RH_Translator` —— 1/9 个有
- `Resize Image for SDXL` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 10 | 9 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1024 | 512 - 1344 | 9 | 67% |
| 高度 | 1024 | 512 - 1536 | 9 | 56% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 10，9 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1344，9 个样本
- 高度 中位数 1024，观测区间 512 - 1536，9 个样本
- 高发问题（8/9 个样本）：Steps较低可能导致细节不足
