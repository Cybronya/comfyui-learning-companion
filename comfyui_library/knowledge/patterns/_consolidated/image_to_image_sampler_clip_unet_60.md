---
name: image_to_image_sampler_clip_unet_60
type: Image To Image
frequency: 7
level: strong
coverage: 0.739143
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Upscaler-jasperai _Flux-高清修复+放大_1960569499613298689.json, 图片生成/图生图/kontext 风格转绘 225 种_2019645428148473857.json, 图片生成/图生图/人物改变动作_1958379196533915649.json, 图片生成/图生图/图片打光-kontext光影增强_1992859522335305730.json, 图片生成/图生图/打光工作流-kontext光影增强-SeedVR2放大_1998573391600844802.json, 图片生成/图生图/打光工作流-kontext光影增强_1951336253025366018.json, 图片生成/图生图/自然光场重建工作流_1994974310416703489.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_60

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Upscaler-jasperai _Flux-高清修复+放大_1960569499613298689.json、图片生成/图生图/kontext 风格转绘 225 种_2019645428148473857.json、图片生成/图生图/人物改变动作_1958379196533915649.json、图片生成/图生图/图片打光-kontext光影增强_1992859522335305730.json、图片生成/图生图/打光工作流-kontext光影增强-SeedVR2放大_1998573391600844802.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 6/7 个有
- `Image Comparer (rgthree)` —— 6/7 个有
- `ReferenceLatent` —— 6/7 个有
- `ConstrainImage|pysssss` —— 5/7 个有
- `JjkText` —— 5/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `CR Text Input Switch (4 way)` —— 4/7 个有
- `ImpactSwitch` —— 4/7 个有
- `Anything Everywhere` —— 2/7 个有
- `AddLabel` —— 1/7 个有
- `ControlNetApplySD3` —— 1/7 个有
- `ControlNetLoader` —— 1/7 个有
- `ImageScaleBy` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `SeedVR2` —— 1/7 个有
- `easy stylesSelector` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 30 | 7 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| ControlNet 权重 | 0.7 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 30，7 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
