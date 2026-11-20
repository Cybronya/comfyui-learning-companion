---
name: unknown_workflow_lora_sampler_vae_10
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.818889
common_nodes: [CLIPLoader, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/251225001.001.QwenEdit2511单图编辑+双图互动_2004198320383946754.json, 图片生成/图生图/AI模特换装换衣电商服装主图详情小红书_2064882924616511489.json, 图片生成/图生图/AI模特换装换衣电商服装主图详情小红书【不戴帽子】_2064893829098074114.json, 图片生成/图生图/FireRed-Edit 99_2026606566086025218.json, 图片生成/图生图/FireRed-Edit 合集_2026226588441907201.json, 图片生成/图生图/FireRed-Edit-最强图片编辑模型？_2026932086405341185.json, 图片生成/图生图/小红书FireRed-Edit万物迁移融图工作流_2029507673841999873.json, 图片生成/图生图/服装迁移FireRed-Edit-最强图片编辑模型？_2030196582573940737.json, 图片生成/文生图/QWEN-edit-2509 万物融图 简单版 手动调节前景图位置 简单易用_2000388136918282241.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_10

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/251225001.001.QwenEdit2511单图编辑+双图互动_2004198320383946754.json、图片生成/图生图/AI模特换装换衣电商服装主图详情小红书_2064882924616511489.json、图片生成/图生图/AI模特换装换衣电商服装主图详情小红书【不戴帽子】_2064893829098074114.json、图片生成/图生图/FireRed-Edit 99_2026606566086025218.json、图片生成/图生图/FireRed-Edit 合集_2026226588441907201.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/9 个有
- `UNETLoader` —— 7/9 个有
- `FastCanvas` —— 6/9 个有
- `FastCanvasTool` —— 6/9 个有
- `Anything Everywhere3` —— 5/9 个有
- `Fast Groups Bypasser (rgthree)` —— 5/9 个有
- `LayerMask: BiRefNetUltraV2` —— 5/9 个有
- `LayerMask: LoadBiRefNetModelV2` —— 5/9 个有
- `CFGNorm` —— 2/9 个有
- `ModelSamplingAuraFlow` —— 2/9 个有
- `TT_img_enc` —— 2/9 个有
- `UnetLoaderGGUF` —— 2/9 个有
- `CR Prompt Text` —— 1/9 个有
- `DWPreprocessor` —— 1/9 个有
- `DuckHideNode` —— 1/9 个有
- `LayerUtility: ImageAutoCrop V2` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 9 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 56% |
| 调度器 | beta | - | 9 | 56% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 56%
- 调度器 最常用 beta，9 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（15/9 个样本）：Steps较低可能导致细节不足
