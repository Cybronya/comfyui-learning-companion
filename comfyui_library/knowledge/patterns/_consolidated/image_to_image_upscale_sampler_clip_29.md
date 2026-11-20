---
name: image_to_image_upscale_sampler_clip_29
type: Image To Image
frequency: 3
level: weak
coverage: 0.838333
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, Image Comparer (rgthree), KSampler, LoadImage, SaveImage, UpscaleModelLoader, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2 - 两阶放大工作流_1958760029983760385.json, 图片生成/图生图/图片放大基础工作流_中文提示词_1958048284105388034.json, 图片生成/图生图/多人合照老照片修复_1903361845489737730.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_29

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2 - 两阶放大工作流_1958760029983760385.json、图片生成/图生图/图片放大基础工作流_中文提示词_1958048284105388034.json、图片生成/图生图/多人合照老照片修复_1903361845489737730.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 2/3 个有
- `ImageUpscaleWithModel` —— 2/3 个有
- `RH_Translator` —— 2/3 个有
- `ChinesePrompt_Mix` —— 1/3 个有
- `ControlNetApply` —— 1/3 个有
- `ControlNetLoader` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `ReActorRestoreFace` —— 1/3 个有
- `UpscaleImageByUsingModel` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 6 - 10 | 3 | 78% |
| Prompt 约束强度(CFG) | 3 | 2 - 5 | 3 | 63% |
| 采样算法 | uni_pc_bh2 | - | 3 | 33% |
| 调度器 | normal | - | 3 | 33% |
| 重绘幅度 | 0.35 | 0.2 - 1 | 3 | 33% |
| ControlNet 权重 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 6 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 2 - 5，3 个样本
- 采样算法 最常用 uni_pc_bh2，3 个样本，一致性 33%
- 调度器 最常用 normal，3 个样本，一致性 33%
- 重绘幅度 中位数 0.35，观测区间 0.2 - 1，3 个样本，取值分散，一致性仅 33%
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
