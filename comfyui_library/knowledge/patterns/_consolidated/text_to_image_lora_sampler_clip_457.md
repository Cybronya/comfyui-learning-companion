---
name: text_to_image_lora_sampler_clip_457
type: Text To Image
frequency: 4
level: moderate
coverage: 0.91325
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图案提取工作流_2036286682303045634.json, 图片生成/图生图/多视角控制_镜头自由调节-Qwen edit工作流_2017864655183552513.json, 图片生成/图生图/多角度分镜生成(产品_摄影_物体)_2009817242749374466.json, 图片生成/图生图/多角度生成器API专用_2010378160902246401.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_457

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/图案提取工作流_2036286682303045634.json、图片生成/图生图/多视角控制_镜头自由调节-Qwen edit工作流_2017864655183552513.json、图片生成/图生图/多角度分镜生成(产品_摄影_物体)_2009817242749374466.json、图片生成/图生图/多角度生成器API专用_2010378160902246401.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenMultiangleCameraNode` —— 3/4 个有
- `easy imageSize` —— 3/4 个有
- `GetNode` —— 1/4 个有
- `MaskToImage` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `easy imageRemBg` —— 1/4 个有
- `easy promptList` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 4 | 81% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1140 | 512 - 1280 | 4 | 69% |
| 高度 | 720 | 512 - 1504 | 4 | 56% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，4 个样本，取值集中（一致性 81%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1140，观测区间 512 - 1280，4 个样本
- 高度 中位数 720，观测区间 512 - 1504，4 个样本
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
