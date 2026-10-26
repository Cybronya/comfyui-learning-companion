---
name: image_to_image_lora_sampler_clip_25
type: Image To Image
frequency: 9
level: strong
coverage: 0.925444
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/产品修图-布料去褶皱_1961638865234759682.json, 图片生成/图生图/产品修图-布料去褶皱_2088506778806996994.json, 图片生成/图生图/产品精修工作流 一键出图细节文字保留_1956371792107634690.json, 图片生成/图生图/产品融入背景v4 真实光影_1957824102613745665.json, 图片生成/图生图/人像光影融合-MAGIC-K-V1_2096507439083511809.json, 图片生成/图生图/人像光影融合-MAGIC-K-V1_2096864329248362497.json, 图片生成/图生图/人像精修_2076044034824564738.json, 图片生成/图生图/人像精修工作流_2048591215414747137.json, 图片生成/图生图/星蝶风格一键转换_1991833267762688001.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_25

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/产品修图-布料去褶皱_1961638865234759682.json、图片生成/图生图/产品修图-布料去褶皱_2088506778806996994.json、图片生成/图生图/产品精修工作流 一键出图细节文字保留_1956371792107634690.json、图片生成/图生图/产品融入背景v4 真实光影_1957824102613745665.json、图片生成/图生图/人像光影融合-MAGIC-K-V1_2096507439083511809.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 5/9 个有
- `RepeatLatentBatch` —— 3/9 个有
- `easy imageScaleDownToSize` —— 3/9 个有
- `DetailTransfer` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `ImageCASharpening+` —— 2/9 个有
- `ImageConcatMulti` —— 2/9 个有
- `ImageResize+` —— 2/9 个有
- `InspyrenetRembg` —— 2/9 个有
- `easy cleanGpuUsed` —— 2/9 个有
- `easy positive` —— 2/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 9 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，9 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
