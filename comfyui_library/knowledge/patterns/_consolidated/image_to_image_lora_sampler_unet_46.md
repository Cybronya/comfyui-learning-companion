---
name: image_to_image_lora_sampler_unet_46
type: Image To Image
frequency: 11
level: strong
coverage: 0.944091
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image-2509-人物镜头多角度展示_1995104571196366850.json, 图片生成/图生图/Qwen-image-2511-Multiple-Angles-LoRA_2013960041979715586.json, 图片生成/图生图/Qwen-image-2511-人物镜头多角度展示_2006023840396218370.json, 图片生成/图生图/Qwen-参考姿态一键换装_1977201193661407234.json, 图片生成/图生图/Qwen-多角度切换_1994398890684190721.json, 图片生成/图生图/WH-AI-Studio-千问2511-一键人物镜头多角度展示（人物固定版）_2021135812963864577.json, 图片生成/图生图/WH-AI-Studio-千问2511-一键人物镜头多角度展示（脸部跟随版）_2015620861742555138.json, 图片生成/图生图/千问2509-人物镜头多角度展示_1994932012010102785.json, 图片生成/图生图/千问2509-人物镜头多角度展示_1998321817486000129.json, 图片生成/图生图/千问2509模型人物多镜头多角度展现_1995297236168978434.json, 图片生成/图生图/图像多角度转换——一张角色图生成多角度视角_1984598564712103937.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_46

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen-image-2509-人物镜头多角度展示_1995104571196366850.json、图片生成/图生图/Qwen-image-2511-Multiple-Angles-LoRA_2013960041979715586.json、图片生成/图生图/Qwen-image-2511-人物镜头多角度展示_2006023840396218370.json、图片生成/图生图/Qwen-参考姿态一键换装_1977201193661407234.json、图片生成/图生图/Qwen-多角度切换_1994398890684190721.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Text Multiline` —— 10/11 个有
- `easy promptLine` —— 10/11 个有
- `ImageScaleToTotalPixels` —— 9/11 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 8/11 个有
- `PreviewImage` —— 4/11 个有
- `AddLabel` —— 3/11 个有
- `ImageResizeKJv2` —— 2/11 个有
- `easy imageSize` —— 2/11 个有
- `Any Switch (rgthree)` —— 1/11 个有
- `Image Comparer (rgthree)` —— 1/11 个有
- `ImageConcatFromBatch` —— 1/11 个有
- `ImageListToImageBatch` —— 1/11 个有
- `Note Plus (mtb)` —— 1/11 个有
- `OpenposePreprocessor` —— 1/11 个有
- `ShowText|pysssss` —— 1/11 个有
- `easy imageListToImageBatch` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
