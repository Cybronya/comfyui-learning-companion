---
name: text_to_image_sampler_clip_unet_137
type: Text To Image
frequency: 6
level: strong
coverage: 0.865833
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/kontext_全能溶图打光 电商产品换背景_1952273907631992834.json, 平台全量/kontext图案提取_1960614247652818946.json, 平台全量/kontext换发型lora加强发型迁移_1942790109421088769.json, 平台全量/服装生成模特kontext_1950769253811183618.json, 平台全量/服装面料材质印花提取(Flux-Kontext)_2000503320991105025.json, 平台全量/模特换装 kontext_1950770847344676865.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_137

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/kontext_全能溶图打光 电商产品换背景_1952273907631992834.json、平台全量/kontext图案提取_1960614247652818946.json、平台全量/kontext换发型lora加强发型迁移_1942790109421088769.json、平台全量/服装生成模特kontext_1950769253811183618.json、平台全量/服装面料材质印花提取(Flux-Kontext)_2000503320991105025.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
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
- `FluxKontextImageScale` —— 4/6 个有
- `ImageStitch` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `PreviewImage` —— 2/6 个有
- `RH_Translator` —— 2/6 个有
- `easy imageScaleDownToSize` —— 2/6 个有
- `ACE_TextGoogleTranslate` —— 1/6 个有
- `CR Text` —— 1/6 个有
- `GetImageSize+` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 6 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 800 | 720 - 1024 | 6 | 85% |
| 高度 | 1264 | 1024 - 1536 | 6 | 86% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，6 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 800，观测区间 720 - 1024，6 个样本，取值集中（一致性 85%）
- 高度 中位数 1264，观测区间 1024 - 1536，6 个样本，取值集中（一致性 86%）
