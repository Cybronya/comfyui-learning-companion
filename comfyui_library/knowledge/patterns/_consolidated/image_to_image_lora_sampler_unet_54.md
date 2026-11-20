---
name: image_to_image_lora_sampler_unet_54
type: Image To Image
frequency: 12
level: strong
coverage: 0.89125
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/胡文的服装设计_2043927068303433730.json, 图片生成/图生图/调整镜头方向Qwen 2511_2037043928532262913.json, 图片生成/图生图/镜头控制Qwen_2511_2049396359823892482.json, 平台全量/5个视角_2010974721340346369.json, 平台全量/Qwen 2511 edit 多视角镜头拍摄 智能多角度生成 qwen image edit_2010617857817710593.json, "平台全量/Qwen Edit 2511+镜头多角度控制,一张图片变换多个角度_2019345368613396481.json", 平台全量/一转五_2017143196706414594.json, 平台全量/万物自由多角度相机控制 Qwen-Edit-2511  镜头自由调节 选择拍摄镜头调整   镜头选择_2013807532858413058.json, 平台全量/多角度场景_2039573087489892354.json, 平台全量/工作流千问篇7-Qwen千问-多角度角色三视图分镜工作流，漫剧神器_2026206861183164418.json, 平台全量/（柯基大佬版）2511+镜头选择_2068077457059700737.json, 视频生成/图生视频/QWEN imageEdit拍摄视角选择器_2010896559696777218.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_54

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/胡文的服装设计_2043927068303433730.json、图片生成/图生图/调整镜头方向Qwen 2511_2037043928532262913.json、图片生成/图生图/镜头控制Qwen_2511_2049396359823892482.json、平台全量/5个视角_2010974721340346369.json、平台全量/Qwen 2511 edit 多视角镜头拍摄 智能多角度生成 qwen image edit_2010617857817710593.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
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
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 11/12 个有
- `FluxKontextMultiReferenceLatentMethod` —— 11/12 个有
- `ImageScaleToTotalPixels` —— 11/12 个有
- `QwenMultiangleCameraNode` —— 11/12 个有
- `easy promptList` —— 9/12 个有
- `Comfly_LLm_API` —— 1/12 个有
- `Comfly_api_set` —— 1/12 个有
- `KepStringList` —— 1/12 个有
- `PreviewAny` —— 1/12 个有
- `ProcessString` —— 1/12 个有
- `easy promptLine` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 12 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
