---
name: image_to_image_lora_sampler_unet_3
type: Image To Image
frequency: 9
level: strong
coverage: 0.761333
common_nodes: [CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, WD14Tagger|pysssss, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, WD14Tagger|pysssss, PIP_图像联结]
members: [图片生成/图生图/2102092515158614017.json, 图片生成/图生图/2102249884001849345.json, 图片生成/图生图/2102291710595387394.json, 图片生成/图生图/2102444759171297281.json, 图片生成/图生图/动漫转真人 漫画转真人  线稿转真人  线稿上色 去AI感 超真实_2107023755083075585.json, 视频生成/图生视频/2068859173051396097.json, 视频生成/图生视频/动漫转真人+漫画转真人++线稿转真人++线稿上色+去AI感+超真实_2089529873101578242.json, 视频生成/图生视频/2066322228135940097.json, 视频生成/图生视频/渲染图_效果图_线稿转写实_线稿上色_2106914155080011778.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_3

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/2102092515158614017.json、图片生成/图生图/2102249884001849345.json、图片生成/图生图/2102291710595387394.json、图片生成/图生图/2102444759171297281.json、图片生成/图生图/动漫转真人 漫画转真人  线稿转真人  线稿上色 去AI感 超真实_2107023755083075585.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WD14Tagger|pysssss`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 8/9 个有
- `ConditioningZeroOut` —— 8/9 个有
- `JoinStrings` —— 8/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/9 个有
- `LayerUtility: PurgeVRAM V2` —— 8/9 个有
- `Qwen3_VQA` —— 8/9 个有
- `ShowText|pysssss` —— 8/9 个有
- `PIP_图像联结` —— 3/9 个有
- `CompressImages` —— 1/9 个有
- `EmptyImage` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `GetNode` —— 1/9 个有
- `ImageScaleBy` —— 1/9 个有
- `SeedVR2LoadDiTModel` —— 1/9 个有
- `SeedVR2LoadVAEModel` —— 1/9 个有
- `SeedVR2VideoUpscaler` —— 1/9 个有
- `SetNode` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有
- `easy clearCacheAll` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 5 - 8 | 9 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | res_2m | - | 9 | 78% |
| 调度器 | sgm_uniform | - | 9 | 78% |
| 重绘幅度 | 1 | 0.6 - 1 | 9 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 5 - 8，9 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2m，9 个样本，一致性 78%
- 调度器 最常用 sgm_uniform，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，9 个样本，取值集中（一致性 82%）
- 高发问题（19/9 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: PurgeVRAM V2、WD14Tagger|pysssss、PIP_图像联结
