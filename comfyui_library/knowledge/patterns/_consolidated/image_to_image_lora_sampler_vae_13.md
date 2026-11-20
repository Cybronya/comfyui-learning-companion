---
name: image_to_image_lora_sampler_vae_13
type: Image To Image
frequency: 8
level: strong
coverage: 0.954625
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, Text Multiline, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader, easy promptLine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一张图生成（角色）lora数据集_1971063735693516801.json, 图片生成/图生图/人物镜头多角度展示_2007372715937767425.json, 图片生成/图生图/人物镜头多角度工作流_1995473495901581313.json, 图片生成/图生图/千问2509-人物镜头多角度展示_1994932012010102785.json, 图片生成/图生图/千问2509-人物镜头多角度展示_1998321817486000129.json, 图片生成/图生图/千问2509模型人物多镜头多角度展现_1995297236168978434.json, 图片生成/图生图/最强-人物不变+多角度写真生成【Qwen2511+lora】_2010916855375994882.json, 图片生成/图生图/超牛的一致性人物多角度展示流！_1995001388340064257.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_13

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/一张图生成（角色）lora数据集_1971063735693516801.json、图片生成/图生图/人物镜头多角度展示_2007372715937767425.json、图片生成/图生图/人物镜头多角度工作流_1995473495901581313.json、图片生成/图生图/千问2509-人物镜头多角度展示_1994932012010102785.json、图片生成/图生图/千问2509-人物镜头多角度展示_1998321817486000129.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImageEditPlus_lrzjason` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `CR Text` —— 1/8 个有
- `EmptySD3LatentImage` —— 1/8 个有
- `ImageListToImageBatch` —— 1/8 个有
- `ImageRemoveAlpha+` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有
- `NunchakuQwenImageDiTLoader` —— 1/8 个有
- `RH_LLMAPI_NODE` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
