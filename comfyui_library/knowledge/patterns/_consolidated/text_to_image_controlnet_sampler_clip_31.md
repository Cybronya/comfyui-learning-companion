---
name: text_to_image_controlnet_sampler_clip_31
type: Text To Image
frequency: 3
level: moderate
coverage: 0.926333
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, KSampler, LoadImage, PreviewImage, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/人物肖像 6宫格_1914704238478356481.json, 数字人/数字人/openpose_1971765145414397953.json, 视频生成/文生视频/ControlNet预处理器_2016518079005593601.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_31

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/人物肖像 6宫格_1914704238478356481.json、数字人/数字人/openpose_1971765145414397953.json、视频生成/文生视频/ControlNet预处理器_2016518079005593601.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

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
- `GetImageSize` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `Canny` —— 1/3 个有
- `DWPreprocessor` —— 1/3 个有
- `IPAdapterFaceID` —— 1/3 个有
- `IPAdapterUnifiedLoaderFaceID` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 0.9 - 1 | 3 | 95% |
| 采样步数 | 20 | 5 - 25 | 3 | 49% |
| Prompt 约束强度(CFG) | 6.5 | 1.8 - 8 | 3 | 51% |
| 采样算法 | dpmpp_sde | - | 3 | 33% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 768 | 512 - 1024 | 3 | 73% |
| 高度 | 1024 | 512 - 1024 | 3 | 72% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 0.9 - 1，3 个样本，取值集中（一致性 95%）
- 采样步数 中位数 20，观测区间 5 - 25，3 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 6.5，观测区间 1.8 - 8，3 个样本
- 采样算法 最常用 dpmpp_sde，3 个样本，一致性 33%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 512 - 1024，3 个样本
- 高度 中位数 1024，观测区间 512 - 1024，3 个样本
