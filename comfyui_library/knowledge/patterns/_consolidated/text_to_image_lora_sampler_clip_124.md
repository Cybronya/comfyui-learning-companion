---
name: text_to_image_lora_sampler_clip_124
type: Text To Image
frequency: 7
level: strong
coverage: 0.781571
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/全自动提示词图像编辑 千问image2.1海报改图优化_2104340100669857794.json, 图片生成/图生图/2102213493909966850.json, 图片生成/图生图/2102258886488186882.json, 图片生成/图生图/2102291809056681986.json, 图片生成/图生图/2102293368142389249.json, 图片生成/图生图/2102522537514196994.json, 图片生成/图生图/2102524212488531970.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_124

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/全自动提示词图像编辑 千问image2.1海报改图优化_2104340100669857794.json、图片生成/图生图/2102213493909966850.json、图片生成/图生图/2102258886488186882.json、图片生成/图生图/2102291809056681986.json、图片生成/图生图/2102293368142389249.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 6/7 个有
- `SaveImageAdvanced` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `DrawMaskOnImage` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `ResizeImageMaskNode` —— 5/7 个有
- `GetImageSize` —— 3/7 个有
- `ImagePadForOutpaint` —— 3/7 个有
- `ComfySwitchNode` —— 2/7 个有
- `GrowMaskWithBlur` —— 2/7 个有
- `ResizeMask` —— 2/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `QwenPERewriteT8` —— 1/7 个有
- `Seed (rgthree)` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `Text Multiline` —— 1/7 个有
- `XinbaoImageStandardizer` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
