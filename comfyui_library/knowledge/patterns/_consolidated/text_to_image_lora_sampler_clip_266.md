---
name: text_to_image_lora_sampler_clip_266
type: Text To Image
frequency: 7
level: strong
coverage: 0.894143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/角色三视图Qwen Image 2.1工作流，图生图角色设计处理工具_2107934196995018753.json, 图片生成/文生图/BF16精度Qwen Image 2.1文生图，小字不崩高质量文字渲染工作流_2102872573246791681.json, 图片生成/文生图/BF16精度Qwen_Image_2.1文生图，小字不崩高质量文字渲染工作流_2105503929613250561.json, 图片生成/文生图/Qwen 2.1基础工作流i2v t2v，文生视频图生视频双模式入门方案_2103210530956726273.json, 图片生成/文生图/Qwen Image 2.1一键抠图直出PNG无缝重塑图像工作流，图生图处理工具_2106498210620596226.json, 图片生成/文生图/Qwen Image 2.1文生图图生图工作流，轻量模型多场景覆盖方案_2103627655844294657.json, 图片生成/文生图/Qwen-Image-2_1-Edit-I2I-Turbo｜6步LORA快速出图 文生图图生图双模式_2104020602133762050.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_266

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/角色三视图Qwen Image 2.1工作流，图生图角色设计处理工具_2107934196995018753.json、图片生成/文生图/BF16精度Qwen Image 2.1文生图，小字不崩高质量文字渲染工作流_2102872573246791681.json、图片生成/文生图/BF16精度Qwen_Image_2.1文生图，小字不崩高质量文字渲染工作流_2105503929613250561.json、图片生成/文生图/Qwen 2.1基础工作流i2v t2v，文生视频图生视频双模式入门方案_2103210530956726273.json、图片生成/文生图/Qwen Image 2.1一键抠图直出PNG无缝重塑图像工作流，图生图处理工具_2106498210620596226.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
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
- `孤海注释` —— 6/7 个有
- `LoadImage` —— 5/7 个有
- `QwenImage21Cache` —— 5/7 个有
- `SaveImageAdvanced` —— 5/7 个有
- `ResolutionSelector` —— 4/7 个有
- `ComfySwitchNode` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `CR Prompt Text` —— 2/7 个有
- `Any Switch (rgthree)` —— 1/7 个有
- `EmptyImage` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `ImageScaleBy` —— 1/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `ImageStitch` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `Seed (rgthree)` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足
