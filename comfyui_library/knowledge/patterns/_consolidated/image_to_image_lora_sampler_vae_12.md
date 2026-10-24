---
name: image_to_image_lora_sampler_vae_12
type: Image To Image
frequency: 6
level: strong
coverage: 0.725833
common_nodes: [CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, Text, TextEncodeQwenImageEdit, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【楚心钟陌】新鲜出炉，2511Edit，真人转动漫_2031425995810541569.json, 图片生成/图生图/【楚心钟陌】消除光影_2021960476623638530.json, 图片生成/图生图/【楚心钟陌】消除卧蚕+磨皮_2028423441262583810.json, 图片生成/图生图/【楚心钟陌】纸绘_2056783431174017025.json, 图片生成/图生图/【楚心钟陌】草稿化_2041465937550905345.json, 图片生成/图生图/【楚心钟陌】表情适配1.0_2028813392890306561.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_12

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/【楚心钟陌】新鲜出炉，2511Edit，真人转动漫_2031425995810541569.json、图片生成/图生图/【楚心钟陌】消除光影_2021960476623638530.json、图片生成/图生图/【楚心钟陌】消除卧蚕+磨皮_2028423441262583810.json、图片生成/图生图/【楚心钟陌】纸绘_2056783431174017025.json、图片生成/图生图/【楚心钟陌】草稿化_2041465937550905345.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `Text`
- `TextEncodeQwenImageEdit`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JoinStrings` —— 5/6 个有
- `LayerUtility: ImageReel` —— 5/6 个有
- `LayerUtility: ImageReelComposit` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `UNETLoader` —— 5/6 个有
- `AIO_Preprocessor` —— 4/6 个有
- `ControlNetApplyAdvanced` —— 4/6 个有
- `ControlNetLoader` —— 4/6 个有
- `SetUnionControlNetType` —— 4/6 个有
- `TextEncodeQwenImageEditPlus` —— 4/6 个有
- `FluxKontextMultiReferenceLatentMethod` —— 3/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `ImageScaleToMegapixels` —— 2/6 个有
- `RunningHub Deepcleaner` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `GetNode` —— 1/6 个有
- `Seed_` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `TextPreview` —— 1/6 个有
- `UnetLoaderGGUF` —— 1/6 个有
- `WujiCleaner` —— 1/6 个有
- `llama_cpp_instruct_adv` —— 1/6 个有
- `llama_cpp_model_loader` —— 1/6 个有
- `llama_cpp_unload_model` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 6 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | res_2m | - | 6 | 67% |
| 调度器 | simple | - | 6 | 33% |
| 重绘幅度 | 0.925 | 0.8 - 1 | 6 | 90% |
| ControlNet 权重 | 0.95 | 0.8 - 1 | 4 | 91% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2m，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 33%
- 重绘幅度 中位数 0.925，观测区间 0.8 - 1，6 个样本，取值集中（一致性 90%）
- ControlNet 权重 中位数 0.95，观测区间 0.8 - 1，4 个样本，取值集中（一致性 91%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
