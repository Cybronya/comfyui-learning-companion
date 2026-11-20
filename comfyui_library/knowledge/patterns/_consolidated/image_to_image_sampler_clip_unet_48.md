---
name: image_to_image_sampler_clip_unet_48
type: Image To Image
frequency: 10
level: strong
coverage: 0.8724
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux_kontext_官方工作流 多图_1938482540896256001.json, 图片生成/图生图/kontext_手绘情侣头像星蝶少女头像一键真人转手绘_2029009784497770498.json, 图片生成/图生图/kontext灰度图工作流_1963233328004575234.json, 图片生成/图生图/产品_人像精修_2071792524552921090.json, 图片生成/图生图/产品精修工作流 一键出图细节文字保留_1956371792107634690.json, 图片生成/图生图/产品融入背景v4 真实光影_1957824102613745665.json, 图片生成/图生图/人像精修+上妆-kontxet_1959201923981324289.json, 图片生成/图生图/冰爷老杨简单溶图-提前PS（省钱版）_1966078677220061185.json, 平台全量/01、Kontext 光影融合（透视矫正）_1997553768847851522.json, 平台全量/冰爷老杨溶图加透视纠正-省钱版_1995004577969844226.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_48

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/flux_kontext_官方工作流 多图_1938482540896256001.json、图片生成/图生图/kontext_手绘情侣头像星蝶少女头像一键真人转手绘_2029009784497770498.json、图片生成/图生图/kontext灰度图工作流_1963233328004575234.json、图片生成/图生图/产品_人像精修_2071792524552921090.json、图片生成/图生图/产品精修工作流 一键出图细节文字保留_1956371792107634690.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 9/10 个有
- `ReferenceLatent` —— 9/10 个有
- `Image Comparer (rgthree)` —— 8/10 个有
- `ConditioningZeroOut` —— 7/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/10 个有
- `FluxKontextImageScale` —— 5/10 个有
- `PreviewImage` —— 5/10 个有
- `DetailTransfer` —— 4/10 个有
- `Seed (rgthree)` —— 3/10 个有
- `Text Concatenate` —— 3/10 个有
- `Text Multiline` —— 3/10 个有
- `easy cleanGpuUsed` —— 3/10 个有
- `ImageConcanate` —— 2/10 个有
- `EmptySD3LatentImage` —— 1/10 个有
- `GoogleTranslateTextNode` —— 1/10 个有
- `ImageResizeKJv2` —— 1/10 个有
- `Preview from image [Crystools]` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 10 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 70% |
| 调度器 | simple | - | 10 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，10 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 70%
- 调度器 最常用 simple，10 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
