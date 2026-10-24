---
name: image_to_image_lora_sampler_unet_186
type: Image To Image
frequency: 3
level: moderate
coverage: 0.819333
common_nodes: [CLIPLoader, CR Text, Fast Groups Bypasser (rgthree), GetImageSize, Image Comparer (rgthree), ImageResizeKJv2, KSampler, LoadImage, LoraLoader, ReferenceLatent, SaveImage, ShowText|pysssss, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, WD14Tagger|pysssss, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/图生图/全自动彩色总图生成工作流_2048602092713025537.json, 图片生成/图生图/全自动素模生成专业住宅效果图+cn控制工作流_2059581390613733378.json, 图片生成/图生图/全自动素模生成专业住宅效果图工作流_2059453336700674049.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_186

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/全自动彩色总图生成工作流_2048602092713025537.json、图片生成/图生图/全自动素模生成专业住宅效果图+cn控制工作流_2059581390613733378.json、图片生成/图生图/全自动素模生成专业住宅效果图工作流_2059453336700674049.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `ReferenceLatent`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WD14Tagger|pysssss`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `CannyEdgePreprocessor` —— 1/3 个有
- `ControlNetApplyAdvanced` —— 1/3 个有
- `ControlNetLoader` —— 1/3 个有
- `LayerUtility: TextJoin` —— 1/3 个有
- `MuyeTextEditOutput` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 0.88 - 1 | 3 | 94% |
| 采样步数 | 30 | 25 - 40 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 3 | 12% |
| 采样算法 | euler_cfg_pp | - | 3 | 67% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 0.75 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 0.88 - 1，3 个样本，取值集中（一致性 94%）
- 采样步数 中位数 30，观测区间 25 - 40，3 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，3 个样本，取值分散，一致性仅 12%
- 采样算法 最常用 euler_cfg_pp，3 个样本，一致性 67%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
