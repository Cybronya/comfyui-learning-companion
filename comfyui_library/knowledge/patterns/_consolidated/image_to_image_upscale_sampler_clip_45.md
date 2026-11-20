---
name: image_to_image_upscale_sampler_clip_45
type: Image To Image
frequency: 2
level: weak
coverage: 0.9215
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), KSampler, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/国风人物变美工作流-ZImage+Kook大佬瑶光lora+Kook如梦似幻lora_2053095520524091394.json, 图片生成/文生图/图生图洗图修复+SeedVR2高清工作流_2050128335044399105.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_45

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/国风人物变美工作流-ZImage+Kook大佬瑶光lora+Kook如梦似幻lora_2053095520524091394.json、图片生成/文生图/图生图洗图修复+SeedVR2高清工作流_2050128335044399105.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
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
- `CR Text` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `FastFilmGrain` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `LayerColor: BrightnessContrastV2` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `MuyeTextEditOutput` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 19 | - | 2 | 42% |
| Prompt 约束强度(CFG) | 2.5 | - | 2 | 40% |
| 采样算法 | res_2m_ode | - | 2 | 50% |
| 调度器 | kl_optimal | - | 2 | 50% |
| 重绘幅度 | 0.625 | - | 2 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 19，样本不足，未给区间，2 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 res_2m_ode，2 个样本，一致性 50%
- 调度器 最常用 kl_optimal，2 个样本，一致性 50%
- 重绘幅度 中位数 0.625，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
