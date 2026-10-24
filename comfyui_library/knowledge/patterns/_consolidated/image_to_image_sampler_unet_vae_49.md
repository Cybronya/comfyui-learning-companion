---
name: image_to_image_sampler_unet_vae_49
type: Image To Image
frequency: 4
level: strong
coverage: 0.85
common_nodes: [Any Switch (rgthree), CFGNorm, CLIPLoader, ConditioningZeroOut, Fast Groups Bypasser (rgthree), ImageConcanate, KSampler, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen_edit服装lora——服装提取、上身迁移工作流_1967424202137591810.json, 图片生成/图生图/万物迁移 · 千问服装迁移 1.0（可提取上身服装）_1967251249718550530.json, 图片生成/图生图/服装提取+上身迁移工作流_1967210000202522625.json, 图片生成/图生图/衣服替换加上身模特_2002451937192755201.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_49

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen_edit服装lora——服装提取、上身迁移工作流_1967424202137591810.json、图片生成/图生图/万物迁移 · 千问服装迁移 1.0（可提取上身服装）_1967251249718550530.json、图片生成/图生图/服装提取+上身迁移工作流_1967210000202522625.json、图片生成/图生图/衣服替换加上身模特_2002451937192755201.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `ImageConcanate`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 3/4 个有
- `LayerUtility: PurgeVRAM V2` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `SeedVR2` —— 2/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `easy imageConcat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 2.5 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 2.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
