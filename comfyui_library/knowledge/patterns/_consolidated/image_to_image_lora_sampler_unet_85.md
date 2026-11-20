---
name: image_to_image_lora_sampler_unet_85
type: Image To Image
frequency: 9
level: strong
coverage: 0.957222
common_nodes: [CFGNorm, CLIPLoader, CR Text, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Qwen2512+CN：视频首帧姿态复刻_2008180605472739330.json, 平台全量/人物换背景qwen2511双图修改_2066099523738488833.json, 平台全量/人物提取衣服 Qwen2511底模_2046500604767375362.json, 平台全量/人物替换 换装换脸换头！加强版  影视二创换人Qwen edit 最新图像编辑换装千问2511_2042045345273745410.json, 平台全量/去水印qwen2511最新图像编辑_2080585884612780034.json, 平台全量/最新稳定一键去水印_2077922922550882306.json, 平台全量/电商产品 衣服提取 服饰白底图生成 qwen2511 千问 加速版_2046751699116756994.json, 视频生成/图生视频/小红书[FireRed-Image-Edit1.1] 三图编辑_2030684351255547905.json, 视频生成/图生视频/小红书[FireRed-Image-Edit1.1] 双图编辑_2030672844018946049.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_85

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/Qwen2512+CN：视频首帧姿态复刻_2008180605472739330.json、平台全量/人物换背景qwen2511双图修改_2066099523738488833.json、平台全量/人物提取衣服 Qwen2511底模_2046500604767375362.json、平台全量/人物替换 换装换脸换头！加强版  影视二创换人Qwen edit 最新图像编辑换装千问2511_2042045345273745410.json、平台全量/去水印qwen2511最新图像编辑_2080585884612780034.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
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
- `FluxKontextMultiReferenceLatentMethod` —— 7/9 个有
- `ImageScaleToTotalPixels` —— 7/9 个有
- `ImageConcanate` —— 6/9 个有
- `ImageResizeKJv2` —— 3/9 个有
- `JWInteger` —— 3/9 个有
- `PreviewImage` —— 3/9 个有
- `FluxKontextImageScale` —— 2/9 个有
- `ReferenceLatent` —— 2/9 个有
- `DWPreprocessor` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `ImageFromBatch+` —— 1/9 个有
- `VHS_LoadVideo` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 9 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
