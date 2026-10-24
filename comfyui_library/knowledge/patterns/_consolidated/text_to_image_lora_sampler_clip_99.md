---
name: text_to_image_lora_sampler_clip_99
type: Text To Image
frequency: 13
level: strong
coverage: 0.683538
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, Image Comparer (rgthree), Int, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI图像编辑控制工作流_精准修图创作工具_2085631571251515393.json, 图片生成/图生图/AI图像编辑控制工作流_精准修图创作工具_2085639717349052417.json, 图片生成/图生图/AI图像编辑控制工作流_精准修图创作工具_2087354723983777793.json, 图片生成/图生图/AI图像编辑控制工作流_精准修图创作工具_2092607643062988802.json, 图片生成/图生图/Qwen-Image多图换装打光融图转角度文生图处理工具_2101036657872035842.json, 图片生成/图生图/图像编辑控制工作流-图生图其它图片处理图片换背景_2086259471852064769.json, 图片生成/图生图/图像编辑控制工作流-图生图其它图片处理图片换背景_2086272043359756289.json, 图片生成/图生图/精准修图创作工具AI图像编辑控制工作流局部重绘图生图换装_2085852998529540097.json, 图片生成/图生图/精准修图创作工具AI图像编辑控制工作流局部重绘图生图换装_2086628996216868865.json, 图片生成/图生图/精准修图创作工具AI图像编辑控制工作流局部重绘图生图换装_2089524732088643585.json, 图片生成/图生图/精准修图创作工具AI图像编辑控制工作流局部重绘图生图换装_2089529386545537025.json, 图片生成/图生图/精准修图创作工具AI图像编辑控制工作流局部重绘图生图换装_2090255198680862722.json, 图片生成/图生图/精准修图创作工具AI图像编辑控制工作流局部重绘图生图换装_2_2090258583735848962.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_99

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/AI图像编辑控制工作流_精准修图创作工具_2085631571251515393.json、图片生成/图生图/AI图像编辑控制工作流_精准修图创作工具_2085639717349052417.json、图片生成/图生图/AI图像编辑控制工作流_精准修图创作工具_2087354723983777793.json、图片生成/图生图/AI图像编辑控制工作流_精准修图创作工具_2092607643062988802.json、图片生成/图生图/Qwen-Image多图换装打光融图转角度文生图处理工具_2101036657872035842.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxKontextMultiReferenceLatentMethod`
- `Image Comparer (rgthree)`
- `Int`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 12/13 个有
- `GetNode` —— 12/13 个有
- `ImageConcanate` —— 12/13 个有
- `PreviewImage` —— 12/13 个有
- `Seed (rgthree)` —— 12/13 个有
- `SetNode` —— 12/13 个有
- `TextEncodeQwenImageEdit` —— 12/13 个有
- `TextInput_` —— 12/13 个有
- `孤海注释` —— 2/13 个有
- `CR Text` —— 1/13 个有
- `EmptyImage` —— 1/13 个有
- `TwoWaySwitch` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 27/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（27/13 个样本）：Steps较低可能导致细节不足
