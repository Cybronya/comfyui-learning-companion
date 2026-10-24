---
name: image_to_image_lora_sampler_unet_24
type: Image To Image
frequency: 16
level: strong
coverage: 0.76175
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveStringMultiline, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWEN快速换装秒出图_1985441625268699137.json, 图片生成/图生图/Qwen Edit 2511 多图编辑版_1970485438093946882.json, 图片生成/图生图/Qwen去水印+高清处理_2011600241761456129.json, 图片生成/图生图/一键去水印高清修复版千问qwen图片编辑2509快速去水印图片去水印加速版_2061066797192933377.json, 图片生成/图生图/一键图片去水印加高清修复_1999007653064007682.json, 图片生成/图生图/人物动作迁移 保持一致性 Qwen-edit多图编辑_1973243474298449922.json, 图片生成/图生图/人物动作迁移_2004095655121436673.json, 图片生成/图生图/人物换衣服_2095498989033578497.json, 图片生成/图生图/人物换衣服加速版qwen edit plus+全节点注释_2055626898692157442.json, 图片生成/图生图/人物换衣服加速版qwen+edit+plus+全节点注释_2060616197187657729.json, 图片生成/图生图/去水印  高清修复_1989266952667492353.json, 图片生成/图生图/去水印  高清修复_2007447402684358657.json, 图片生成/图生图/衣服提取提取衣服（加速版）qweneditplus_1971448005004083201.json, 图片生成/图生图/衣服提取提取衣服（加速版）qweneditplus_2041345450657193986.json, 图片生成/文生图/人物换衣服加速版qwen edit plus+全节点注释_2055669100139040769.json, 图片生成/文生图/千问 手办盲盒超火模型_1993973079732846594.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_24

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/QWEN快速换装秒出图_1985441625268699137.json、图片生成/图生图/Qwen Edit 2511 多图编辑版_1970485438093946882.json、图片生成/图生图/Qwen去水印+高清处理_2011600241761456129.json、图片生成/图生图/一键去水印高清修复版千问qwen图片编辑2509快速去水印图片去水印加速版_2061066797192933377.json、图片生成/图生图/一键图片去水印加高清修复_1999007653064007682.json…）

- **类型**：Image To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 16 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PrimitiveStringMultiline`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 15/16 个有
- `CR Simple Image Compare` —— 13/16 个有
- `easy imageConcat` —— 7/16 个有
- `DWPreprocessor` —— 3/16 个有
- `PreviewImage` —— 2/16 个有
- `Any Switch (rgthree)` —— 1/16 个有
- `EmptyLatentImage` —— 1/16 个有
- `Fast Groups Muter (rgthree)` —— 1/16 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/16 个有
- `easy imageSizeByLongerSide` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 16 | 100% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 960 | - | 1 | 100% |
| 高度 | 1280 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（18/16 个样本）：Steps较低可能导致细节不足
