---
name: text_to_image_lora_sampler_clip_407
type: Text To Image
frequency: 4
level: strong
coverage: 0.8605
common_nodes: [BatchImagesNode, CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageConcatMulti, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1 BFS换脸换头工作流，角色一致性图生图面部替换_2106134123172683777.json, 图片生成/图生图/Qwen Image 2.1 BFS换脸换头工作流，角色一致性图生图面部替换工具_2105787847952392193.json, 图片生成/图生图/Qwen Image 2.1 BFS换脸换头工作流，角色一致性图生图面部替换工具_2106129646071926786.json, 图片生成/图生图/Qwen Image 2.1多图编辑工作流，多张参考图同时编辑的图生图方案_2103201028756824065.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_407

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 BFS换脸换头工作流，角色一致性图生图面部替换_2106134123172683777.json、图片生成/图生图/Qwen Image 2.1 BFS换脸换头工作流，角色一致性图生图面部替换工具_2105787847952392193.json、图片生成/图生图/Qwen Image 2.1 BFS换脸换头工作流，角色一致性图生图面部替换工具_2106129646071926786.json、图片生成/图生图/Qwen Image 2.1多图编辑工作流，多张参考图同时编辑的图生图方案_2103201028756824065.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageConcatMulti`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImageGoohai` —— 3/4 个有
- `MuyeTextEditOutput` —— 3/4 个有
- `SplitImageWithAlpha` —— 3/4 个有
- `TextGenerate` —— 3/4 个有
- `VOSR2ModelLoader` —— 3/4 个有
- `VOSR2Upscale` —— 3/4 个有
- `ImpactConditionalBranch` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `TextGenerateLTX2Prompt` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
