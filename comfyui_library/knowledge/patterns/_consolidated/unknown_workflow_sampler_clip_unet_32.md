---
name: unknown_workflow_sampler_clip_unet_32
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.916
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, ImageSharpen, KSamplerAdvanced, KSamplerSelect, ModelSamplingAuraFlow, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/krea 2 and flux klein__文生图_2100042090527940610.json, 图片生成/文生图/Hyperrealistic_ Z-image + Flux klein_2017132941884788737.json, 图片生成/文生图/Z-image-base-邪修双采+高清放大_2016379330103873538.json, 图片生成/文生图/Z-image-base-邪修双采+高清放大_2018103457047126018.json, 图片生成/文生图/krea_2_and_flux_klein_文生图_2101080842247426049.json, 图片生成/文生图/z-iamge多功能生图工作流_2050156379784138753.json, 图片生成/文生图/z-images 文生图 高质量版_2028826690939527170.json, 图片生成/文生图/万能图像生成器 - 直出4K.6K.8K图_2029090503827922945.json, 图片生成/文生图/万能图像生成器 Z-image 三阶采样 多样性超写实 文生图 万能图像生成器一键直出4K大图_2051105971912622082.json, 图片生成/文生图/万能图像生成器 一键直出4K_2040718467866828802.json, 图片生成/文生图/万能图像生成器-直出4K_2055990233665155073.json, 图片生成/文生图/万能图像生成器-邻家AI大女孩_2042230797427544066.json, 图片生成/文生图/万能图像生成器_2028113030734680066.json, 图片生成/文生图/万能图像生成器_2041868257631670273.json, 图片生成/文生图/万能图像生成器_2053646155682201602.json, 图片生成/文生图/万能图像生成器（z-image+Flux2-klein+自动化提示词）_2034136038548967425.json, 图片生成/文生图/万能文生图—阿浩_2039866907611893761.json, 图片生成/文生图/人物生成_2033068431771176961.json, 图片生成/文生图/什么都能生的万能图像生成器_2044715424964677634.json, 图片生成/文生图/文生图图像生成器_2036011868971601922.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_32

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/krea 2 and flux klein__文生图_2100042090527940610.json、图片生成/文生图/Hyperrealistic_ Z-image + Flux klein_2017132941884788737.json、图片生成/文生图/Z-image-base-邪修双采+高清放大_2016379330103873538.json、图片生成/文生图/Z-image-base-邪修双采+高清放大_2018103457047126018.json、图片生成/文生图/krea_2_and_flux_klein_文生图_2101080842247426049.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 20 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageSharpen`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `ModelSamplingAuraFlow`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 19/20 个有
- `Image Comparer (rgthree)` —— 19/20 个有
- `ImageScaleToTotalPixels` —— 19/20 个有
- `LoraLoaderModelOnly` —— 19/20 个有
- `PreviewImage` —— 18/20 个有
- `CR Text` —— 17/20 个有
- `SeedVR2LoadDiTModel` —— 17/20 个有
- `SeedVR2LoadVAEModel` —— 17/20 个有
- `SeedVR2VideoUpscaler` —— 17/20 个有
- `LayerUtility: PurgeVRAM V2` —— 16/20 个有
- `INTConstant` —— 15/20 个有
- `Int` —— 14/20 个有
- `Label (rgthree)` —— 11/20 个有
- `CLIPLoaderGGUF` —— 7/20 个有
- `Fast Groups Bypasser (rgthree)` —— 7/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/20 个有
- `BasicScheduler` —— 2/20 个有
- `DetailDaemonSamplerNode` —— 2/20 个有
- `FaceDetailer` —— 2/20 个有
- `SAMLoader` —— 2/20 个有
- `SamplerCustom` —— 2/20 个有
- `UltralyticsDetectorProvider` —— 2/20 个有
- `DuckHideNode` —— 1/20 个有
- `EmptyImage` —— 1/20 个有
- `EmptySD3LatentImage` —— 1/20 个有
- `GetNode` —— 1/20 个有
- `LoadImage` —— 1/20 个有
- `MemoryCleaner` —— 1/20 个有
- `RH_LLMAPI_NODE` —— 1/20 个有
- `SetNode` —— 1/20 个有
- `ShowText|pysssss` —— 1/20 个有
- `TTResolutionSelector` —— 1/20 个有
- `easy cleanGpuUsed` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 20 | 100% |
| Prompt 约束强度(CFG) | 3 | 1.15 - 12 | 20 | 37% |
| 采样算法 | 1 | 1 - 2 | 20 | 73% |
| 调度器 | euler | - | 20 | 85% |
| 重绘幅度 | simple | - | 20 | 85% |
| 宽度 | 1024 | 1024 - 2816 | 19 | 55% |
| 高度 | 1536 | 1536 - 1536 | 19 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，20 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 3，观测区间 1.15 - 12，20 个样本，取值分散，一致性仅 37%
- 采样算法 中位数 1，观测区间 1 - 2，20 个样本
- 调度器 最常用 euler，20 个样本，一致性 85%
- 重绘幅度 最常用 simple，20 个样本，一致性 85%
- 宽度 中位数 1024，观测区间 1024 - 2816，19 个样本
- 高度 中位数 1536，观测区间 1536 - 1536，19 个样本，取值集中（一致性 100%）
