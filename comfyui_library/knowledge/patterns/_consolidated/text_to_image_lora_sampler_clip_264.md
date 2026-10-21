---
name: text_to_image_lora_sampler_clip_264
type: Text To Image
frequency: 4
level: weak
coverage: 0.83375
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyImage, EmptyLatentImage, INTConstant, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, PrimitiveStringMultiline, ResolutionSelector, SaveImage, ShowText|pysssss, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy seed, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen 2.1超细节洗图生图二合一，支持Qwen 3.5自由切换的反推提示词工作流_2102878744355627010.json, 图片生成/文生图/krea2 超细节增强 洗图生图2合1工作流（自由切换版）_qwen3.5😼_2077340261931380738.json, 图片生成/文生图/krea2 风格之王 全能模型 Qwen3.5自动提示词文生图工作流（自由版）_2070756328192172034.json, 视频生成/图生视频/Qwen_2.1超细节洗图生图二合一，支持Qwen_3.5自由切换的反推提示词工作流_2105120232384851969.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_264

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen 2.1超细节洗图生图二合一，支持Qwen 3.5自由切换的反推提示词工作流_2102878744355627010.json、图片生成/文生图/krea2 超细节增强 洗图生图2合1工作流（自由切换版）_qwen3.5😼_2077340261931380738.json、图片生成/文生图/krea2 风格之王 全能模型 Qwen3.5自动提示词文生图工作流（自由版）_2070756328192172034.json、视频生成/图生视频/Qwen_2.1超细节洗图生图二合一，支持Qwen_3.5自由切换的反推提示词工作流_2105120232384851969.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyImage`
- `EmptyLatentImage`
- `INTConstant`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `ShowText|pysssss`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `Switch any [Crystools]` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `Label (rgthree)` —— 2/4 个有
- `TextEncodeQwenImage21` —— 2/4 个有
- `TextGenerateLTX2Prompt` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `solarL_SaveImagesToZip` —— 2/4 个有
- `ConditioningKrea2Rebalance` —— 1/4 个有
- `LatentUpscaleBy` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 552 | 80 - 1024 | 4 | 14% |
| 高度 | 808 | 80 - 1536 | 4 | 10% |
| 采样步数 | 6 | 4 - 8 | 4 | 67% |
| Prompt 约束强度(CFG) | 2.75 | 1 - 4.5 | 4 | 36% |
| 采样算法 | er_sde | - | 4 | 50% |
| 调度器 | beta | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 552，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 14%
- 高度 中位数 808，观测区间 80 - 1536，4 个样本，取值分散，一致性仅 10%
- 采样步数 中位数 6，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 2.75，观测区间 1 - 4.5，4 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 er_sde，4 个样本，一致性 50%
- 调度器 最常用 beta，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
