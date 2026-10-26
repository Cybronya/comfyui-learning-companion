---
name: image_to_image_sampler_clip_vae_28
type: Image To Image
frequency: 7
level: strong
coverage: 0.792429
common_nodes: [Anything Everywhere, CFGNorm, CLIPLoader, CLIPTextEncode, FluxKontextImageScale, Image Comparer (rgthree), KSampler, LoadImage, ModelSamplingAuraFlow, PreviewImage, RH_Translator, SaveImage, Text, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit Plus 2509 风格一致性保持 Next Scene_1977589860267642882.json, 图片生成/图生图/Qwen 转换视角，多角度，双截棍_1982415074893668353.json, 图片生成/图生图/一键Q版。中头，大头，超大头_1986366470634565633.json, 图片生成/图生图/人物变Q版_1988519917018333186.json, 图片生成/图生图/千问 Qwen Image Edit  Plus 2509_1972112310963793922.json, 图片生成/图生图/千问图像编辑 2509 Qwen Edit Plus 8步加速 Lora版_1974660074465570818.json, 图片生成/图生图/视角转换 千问Qwen_1982427238756958209.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_28

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen Edit Plus 2509 风格一致性保持 Next Scene_1977589860267642882.json、图片生成/图生图/Qwen 转换视角，多角度，双截棍_1982415074893668353.json、图片生成/图生图/一键Q版。中头，大头，超大头_1986366470634565633.json、图片生成/图生图/人物变Q版_1988519917018333186.json、图片生成/图生图/千问 Qwen Image Edit  Plus 2509_1972112310963793922.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 7 个 workflow 都包含：
- `Anything Everywhere`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RH_Translator`
- `SaveImage`
- `Text`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/7 个有
- `NunchakuQwenImageDiTLoader` —— 5/7 个有
- `LoraLoaderModelOnly` —— 4/7 个有
- `FluxEmptyLatentSizePicker` —— 2/7 个有
- `JjkText` —— 2/7 个有
- `NunchakuQwenImageLoraStack` —— 2/7 个有
- `QwenImageLatentAspectRatio` —— 2/7 个有
- `SDPoseOODLoader` —— 2/7 个有
- `SDPoseOODProcessor` —— 2/7 个有
- `UNETLoader` —— 2/7 个有
- `NunchakuQwenImageLoraStackV3` —— 1/7 个有
- `TextCombinerTwo` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 5 - 8 | 7 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1.5MP | - | 2 | 100% |
| 高度 | 16:9 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 5 - 8，7 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 最常用 1.5MP，2 个样本，一致性 100%
- 高度 最常用 16:9，2 个样本，一致性 100%
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
