---
name: image_to_image_lora_sampler_clip_9
type: Image To Image
frequency: 15
level: strong
coverage: 0.9576
common_nodes: [CLIPTextEncode, DualCLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX.1图生图工作流_2088546573432217602.json, 图片生成/图生图/Flex.2-preview-图生图_1917082177446809601.json, 图片生成/图生图/Flux.1基础图生图工作流_2100839312702132226.json, 图片生成/图生图/Kontext  模特服装展示｜试穿_1942401666282893314.json, 图片生成/图生图/Kontext [dev] 多图融合｜多物体融合_1939513365821833217.json, 图片生成/图生图/Kontext dev 人物衣服试穿｜虚拟试穿_1939656115514679298.json, 图片生成/图生图/Kontext-一键转画风_1948255124436201474.json, 图片生成/图生图/Kontext-图片精修_1960220426934890498.json, 图片生成/图生图/Kontext-静物图提取lora_1960182192410406913.json, 图片生成/图生图/Kontext人像摄影 _ 一键更换战国袍_1953338187823370241.json, 图片生成/图生图/Kontext图像编辑工作流_1986390332885630978.json, 图片生成/图生图/PS高阶-光影优化V2_1963143771179429889.json, 图片生成/图生图/kontext一句话编辑_2009592730074222594.json, 图片生成/图生图/kontext老照片修复工作流_2079953891206189058.json, 图片生成/图生图/星蝶风格一键转换_1991833267762688001.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_9

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/FLUX.1图生图工作流_2088546573432217602.json、图片生成/图生图/Flex.2-preview-图生图_1917082177446809601.json、图片生成/图生图/Flux.1基础图生图工作流_2100839312702132226.json、图片生成/图生图/Kontext  模特服装展示｜试穿_1942401666282893314.json、图片生成/图生图/Kontext [dev] 多图融合｜多物体融合_1939513365821833217.json…）

- **类型**：Image To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 14/15 个有
- `ConditioningZeroOut` —— 12/15 个有
- `ReferenceLatent` —— 12/15 个有
- `Image Comparer (rgthree)` —— 9/15 个有
- `FluxKontextImageScale` —— 8/15 个有
- `ImageConcatMulti` —— 7/15 个有
- `easy imageScaleDownToSize` —— 7/15 个有
- `EmptySD3LatentImage` —— 5/15 个有
- `RepeatLatentBatch` —— 4/15 个有
- `ImageScaleToTotalPixels` —— 3/15 个有
- `easy imageSize` —— 3/15 个有
- `ImageResizeKJ` —— 2/15 个有
- `ImageScale` —— 2/15 个有
- `Flex2Conditioner` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 15 | 85% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 93% |
| 调度器 | simple | - | 15 | 93% |
| 重绘幅度 | 1 | 0.5 - 1 | 15 | 81% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，15 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 93%
- 调度器 最常用 simple，15 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，15 个样本，取值集中（一致性 81%）
