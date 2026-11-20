---
name: text_to_image_lora_sampler_clip_355
type: Text To Image
frequency: 6
level: strong
coverage: 0.891167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1 PE文生图优化版｜出图质量再打磨｜细节党放心冲_2102587044131336194.json, 图片生成/文生图/Qwen Image 2.1 Turbo文生图工作流，指令生图速度快质量高_2114481503345405954.json, 图片生成/文生图/Qwen Image 2.1 Turbo文生图，创意形象快速直出_2110829189711622145.json, 图片生成/文生图/Qwen Image 2.1 Turbo文生图｜一句话生成高质量图片_2114173392453722113.json, 图片生成/文生图/Qwen Image 2.1 V2文生图，文本到图像生成升级版本工作流_2103243206614937601.json, 图片生成/文生图/Qwen_Image_2.1_Turbo文生图工作流，指令生图速度快质量高_2116821106115043330.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_355

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1 PE文生图优化版｜出图质量再打磨｜细节党放心冲_2102587044131336194.json、图片生成/文生图/Qwen Image 2.1 Turbo文生图工作流，指令生图速度快质量高_2114481503345405954.json、图片生成/文生图/Qwen Image 2.1 Turbo文生图，创意形象快速直出_2110829189711622145.json、图片生成/文生图/Qwen Image 2.1 Turbo文生图｜一句话生成高质量图片_2114173392453722113.json、图片生成/文生图/Qwen Image 2.1 V2文生图，文本到图像生成升级版本工作流_2103243206614937601.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 5/6 个有
- `ResolutionSelector` —— 5/6 个有
- `孤海注释` —— 5/6 个有
- `CFGGuider` —— 4/6 个有
- `KSamplerSelect` —— 4/6 个有
- `ManualSigmas` —— 4/6 个有
- `RandomNoise` —— 4/6 个有
- `SamplerCustomAdvanced` —— 4/6 个有
- `PreviewAny` —— 3/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `SaveImageAdvanced` —— 2/6 个有
- `TextGenerate` —— 2/6 个有
- `ComfySwitchNode` —— 1/6 个有
- `QwenPECanvasT8` —— 1/6 个有
- `QwenPERewriteT8` —— 1/6 个有
- `RegexExtract` —— 1/6 个有
- `StringConcatenate` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
