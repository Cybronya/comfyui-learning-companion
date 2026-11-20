---
name: image_to_image_lora_sampler_unet_50
type: Image To Image
frequency: 11
level: moderate
coverage: 0.754727
common_nodes: [CFGNorm, CLIPLoader, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveFloat, PrimitiveInt, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【阡陌】小红书FireRed-Image-Edit-1.1妆容迁移工作流_2032346640891256833.json, 图片生成/图生图/【阡陌】小红书FireRed-Image-Edit-1.1超强换装工作流_2031686157397921794.json, 图片生成/图生图/全新图像编辑模型 FireRed-Image-Edit V1.1_2029909224012124161.json, 图片生成/图生图/去水印_2041493178670391297.json, 图片生成/图生图/四图工作流_2078025777152610306.json, 图片生成/图生图/字体效果模仿-风格迁移_2040441829853765633.json, 图片生成/图生图/字体效果模仿-风格迁移_2040581730507169793.json, 图片生成/图生图/字体效果模仿-风格迁移_2052378015811813378.json, 图片生成/图生图/字体生成 字体效果模仿-风格迁移 FireRed-lmage-Edit_2052927368418869250.json, 图片生成/图生图/字体风格模仿_风格迁移_2047127912586944514.json, 图片生成/图生图/字体风格模仿_风格迁移_2048030824334893058.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_50

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/【阡陌】小红书FireRed-Image-Edit-1.1妆容迁移工作流_2032346640891256833.json、图片生成/图生图/【阡陌】小红书FireRed-Image-Edit-1.1超强换装工作流_2031686157397921794.json、图片生成/图生图/全新图像编辑模型 FireRed-Image-Edit V1.1_2029909224012124161.json、图片生成/图生图/去水印_2041493178670391297.json、图片生成/图生图/四图工作流_2078025777152610306.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 10/11 个有
- `ComfySwitchNode` —— 8/11 个有
- `CR Text` —— 6/11 个有
- `CR Text Concatenate` —— 6/11 个有
- `easy imageConcat` —— 6/11 个有
- `ConditioningZeroOut` —— 2/11 个有
- `MuyeSizeSelector` —— 2/11 个有
- `Switch any [Crystools]` —— 2/11 个有
- `Bool` —— 1/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `ImageConcatMulti` —— 1/11 个有
- `ImageScale` —— 1/11 个有
- `ImpactConditionalBranch` —— 1/11 个有
- `LayerUtility: TextBox` —— 1/11 个有
- `PreviewAny` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 4 - 40 | 11 | 72% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 11 | 77% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 40，观测区间 4 - 40，11 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，11 个样本
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
