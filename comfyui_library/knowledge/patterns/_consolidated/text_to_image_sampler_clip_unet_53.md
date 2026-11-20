---
name: text_to_image_sampler_clip_unet_53
type: Text To Image
frequency: 11
level: weak
coverage: 0.778273
common_nodes: [Anything Everywhere3, CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, PreviewAny, PreviewImage, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image2.1全功能合集 By 像素幻想Lab_2102063835665494017.json, 图片生成/文生图/Qwen Image 2.1全功能合集，文生图局部重绘角色多视图图像编辑全覆盖_2103169560424837122.json, 图片生成/文生图/Qwen Image 2.1全功能合集，覆盖角色一致性文生图图生图多场景_2102847595486998530.json, 图片生成/文生图/Qwen Image 2.1全功能合集｜像素幻想Lab出品｜角色一致性生图修图全包_2102656370532245505.json, 图片生成/文生图/Qwen Image 2.1多视图角色三视图生成，文生图图生图角色设计方案_2103626026252333057.json, 图片生成/文生图/Qwen image2.1全功能合集最新优化官方加速lora 全能图像编辑_2109337733801005058.json, 图片生成/文生图/Qwen-image2.1全功能合集 By 像素幻想Lab_2102063835665494017.json, 图片生成/文生图/Qwen-image2.1全功能合集_2102448185208823809.json, 图片生成/文生图/Qwen-image2.1全功能合集_2103043228093206529.json, 视频生成/图生视频/Qwen-image2.1全功能合集_2106179469034741762.json, 视频生成/图生视频/Qwen_Image_2.1全功能合集，覆盖角色一致性文生图图生图多场景_2105854013261565953.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_53

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen-image2.1全功能合集 By 像素幻想Lab_2102063835665494017.json、图片生成/文生图/Qwen Image 2.1全功能合集，文生图局部重绘角色多视图图像编辑全覆盖_2103169560424837122.json、图片生成/文生图/Qwen Image 2.1全功能合集，覆盖角色一致性文生图图生图多场景_2102847595486998530.json、图片生成/文生图/Qwen Image 2.1全功能合集｜像素幻想Lab出品｜角色一致性生图修图全包_2102656370532245505.json、图片生成/文生图/Qwen Image 2.1多视图角色三视图生成，文生图图生图角色设计方案_2103626026252333057.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 11 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `PreviewAny`
- `PreviewImage`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 10/11 个有
- `ComfySwitchNode` —— 10/11 个有
- `DrawMaskOnImage` —— 10/11 个有
- `GetImageSize` —— 10/11 个有
- `GrowMask` —— 10/11 个有
- `Image Comparer (rgthree)` —— 10/11 个有
- `Mask Fill Holes` —— 10/11 个有
- `RHLLMChatNode` —— 10/11 个有
- `SAM3_Detect` —— 10/11 个有
- `LoraLoaderModelOnly` —— 7/11 个有
- `孤海注释` —— 7/11 个有
- `JjkText` —— 6/11 个有
- `solarL_SaveImagesToZip` —— 6/11 个有
- `EmptyImage` —— 2/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 40 | 11 | 4% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 11 | 40% |
| 采样算法 | er_sde | - | 11 | 55% |
| 调度器 | beta | - | 11 | 55% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 1024 | 11 | 8% |
| 高度 | 80 | 80 - 1024 | 11 | 8% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 40，11 个样本，取值分散，一致性仅 4%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，11 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 er_sde，11 个样本，一致性 55%
- 调度器 最常用 beta，11 个样本，一致性 55%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，11 个样本，取值分散，一致性仅 8%
- 高度 中位数 80，观测区间 80 - 1024，11 个样本，取值分散，一致性仅 8%
- 高发问题（6/11 个样本）：Steps较低可能导致细节不足
