---
name: image_to_image_sampler_clip_unet_74
type: Image To Image
frequency: 8
level: strong
coverage: 0.892625
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, ImageConcatMulti, ImageCrop, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/电商产品任意更换颜色 万能真实换色  服饰指定换色 保持材质不变_2052695533499756546.json, 图片生成/图生图/电商产品任意更换颜色_万能真实换色_服饰指定换色_保持材质不变_2096800408797794305.json, 图片生成/图生图/电商产品任意更换颜色_万能真实换色_服饰指定换色_保持材质不变_2097143368966041602.json, 图片生成/文生图/Kontext_Canny  参考线稿引导，图像一致编辑：目前最稳定图像质量最好的控制lLORA_1962350864377823234.json, 图片生成/文生图/电商改色丨Flux丨AI改色图生成_2100864143933919233.json, 平台全量/Kontext_Depth 参考深度引导，图像一致编辑：目前最稳定图像质量最好的控制lLORA_1959258583563186177.json, 平台全量/Kontext_OpenPose_参考姿态引导图像一致编辑_目前最稳定图像质量最好的控制lLORA_2074046076751011842.json, 平台全量/【完美姿态控制】Kontext_OpenPose  参考姿态引导图像一致编辑 一致性和自由变换姿势_1985952107721367554.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_74

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/电商产品任意更换颜色 万能真实换色  服饰指定换色 保持材质不变_2052695533499756546.json、图片生成/图生图/电商产品任意更换颜色_万能真实换色_服饰指定换色_保持材质不变_2096800408797794305.json、图片生成/图生图/电商产品任意更换颜色_万能真实换色_服饰指定换色_保持材质不变_2097143368966041602.json、图片生成/文生图/Kontext_Canny  参考线稿引导，图像一致编辑：目前最稳定图像质量最好的控制lLORA_1962350864377823234.json、图片生成/文生图/电商改色丨Flux丨AI改色图生成_2100864143933919233.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageConcatMulti`
- `ImageCrop`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 4/8 个有
- `Colored Image (mtb)` —— 4/8 个有
- `GetImageSizeAndCount` —— 4/8 个有
- `ImageResize+` —— 4/8 个有
- `ImageScaleDownToSize` —— 4/8 个有
- `ImageStitch` —— 4/8 个有
- `ImpactInt` —— 4/8 个有
- `LoraLoaderModelOnly` —— 4/8 个有
- `MathExpression|pysssss` —— 4/8 个有
- `RH_Translator` —— 4/8 个有
- `Text Multiline` —— 3/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
