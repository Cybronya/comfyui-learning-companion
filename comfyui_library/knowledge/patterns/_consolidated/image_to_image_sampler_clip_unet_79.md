---
name: image_to_image_sampler_clip_unet_79
type: Image To Image
frequency: 6
level: strong
coverage: 0.811
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux_kontext_example-官方工作流_1938480873924943873.json, 图片生成/图生图/flux_kontext_官方工作流 多图_1938482540896256001.json, 图片生成/图生图/flux_kontext_照片转换素描_1948621429297283073.json, 图片生成/图生图/flux_kontext_综合-场景集合 (1)_1982460983069286402.json, 图片生成/图生图/kontext 正面转反面_1942431853267595265.json, 图片生成/图生图/kontext_手绘情侣头像星蝶少女头像一键真人转手绘_2029009784497770498.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_79

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/flux_kontext_example-官方工作流_1938480873924943873.json、图片生成/图生图/flux_kontext_官方工作流 多图_1938482540896256001.json、图片生成/图生图/flux_kontext_照片转换素描_1948621429297283073.json、图片生成/图生图/flux_kontext_综合-场景集合 (1)_1982460983069286402.json、图片生成/图生图/kontext 正面转反面_1942431853267595265.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
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
- `FluxKontextImageScale` —— 5/6 个有
- `ReferenceLatent` —— 5/6 个有
- `EmptySD3LatentImage` —— 4/6 个有
- `ImageConcanate` —— 3/6 个有
- `ImageScaleBy` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `Anything Everywhere3` —— 1/6 个有
- `ConditioningZeroOut` —— 1/6 个有
- `GoogleTranslateTextNode` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `Preview from image [Crystools]` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `easy seed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 6 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，6 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
