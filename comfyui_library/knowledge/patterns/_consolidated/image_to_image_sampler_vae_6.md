---
name: image_to_image_sampler_vae_6
type: Image To Image
frequency: 18
level: weak
coverage: 0.835111
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen千问多图编辑4步_双节棍nunchaku加速版本_1971470726085722113.json, 图片生成/图生图/qwen千问多图编辑4步_双节棍nunchaku加速版本_1977867242929016833.json, 图片生成/图生图/【遇见AI】Qwen-image-edit 图生图基础_2051187067786407937.json, 图片生成/图生图/一致性去水印_1992437141525385218.json, 图片生成/图生图/一键去水印高清修复版千问qwen图片编辑2509快速去水印图片去水印加速版_2061066797192933377.json, 图片生成/图生图/一键图片去水印加高清修复_1999007653064007682.json, 图片生成/图生图/一键生成人物不同姿态_1987670680714022914.json, 图片生成/图生图/一键生成人物穿搭_1991670602532659201.json, 图片生成/图生图/去水印  高清修复_1989266952667492353.json, 图片生成/图生图/去水印  高清修复_2007447402684358657.json, 图片生成/图生图/去水印+高清修复Qwen_1984580964695293954.json, 图片生成/图生图/去水印_qwen_1989895318252736513.json, 图片生成/图生图/去水印加高清修复_qwen_1959592150470176770.json, 图片生成/图生图/去水印加高清修复_qwen_1992628418007158786.json, 图片生成/图生图/去水印加高清修复_qwen_2019294380909142017.json, 图片生成/图生图/衣服提取提取衣服（加速版）qweneditplus_1971448005004083201.json, 图片生成/图生图/衣服提取提取衣服（加速版）qweneditplus_2041345450657193986.json, 图片生成/图生图/👾怪獸-千问多图编辑8步版👾_1977240342351237121.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_6

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/qwen千问多图编辑4步_双节棍nunchaku加速版本_1971470726085722113.json、图片生成/图生图/qwen千问多图编辑4步_双节棍nunchaku加速版本_1977867242929016833.json、图片生成/图生图/【遇见AI】Qwen-image-edit 图生图基础_2051187067786407937.json、图片生成/图生图/一致性去水印_1992437141525385218.json、图片生成/图生图/一键去水印高清修复版千问qwen图片编辑2509快速去水印图片去水印加速版_2061066797192933377.json…）

- **类型**：Image To Image
- **样本数**：18
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 18 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 17/18 个有
- `ConditioningZeroOut` —— 16/18 个有
- `UNETLoader` —— 16/18 个有
- `ImageScaleToTotalPixels` —— 15/18 个有
- `LoraLoaderModelOnly` —— 15/18 个有
- `CR Simple Image Compare` —— 10/18 个有
- `PathchSageAttentionKJ` —— 5/18 个有
- `ImageConcatMulti` —— 3/18 个有
- `EmptySD3LatentImage` —— 2/18 个有
- `NunchakuQwenImageDiTLoader` —— 2/18 个有
- `PreviewImage` —— 2/18 个有
- `DWPreprocessor` —— 1/18 个有
- `Image Resize Factor (mtb)` —— 1/18 个有
- `ImageUpscaleWithModel` —— 1/18 个有
- `PlaySound|pysssss` —— 1/18 个有
- `UpscaleModelLoader` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 40 | 18 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 18 | 68% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | simple | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 40，18 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，18 个样本
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 simple，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（17/18 个样本）：Steps较低可能导致细节不足
