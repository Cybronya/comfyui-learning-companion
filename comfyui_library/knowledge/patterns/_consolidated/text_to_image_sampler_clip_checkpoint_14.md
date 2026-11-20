---
name: text_to_image_sampler_clip_checkpoint_14
type: Text To Image
frequency: 6
level: moderate
coverage: 0.9175
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, LoadImage, PulidEvaClipLoader, PulidInsightFaceLoader, PulidModelLoader, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/PuLID+IPAdapter官方工作流_风格转移_1930702764505280514.json, 图片生成/图生图/PuLID_官方工作流_基础工作流_1930702307548135426.json, 图片生成/图生图/【遇见AI】换脸之PuLID_2019297806829228034.json, 平台全量/Multiple Poses of Yourself from a Single Photo_1881228156521836546.json, 平台全量/PuLID+StyleTransfer_1893920487523921921.json, 平台全量/一张照片做电影女主_1842204148338229250.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_14

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/PuLID+IPAdapter官方工作流_风格转移_1930702764505280514.json、图片生成/图生图/PuLID_官方工作流_基础工作流_1930702307548135426.json、图片生成/图生图/【遇见AI】换脸之PuLID_2019297806829228034.json、平台全量/Multiple Poses of Yourself from a Single Photo_1881228156521836546.json、平台全量/PuLID+StyleTransfer_1893920487523921921.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
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
- `PreviewImage` —— 5/6 个有
- `ApplyPulid` —— 4/6 个有
- `Anything Everywhere3` —— 2/6 个有
- `ApplyPulidAdvanced` —— 2/6 个有
- `IPAdapterAdvanced` —— 2/6 个有
- `IPAdapterUnifiedLoader` —— 2/6 个有
- `Prompts Everywhere` —— 2/6 个有
- `RH_Prompter` —— 1/6 个有
- `SDXLPromptStylerAll` —— 1/6 个有
- `Text Input [Dream]` —— 1/6 个有
- `WD14Tagger|pysssss` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | 768 - 1024 | 6 | 86% |
| 高度 | 1024 | 1024 - 1024 | 6 | 100% |
| 采样步数 | 19 | 5 - 30 | 6 | 33% |
| Prompt 约束强度(CFG) | 3 | 1.2 - 6 | 6 | 42% |
| 采样算法 | dpmpp_2m | - | 6 | 50% |
| 调度器 | sgm_uniform | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 896，观测区间 768 - 1024，6 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 19，观测区间 5 - 30，6 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 3，观测区间 1.2 - 6，6 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 dpmpp_2m，6 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
