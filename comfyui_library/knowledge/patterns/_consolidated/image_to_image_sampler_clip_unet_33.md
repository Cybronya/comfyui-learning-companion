---
name: image_to_image_sampler_clip_unet_33
type: Image To Image
frequency: 10
level: strong
coverage: 0.8859
common_nodes: [CLIPTextEncode, DualCLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX.1图生图工作流_2088546573432217602.json, 图片生成/图生图/Flex.2-preview-图生图_1917082177446809601.json, 图片生成/图生图/Flux.1基础图生图工作流_2100839312702132226.json, 图片生成/图生图/flux_kontext_example-官方工作流_1938480873924943873.json, 图片生成/图生图/flux_kontext_照片转换素描_1948621429297283073.json, 图片生成/图生图/flux_kontext_综合-场景集合 (1)_1982460983069286402.json, 图片生成/图生图/产品精修-金属类_1951522356852371458.json, 图片生成/图生图/手办模型_1961814911435345921.json, 图片生成/图生图/手办模型盲盒_2047665313591857154.json, 图片生成/图生图/手办模型盲盒_2063493693570633730.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_33

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/FLUX.1图生图工作流_2088546573432217602.json、图片生成/图生图/Flex.2-preview-图生图_1917082177446809601.json、图片生成/图生图/Flux.1基础图生图工作流_2100839312702132226.json、图片生成/图生图/flux_kontext_example-官方工作流_1938480873924943873.json、图片生成/图生图/flux_kontext_照片转换素描_1948621429297283073.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 9/10 个有
- `LoraLoaderModelOnly` —— 8/10 个有
- `FluxKontextImageScale` —— 7/10 个有
- `ReferenceLatent` —— 7/10 个有
- `CR Text` —— 5/10 个有
- `EmptySD3LatentImage` —— 5/10 个有
- `ConstrainImage|pysssss` —— 4/10 个有
- `Image Comparer (rgthree)` —— 4/10 个有
- `ImageScaleBy` —— 3/10 个有
- `ImageScale` —— 2/10 个有
- `Flex2Conditioner` —— 1/10 个有
- `ImageResizeKJ` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 10 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 90% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 0.5 - 1 | 10 | 77% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，10 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 90%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，10 个样本
