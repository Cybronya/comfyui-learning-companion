---
name: text_to_image_lora_sampler_clip_425
type: Text To Image
frequency: 4
level: strong
coverage: 0.92075
common_nodes: [CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, GoogleTranslateTextNode, ImageConcanate, ImageStitch, KSampler, LoadImage, LoadImageOutput, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Kontext Dev手办多视图加速版v1_1942617096314662914.json, 图片生成/图生图/Flux Kontext万物邮票风加速版v1_1948676772624773121.json, 图片生成/图生图/Flux Kontext场景缩小加速版v1_1948665758464245761.json, 图片生成/图生图/Flux Kontext新三视图加速版v1_1948660015625318401.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_425

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux Kontext Dev手办多视图加速版v1_1942617096314662914.json、图片生成/图生图/Flux Kontext万物邮票风加速版v1_1948676772624773121.json、图片生成/图生图/Flux Kontext场景缩小加速版v1_1948665758464245761.json、图片生成/图生图/Flux Kontext新三视图加速版v1_1948660015625318401.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GoogleTranslateTextNode`
- `ImageConcanate`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `LoadImageOutput`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PDIMAGE_LongerSize` —— 3/4 个有
- `TeaCache` —— 3/4 个有
- `JWInteger` —— 1/4 个有
- `MagCache` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1024 | 4 | 75% |
| 高度 | 1024 | 512 - 1024 | 4 | 75% |
| 采样步数 | 20 | 20 - 30 | 4 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1024，4 个样本
- 高度 中位数 1024，观测区间 512 - 1024，4 个样本
- 采样步数 中位数 20，观测区间 20 - 30，4 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
