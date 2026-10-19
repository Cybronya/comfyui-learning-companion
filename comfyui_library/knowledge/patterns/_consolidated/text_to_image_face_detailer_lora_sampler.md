---
name: text_to_image_face_detailer_lora_sampler
type: Text To Image
frequency: 3
level: strong
coverage: 0.871333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, FaceDetailer, FluxKontextImageScale, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, PurgeVRAM_UTK, RMBG, RTXVideoSuperResolution, ResolutionSelector, SAMLoader, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, UltralyticsDetectorProvider, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Krea2参考图像洗图生成参考图优化高质量出图，图生图工具_2105775693199142913.json, 图片生成/反推提示词/krea2参考图像洗图生成 参考图优化高质量出图_2105131515473649665.json, 数字人/数字人/krea2参考图像洗图生成 参考图优化高质量出图_2105059899620286466.json]
source: knowledge_consolidation
---

# text_to_image_face_detailer_lora_sampler

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/Krea2参考图像洗图生成参考图优化高质量出图，图生图工具_2105775693199142913.json、图片生成/反推提示词/krea2参考图像洗图生成 参考图优化高质量出图_2105131515473649665.json、数字人/数字人/krea2参考图像洗图生成 参考图优化高质量出图_2105059899620286466.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `FaceDetailer`
- `FluxKontextImageScale`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `PurgeVRAM_UTK`
- `RMBG`
- `RTXVideoSuperResolution`
- `ResolutionSelector`
- `SAMLoader`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（10/3 个样本）：Steps较低可能导致细节不足
