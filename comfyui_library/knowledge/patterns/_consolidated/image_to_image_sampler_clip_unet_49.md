---
name: image_to_image_sampler_clip_unet_49
type: Image To Image
frequency: 10
level: strong
coverage: 0.9094
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/Kontext去水印_2054793481717075969.json, "平台全量/Kontext图片修改,简单易用-中文提示词_1939283749022441474.json", 平台全量/Kontext图片去水印+高清放大（单张）_2040464320450007041.json, 平台全量/Kontext图片去水印_2038893543946719234.json, 平台全量/Kontext溶图_1986004547019649026.json, 平台全量/Kontext老照片修复（Flux kontext全自动修复）_1986388199532593154.json, 平台全量/Kontext老照片修复（Flux kontext全自动修复）_2006980341176733697.json, 平台全量/Kontext试衣间——泳装篇_1956941907341533185.json, 平台全量/最强去水印_1953706612420739074.json, 平台全量/老照片修复-Flux-Kontext图像编辑_1955498141955100674.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_49

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/Kontext去水印_2054793481717075969.json、平台全量/Kontext图片修改,简单易用-中文提示词_1939283749022441474.json、平台全量/Kontext图片去水印+高清放大（单张）_2040464320450007041.json、平台全量/Kontext图片去水印_2038893543946719234.json、平台全量/Kontext溶图_1986004547019649026.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 9/10 个有
- `FluxKontextImageScale` —— 7/10 个有
- `Image Comparer (rgthree)` —— 7/10 个有
- `LoraLoaderModelOnly` —— 5/10 个有
- `PreviewImage` —— 4/10 个有
- `ImageConcatMulti` —— 3/10 个有
- `ImageStitch` —— 3/10 个有
- `CompressImages` —— 2/10 个有
- `RepeatLatentBatch` —— 2/10 个有
- `ShowText|pysssss` —— 2/10 个有
- `Text Multiline` —— 2/10 个有
- `CR Latent Input Switch` —— 1/10 个有
- `CR SDXL Aspect Ratio` —— 1/10 个有
- `DeepTranslatorTextNode` —— 1/10 个有
- `ResizeImagesByLongerEdge` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 25 | 10 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 25，10 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
