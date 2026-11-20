---
name: text_to_image_controlnet_sampler_clip_30
type: Text To Image
frequency: 3
level: moderate
coverage: 0.809667
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, KSampler, LoadImage, PreviewImage, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/基础SD图像生成工作流（新手版）_2052222515711361026.json, 平台全量/Simple Style Transfer with ControlNet + IPAdapter_1887078080589230082.json, "平台全量/XXL,IPA风格迁移电商工作流_1924004454260273154.json"]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_30

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/基础SD图像生成工作流（新手版）_2052222515711361026.json、平台全量/Simple Style Transfer with ControlNet + IPAdapter_1887078080589230082.json、平台全量/XXL,IPA风格迁移电商工作流_1924004454260273154.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 2/3 个有
- `DepthAnythingPreprocessor` —— 2/3 个有
- `IPAdapterAdvanced` —— 2/3 个有
- `IPAdapterUnifiedLoader` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `TilePreprocessor` —— 1/3 个有
- `VAEEncode` —— 1/3 个有
- `VAELoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.8 | 0.6 - 1 | 3 | 80% |
| 宽度 | 768 | 768 - 792 | 3 | 99% |
| 高度 | 1344 | 1280 - 1448 | 3 | 95% |
| 采样步数 | 8 | 5 - 25 | 3 | 30% |
| Prompt 约束强度(CFG) | 2 | 1.5 - 5 | 3 | 45% |
| 采样算法 | euler_ancestral | - | 3 | 33% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.8，观测区间 0.6 - 1，3 个样本
- 宽度 中位数 768，观测区间 768 - 792，3 个样本，取值集中（一致性 99%）
- 高度 中位数 1344，观测区间 1280 - 1448，3 个样本，取值集中（一致性 95%）
- 采样步数 中位数 8，观测区间 5 - 25，3 个样本，取值分散，一致性仅 30%
- Prompt 约束强度(CFG) 中位数 2，观测区间 1.5 - 5，3 个样本，取值分散，一致性仅 45%
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 33%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
