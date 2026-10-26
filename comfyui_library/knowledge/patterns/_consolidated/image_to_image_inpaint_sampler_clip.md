---
name: image_to_image_inpaint_sampler_clip
type: Image To Image
frequency: 28
level: strong
coverage: 0.70225
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, DownloadAndLoadFlorence2Model, EmptyFlux2LatentImage, Florence2Run, Flux2Scheduler, GetImageSize, GrowMaskWithBlur, INTConstant, Image Comparer (rgthree), ImageScaleToTotalPixels, InpaintModelConditioning, JWStringConcat, KSampler, KSamplerSelect, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, Qwen3_VQA, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX-Klein极速分镜流 _ 连贯九宫格 +快速生成+万能修复_2046845128618287106.json, 图片生成/图生图/FLUX-Klein超强分镜流 _  一致性超强九宫格 _  超强连贯性  手部修复局部重绘 林耀_2013637884384907265.json, 图片生成/图生图/FLUX-Klein超强分镜流 _  一致性超强九宫格 _  超强连贯性+超快速生成_2012959545563291649.json, 图片生成/图生图/FLUX-Klein超强分镜流 _  一致性超强九宫格 _  超强连贯性+超快速生成_2014217162184986626.json, 图片生成/图生图/FLUX-Klein超强分镜流 _  一致性超强九宫格 _  超强连贯性+超快速生成_2014331765292277761.json, 图片生成/图生图/FLUX-Klein超强分镜流 _  一致性超强九宫格 _  超强连贯性+超快速生成_2014334559835394050.json, 图片生成/图生图/FLUX-Klein超强分镜流 _  一致性超强九宫格 _  超强连贯性+超快速生成_2059979668664700929.json, 图片生成/图生图/FLUX-Klein超强分镜流 _  一致性超强九宫格_2014518931406458881.json, 图片生成/图生图/FLUX-Klein超强分镜流 _ 连贯九宫格 +超快速生成+万能修复_2046832129509691393.json, 图片生成/图生图/FLUX-Klein超强分镜流_一致性超强九宫格_2062858989511204865.json, 图片生成/图生图/FLUX-Klein超强分镜流_一致性超强九宫格_2096803300086738946.json, 图片生成/图生图/FLUX-Klein超强分镜流_一致性超强九宫格_2097147587366309890.json, 图片生成/图生图/FLUX-Klein超强分镜流：一致性超强九宫格与连贯性快速生成分镜图_2049700267888787458.json, 图片生成/图生图/FLUX-Klein超强分镜流：角色一致性超强九宫格 _ 超强连贯性快速生成分镜图_2050427161806426114.json, 图片生成/图生图/FLUX-Klein超强分镜流：角色一致性超强九宫格 _ 超强连贯性快速生成分镜图_2069014902089543682.json, 图片生成/图生图/FLUX-Klein超强分镜流：角色一致性超强九宫格 _ 超强连贯性快速生成分镜图_2082808769179897858.json, 图片生成/图生图/FLUX-Klein超强分镜流：角色一致性超强九宫格 _ 超强连贯性快速生成分镜图_2093293282632749058.json, 图片生成/图生图/FLUX-Klein超强分镜流：角色一致性超强九宫格 _ 超强连贯性快速生成分镜图_2093305986097442818.json, 图片生成/图生图/FLUX-Klein超强分镜流：角色一致性超强九宫格 _ 超强连贯性快速生成分镜图_2096912630391857154.json, 图片生成/图生图/FLUX-Klein超强分镜流：角色一致性超强九宫格 _ 超强连贯性快速生成分镜图_2096943739875979266.json, 图片生成/图生图/FLUX-Klein超强分镜流：角色一致性超强九宫格 _ 超强连贯性快速生成分镜图_2105188009359532033.json, 图片生成/图生图/FLUX-Klein超强分镜流：角色一致性超强九宫格 _ 超强连贯性快速生成分镜图_2114668542120513538.json, 图片生成/图生图/FLUX-Klein超强快速一致性分镜流 _ 局部修复_2018497463253999618.json, 图片生成/图生图/【推荐，快速分镜】FLUX-Klein超强快速一致性分镜流 _ 局部修复_2017637908546588674.json, 图片生成/图生图/快速生成-FLUX-Klein超强分镜流一致性超强九宫格_2054001341873303554.json, 图片生成/图生图/超强分镜流(一致性超强九宫格)-邻家AI大女孩_2049503706613288962.json, 图片生成/文生图/FLUX-Klein超强分镜流 一致性超强九宫格_2052922333702180866.json, 图片生成/文生图/FLUX-Klein超强分镜流 一致性超强九宫格_2054763247810686977.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_sampler_clip

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（图片生成/图生图/FLUX-Klein极速分镜流 _ 连贯九宫格 +快速生成+万能修复_2046845128618287106.json、图片生成/图生图/FLUX-Klein超强分镜流 _  一致性超强九宫格 _  超强连贯性  手部修复局部重绘 林耀_2013637884384907265.json、图片生成/图生图/FLUX-Klein超强分镜流 _  一致性超强九宫格 _  超强连贯性+超快速生成_2012959545563291649.json、图片生成/图生图/FLUX-Klein超强分镜流 _  一致性超强九宫格 _  超强连贯性+超快速生成_2014217162184986626.json、图片生成/图生图/FLUX-Klein超强分镜流 _  一致性超强九宫格 _  超强连贯性+超快速生成_2014331765292277761.json…）

- **类型**：Image To Image
- **样本数**：28
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 28 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `DownloadAndLoadFlorence2Model`
- `EmptyFlux2LatentImage`
- `Florence2Run`
- `Flux2Scheduler`
- `GetImageSize`
- `GrowMaskWithBlur`
- `INTConstant`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `InpaintModelConditioning`
- `JWStringConcat`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `Qwen3_VQA`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 27/28 个有
- `Fast Groups Bypasser (rgthree)` —— 26/28 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 28 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 28 | 100% |
| 采样算法 | euler | - | 28 | 100% |
| 调度器 | beta | - | 28 | 100% |
| 重绘幅度 | 0.3 | 0.3 - 0.3 | 28 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/28 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，28 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，28 个样本，一致性 100%
- 调度器 最常用 beta，28 个样本，一致性 100%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 0.3，28 个样本，取值集中（一致性 100%）
- 高发问题（28/28 个样本）：Steps较低可能导致细节不足
