---
name: image_to_image_lora_sampler_unet_139
type: Image To Image
frequency: 6
level: strong
coverage: 0.894667
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Qwen Image Edit 2511-（换脸）_2015328747402043393.json, 平台全量/Qwen-Edit-2511-单图编辑_2003622402825306114.json, 平台全量/Qwen_Edit_2511_单图编辑零偏移&照片修复工作流_2049743253100085249.json, 平台全量/图像处理-去除水印_2112730068043788290.json, 平台全量/图片去水印-通用版_2020393131711143938.json, 平台全量/测试是否在画布中能用_2066725896819666946.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_139

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/Qwen Image Edit 2511-（换脸）_2015328747402043393.json、平台全量/Qwen-Edit-2511-单图编辑_2003622402825306114.json、平台全量/Qwen_Edit_2511_单图编辑零偏移&照片修复工作流_2049743253100085249.json、平台全量/图像处理-去除水印_2112730068043788290.json、平台全量/图片去水印-通用版_2020393131711143938.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 5/6 个有
- `Image Comparer (rgthree)` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `FluxKontextImageScale` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `AutoCropFaces` —— 1/6 个有
- `CR Text` —— 1/6 个有
- `EmptySD3LatentImage` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `LayerUtility: TextJoin` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `Text` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4.5 | 4 - 8 | 6 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4.5，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
