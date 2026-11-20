---
name: unknown_workflow_sampler_clip_unet_408
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.920667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoadImage, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux SRPO仿图_1969765351493935106.json, 图片生成/图生图/修复结构_1964879807592939522.json, 平台全量/Minion Metamorphosis by 金运_1841840029869244417.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_408

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/flux SRPO仿图_1969765351493935106.json、图片生成/图生图/修复结构_1964879807592939522.json、平台全量/Minion Metamorphosis by 金运_1841840029869244417.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_Captioner` —— 2/3 个有
- `DF_Get_image_size` —— 1/3 个有
- `ImageScaleToMegapixels` —— 1/3 个有
- `JoyCaption` —— 1/3 个有
- `LatentUpscaleBy` —— 1/3 个有
- `RepeatLatentBatch` —— 1/3 个有
- `SDXLEmptyLatentSizePicker+` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有
- `easy clearCacheAll` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024x1024 (1.0) | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
