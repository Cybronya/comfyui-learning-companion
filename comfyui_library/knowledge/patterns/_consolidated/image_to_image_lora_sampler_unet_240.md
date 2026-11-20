---
name: image_to_image_lora_sampler_unet_240
type: Image To Image
frequency: 3
level: strong
coverage: 0.791333
common_nodes: [CFGNorm, CLIPLoader, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/小红书FireRed-Image-Edit-1.1单图图像编辑工作流_2117631454963388417.json, 平台全量/门头、文化墙效果图工作流_2029783413703577601.json, 数字人/数字人/小红书编辑模型FireRed Image Edit 1.1 8步加速_2029994284878929921.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_240

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/小红书FireRed-Image-Edit-1.1单图图像编辑工作流_2117631454963388417.json、平台全量/门头、文化墙效果图工作流_2029783413703577601.json、数字人/数字人/小红书编辑模型FireRed Image Edit 1.1 8步加速_2029994284878929921.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
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
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `Switch any [Crystools]` —— 2/3 个有
- `ComfySwitchNode` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `LazyCache` —— 1/3 个有
- `ModelAttentionBackend` —— 1/3 个有
- `MuyeSizeSelector` —— 1/3 个有
- `easy anythingIndexSwitch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 40 - 40 | 3 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 40 - 40，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
