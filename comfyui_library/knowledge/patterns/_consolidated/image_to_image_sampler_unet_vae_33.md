---
name: image_to_image_sampler_unet_vae_33
type: Image To Image
frequency: 6
level: strong
coverage: 0.903333
common_nodes: [CLIPLoader, ImageConcatMulti, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit-2511一致性人物多角度_2005144545023197186.json, 图片生成/图生图/Qwen-Image-Edit-2511人物多角度视图_2007988043424206849.json, 图片生成/图生图/Qwen-image-edit-2511  万物“角色_场景_产品”360度96个机位多角度一致性_2067314878532116481.json, 图片生成/图生图/人物多角度及人物卡_2029386699406577665.json, 图片生成/图生图/图像编辑大对比FireRed-edit1.1 VS Klein VS Qwen-edit-2511_2030253666074107905.json, 图片生成/文生图/Qwen-Image-Edit-2511人物多角度视图_2009191764946587649.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_33

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit-2511一致性人物多角度_2005144545023197186.json、图片生成/图生图/Qwen-Image-Edit-2511人物多角度视图_2007988043424206849.json、图片生成/图生图/Qwen-image-edit-2511  万物“角色_场景_产品”360度96个机位多角度一致性_2067314878532116481.json、图片生成/图生图/人物多角度及人物卡_2029386699406577665.json、图片生成/图生图/图像编辑大对比FireRed-edit1.1 VS Klein VS Qwen-edit-2511_2030253666074107905.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `ImageConcatMulti`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `RHHiddenNodes` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `CFGNorm` —— 4/6 个有
- `EmptySD3LatentImage` —— 4/6 个有
- `ModelSamplingAuraFlow` —— 4/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `MuyeTextEditOutput` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `TextConcatenate` —— 2/6 个有
- `AddLabel` —— 1/6 个有
- `DWPreprocessor` —— 1/6 个有
- `EmptyLatentImage` —— 1/6 个有
- `ImpactInt` —— 1/6 个有
- `PainterFluxImageEdit` —— 1/6 个有
- `QwenMultiangleCameraNode` —— 1/6 个有
- `Text` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 512 | - | 1 | 100% |
| 高度 | 512 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 49/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（49/6 个样本）：Steps较低可能导致细节不足
