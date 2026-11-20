---
name: text_to_image_lora_sampler_clip_365
type: Text To Image
frequency: 5
level: strong
coverage: 0.8686
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Gemma4 FT反推提示词 图片反推提示词生成工具_2099218768928006145.json, 图片生成/反推提示词/Gemma4视频FT微调流｜视频内容反推提示词更精准_2111768126886076417.json, 图片生成/反推提示词/Image2.5光影迁移重打光｜一键换光线换氛围光，画面光影重塑_2104512814172954625.json, 图片生成/反推提示词/Llama-cpp提示词反推工作流｜图像描述文字提取生成_2097096966701404161.json, 图片生成/反推提示词/Llama-cpp提示词反推｜看图直接反写咒语_2097154776684388353.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_365

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/反推提示词/Gemma4 FT反推提示词 图片反推提示词生成工具_2099218768928006145.json、图片生成/反推提示词/Gemma4视频FT微调流｜视频内容反推提示词更精准_2111768126886076417.json、图片生成/反推提示词/Image2.5光影迁移重打光｜一键换光线换氛围光，画面光影重塑_2104512814172954625.json、图片生成/反推提示词/Llama-cpp提示词反推工作流｜图像描述文字提取生成_2097096966701404161.json、图片生成/反推提示词/Llama-cpp提示词反推｜看图直接反写咒语_2097154776684388353.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `VHS_LoadVideo` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `GetVideoComponents` —— 2/5 个有
- `LoadVideo` —— 2/5 个有
- `SaveText|pysssss` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有
- `TextGenerate` —— 2/5 个有
- `llama_cpp_instruct_adv` —— 2/5 个有
- `llama_cpp_model_loader` —— 2/5 个有
- `llama_cpp_parameters` —— 2/5 个有
- `RH_RhartImageG25FlareImageToImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
