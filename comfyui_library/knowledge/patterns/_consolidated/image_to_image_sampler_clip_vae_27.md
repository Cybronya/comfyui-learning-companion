---
name: image_to_image_sampler_clip_vae_27
type: Image To Image
frequency: 9
level: strong
coverage: 0.978556
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/小红书卡通人像贴纸（吉卜力风格）_1953749401648943106.json, 图片生成/图生图/新-kontext商业级印花提取工作流V2版本_1956004419567583233.json, 图片生成/图生图/最好用的 nunchaku flux kontext 去水印_2053752457087467522.json, 图片生成/文生图/芝麻街特效_2073346446350442497.json, 平台全量/kontext生成证件照_1945843096657817601.json, 平台全量/最快nunchaku flux kontext去水印_1944047637513273345.json, 平台全量/线稿上色速写淡彩风格_1964231325957898241.json, 平台全量/超强flux kontext老照片修复_1942224245223264257.json, 数字人/数字人/【服饰提取】人物模特服装衣物精确提取_1944933239409795073.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_27

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/小红书卡通人像贴纸（吉卜力风格）_1953749401648943106.json、图片生成/图生图/新-kontext商业级印花提取工作流V2版本_1956004419567583233.json、图片生成/图生图/最好用的 nunchaku flux kontext 去水印_2053752457087467522.json、图片生成/文生图/芝麻街特效_2073346446350442497.json、平台全量/kontext生成证件照_1945843096657817601.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 8/9 个有
- `LoraLoaderModelOnly` —— 6/9 个有
- `UNETLoader` —— 6/9 个有
- `NunchakuFluxDiTLoader` —— 3/9 个有
- `BiRefNetRMBG` —— 1/9 个有
- `DF_Image_scale_to_side` —— 1/9 个有
- `GrowMask` —— 1/9 个有
- `InvertMask` —— 1/9 个有
- `LayerUtility: ImageBlendAdvance V3` —— 1/9 个有
- `LoraLoader` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 25 | 9 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | beta | - | 9 | 56% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 25，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
