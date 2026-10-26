---
name: image_to_image_lora_sampler_unet_115
type: Image To Image
frequency: 6
level: strong
coverage: 0.885
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/胡文的服装设计_2043927068303433730.json, 图片生成/图生图/调整镜头方向Qwen 2511_2037043928532262913.json, 图片生成/图生图/镜头控制Qwen_2511_2049396359823892482.json, 图片生成/图生图/👾怪獸-人物道具场景多视角加速版👾_2058103710215131137.json, 图片生成/图生图/🦖2511可视化重打灯光_2011613758954676226.json, 视频生成/图生视频/QWEN imageEdit拍摄视角选择器_2010896559696777218.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_115

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/胡文的服装设计_2043927068303433730.json、图片生成/图生图/调整镜头方向Qwen 2511_2037043928532262913.json、图片生成/图生图/镜头控制Qwen_2511_2049396359823892482.json、图片生成/图生图/👾怪獸-人物道具场景多视角加速版👾_2058103710215131137.json、图片生成/图生图/🦖2511可视化重打灯光_2011613758954676226.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
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
- `EmptySD3LatentImage` —— 5/6 个有
- `ImageScaleToTotalPixels` —— 5/6 个有
- `easy showAnything` —— 5/6 个有
- `QwenMultiangleCameraNode` —— 4/6 个有
- `easy promptList` —— 3/6 个有
- `Comfly_LLm_API` —— 1/6 个有
- `Comfly_api_set` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `ProcessString` —— 1/6 个有
- `QwenMultiangleLightningNode` —— 1/6 个有
- `easy promptLine` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 6 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
