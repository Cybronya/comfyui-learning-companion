---
name: image_to_image_lora_sampler_unet_19
type: Image To Image
frequency: 20
level: strong
coverage: 0.9727
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键多角度一致性_1986711907254087682.json, 图片生成/图生图/一键完美图片去水印TextEncode QwenlmageEdit2511_1988876685514772482.json, 图片生成/图生图/一键换衣千问qwen2511最新图像编辑换装千问2511_2034603108478754818.json, 图片生成/图生图/一键换装工作流，无需遮罩_2096447517775978497.json, 图片生成/图生图/一键美瞳_2009605418158399489.json, 图片生成/图生图/人物替换2.0影视二创换人qwen2511最新图像编辑换装千问2511追赶+全能图片V1_2005243921284431874.json, 图片生成/图生图/人物电商万物换背景优化版本qwen2511_2066095762181808129.json, 图片生成/图生图/千问2511三图编辑_2004810240099053569.json, 图片生成/图生图/千问2511双图编辑_2004808317312663553.json, 图片生成/图生图/去水印qwen2511图像编辑_2085425004350631937.json, 图片生成/图生图/去水印qwen2511最新图像编辑_2046215955486871553.json, 图片生成/图生图/去水印qwen2511最新图像编辑_2077306954288029698.json, 图片生成/图生图/去水印qwen2511最新图像编辑_2116398640972521474.json, 图片生成/图生图/去水印qwen2511最新图像编辑换装千问2511追赶+全能图片V1(2)_2004758081252847618.json, 图片生成/图生图/去水印qwen2511最新图像编辑换装千问2511追赶+全能图片V1_2053656485862887425.json, 图片生成/图生图/图片去水印-Qwen2511-无角标出图_2079924667032363010.json, 图片生成/图生图/图片去水印_2038881204849610753.json, 平台全量/去水印+换装换脸多图编辑高清修复  QwenEdit最新图像编辑换装全能图片2.0_2038774886381920258.json, 平台全量/多图编辑 去水印+换装换脸高清修复 QwenEdit最新图像编辑换装全能图片2.0_2039222441611894786.json, 平台全量/换头换脸换装+去水印 双图编辑 Qwen2511最新图像编辑换装千问2511全能图片_2053639223097479170.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_19

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/一键多角度一致性_1986711907254087682.json、图片生成/图生图/一键完美图片去水印TextEncode QwenlmageEdit2511_1988876685514772482.json、图片生成/图生图/一键换衣千问qwen2511最新图像编辑换装千问2511_2034603108478754818.json、图片生成/图生图/一键换装工作流，无需遮罩_2096447517775978497.json、图片生成/图生图/一键美瞳_2009605418158399489.json…）

- **类型**：Image To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 20 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
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
- `FluxKontextMultiReferenceLatentMethod` —— 19/20 个有
- `CR Text` —— 18/20 个有
- `ImageConcanate` —— 16/20 个有
- `Fast Groups Bypasser (rgthree)` —— 4/20 个有
- `CustomAddLabel` —— 1/20 个有
- `GetImageSize` —— 1/20 个有
- `ImageScale` —— 1/20 个有
- `JDCN_StringToList` —— 1/20 个有
- `PreviewImage` —— 1/20 个有
- `PrimitiveStringMultiline` —— 1/20 个有
- `easy imageSize` —— 1/20 个有
- `easy seed` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 20 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 20 | 100% |
| 采样算法 | euler | - | 20 | 100% |
| 调度器 | simple | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，20 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，20 个样本，一致性 100%
- 调度器 最常用 simple，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（20/20 个样本）：Steps较低可能导致细节不足
