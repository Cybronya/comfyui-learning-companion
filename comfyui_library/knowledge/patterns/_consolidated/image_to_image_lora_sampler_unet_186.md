---
name: image_to_image_lora_sampler_unet_186
type: Image To Image
frequency: 3
level: strong
coverage: 0.8
common_nodes: [CLIPLoader, ConditioningZeroOut, FluxKontextImageScale, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEdit 小志版与原版一致性对比_2073056256641822721.json, 图片生成/图生图/QwenEdit偏移问题解决方案_1965093253525684225.json, 图片生成/文生图/Qwen-Edit-偏移纠正_1979205553991880706.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_186

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/QwenEdit 小志版与原版一致性对比_2073056256641822721.json、图片生成/图生图/QwenEdit偏移问题解决方案_1965093253525684225.json、图片生成/文生图/Qwen-Edit-偏移纠正_1979205553991880706.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `seed _O` —— 2/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `Seed Everywhere` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/3 个有
- `TextEncodeQwenImageEdit_lrzjason` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta57 | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta57，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（20/3 个样本）：Steps较低可能导致细节不足
