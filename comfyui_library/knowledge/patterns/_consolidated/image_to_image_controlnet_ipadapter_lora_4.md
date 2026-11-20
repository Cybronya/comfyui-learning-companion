---
name: image_to_image_controlnet_ipadapter_lora_4
type: Image To Image
frequency: 4
level: strong
coverage: 0.8645
common_nodes: [ACN_ControlNet++LoaderSingle, AnyLineArtPreprocessor_aux, Automatic CFG, BRIA_RMBG_ModelLoader_Zho, BRIA_RMBG_Zho, EmptyImage, EmptyLatentImage, FeatheredMask, IPAdapter, IPAdapterUnifiedLoader, ImageBatch, ImageCompositeMasked, ImageResize+, KSampler, Label (rgthree), LayerUtility: ImageRemoveAlpha, LoadImage, MaskComposite, PreviewImage, PreviewMask_, RH_Captioner, SaveImage, SolidMask, Text Concatenate, VAEDecode, VAEEncode, easy cleanGpuUsed, easy controlnetLoaderADV, easy fullLoader, easy imageSize, easy kSampler, easy loraStack, easy pipeOut, easy preSampling]
problems: []
missing: []
members: [图片生成/图生图/照片转手绘插画头像_1933823240638746626.json, 平台全量/情侣合照_1851481596397318145.json, 平台全量/插画头像_1851152382355984385.json, 平台全量/插画头像_1851563028020948993.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_lora_4

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/照片转手绘插画头像_1933823240638746626.json、平台全量/情侣合照_1851481596397318145.json、平台全量/插画头像_1851152382355984385.json、平台全量/插画头像_1851563028020948993.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `ACN_ControlNet++LoaderSingle`
- `AnyLineArtPreprocessor_aux`
- `Automatic CFG`
- `BRIA_RMBG_ModelLoader_Zho`
- `BRIA_RMBG_Zho`
- `EmptyImage`
- `EmptyLatentImage`
- `FeatheredMask`
- `IPAdapter`
- `IPAdapterUnifiedLoader`
- `ImageBatch`
- `ImageCompositeMasked`
- `ImageResize+`
- `KSampler`
- `Label (rgthree)`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `MaskComposite`
- `PreviewImage`
- `PreviewMask_`
- `RH_Captioner`
- `SaveImage`
- `SolidMask`
- `Text Concatenate`
- `VAEDecode`
- `VAEEncode`
- `easy cleanGpuUsed`
- `easy controlnetLoaderADV`
- `easy fullLoader`
- `easy imageSize`
- `easy kSampler`
- `easy loraStack`
- `easy pipeOut`
- `easy preSampling`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 2/4 个有
- `easy prompt` —— 2/4 个有
- `RHHiddenNodes` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 100% |
| 调度器 | normal | - | 4 | 100% |
| 重绘幅度 | 0.36 | 0.36 - 0.36 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 100%
- 重绘幅度 中位数 0.36，观测区间 0.36 - 0.36，4 个样本，取值集中（一致性 100%）
