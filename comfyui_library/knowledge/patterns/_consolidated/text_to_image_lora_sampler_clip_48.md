---
name: text_to_image_lora_sampler_clip_48
type: Text To Image
frequency: 15
level: strong
coverage: 0.8968
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: [CR Prompt Text]
members: [图片生成/图生图/2102222773492994049.json, 图片生成/图生图/2102260297569488898.json, 图片生成/图生图/2102268788170387457.json, 图片生成/图生图/2102270303454982146.json, 图片生成/图生图/2102277686113693698.json, 图片生成/图生图/2102283966899380226.json, 图片生成/图生图/2102285690850598914.json, 图片生成/图生图/2102290282900451330.json, 图片生成/图生图/2102320037234302977.json, 图片生成/图生图/2102321477453443073.json, 图片生成/图生图/2102483334352953345.json, 图片生成/图生图/2102516145378127874.json, 图片生成/图生图/2102559055175835650.json, 图片生成/图生图/2105851031333728258.json, 视频生成/图生视频/Qwen_Image_2.1图片编辑工作流，简洁高效的图生图处理方案_2105520911070875649.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_48

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/2102222773492994049.json、图片生成/图生图/2102260297569488898.json、图片生成/图生图/2102268788170387457.json、图片生成/图生图/2102270303454982146.json、图片生成/图生图/2102277686113693698.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 14/15 个有
- `TextEncodeQwenImage21` —— 14/15 个有
- `ComfySwitchNode` —— 12/15 个有
- `ResolutionSelector` —— 12/15 个有
- `孤海注释` —— 11/15 个有
- `TextGenerateLTX2Prompt` —— 8/15 个有
- `BatchImagesNode` —— 7/15 个有
- `SaveImageAdvanced` —— 5/15 个有
- `EmptyImage` —— 4/15 个有
- `PreviewImage` —— 4/15 个有
- `RHLLMChatNode` —— 3/15 个有
- `CR Prompt Text` —— 2/15 个有
- `PrimitiveStringMultiline` —— 2/15 个有
- `easy showAnything` —— 2/15 个有
- `Float` —— 1/15 个有
- `GetImageSize` —— 1/15 个有
- `RH_RhartImageG2ImageToImage` —— 1/15 个有
- `RTXVideoSuperResolution` —— 1/15 个有
- `StringConcatenate` —— 1/15 个有
- `TextInput_` —— 1/15 个有
- `ZNGB_ImageBatchMulti` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt Text
