---
name: image_to_image_sampler_clip_unet_147
type: Image To Image
frequency: 3
level: strong
coverage: 0.872
common_nodes: [CLIPLoader, CLIPTextEncode, ImageResize+, KSampler, LoadImage, PathchSageAttentionKJ, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen洗图工作流_1979443021655740417.json, 图片生成/图生图/qwen的洗图工作流_1991484394913406977.json, 图片生成/图生图/wan2.2洗图工作流_1979432161042403329.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_147

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/qwen洗图工作流_1979443021655740417.json、图片生成/图生图/qwen的洗图工作流_1991484394913406977.json、图片生成/图生图/wan2.2洗图工作流_1979432161042403329.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResize+`
- `KSampler`
- `LoadImage`
- `PathchSageAttentionKJ`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JanusImage2Text` —— 2/3 个有
- `LoadJanusModel` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Joy_caption_two` —— 1/3 个有
- `Joy_caption_two_load` —— 1/3 个有
- `LoraLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 10 | 3 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 0.5 | 0.5 - 0.52 | 3 | 98% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 0.5，观测区间 0.5 - 0.52，3 个样本，取值集中（一致性 98%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
