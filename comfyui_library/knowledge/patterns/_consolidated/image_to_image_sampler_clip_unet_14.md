---
name: image_to_image_sampler_clip_unet_14
type: Image To Image
frequency: 13
level: moderate
coverage: 0.957923
common_nodes: [CLIPLoader, CLIPTextEncode, ImageScaleToTotalPixels, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/54bejingxiaoshi_2051276423373045762.json, 图片生成/图生图/3-Flux 2 Klein（图像编辑）Flux 2 Klein 9B Edit_2053399496402456578.json, 图片生成/图生图/B妮B妳-N_S_F_W_系列-DarkBeast-Klein9b-BFS_2033122326463651841.json, 图片生成/图生图/Qwen-Image-Layered图像分层_2017069015822245890.json, 图片生成/图生图/Qwen-Image-Layered图像分层_拆分图层_2030837051507089409.json, 图片生成/图生图/Qwen-Image-Layered图像分层_拆分图层_2096516146404085762.json, 图片生成/图生图/Qwen-Image-Layered图像分层_拆分图层_2096873987820310529.json, 图片生成/图生图/Qwen-Image-Layered图像分层多个 RGBA 图层_2021876336322678785.json, 图片生成/图生图/Qwen-Image-Layered图像分层工作流_2038849289849409537.json, 图片生成/图生图/Qwen-Image-Layered图像分层，将图片拆成多个 RGBA 图层_2002281908631400449.json, 图片生成/图生图/Qwen图像分层，将图片拆成多个+RGBA+图层_2017122772144627713.json, 图片生成/图生图/背景消失术：一键实现人物与海报文字的完美分离_2008910987314864130.json, 图片生成/图生图/🦖Image-Layered图片拆分图层_2010567440442331137.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_14

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/反推提示词/54bejingxiaoshi_2051276423373045762.json、图片生成/图生图/3-Flux 2 Klein（图像编辑）Flux 2 Klein 9B Edit_2053399496402456578.json、图片生成/图生图/B妮B妳-N_S_F_W_系列-DarkBeast-Klein9b-BFS_2033122326463651841.json、图片生成/图生图/Qwen-Image-Layered图像分层_2017069015822245890.json、图片生成/图生图/Qwen-Image-Layered图像分层_拆分图层_2030837051507089409.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 12/13 个有
- `EmptyQwenImageLayeredLatentImage` —— 11/13 个有
- `JWInteger` —— 11/13 个有
- `LatentCutToBatch` —— 11/13 个有
- `ModelSamplingAuraFlow` —— 11/13 个有
- `PreviewImage` —— 7/13 个有
- `ConditioningZeroOut` —— 2/13 个有
- `EmptyFlux2LatentImage` —— 2/13 个有
- `GetImageSize+` —— 1/13 个有
- `HAIGC_SaveImagesToZip` —— 1/13 个有
- `Image Comparer (rgthree)` —— 1/13 个有
- `LayerUtility: PurgeVRAM V2` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 20 | 13 | 68% |
| Prompt 约束强度(CFG) | 2.5 | 0.5 - 2.5 | 13 | 66% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 20，13 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 0.5 - 2.5，13 个样本
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.5，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
