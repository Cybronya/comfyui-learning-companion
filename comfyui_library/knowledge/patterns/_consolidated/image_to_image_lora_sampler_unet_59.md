---
name: image_to_image_lora_sampler_unet_59
type: Image To Image
frequency: 11
level: moderate
coverage: 0.882909
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2511任意姿态生成_2103492106114387969.json, 图片生成/图生图/Qwen图像编辑_1957991828404449282.json, 图片生成/图生图/USO平替QwenImageEditLora4步-动物换背景和动态_1963759656961282049.json, 图片生成/图生图/USO平替QwenImageEditLora4步-换背景该动作_1963757228963745794.json, 图片生成/图生图/USO平替QwenImageEditLora4步-生成相同风格的图片_1963764180477366273.json, 图片生成/图生图/Y-image_qwen_image_edit_线稿_2003001296292573186.json, 图片生成/图生图/一键搞笑漫画风格_1987493162623111169.json, 图片生成/图生图/全能图片V1平替QwenImageEditLora4步-2D转3D动画皮克斯风格_1963414314948464641.json, 图片生成/图生图/全能图片V1平替QwenImageEditLora4步-3D转毛毡风格_1963417264743755778.json, 图片生成/文生图/Qwen Image Edit 千问模型-图像编辑 @橘子_SJRJT_1963120825828356098.json, 平台全量/Qwen图像编辑v1_1961317525357268994.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_59

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen2511任意姿态生成_2103492106114387969.json、图片生成/图生图/Qwen图像编辑_1957991828404449282.json、图片生成/图生图/USO平替QwenImageEditLora4步-动物换背景和动态_1963759656961282049.json、图片生成/图生图/USO平替QwenImageEditLora4步-换背景该动作_1963757228963745794.json、图片生成/图生图/USO平替QwenImageEditLora4步-生成相同风格的图片_1963764180477366273.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 10/11 个有
- `ModelSamplingAuraFlow` —— 10/11 个有
- `TextEncodeQwenImageEdit` —— 10/11 个有
- `ImageScaleToTotalPixels` —— 8/11 个有
- `ConditioningZeroOut` —— 2/11 个有
- `EmptyLatentImage` —— 2/11 个有
- `GetImageSize` —— 2/11 个有
- `ComfySwitchNode` —— 1/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/11 个有
- `QwenEditTextEncode_EditUtils` —— 1/11 个有
- `ResolutionSelector` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 67% |
| 高度 | 768 | - | 2 | 67% |
| 采样步数 | 4 | 4 - 20 | 11 | 26% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 11 | 55% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本
- 高度 中位数 768，样本不足，未给区间，2 个样本
- 采样步数 中位数 4，观测区间 4 - 20，11 个样本，取值分散，一致性仅 26%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，11 个样本
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（10/11 个样本）：Steps较低可能导致细节不足
