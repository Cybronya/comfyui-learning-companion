---
name: text_to_image_lora_sampler_clip_171
type: Text To Image
frequency: 10
level: strong
coverage: 0.7916
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102557478423715841.json, 图片生成/图生图/Qwen Image 2.1图像编辑基础版｜改字改色改细节｜日常修图够用了_2102634269028999170.json, 图片生成/图生图/Qwen Image 2.1图像编辑工作流，图生图处理方案_2106515424149065729.json, 图片生成/图生图/Qwen Image 2.1图像编辑工作流，简洁实用的图生图处理方案_2102836660949053442.json, 图片生成/图生图/Qwen Image 2.1图像编辑工作流，简洁实用的图生图处理方案_2106492632359849986.json, 图片生成/图生图/Qwen Image 2.1图像编辑最多十张参考图，2K原生输出图生图处理工具_2106447204092309505.json, 图片生成/图生图/Qwen Image 2.1图片编辑工作流，简洁高效的图生图处理方案_2102853729841139713.json, 图片生成/图生图/Qwen Image 2.1图片编辑简洁高效，图生图处理方案_2103268539221241858.json, 图片生成/图生图/Qwen Image 2.1多合一工作流图生图文生图处理工具_2102465754015821825.json, 图片生成/文生图/Qwen Image 2.1多合一工作流 全能图像编辑方案_2109008831576625154.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_171

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102557478423715841.json、图片生成/图生图/Qwen Image 2.1图像编辑基础版｜改字改色改细节｜日常修图够用了_2102634269028999170.json、图片生成/图生图/Qwen Image 2.1图像编辑工作流，图生图处理方案_2106515424149065729.json、图片生成/图生图/Qwen Image 2.1图像编辑工作流，简洁实用的图生图处理方案_2102836660949053442.json、图片生成/图生图/Qwen Image 2.1图像编辑工作流，简洁实用的图生图处理方案_2106492632359849986.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 10 个 workflow 都包含：
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
- `ComfySwitchNode` —— 7/10 个有
- `BatchImagesNode` —— 5/10 个有
- `TextGenerateLTX2Prompt` —— 5/10 个有
- `easy showAnything` —— 5/10 个有
- `Fast Groups Bypasser (rgthree)` —— 4/10 个有
- `GetNode` —— 4/10 个有
- `SetNode` —— 4/10 个有
- `PrimitiveStringMultiline` —— 3/10 个有
- `SaveImageAdvanced` —— 3/10 个有
- `ConditioningZeroOut` —— 2/10 个有
- `CropWithPadInfo_EditUtils` —— 2/10 个有
- `EditTextEncode_EditUtils` —— 2/10 个有
- `GetImageSize` —— 2/10 个有
- `Image Comparer (rgthree)` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `PrimitiveInt` —— 2/10 个有
- `QwenImage21ConfigPreparer_EditUtils` —— 2/10 个有
- `QwenImage21ModelConfig_EditUtils` —— 2/10 个有
- `TextInput_` —— 2/10 个有
- `EmptyImage` —— 1/10 个有
- `FastGroupsBypassSwitch` —— 1/10 个有
- `GH_ImageVideoComparer` —— 1/10 个有
- `QwenPERewriteT8` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（12/10 个样本）：Steps较低可能导致细节不足
