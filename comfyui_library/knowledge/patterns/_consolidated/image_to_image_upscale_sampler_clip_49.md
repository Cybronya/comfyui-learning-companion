---
name: image_to_image_upscale_sampler_clip_49
type: Image To Image
frequency: 3
level: moderate
coverage: 0.914333
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), KSampler, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/国风人物变美工作流-ZImage+Kook大佬瑶光lora+Kook如梦似幻lora_2053095520524091394.json, 图片生成/图生图/图生图洗图修复+SeedVR2高清工作流_2050168318803365889.json, 图片生成/文生图/图生图洗图修复+SeedVR2高清工作流_2050128335044399105.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_49

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/国风人物变美工作流-ZImage+Kook大佬瑶光lora+Kook如梦似幻lora_2053095520524091394.json、图片生成/图生图/图生图洗图修复+SeedVR2高清工作流_2050168318803365889.json、图片生成/文生图/图生图洗图修复+SeedVR2高清工作流_2050128335044399105.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `FastFilmGrain` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `LayerColor: BrightnessContrastV2` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `MuyeTextEditOutput` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 8 - 30 | 3 | 54% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 3 | 53% |
| 采样算法 | res_multistep | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 0.5 | 0.5 - 0.75 | 3 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 8 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，3 个样本
- 采样算法 最常用 res_multistep，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 0.5，观测区间 0.5 - 0.75，3 个样本
