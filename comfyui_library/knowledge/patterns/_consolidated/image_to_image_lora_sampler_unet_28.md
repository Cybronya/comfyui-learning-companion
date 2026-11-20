---
name: image_to_image_lora_sampler_unet_28
type: Image To Image
frequency: 18
level: strong
coverage: 0.764944
common_nodes: [CFGNorm, CLIPLoader, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveFloat, PrimitiveInt, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【阡陌】小红书FireRed-Image-Edit-1.1妆容迁移工作流_2032346640891256833.json, 图片生成/图生图/【阡陌】小红书FireRed-Image-Edit-1.1超强换装工作流_2031686157397921794.json, 图片生成/图生图/全新图像编辑模型 FireRed-Image-Edit V1.1_2029909224012124161.json, 图片生成/图生图/去水印_2041493178670391297.json, 图片生成/图生图/字体效果模仿-风格迁移_2040441829853765633.json, 图片生成/图生图/字体效果模仿-风格迁移_2040581730507169793.json, 图片生成/图生图/字体效果模仿-风格迁移_2052378015811813378.json, 图片生成/图生图/字体生成 字体效果模仿-风格迁移 FireRed-lmage-Edit_2052927368418869250.json, 图片生成/图生图/字体风格模仿_风格迁移_2047127912586944514.json, 图片生成/图生图/字体风格模仿_风格迁移_2048030824334893058.json, 图片生成/图生图/小红书FireRed-Image-Edit-1.1单图图像编辑工作流_2039767259761090561.json, 图片生成/文生图/FireRed Image Edit 1.1 8步加速_2073313339664584705.json, 平台全量/Redfire image edit1.1_2041891894988382209.json, 平台全量/【阡陌】小红书FireRed-Image-Edit-1.1单图图像编辑工作流_2031303078774837250.json, 平台全量/【阡陌】小红书FireRed-Image-Edit-1.1双图_多图图像编辑工作流_2031561725320892418.json, 平台全量/【阡陌】小红书FireRed-Image-Edit-1.1老照片修复上色工作流_2032374121467744258.json, 平台全量/单图编辑FireRed-Image-Edit-1.1_2043123949629870082.json, 平台全量/字体效果模仿-风格迁移_2055553033274175489.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_28

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/【阡陌】小红书FireRed-Image-Edit-1.1妆容迁移工作流_2032346640891256833.json、图片生成/图生图/【阡陌】小红书FireRed-Image-Edit-1.1超强换装工作流_2031686157397921794.json、图片生成/图生图/全新图像编辑模型 FireRed-Image-Edit V1.1_2029909224012124161.json、图片生成/图生图/去水印_2041493178670391297.json、图片生成/图生图/字体效果模仿-风格迁移_2040441829853765633.json…）

- **类型**：Image To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 18 个 workflow 都包含：
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
- `PrimitiveBoolean` —— 16/18 个有
- `ComfySwitchNode` —— 12/18 个有
- `CR Text` —— 7/18 个有
- `CR Text Concatenate` —— 7/18 个有
- `MuyeSizeSelector` —— 7/18 个有
- `easy imageConcat` —— 7/18 个有
- `ConditioningZeroOut` —— 4/18 个有
- `Switch any [Crystools]` —— 4/18 个有
- `Fast Groups Bypasser (rgthree)` —— 3/18 个有
- `Bool` —— 2/18 个有
- `INTConstant` —— 2/18 个有
- `ImpactConditionalBranch` —— 2/18 个有
- `EmptyLatentImage` —— 1/18 个有
- `ImageConcatMulti` —— 1/18 个有
- `LayerUtility: TextBox` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 40 - 40 | 18 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 18 | 100% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | simple | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 1200 | - | 1 | 100% |
| 高度 | 1600 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 40 - 40，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 simple，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
