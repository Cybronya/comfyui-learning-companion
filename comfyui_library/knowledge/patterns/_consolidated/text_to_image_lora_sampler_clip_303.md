---
name: text_to_image_lora_sampler_clip_303
type: Text To Image
frequency: 3
level: strong
coverage: 0.823667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1图片编辑工作流，文生图图生图处理方案_2103967167434813441.json, 图片生成/文生图/Qwen Image 2.1文生图图生图工作流，轻量模型多场景覆盖方案_2103627655844294657.json, 图片生成/文生图/Qwen Image 2.1文生图工作流，高质量文本到图像生成方案_2103968730760962050.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_303

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1图片编辑工作流，文生图图生图处理方案_2103967167434813441.json、图片生成/文生图/Qwen Image 2.1文生图图生图工作流，轻量模型多场景覆盖方案_2103627655844294657.json、图片生成/文生图/Qwen Image 2.1文生图工作流，高质量文本到图像生成方案_2103968730760962050.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
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
- `ComfySwitchNode` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `QwenImage21Cache` —— 2/3 个有
- `ResizeImageMaskNode` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `SeedVR2Conditioning` —— 2/3 个有
- `SeedVR2PostProcessing` —— 2/3 个有
- `SeedVR2Preprocess` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `VAEDecodeTiled` —— 2/3 个有
- `VAEEncodeTiled` —— 2/3 个有

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
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
