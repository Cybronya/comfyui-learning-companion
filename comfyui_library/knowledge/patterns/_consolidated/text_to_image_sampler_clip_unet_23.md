---
name: text_to_image_sampler_clip_unet_23
type: Text To Image
frequency: 15
level: weak
coverage: 0.7726
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/全自动提示词图像编辑 千问image2.1海报改图优化_2104340100669857794.json, 图片生成/图生图/BF16精度Qwen Image 2.1图片编辑，小字不崩的图生图处理方案_2102871104883879938.json, 图片生成/图生图/Qwen Image 2.1 AI短剧漫剧人物三视图，图生图角色一致性设计工具_2103949584014860290.json, 图片生成/图生图/Qwen Image 2.1全功能集合文生图图生图处理工作流_2102094333674614786.json, 图片生成/图生图/Qwen Image 2.1图像合集人像写真实图生图处理工具_2102543389462982657.json, 图片生成/图生图/Qwen Image 2.1图像生成二十步大合集，全方位图生图能力覆盖_2102828879642714114.json, 图片生成/图生图/Qwen Image 2.1图像生成大合集，场景换装图生图多场景一站式工具_2103254188389130241.json, 图片生成/图生图/Qwen Image 2.1图像生成大合集｜文生图图生图全都有｜收藏一个够用了_2102628402149806081.json, 图片生成/图生图/Qwen Image 2.1工作流合集图生图处理生成工具_2102495775229046786.json, 图片生成/图生图/Qwen Image 2.1工作流合集文生图图生图处理工具_2102555854674419713.json, 图片生成/图生图/Qwen Image 2.1工作流大合集｜图生图多种玩法一网打尽｜新手必存_2102238523955965954.json, 图片生成/图生图/Qwen2.1双图版_Flux2Klein自动生成图_2102391245615230977.json, 图片生成/图生图/Qwen2.1双图版｜Flux2Klein自动生成图｜双参考融合效果更自然_2102585557531578370.json, 图片生成/文生图/Qwen Image 2.1文生编辑一锅端工作流详拆系列，局部重绘文生图图生图_2103952709224325121.json, 图片生成/文生图/Qwen Image 2.1文生编辑一锅端详拆第11集｜新手逐节点拆解_2103728447376936962.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_23

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/反推提示词/全自动提示词图像编辑 千问image2.1海报改图优化_2104340100669857794.json、图片生成/图生图/BF16精度Qwen Image 2.1图片编辑，小字不崩的图生图处理方案_2102871104883879938.json、图片生成/图生图/Qwen Image 2.1 AI短剧漫剧人物三视图，图生图角色一致性设计工具_2103949584014860290.json、图片生成/图生图/Qwen Image 2.1全功能集合文生图图生图处理工作流_2102094333674614786.json、图片生成/图生图/Qwen Image 2.1图像合集人像写真实图生图处理工具_2102543389462982657.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 14/15 个有
- `Image Comparer (rgthree)` —— 14/15 个有
- `JjkText` —— 14/15 个有
- `LoraLoaderModelOnly` —— 14/15 个有
- `ShowText|pysssss` —— 14/15 个有
- `solarL_SaveImagesToZip` —— 14/15 个有
- `孤海注释` —— 14/15 个有
- `Anything Everywhere3` —— 13/15 个有
- `LayerUtility: ImageReel` —— 13/15 个有
- `LayerUtility: ImageReelComposit` —— 13/15 个有
- `PreviewImage` —— 13/15 个有
- `Seed (rgthree)` —— 13/15 个有
- `easy setNode` —— 13/15 个有
- `Fast Groups Bypasser (rgthree)` —— 12/15 个有
- `GetNode` —— 11/15 个有
- `SetNode` —— 11/15 个有
- `TextGenerateLTX2Prompt` —— 10/15 个有
- `BatchImagesNode` —— 9/15 个有
- `PreviewAny` —— 9/15 个有
- `easy showAnything` —— 9/15 个有
- `Any Switch (rgthree)` —— 3/15 个有
- `RHLLMChatNode` —— 3/15 个有
- `ResizeLongestToNode` —— 3/15 个有
- `SeedVR2LoadDiTModel` —— 3/15 个有
- `SeedVR2LoadVAEModel` —— 3/15 个有
- `SeedVR2VideoUpscaler` —— 3/15 个有
- `easy getNode` —— 3/15 个有
- `EmptyFlux2LatentImage` —— 2/15 个有
- `Fast Bypasser (rgthree)` —— 2/15 个有
- `ImageScaleBy` —— 2/15 个有
- `LoraLoader` —— 2/15 个有
- `PrimitiveBoolean` —— 2/15 个有
- `SaveImageAdvanced` —— 2/15 个有
- `SplitImageWithAlpha` —— 2/15 个有
- `VOSR2ModelLoader` —— 2/15 个有
- `VOSR2Upscale` —— 2/15 个有
- `easy float` —— 2/15 个有
- `easy int` —— 2/15 个有
- `QwenPERewriteT8` —— 1/15 个有
- `Text Multiline` —— 1/15 个有
- `XinbaoImageStandardizer` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 15 | 0% |
| 高度 | 80 | 80 - 1024 | 15 | 0% |
| 采样步数 | 4 | 4 - 20 | 15 | 21% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 15 | 80% |
| 采样算法 | er_sde | - | 15 | 93% |
| 调度器 | beta | - | 15 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| LoRA 模型强度 | 0.4 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，15 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，15 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 20，15 个样本，取值分散，一致性仅 21%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，15 个样本
- 采样算法 最常用 er_sde，15 个样本，一致性 93%
- 调度器 最常用 beta，15 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（16/15 个样本）：Steps较低可能导致细节不足
