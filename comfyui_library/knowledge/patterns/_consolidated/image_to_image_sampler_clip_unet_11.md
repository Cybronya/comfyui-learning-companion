---
name: image_to_image_sampler_clip_unet_11
type: Image To Image
frequency: 17
level: strong
coverage: 0.959471
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-Klein图生图_2012141948076826625.json, 图片生成/图生图/Flux2-Klein真实人像质感御姐美女_2040676390156115969.json, 图片生成/图生图/Flux2-klein单图编辑_2012160766627028993.json, 图片生成/图生图/Flux2-klein单图编辑快速改图改动作改头发改衣服动画改图修复图片30秒完成_2012164663273852929.json, 图片生成/图生图/Flux2-klein材质替换_2012507605150736386.json, 图片生成/图生图/Flux2-klein洗图真实人像质感美女_2038109616621490178.json, 图片生成/图生图/Flux2_Klein_9B印花提取V8_2104445424978452481.json, 图片生成/图生图/HL_2071329763985285121.json, 图片生成/图生图/flux一分钟快速换脸工作流图片换脸人脸变换_2089571788379475970.json, 图片生成/图生图/flux一分钟快速换脸工作流图片换脸人脸变换图生图_2089674597674344449.json, 图片生成/图生图/ht_2076413527618838529.json, 图片生成/图生图/klein9b 换头1_2033166861201842178.json, 图片生成/图生图/pipiai换脸神器_2034967727894437889.json, 图片生成/图生图/人物换脸换头-黑兽Klein 9B BFS_2036793996411936770.json, 图片生成/图生图/史上最强换脸工作流 黑兽Klein 9B BFS换脸V1 林耀3.26_2037080557837881346.json, 图片生成/图生图/土狗002_2043476116144394242.json, 图片生成/图生图/土狗0425API更新版_2046545303985201154.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_11

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein图生图_2012141948076826625.json、图片生成/图生图/Flux2-Klein真实人像质感御姐美女_2040676390156115969.json、图片生成/图生图/Flux2-klein单图编辑_2012160766627028993.json、图片生成/图生图/Flux2-klein单图编辑快速改图改动作改头发改衣服动画改图修复图片30秒完成_2012164663273852929.json、图片生成/图生图/Flux2-klein材质替换_2012507605150736386.json…）

- **类型**：Image To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 16/17 个有
- `ImageScaleToTotalPixels` —— 14/17 个有
- `ReferenceLatent` —— 14/17 个有
- `EmptyFlux2LatentImage` —— 11/17 个有
- `GetImageSize` —— 11/17 个有
- `ImageConcatMulti` —— 10/17 个有
- `LayerUtility: PurgeVRAM V2` —— 10/17 个有
- `easy imageConcat` —— 10/17 个有
- `Image Comparer (rgthree)` —— 9/17 个有
- `AddLabel` —— 8/17 个有
- `LoraLoader` —— 4/17 个有
- `PIP_图像联结` —— 3/17 个有
- `scale` —— 3/17 个有
- `AutoCropFaces` —— 2/17 个有
- `CR Prompt Text` —— 2/17 个有
- `CR Text` —— 2/17 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 2/17 个有
- `RH_Nano_Banana2_Image2Image` —— 2/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 10 | 17 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 17 | 100% |
| 采样算法 | euler | - | 17 | 100% |
| 调度器 | simple | - | 17 | 82% |
| 重绘幅度 | 1 | 0.3 - 1 | 17 | 70% |
| LoRA 模型强度 | 0.8 | 0.8 - 1 | 4 | 90% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 10，17 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，17 个样本，一致性 100%
- 调度器 最常用 simple，17 个样本，一致性 82%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，17 个样本
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 1，4 个样本，取值集中（一致性 90%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（15/17 个样本）：Steps较低可能导致细节不足
