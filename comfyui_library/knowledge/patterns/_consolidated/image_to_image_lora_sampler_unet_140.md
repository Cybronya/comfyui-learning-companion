---
name: image_to_image_lora_sampler_unet_140
type: Image To Image
frequency: 5
level: moderate
coverage: 0.6602
common_nodes: [CFGNorm, CLIPLoader, ComfySwitchNode, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/小红书FireRed-Image-Edit-1.1单图图像编辑工作流_2039767259761090561.json, 图片生成/图生图/小红书firered_图像编辑_2029929480688504834.json, 图片生成/图生图/工作流基础系列15-FireRed-Image-Edit图像编辑工作流_2047986247905320961.json, 图片生成/图生图/👾老许Gary：FireRed官方基础工作流_2029592443598938113.json, 图片生成/文生图/参考图片打光+全节点注释_2055855007165108225.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_140

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/小红书FireRed-Image-Edit-1.1单图图像编辑工作流_2039767259761090561.json、图片生成/图生图/小红书firered_图像编辑_2029929480688504834.json、图片生成/图生图/工作流基础系列15-FireRed-Image-Edit图像编辑工作流_2047986247905320961.json、图片生成/图生图/👾老许Gary：FireRed官方基础工作流_2029592443598938113.json、图片生成/文生图/参考图片打光+全节点注释_2055855007165108225.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ComfySwitchNode`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/5 个有
- `CR Simple Image Compare` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `INTConstant` —— 1/5 个有
- `LayerUtility: TextBox` —— 1/5 个有
- `MuyeSizeSelector` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `easy ifElse` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 4 - 40 | 5 | 56% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 5 | 65% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 40，观测区间 4 - 40，5 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
