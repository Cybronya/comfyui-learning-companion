---
name: unknown_workflow_lora_sampler_unet_14
type: Unknown Workflow
frequency: 27
level: strong
coverage: 0.852667
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI代码侠土豆 Qwen-Edit 2511 可视化导演镜头控制_2009862061148348417.json, 图片生成/图生图/AI换装丨FireRed-Image-Edit 1.1丨双图服装迁移_2099794627078483970.json, 图片生成/图生图/AI换装丨FireRed-Image-Edit 1.1丨双图服装迁移_2100135805372157954.json, 图片生成/图生图/AI换装丨FireRed-Image-Edit 1.1丨服装迁移·对比输出_2099798161740095489.json, 图片生成/图生图/AI换装丨FireRed-Image-Edit-1.1丨双图换装·对比预览_2113205586367180801.json, 图片生成/图生图/AI换装丨FireRed-Image-Edit_1.1丨双图服装迁移_2100391034046992386.json, 图片生成/图生图/AI换装丨FireRed-Image-Edit_1.1丨双图服装迁移_2100415738598219778.json, 图片生成/图生图/FireRed-Image-Edit电商服装展示_2089953268666556418.json, 图片生成/图生图/FireRed-lmage-Edit1.1换装_换衣_一键换衣_电商服装展示_2068293485232480257.json, 图片生成/图生图/FireRedImageEdit1.1换衣换装模特服装展示_2060342153183850498.json, 图片生成/图生图/Image-Edit 超简单1_1换装_2092788196512976897.json, 图片生成/图生图/Image-Edit+超简单1：1换装_2092811719927226369.json, 图片生成/图生图/一键快速换装 换衣 电商服装展示 FireRed-Image-Edit 小红书_2090019466867462145.json, 图片生成/图生图/一键快速换装 换衣 电商服装展示 FireRed-Image-Edit 小红书_2090059115530899458.json, 图片生成/图生图/一键换衣 服装展示_2080315710777159682.json, 图片生成/图生图/一键换装  换衣  一键换衣 电商服装展示_2088152490834489346.json, 图片生成/图生图/一键换装 一键换衣  电商服装展示 FireRed-Image-Edit 小红书_2079635494593449985.json, 图片生成/图生图/一键换装 一键换衣  电商服装展示 FireRed-Image-Edit 小红书_2080929952987435009.json, 图片生成/图生图/一键换装 一键换衣  电商服装展示 FireRed-Image-Edit 小红书_2082175037053947906.json, 图片生成/图生图/一键换装 一键换衣  电商服装展示 FireRed-Image-Edit 小红书_2082539309051236353.json, 图片生成/图生图/一键换装 一键换衣  电商服装展示 FireRed-Image-Edit 小红书_2085043026375827458.json, 图片生成/图生图/一键换装 一键换衣  电商服装展示 FireRed-Image-Edit 小红书_2086684594333638658.json, 图片生成/图生图/一键换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2079492729381408769.json, 图片生成/图生图/一键换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2080547652789424129.json, 图片生成/图生图/一键换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2081735465606148098.json, 图片生成/图生图/一键换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2082544098346627074.json, 图片生成/图生图/一键换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2084166560939339777.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_14

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（图片生成/图生图/AI代码侠土豆 Qwen-Edit 2511 可视化导演镜头控制_2009862061148348417.json、图片生成/图生图/AI换装丨FireRed-Image-Edit 1.1丨双图服装迁移_2099794627078483970.json、图片生成/图生图/AI换装丨FireRed-Image-Edit 1.1丨双图服装迁移_2100135805372157954.json、图片生成/图生图/AI换装丨FireRed-Image-Edit 1.1丨服装迁移·对比输出_2099798161740095489.json、图片生成/图生图/AI换装丨FireRed-Image-Edit-1.1丨双图换装·对比预览_2113205586367180801.json…）

- **类型**：Unknown Workflow
- **样本数**：27
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 27 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 25/27 个有
- `LayerUtility: ImageReelComposit` —— 25/27 个有
- `PIP_图像联结` —— 24/27 个有
- `Image Comparer (rgthree)` —— 18/27 个有
- `GetNode` —— 1/27 个有
- `KepStringList` —— 1/27 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/27 个有
- `LayerUtility: PurgeVRAM` —— 1/27 个有
- `QwenMultiangleCameraNode` —— 1/27 个有
- `SetNode` —— 1/27 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 27 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 27 | 100% |
| 采样算法 | euler | - | 27 | 96% |
| 调度器 | simple | - | 27 | 96% |
| 重绘幅度 | 1 | 1 - 1 | 27 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 27/27 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，27 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，27 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，27 个样本，一致性 96%
- 调度器 最常用 simple，27 个样本，一致性 96%
- 重绘幅度 中位数 1，观测区间 1 - 1，27 个样本，取值集中（一致性 100%）
- 高发问题（27/27 个样本）：Steps较低可能导致细节不足
