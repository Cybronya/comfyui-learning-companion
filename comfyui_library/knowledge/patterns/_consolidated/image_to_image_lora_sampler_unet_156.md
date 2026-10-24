---
name: image_to_image_lora_sampler_unet_156
type: Image To Image
frequency: 4
level: strong
coverage: 0.9295
common_nodes: [CFGNorm, CLIPLoader, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/小红书FireRed Image Edit 1.1 超高一致性｜单图编辑｜局部重绘_2090595616262021121.json, 图片生成/图生图/小红书FireRed1.1单图编辑_2047551024805715969.json, 图片生成/图生图/换脸换装FireRed人物一致性_2031960497838366722.json, 图片生成/图生图/换装换脸FireRed人物一致性_2031963984508751873.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_156

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/小红书FireRed Image Edit 1.1 超高一致性｜单图编辑｜局部重绘_2090595616262021121.json、图片生成/图生图/小红书FireRed1.1单图编辑_2047551024805715969.json、图片生成/图生图/换脸换装FireRed人物一致性_2031960497838366722.json、图片生成/图生图/换装换脸FireRed人物一致性_2031963984508751873.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `CR Prompt Text` —— 2/4 个有
- `CR Text` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `InpaintModelConditioning` —— 1/4 个有
- `MaskFillHoles` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 4 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
