---
name: image_to_image_sampler_unet_vae_54
type: Image To Image
frequency: 3
level: strong
coverage: 0.901667
common_nodes: [CFGNorm, CLIPLoader, CR Text, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Imgae Edit任意产品纹理提取与纹理迁移工作流_2066960213785268225.json, 图片生成/图生图/Qwen-Image-Edit 2509-模特分镜多角度_1987910970393694209.json, 图片生成/图生图/印花提取-V5优化版_1994271715236790274.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_54

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen Imgae Edit任意产品纹理提取与纹理迁移工作流_2066960213785268225.json、图片生成/图生图/Qwen-Image-Edit 2509-模特分镜多角度_1987910970393694209.json、图片生成/图生图/印花提取-V5优化版_1994271715236790274.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 2/3 个有
- `CR Text Concatenate` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `RHHiddenNodes` —— 2/3 个有
- `TextEncodeQwenImageEditPlus` —— 2/3 个有
- `EmptyLatentImage` —— 1/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `LayerColor: AutoAdjustV2` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `TextEncodeQwenImageEdit` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 10 | 3 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1536 | - | 1 | 100% |
| 高度 | 2480 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
