---
name: text_to_image_lora_sampler_clip_231
type: Text To Image
frequency: 3
level: strong
coverage: 0.791667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetNode, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, QwenImage21Cache, ResolutionSelector, SaveImage, SetNode, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1图像编辑加二次采样放大，去提示词增强精简版图生图方案_2103533493711106050.json, 数字人/数字人/Qwen 2.1透明背景抠图，一键生成PNG透明图生图工具_2102899365059846146.json, 视频生成/图生视频/Qwen_2.1透明背景抠图，一键生成PNG透明图生图工具_2104737318635659265.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_231

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1图像编辑加二次采样放大，去提示词增强精简版图生图方案_2103533493711106050.json、数字人/数字人/Qwen 2.1透明背景抠图，一键生成PNG透明图生图工具_2102899365059846146.json、视频生成/图生视频/Qwen_2.1透明背景抠图，一键生成PNG透明图生图工具_2104737318635659265.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `FastGroupsBypassSwitch` —— 2/3 个有
- `TextCombinerTwo` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `ComfyMathExpression` —— 1/3 个有
- `EmptyImage` —— 1/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `Textbox` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy clearCacheAll` —— 1/3 个有

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
