---
name: text_to_image_lora_sampler_clip_247
type: Text To Image
frequency: 8
level: strong
coverage: 0.847
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfySwitchNode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, ResizeLongestToNode, ResolutionSelector, SaveImage, ShowText|pysssss, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1全功能集合文生图图生图处理工作流_2102094333674614786.json, 图片生成/图生图/Qwen Image 2.1单图编辑产品展示图生图处理工具_2102489354336821249.json, 图片生成/图生图/Qwen Image 2.1单图编辑流｜局部修改想改哪里改哪里_2108081920897806338.json, 图片生成/图生图/Qwen Image 2.1单图编辑｜图生图局部修改｜一张图也能精修到位_2104763014581940225.json, 图片生成/图生图/Qwen Image 2.1单图编辑｜图生图局部修改｜一张图也能精修到位_2108523054933561346.json, 图片生成/图生图/Qwen Image 2.1单图编辑｜图生图局部修改｜想修哪里修哪里_2107745036996800513.json, 图片生成/文生图/Qwen Image 2.1文生编辑一锅端工作流详拆系列，局部重绘文生图图生图_2103952709224325121.json, 图片生成/文生图/Qwen Image 2.1文生编辑一锅端详拆第11集｜新手逐节点拆解_2103728447376936962.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_247

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1全功能集合文生图图生图处理工作流_2102094333674614786.json、图片生成/图生图/Qwen Image 2.1单图编辑产品展示图生图处理工具_2102489354336821249.json、图片生成/图生图/Qwen Image 2.1单图编辑流｜局部修改想改哪里改哪里_2108081920897806338.json、图片生成/图生图/Qwen Image 2.1单图编辑｜图生图局部修改｜一张图也能精修到位_2104763014581940225.json、图片生成/图生图/Qwen Image 2.1单图编辑｜图生图局部修改｜一张图也能精修到位_2108523054933561346.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `ResizeLongestToNode`
- `ResolutionSelector`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 7/8 个有
- `Seed (rgthree)` —— 7/8 个有
- `孤海注释` —— 7/8 个有
- `CR Text Concatenate` —— 4/8 个有
- `RHLLMChatNode` —— 4/8 个有
- `TextGenerate` —— 4/8 个有
- `Any Switch (rgthree)` —— 3/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `Image Comparer (rgthree)` —— 3/8 个有
- `LayerUtility: ImageReel` —— 3/8 个有
- `LayerUtility: ImageReelComposit` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `SeedVR2LoadDiTModel` —— 3/8 个有
- `SeedVR2LoadVAEModel` —— 3/8 个有
- `SeedVR2VideoUpscaler` —— 3/8 个有
- `easy getNode` —— 3/8 个有
- `easy setNode` —— 3/8 个有
- `Fast Bypasser (rgthree)` —— 2/8 个有
- `ImageScaleBy` —— 2/8 个有
- `PrimitiveBoolean` —— 2/8 个有
- `SplitImageWithAlpha` —— 2/8 个有
- `VOSR2ModelLoader` —— 2/8 个有
- `VOSR2Upscale` —— 2/8 个有
- `easy float` —— 2/8 个有
- `easy int` —— 2/8 个有
- `CompressImages` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
