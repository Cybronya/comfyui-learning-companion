---
name: image_to_image_sampler_clip_unet_36
type: Image To Image
frequency: 11
level: strong
coverage: 0.903818
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX-kontext-产品精修_1950600662713307138.json, 图片生成/图生图/FLUX-kontext-产品精修_1953099483317997569.json, 图片生成/图生图/Flux-kontext溶图_2108481679651328001.json, 图片生成/图生图/Flux-kontext溶图打光｜1536与2048两种尺寸直出_2114721487092535298.json, 图片生成/图生图/Kontext dev 动漫转真人 减少模型欧美人物影响_1943510897216135169.json, 图片生成/图生图/Kontext 人像精修工作流_2091472960262598658.json, 图片生成/图生图/Kontext_人像精修工作流_2099054173085069313.json, 图片生成/图生图/Kontext_人像精修工作流_2099659188644433921.json, 图片生成/图生图/Kontext超强动漫转真人_1956571286262697986.json, 平台全量/箱包_鞋类产品精修，kontext工业渲染级别质感_2007699136056926210.json, 平台全量/质感还原 箱包_鞋类产品精修，服装 箱包 鞋除皱精修 产品精修 去除褶皱背包修图 kontext工业_2009820910844387330.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_36

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/FLUX-kontext-产品精修_1950600662713307138.json、图片生成/图生图/FLUX-kontext-产品精修_1953099483317997569.json、图片生成/图生图/Flux-kontext溶图_2108481679651328001.json、图片生成/图生图/Flux-kontext溶图打光｜1536与2048两种尺寸直出_2114721487092535298.json、图片生成/图生图/Kontext dev 动漫转真人 减少模型欧美人物影响_1943510897216135169.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 9/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/11 个有
- `Image Comparer (rgthree)` —— 8/11 个有
- `LoraLoader` —— 6/11 个有
- `easy hiresFix` —— 5/11 个有
- `PreviewImage` —— 3/11 个有
- `easy imageConcat` —— 3/11 个有
- `easy int` —— 3/11 个有
- `Anything Everywhere` —— 2/11 个有
- `FluxKontextImageScale` —— 2/11 个有
- `ImageStitch` —— 2/11 个有
- `RHHiddenNodes` —— 2/11 个有
- `Checkpoint Loader (Simple)` —— 1/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/11 个有
- `LoraLoaderModelOnly` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 12 - 30 | 11 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| LoRA 模型强度 | 1 | 0.82 - 1 | 6 | 91% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 12 - 30，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0.82 - 1，6 个样本，取值集中（一致性 91%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
