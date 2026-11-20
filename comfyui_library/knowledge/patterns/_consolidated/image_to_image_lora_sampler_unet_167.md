---
name: image_to_image_lora_sampler_unet_167
type: Image To Image
frequency: 4
level: strong
coverage: 0.979
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/成图以后再次bfs edit qwen 2511换脸_2034920099492143105.json, 图片生成/图生图/简单极速图片去水印_2027576063118811138.json, 图片生成/图生图/🔥Qwen Image Edit多角度相机控制：拖拽手柄即可生成96种摄像机角度_2010767191389507586.json, 图片生成/文生图/2030095760506753026.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_167

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/成图以后再次bfs edit qwen 2511换脸_2034920099492143105.json、图片生成/图生图/简单极速图片去水印_2027576063118811138.json、图片生成/图生图/🔥Qwen Image Edit多角度相机控制：拖拽手柄即可生成96种摄像机角度_2010767191389507586.json、图片生成/文生图/2030095760506753026.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 3/4 个有
- `FluxKontextMultiReferenceLatentMethod` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `CR Prompt Text` —— 2/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `EmptyLatentImage` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `QwenMultiangleCameraNode` —— 1/4 个有
- `RH_Nano_Banana_Image2Image` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `SeargePreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 4 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1920 | - | 1 | 100% |
| 高度 | 1080 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
