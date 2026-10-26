---
name: text_to_image_upscale_sampler_clip_9
type: Text To Image
frequency: 10
level: strong
coverage: 0.7858
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图像修复放大 - Zimage_2008563835296288770.json, 图片生成/图生图/图像修复放大+-+Zimage_2021785801733971970.json, 图片生成/图生图/小红书 FireRed-V1.1虚拟换装_2041129593666539522.json, 图片生成/文生图/001.Z-Image+lora文生图.json_2092039413546176513.json, 图片生成/文生图/001.Z-image生图巅峰001.lora文生图+放大_2033714274614386690.json, 图片生成/文生图/5.其他类型-6.NSF+-09.Z-image生图001.Z-Image+lora文生图带放大_2021966017785761793.json, 图片生成/文生图/AI代码侠土豆 瑶光电商图专用_换产品_衣服_2034897021122908162.json, 图片生成/文生图/电商图专用_换产品_衣服_2039333002022490113.json, 图片生成/文生图/电商图专用_换产品_衣服_2041164747680260098.json, 数字人/数字人/HuoHuo换装模特工作流（瑶光）_2045884499656970241.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_9

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/图像修复放大 - Zimage_2008563835296288770.json、图片生成/图生图/图像修复放大+-+Zimage_2021785801733971970.json、图片生成/图生图/小红书 FireRed-V1.1虚拟换装_2041129593666539522.json、图片生成/文生图/001.Z-Image+lora文生图.json_2092039413546176513.json、图片生成/文生图/001.Z-image生图巅峰001.lora文生图+放大_2033714274614386690.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Text` —— 7/10 个有
- `Image Comparer (rgthree)` —— 6/10 个有
- `ImageScaleBy` —— 5/10 个有
- `LoadImage` —— 5/10 个有
- `LoraLoaderModelOnly` —— 5/10 个有
- `TTResolutionSelector` —— 5/10 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 5/10 个有
- `easy imageSizeBySide` —— 5/10 个有
- `GetNode` —— 4/10 个有
- `SetNode` —— 4/10 个有
- `LoraLoader` —— 3/10 个有
- `easy promptList` —— 2/10 个有
- `ImageResize+` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 616 | 512 - 1080 | 10 | 69% |
| 高度 | 896 | 512 - 1920 | 10 | 46% |
| 采样步数 | 8.5 | 4 - 9 | 10 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 70% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 10 | 30% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 616，观测区间 512 - 1080，10 个样本
- 高度 中位数 896，观测区间 512 - 1920，10 个样本，取值分散，一致性仅 46%
- 采样步数 中位数 8.5，观测区间 4 - 9，10 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 70%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，10 个样本，一致性 30%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（16/10 个样本）：Steps较低可能导致细节不足
