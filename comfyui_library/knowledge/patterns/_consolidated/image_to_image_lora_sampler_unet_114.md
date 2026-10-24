---
name: image_to_image_lora_sampler_unet_114
type: Image To Image
frequency: 6
level: strong
coverage: 0.833667
common_nodes: [CFGNorm, CLIPLoader, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, SaveImage, Switch any [Crystools], TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/瓷器-换产品_2032924200163352578.json, 图片生成/图生图/瓷器-白底2.0_2035598661832413185.json, 图片生成/图生图/瓷器-白底2.2_2036037358008668161.json, 图片生成/图生图/瓷器-白底_2033061093744054274.json, 图片生成/文生图/FireRed Image Edit 1.1 8步加速_2073313339664584705.json, 图片生成/文生图/FireRed Image Edit 1.1 阿凡达 Lora 测试流_2073314483048640514.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_114

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/瓷器-换产品_2032924200163352578.json、图片生成/图生图/瓷器-白底2.0_2035598661832413185.json、图片生成/图生图/瓷器-白底2.2_2036037358008668161.json、图片生成/图生图/瓷器-白底_2033061093744054274.json、图片生成/文生图/FireRed Image Edit 1.1 8步加速_2073313339664584705.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
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
- `Switch any [Crystools]`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EG_TX_SFBLS` —— 4/6 个有
- `LayerUtility: TextBox` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `GetImageSize+` —— 3/6 个有
- `ImageResizePresetNode` —— 3/6 个有
- `LayerMask: SegmentAnythingUltra V2` —— 3/6 个有
- `LayerUtility: ColorImage V2` —— 3/6 个有
- `LayerUtility: ImageBlendAdvance V2` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 40 - 40 | 6 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 40 - 40，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
