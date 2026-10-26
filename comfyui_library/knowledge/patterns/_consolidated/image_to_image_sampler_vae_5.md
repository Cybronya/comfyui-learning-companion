---
name: image_to_image_sampler_vae_5
type: Image To Image
frequency: 19
level: strong
coverage: 0.918684
common_nodes: [CFGNorm, FluxKontextMultiReferenceLatentMethod, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人像摄影-可视化调整镜头角度焦距-9个操作面板_2010127457524916226.json, 图片生成/图生图/千问2511镜头多角度转换可输入额外提示词_2010224578517278721.json, 图片生成/图生图/千问edit2511可视化调整镜头角度（9个操作面板-zip打包下载）_2009846105042849794.json, 图片生成/图生图/千问edit2511多角度转换（批量提示词）_2009254825124438017.json, 图片生成/图生图/千问edit2511镜头角度转换_2082369715707666433.json, 图片生成/图生图/千问edit2511镜头角度转换_2083451577360281602.json, 图片生成/图生图/千问edit2511镜头角度转换可视化操作_2009839001498296321.json, 图片生成/图生图/多角度控制拍摄_2010308549825536001.json, 图片生成/图生图/多角度摄像控制（96种机位选择）+直观便捷操作_2009893150126514178.json, 图片生成/图生图/多角度摄像控制（96种机位选择）+直观便捷操作_2011827730614067202.json, 图片生成/图生图/多角度摄像控制（96种机位选择）+直观便捷操作_2036733513197690881.json, 图片生成/图生图/多角度摄像控制（96种机位选择）+直观便捷操作_2055634329270792194.json, 图片生成/图生图/镜头可视化自由视角_2061269943475331073.json, 图片生成/图生图/镜头可视化自由视角_2061611687635144706.json, 图片生成/图生图/🦖Qwen2511一键多角度_2010558215834046465.json, 图片生成/文生图/2511多角度可视化控制_2009448935689035777.json, 图片生成/文生图/一键多角度摄像控制（96种机位选择）+直观便捷操作 V1.0_2011111925689618434.json, 图片生成/文生图/多角度摄像控制（96种机位选择）+直观便捷操作_2036073760159174657.json, 数字人/数字人/多角度摄像控制（96种机位选择）+直观便捷操作_2056928106224644097.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_5

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/人像摄影-可视化调整镜头角度焦距-9个操作面板_2010127457524916226.json、图片生成/图生图/千问2511镜头多角度转换可输入额外提示词_2010224578517278721.json、图片生成/图生图/千问edit2511可视化调整镜头角度（9个操作面板-zip打包下载）_2009846105042849794.json、图片生成/图生图/千问edit2511多角度转换（批量提示词）_2009254825124438017.json、图片生成/图生图/千问edit2511镜头角度转换_2082369715707666433.json…）

- **类型**：Image To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 19 个 workflow 都包含：
- `CFGNorm`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 18/19 个有
- `LoraLoaderModelOnly` —— 18/19 个有
- `QwenMultiangleCameraNode` —— 18/19 个有
- `UNETLoader` —— 18/19 个有
- `VAELoader` —— 18/19 个有
- `Text Concatenate` —— 12/19 个有
- `KepStringList` —— 9/19 个有
- `PrimitiveInt` —— 9/19 个有
- `PromptBatchQueue` —— 9/19 个有
- `easy string` —— 9/19 个有
- `CR Text` —— 5/19 个有
- `Fast Groups Bypasser (rgthree)` —— 4/19 个有
- `CR Text Concatenate` —— 2/19 个有
- `HAIGC_SaveImagesToZip` —— 2/19 个有
- `EmptySD3LatentImage` —— 1/19 个有
- `RHHiddenNodes` —— 1/19 个有
- `RH_Nano_Banana2_Image2Image` —— 1/19 个有
- `SeedVR2` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 19 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 19 | 100% |
| 采样算法 | euler | - | 19 | 100% |
| 调度器 | simple | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，19 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，19 个样本，一致性 100%
- 调度器 最常用 simple，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（19/19 个样本）：Steps较低可能导致细节不足
