---
name: image_to_image_lora_sampler_unet_73
type: Image To Image
frequency: 10
level: weak
coverage: 0.9138
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/QIE2511剪纸风格转换_2051634112317935617.json, 平台全量/Qwen 2509图像编辑模型-单图_1982626441730899970.json, 平台全量/Qwen edit 2511 人物融图_2051483845379280897.json, 平台全量/Qwen-Image-Edit 懒人版一键去水印换背景 V1.0_1964345381922422785.json, 平台全量/Qwen-Image-Edit-2509-Light_restoration_1987128601533419522.json, 平台全量/Qwen-edit-2511 换装-改画风-换背景-合影_2006264153735958529.json, 平台全量/【阡陌】Qwen-Image-Edit-2509升级Plus版nunchaku加速_1970874756071362562.json, 平台全量/【阡陌】Qwen-Image-Edit-2509升级Plus版nunchaku加速证件照生成_1971036322481770497.json, 平台全量/【阡陌】Qwen-Image-Edit-2511超强一致性单图编辑工作流_2003808935779942402.json, 平台全量/【阡陌】Qwen-Image-Edit-2511超强一致性双图_多图编辑工作流_2003818488915501058.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_73

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/QIE2511剪纸风格转换_2051634112317935617.json、平台全量/Qwen 2509图像编辑模型-单图_1982626441730899970.json、平台全量/Qwen edit 2511 人物融图_2051483845379280897.json、平台全量/Qwen-Image-Edit 懒人版一键去水印换背景 V1.0_1964345381922422785.json、平台全量/Qwen-Image-Edit-2509-Light_restoration_1987128601533419522.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 8/10 个有
- `ImageScaleToTotalPixels` —— 8/10 个有
- `ModelSamplingAuraFlow` —— 8/10 个有
- `TextEncodeQwenImageEditPlus` —— 8/10 个有
- `ConditioningZeroOut` —— 6/10 个有
- `CFGNorm` —— 5/10 个有
- `EmptyLatentImage` —— 4/10 个有
- `UnetLoaderGGUF` —— 4/10 个有
- `FluxKontextMultiReferenceLatentMethod` —— 3/10 个有
- `NunchakuQwenImageDiTLoader` —— 2/10 个有
- `TextEncodeQwenImageEdit` —— 2/10 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 2/10 个有
- `FluxKontextImageScale` —— 1/10 个有
- `easy imageScaleDownToSize` —— 1/10 个有
- `easy imageSize` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 50 | 10 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 10 | 40% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 512 | 512 - 768 | 4 | 81% |
| 高度 | 768 | 512 - 1024 | 4 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 50，10 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，10 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 768，4 个样本，取值集中（一致性 81%）
- 高度 中位数 768，观测区间 512 - 1024，4 个样本
- 高发问题（6/10 个样本）：Steps较低可能导致细节不足
