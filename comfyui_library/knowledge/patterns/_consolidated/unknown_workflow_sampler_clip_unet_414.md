---
name: unknown_workflow_sampler_clip_unet_414
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.952333
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, ImageResizeKJv2, KSampler, LoadImage, MathExpression|pysssss, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecodeTiled, VAELoader, Wan22ImageToVideoLatent]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/wan2.2-5B图生视频 官方工作流_1950030033369874433.json, 视频生成/图生视频/wan2.2-5B图生视频-ComfyUI官方_1950015509658034177.json, 视频生成/图生视频/wan2.2-TI2V-5B-ComfyUI官方_1949844295606034434.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_414

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/wan2.2-5B图生视频 官方工作流_1950030033369874433.json、视频生成/图生视频/wan2.2-5B图生视频-ComfyUI官方_1950015509658034177.json、视频生成/图生视频/wan2.2-TI2V-5B-ComfyUI官方_1949844295606034434.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `Wan22ImageToVideoLatent`

**可变部分**（部分 workflow 才有）：
- `Primitive integer [Crystools]` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `ConstrainImage|pysssss` —— 1/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `Int` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 3 | 89% |
| Prompt 约束强度(CFG) | 5 | 5 - 5 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 3/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：发现KSampler但没有VAEDecode
