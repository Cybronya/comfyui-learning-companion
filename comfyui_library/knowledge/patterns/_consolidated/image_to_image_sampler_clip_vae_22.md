---
name: image_to_image_sampler_clip_vae_22
type: Image To Image
frequency: 11
level: strong
coverage: 0.767091
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, FluxKontextImageScale, ImageStitch, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/nunchaku3.0+kontextDev超级加速_1941866485851779074.json, 平台全量/全屏格子水印去除极速去除_1947136244767973378.json, 平台全量/开源kontext万能做图流 小白友好_1939207921509048322.json, 平台全量/无痕去除水印｜无损高清_1952542390508818433.json, 平台全量/最强FLUX fill极速图像水印擦除无损文字_1940587337179099138.json, 平台全量/极速图像水印擦除无损文字_1941126768722079745.json, 平台全量/极速图像水印擦除无损文字_1944355199295082497.json, 平台全量/极速图像水印擦除无损文字_2022099199340322818.json, 平台全量/水印擦除_2016438653496594434.json, 平台全量/水印擦除无损文字_1942749566200385537.json, 平台全量/水印擦除无损文字_1942755391799234561.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_22

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（平台全量/nunchaku3.0+kontextDev超级加速_1941866485851779074.json、平台全量/全屏格子水印去除极速去除_1947136244767973378.json、平台全量/开源kontext万能做图流 小白友好_1939207921509048322.json、平台全量/无痕去除水印｜无损高清_1952542390508818433.json、平台全量/最强FLUX fill极速图像水印擦除无损文字_1940587337179099138.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImageOutput` —— 10/11 个有
- `NunchakuFluxDiTLoader` —— 10/11 个有
- `ApplyFBCacheOnModel` —— 1/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `LoraLoader` —— 1/11 个有
- `UNETLoader` —— 1/11 个有
- `easy anythingIndexSwitch` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
