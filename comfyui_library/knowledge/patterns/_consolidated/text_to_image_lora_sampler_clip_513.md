---
name: text_to_image_lora_sampler_clip_513
type: Text To Image
frequency: 3
level: strong
coverage: 0.938667
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CustomSigmas, EmptyLatentImage, INTConstant, ImageConcatMulti, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, StringConstantMultiline, T8QwenImage21FunAccPDD4Step, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1文生图原生FUN Viggle三图对比，图生图处理方案_2105795635810226177.json, 图片生成/文生图/Qwen Image2.1图像编辑｜原生FUN Viggle三图对比 效果一目了然_2105535536256602113.json, 图片生成/文生图/Qwen Image2.1文生图三件套｜原生FUN Viggle三图对比全都有_2105538670647406594.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_513

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1文生图原生FUN Viggle三图对比，图生图处理方案_2105795635810226177.json、图片生成/文生图/Qwen Image2.1图像编辑｜原生FUN Viggle三图对比 效果一目了然_2105535536256602113.json、图片生成/文生图/Qwen Image2.1文生图三件套｜原生FUN Viggle三图对比全都有_2105538670647406594.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CustomSigmas`
- `EmptyLatentImage`
- `INTConstant`
- `ImageConcatMulti`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringConstantMultiline`
- `T8QwenImage21FunAccPDD4Step`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 2/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `LoadImage` —— 1/3 个有

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
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
