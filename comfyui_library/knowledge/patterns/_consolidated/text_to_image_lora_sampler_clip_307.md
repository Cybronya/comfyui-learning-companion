---
name: text_to_image_lora_sampler_clip_307
type: Text To Image
frequency: 7
level: strong
coverage: 0.897429
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1 Viggle 4-Step极速文生图工作流四步出图_2106210534201843714.json, 图片生成/文生图/Qwen Image 2.1 主体去背景｜透明PNG遮罩预览_2112467188685828098.json, 图片生成/文生图/Qwen Image 2.1 图片换人｜双图替换保留原姿态_2112454776331001858.json, 图片生成/文生图/Qwen Image 2.1 透明素材生成｜文生图直出透明PNG_2112462903986180098.json, 图片生成/文生图/qwen2.1文生图基础工作流 新手友好稳定出图_2104664392800489473.json, 图片生成/文生图/qwen2.1文生图基础工作流 新手友好稳定出图_2105070911778021377.json, 数字人/数字人/千问大模型驱动的数字人工作流，多功能AI生成方案_2102883846000828418.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_307

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1 Viggle 4-Step极速文生图工作流四步出图_2106210534201843714.json、图片生成/文生图/Qwen Image 2.1 主体去背景｜透明PNG遮罩预览_2112467188685828098.json、图片生成/文生图/Qwen Image 2.1 图片换人｜双图替换保留原姿态_2112454776331001858.json、图片生成/文生图/Qwen Image 2.1 透明素材生成｜文生图直出透明PNG_2112462903986180098.json、图片生成/文生图/qwen2.1文生图基础工作流 新手友好稳定出图_2104664392800489473.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 6/7 个有
- `ComfySwitchNode` —— 5/7 个有
- `ResolutionSelector` —— 5/7 个有
- `LoadImage` —— 3/7 个有
- `ImageResizeKJv2` —— 2/7 个有
- `MaskToImage` —— 2/7 个有
- `PrimitiveInt` —— 2/7 个有
- `SplitImageWithAlpha` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `ImageScale` —— 1/7 个有
- `ModelAttentionBackend` —— 1/7 个有
- `ModelSamplingFlux` —— 1/7 个有
- `easy imageConcat` —— 1/7 个有

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
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足
