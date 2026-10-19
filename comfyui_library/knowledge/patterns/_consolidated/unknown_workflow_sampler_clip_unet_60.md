---
name: unknown_workflow_sampler_clip_unet_60
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.921
common_nodes: [AILab_QwenVL, BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, KSamplerSelect, LoadImage, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/2105994124833943553.json, 图片生成/图生图/2106023301272399873.json, 数字人/数字人/风格复制 图生图+洗图=krea2+i2i！_2086999597515362305.json, 数字人/数字人/高清放大洗图krea2 +SeedVR+放大+图生图 直出4K_2088859290869264386.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_60

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2105994124833943553.json、图片生成/图生图/2106023301272399873.json、数字人/数字人/风格复制 图生图+洗图=krea2+i2i！_2086999597515362305.json、数字人/数字人/高清放大洗图krea2 +SeedVR+放大+图生图 直出4K_2088859290869264386.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `AILab_QwenVL`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 3/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `Int` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `SeedVR2LoadDiTModel` —— 1/4 个有
- `SeedVR2LoadVAEModel` —— 1/4 个有
- `SeedVR2VideoUpscaler` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
