---
name: text_to_image_sampler_clip_checkpoint_20
type: Text To Image
frequency: 3
level: strong
coverage: 0.953667
common_nodes: [ApplyPulid, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, LoadImage, PulidEvaClipLoader, PulidInsightFaceLoader, PulidModelLoader, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/PuLID+IPAdapter官方工作流_风格转移_1930702764505280514.json, 图片生成/图生图/PuLID_官方工作流_基础工作流_1930702307548135426.json, 图片生成/图生图/【遇见AI】换脸之PuLID_2019297806829228034.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_20

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/PuLID+IPAdapter官方工作流_风格转移_1930702764505280514.json、图片生成/图生图/PuLID_官方工作流_基础工作流_1930702307548135426.json、图片生成/图生图/【遇见AI】换脸之PuLID_2019297806829228034.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyPulid`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PulidEvaClipLoader`
- `PulidInsightFaceLoader`
- `PulidModelLoader`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `IPAdapterAdvanced` —— 1/3 个有
- `IPAdapterUnifiedLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 1024 | 3 | 86% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | 30 | 30 - 30 | 3 | 100% |
| Prompt 约束强度(CFG) | 6 | 4 - 6 | 3 | 82% |
| 采样算法 | dpmpp_2m | - | 3 | 67% |
| 调度器 | sgm_uniform | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 1024，3 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 30 - 30，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 6，3 个样本，取值集中（一致性 82%）
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 67%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
