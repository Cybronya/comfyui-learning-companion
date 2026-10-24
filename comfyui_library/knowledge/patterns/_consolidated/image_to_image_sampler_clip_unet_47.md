---
name: image_to_image_sampler_clip_unet_47
type: Image To Image
frequency: 8
level: strong
coverage: 0.950625
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/FLUX2 Klein 多图编辑、多图融合工作流_2052361394179321858.json, 图片生成/图生图/FLUX2 Klein 多图编辑、多图融合工作流教学版（内含教程）_2020116611205701634.json, 图片生成/图生图/FLUX2-Klein单图、多图编辑工作流_2068602290797375490.json, 图片生成/图生图/Flux 2 Klein 9B Edit_2063304186351149058.json, 图片生成/图生图/Flux Klein 多图编辑工作流 可多图融合_2018923003224002561.json, 图片生成/图生图/Flux-2-klein-图片编辑（三图）_2081417532673712130.json, 图片生成/图生图/▶flux-2-klein-多图编辑本地调用API_2016187646481010689.json, 图片生成/图生图/电商主图----G-image-2+提示词优化_2069956426201657346.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_47

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/FLUX2 Klein 多图编辑、多图融合工作流_2052361394179321858.json、图片生成/图生图/FLUX2 Klein 多图编辑、多图融合工作流教学版（内含教程）_2020116611205701634.json、图片生成/图生图/FLUX2-Klein单图、多图编辑工作流_2068602290797375490.json、图片生成/图生图/Flux 2 Klein 9B Edit_2063304186351149058.json、图片生成/图生图/Flux Klein 多图编辑工作流 可多图融合_2018923003224002561.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 7/8 个有
- `EmptyFlux2LatentImage` —— 6/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/8 个有
- `ConditioningZeroOut` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `ImageScaleToTotalPixels` —— 4/8 个有
- `EmptySD3LatentImage` —— 3/8 个有
- `GetImageSize` —— 3/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `CR Prompt Text` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `CLIPLoaderGGUF` —— 1/8 个有
- `Float` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `RHImg2ImgPromptOptimizer` —— 1/8 个有
- `RH_RhartImageG2ImageToImage` —— 1/8 个有
- `SaveLatent` —— 1/8 个有
- `UnetLoaderGGUF` —— 1/8 个有
- `ZhangyuAPITextListEditor` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 8 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/8 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（11/8 个样本）：Steps较低可能导致细节不足
