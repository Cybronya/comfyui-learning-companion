---
name: text_to_image_lora_sampler_clip_49
type: Text To Image
frequency: 18
level: strong
coverage: 0.715722
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, PixaromaGroupSwitch, QwenImage21Cache, QwenPERewriteT8, SaveImage, SaveImageAdvanced, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen Image 2.1图像编辑V1.0｜2026开源最强模型图生图工作流_2104509451624603649.json, 图片生成/反推提示词/Qwen Image 2.1图生图图像编辑2026开源最强模型工作流，文生图图生图方案_2107156037143982082.json, 图片生成/反推提示词/Qwen Image 2.1图生图图像编辑工作流，2026开源最强模型多场景覆盖方案_2106067768159326209.json, 图片生成/反推提示词/Qwen Image 2.1文生图2026开源最强模型工作流，高质量文本到图像生成方案_2107157719223455746.json, 图片生成/反推提示词/Qwen Image 2.1文生图工作流V1.0｜2026开源最强模型高质量出图_2104514477067694082.json, 图片生成/反推提示词/开源最强模型Qwen Image 2.1文生图工作流V1.0｜文生图反推一应俱全_2106917950035947522.json, 图片生成/图生图/Qwen Image 2.1图像编辑2026开源最强模型V1.0工作流，反推提示词图生图方案_2108316718539034625.json, 图片生成/图生图/Qwen Image 2.1图像编辑V1.0增强｜十图编辑提示词优化_2108088006333784066.json, 图片生成/图生图/Qwen Image 2.1图像编辑V1.0｜2026开源最强带反推提示词_2108084985277272066.json, 图片生成/图生图/Qwen Image 2.1图像编辑全功能版｜反推提示词智能配文_2108092452891615233.json, 图片生成/图生图/Qwen Image 2.1多图编辑V1.0，角色一致性设计开源最强图生图_2112676635475533826.json, 图片生成/图生图/Qwen Image 2.1多图编辑V1.0｜角色一致性设计出图_2108091016531234818.json, 图片生成/图生图/开源最强模型Qwen_Image_2.1文生图工作流V1.0｜文生图反推一应俱全_2112364776969035777.json, 图片生成/文生图/Qwen Image 2.1图像编辑工作流｜文生图反推提示词图生图_2108397884294127617.json, 图片生成/文生图/Qwen Image 2.1图生图图像编辑2026开源最强模型工作流_2108630605763272706.json, 图片生成/文生图/Qwen Image 2.1图生图编辑神器｜2026开源最强图像处理_2108410842583752705.json, 图片生成/文生图/Qwen Image 2.1海报生成专属工作流，文生图海报制作字体文本到图像方案_2107585434829279233.json, 视频生成/图生视频/开源最强模型Qwen_Image_2.1文生图工作流V1.0｜文生图反推一应俱全_2108366475907133441.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_49

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image 2.1图像编辑V1.0｜2026开源最强模型图生图工作流_2104509451624603649.json、图片生成/反推提示词/Qwen Image 2.1图生图图像编辑2026开源最强模型工作流，文生图图生图方案_2107156037143982082.json、图片生成/反推提示词/Qwen Image 2.1图生图图像编辑工作流，2026开源最强模型多场景覆盖方案_2106067768159326209.json、图片生成/反推提示词/Qwen Image 2.1文生图2026开源最强模型工作流，高质量文本到图像生成方案_2107157719223455746.json、图片生成/反推提示词/Qwen Image 2.1文生图工作流V1.0｜2026开源最强模型高质量出图_2104514477067694082.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 18 个 workflow 都包含：
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
- `Fast Bypasser (rgthree)` —— 17/18 个有
- `Mute / Bypass Repeater (rgthree)` —— 17/18 个有
- `孤海注释` —— 16/18 个有
- `CR Text Concatenate` —— 13/18 个有
- `GetNode` —— 13/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 13/18 个有
- `ResolutionSelector` —— 13/18 个有
- `SetNode` —— 13/18 个有
- `ShowText|pysssss` —— 13/18 个有
- `Fast Groups Muter (rgthree)` —— 12/18 个有
- `PixaromaResolution` —— 6/18 个有
- `PreviewAny` —— 6/18 个有
- `llama_cpp_instruct_adv` —— 4/18 个有
- `llama_cpp_model_loader` —— 4/18 个有
- `llama_cpp_parameters` —— 4/18 个有
- `ModelAttentionBackend` —— 2/18 个有
- `EmptyImage` —— 1/18 个有
- `PreviewImage` —— 1/18 个有
- `VRAM_Debug` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 18 | 100% |
| 采样算法 | er_sde | - | 18 | 100% |
| 调度器 | beta | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 80 | 80 - 80 | 18 | 100% |
| 高度 | 80 | 80 - 80 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 35/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高发问题（35/18 个样本）：Steps较低可能导致细节不足
