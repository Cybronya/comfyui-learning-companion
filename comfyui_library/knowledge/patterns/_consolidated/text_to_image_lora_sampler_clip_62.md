---
name: text_to_image_lora_sampler_clip_62
type: Text To Image
frequency: 13
level: strong
coverage: 0.731462
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, PixaromaGroupSwitch, QwenImage21Cache, QwenPERewriteT8, SaveImage, SaveImageAdvanced, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: [CR Text Concatenate, Fast Bypasser (rgthree), LayerUtility: ImageScaleByAspectRatio V2, Mute / Bypass Repeater (rgthree), CR Prompt Text]
members: [图片生成/反推提示词/Qwen Image 2.1图像编辑V1.0｜2026开源最强模型图生图工作流_2104509451624603649.json, 图片生成/反推提示词/Qwen Image 2.1图生图图像编辑2026开源最强模型工作流，文生图图生图方案_2107156037143982082.json, 图片生成/反推提示词/Qwen Image 2.1图生图图像编辑工作流，2026开源最强模型多场景覆盖方案_2106067768159326209.json, 图片生成/反推提示词/Qwen Image 2.1文生图2026开源最强模型工作流，高质量文本到图像生成方案_2107157719223455746.json, 图片生成/反推提示词/Qwen Image 2.1文生图工作流V1.0｜2026开源最强模型高质量出图_2104514477067694082.json, 图片生成/反推提示词/开源最强模型Qwen Image 2.1文生图工作流V1.0｜文生图反推一应俱全_2106917950035947522.json, 图片生成/图生图/2106067768159326209.json, 图片生成/文生图/Qwen Image 2.1图像编辑V1.0｜2026开源最强模型图生图工作流_2104509451624603649.json, 图片生成/文生图/Qwen Image 2.1图像编辑工作流｜文生图反推提示词图生图_2108397884294127617.json, 图片生成/文生图/Qwen Image 2.1图生图编辑神器｜2026开源最强图像处理_2108410842583752705.json, 图片生成/文生图/Qwen Image 2.1文生图工作流V1.0｜2026开源最强模型高质量出图_2104514477067694082.json, 图片生成/文生图/Qwen Image 2.1海报生成专属工作流，文生图海报制作字体文本到图像方案_2107585434829279233.json, 视频生成/图生视频/开源最强模型Qwen_Image_2.1文生图工作流V1.0｜文生图反推一应俱全_2108366475907133441.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_62

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image 2.1图像编辑V1.0｜2026开源最强模型图生图工作流_2104509451624603649.json、图片生成/反推提示词/Qwen Image 2.1图生图图像编辑2026开源最强模型工作流，文生图图生图方案_2107156037143982082.json、图片生成/反推提示词/Qwen Image 2.1图生图图像编辑工作流，2026开源最强模型多场景覆盖方案_2106067768159326209.json、图片生成/反推提示词/Qwen Image 2.1文生图2026开源最强模型工作流，高质量文本到图像生成方案_2107157719223455746.json、图片生成/反推提示词/Qwen Image 2.1文生图工作流V1.0｜2026开源最强模型高质量出图_2104514477067694082.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 13 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PixaromaGroupSwitch`
- `QwenImage21Cache`
- `QwenPERewriteT8`
- `SaveImage`
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Fast Bypasser (rgthree)` —— 12/13 个有
- `Mute / Bypass Repeater (rgthree)` —— 12/13 个有
- `孤海注释` —— 12/13 个有
- `GetNode` —— 8/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/13 个有
- `ResolutionSelector` —— 8/13 个有
- `SetNode` —— 8/13 个有
- `ShowText|pysssss` —— 8/13 个有
- `CR Text Concatenate` —— 7/13 个有
- `Fast Groups Muter (rgthree)` —— 7/13 个有
- `PixaromaResolution` —— 6/13 个有
- `PreviewAny` —— 6/13 个有
- `llama_cpp_instruct_adv` —— 4/13 个有
- `llama_cpp_model_loader` —— 4/13 个有
- `llama_cpp_parameters` —— 4/13 个有
- `ModelAttentionBackend` —— 2/13 个有
- `EmptyImage` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `VRAM_Debug` —— 1/13 个有

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
| Steps较低可能导致细节不足 | 25/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（25/13 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Concatenate、Fast Bypasser (rgthree)、LayerUtility: ImageScaleByAspectRatio V2、Mute / Bypass Repeater (rgthree)、CR Prompt Text
