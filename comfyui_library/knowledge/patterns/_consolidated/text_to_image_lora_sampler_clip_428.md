---
name: text_to_image_lora_sampler_clip_428
type: Text To Image
frequency: 4
level: strong
coverage: 0.9115
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, QwenMultiangleCameraNode, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/多视角控制_镜头自由调节-Qwen edit工作流_2017864655183552513.json, 图片生成/图生图/多角度分镜生成(产品_摄影_物体)_2009817242749374466.json, 图片生成/图生图/多角度生成器API专用_2010378160902246401.json, 图片生成/图生图/多角度视图（qwen-image-edit-2511）_2010197243218890753.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_428

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/多视角控制_镜头自由调节-Qwen edit工作流_2017864655183552513.json、图片生成/图生图/多角度分镜生成(产品_摄影_物体)_2009817242749374466.json、图片生成/图生图/多角度生成器API专用_2010378160902246401.json、图片生成/图生图/多角度视图（qwen-image-edit-2511）_2010197243218890753.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenMultiangleCameraNode`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `CFGNorm` —— 1/4 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `KepStringList` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `SeedVR2` —— 1/4 个有
- `SeedVR2BlockSwap` —— 1/4 个有
- `SeedVR2ExtraArgs` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy promptList` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 512 - 1280 | 4 | 69% |
| 高度 | 720 | 512 - 720 | 4 | 87% |
| 采样步数 | 8 | 5 - 8 | 4 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1280，观测区间 512 - 1280，4 个样本
- 高度 中位数 720，观测区间 512 - 720，4 个样本，取值集中（一致性 87%）
- 采样步数 中位数 8，观测区间 5 - 8，4 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
