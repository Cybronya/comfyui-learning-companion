---
name: image_to_image_sampler_clip_unet_16
type: Image To Image
frequency: 13
level: strong
coverage: 0.964769
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, GetImageSize, ImageConcatMulti, ImageScaleToTotalPixels, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageConcat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/HL_2071329763985285121.json, 图片生成/图生图/flux一分钟快速换脸工作流图片换脸人脸变换_2089571788379475970.json, 图片生成/图生图/flux一分钟快速换脸工作流图片换脸人脸变换图生图_2089674597674344449.json, 图片生成/图生图/ht_2076413527618838529.json, 图片生成/图生图/klein9b 换头1_2033166861201842178.json, 图片生成/图生图/pipiai换脸神器_2034967727894437889.json, 图片生成/图生图/人物换脸换头-黑兽Klein 9B BFS_2036793996411936770.json, 图片生成/图生图/史上最强换脸工作流 黑兽Klein 9B BFS换脸V1 林耀3.26_2037080557837881346.json, 图片生成/图生图/土狗002_2043476116144394242.json, 图片生成/图生图/土狗0425API更新版_2046545303985201154.json, 图片生成/图生图/黑兽Klein 9B BFS换脸V1_2036758096441253889.json, 图片生成/图生图/黑兽Klein 9B BFS换脸V1_2038144395391803393.json, 图片生成/图生图/黑兽Klein 9B BFS换脸工作流_2036780449925701634.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_16

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/HL_2071329763985285121.json、图片生成/图生图/flux一分钟快速换脸工作流图片换脸人脸变换_2089571788379475970.json、图片生成/图生图/flux一分钟快速换脸工作流图片换脸人脸变换图生图_2089674597674344449.json、图片生成/图生图/ht_2076413527618838529.json、图片生成/图生图/klein9b 换头1_2033166861201842178.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `ImageConcatMulti`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageConcat`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 8/13 个有
- `Image Comparer (rgthree)` —— 8/13 个有
- `CR Prompt Text` —— 5/13 个有
- `AutoCropFaces` —— 2/13 个有
- `CR Text` —— 2/13 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 2/13 个有
- `RH_Nano_Banana2_Image2Image` —— 2/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 5 - 10 | 13 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 5 - 10，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（11/13 个样本）：Steps较低可能导致细节不足
