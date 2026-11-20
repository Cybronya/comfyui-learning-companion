---
name: image_to_image_sampler_unet_vae_54
type: Image To Image
frequency: 2
level: weak
coverage: 0.906
common_nodes: [CFGNorm, CLIPLoader, CR Text, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RHHiddenNodes, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Imgae Edit任意产品纹理提取与纹理迁移工作流_2066960213785268225.json, 图片生成/图生图/Qwen-Image-Edit 2509-模特分镜多角度_1987910970393694209.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_54

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen Imgae Edit任意产品纹理提取与纹理迁移工作流_2066960213785268225.json、图片生成/图生图/Qwen-Image-Edit 2509-模特分镜多角度_1987910970393694209.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RHHiddenNodes`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `LayerColor: AutoAdjustV2` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
