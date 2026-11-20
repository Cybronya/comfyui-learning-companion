---
name: text_to_image_sampler_clip_checkpoint_6
type: Text To Image
frequency: 12
level: weak
coverage: 0.969917
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/flux文生图99_1969418975585202177.json, 图片生成/文生图/generate_image_2069748514313293826.json, 图片生成/文生图/girl_2069831968304488450.json, 图片生成/文生图/grass_2069806965517283330.json, 图片生成/文生图/ground_2069833349966942209.json, 图片生成/文生图/ip形象_2064388541148385281.json, 图片生成/文生图/jiami_test_2040045480884838401.json, 图片生成/文生图/new01_2046592687888928769.json, 图片生成/文生图/【AI小王子】10.文生图工作流_2046802677945868290.json, 图片生成/文生图/【AI小王子】20.LCM lora八步生成_2046843881974665218.json, 图片生成/文生图/仿真画风_2052371545665875969.json, 图片生成/文生图/儿童卡通绘本_1928363238206128129.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_6

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/flux文生图99_1969418975585202177.json、图片生成/文生图/generate_image_2069748514313293826.json、图片生成/文生图/girl_2069831968304488450.json、图片生成/文生图/grass_2069806965517283330.json、图片生成/文生图/ground_2069833349966942209.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 7/12 个有
- `LoraLoader|pysssss` —— 2/12 个有
- `PreviewImage` —— 2/12 个有
- `FluxGuidance` —— 1/12 个有
- `JjkText` —— 1/12 个有
- `LatentUpscaleBy` —— 1/12 个有
- `TextCombinerTwo` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 12 | 83% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 12 | 63% |
| 采样算法 | dpmpp_2m | - | 12 | 50% |
| 调度器 | karras | - | 12 | 58% |
| 重绘幅度 | 1 | 0.5 - 1 | 12 | 86% |
| 宽度 | 1024 | 512 - 1288 | 12 | 68% |
| 高度 | 720 | 512 - 1024 | 12 | 74% |
| LoRA 模型强度 | 0.25 | 0.09 - 1.15 | 7 | 10% |
| LoRA 文本强度 | 0.3 | 0.16 - 1 | 7 | 25% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，12 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，12 个样本
- 采样算法 最常用 dpmpp_2m，12 个样本，一致性 50%
- 调度器 最常用 karras，12 个样本，一致性 58%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，12 个样本，取值集中（一致性 86%）
- 宽度 中位数 1024，观测区间 512 - 1288，12 个样本
- 高度 中位数 720，观测区间 512 - 1024，12 个样本
- LoRA 模型强度 中位数 0.25，观测区间 0.09 - 1.15，7 个样本，取值分散，一致性仅 10%
- LoRA 文本强度 中位数 0.3，观测区间 0.16 - 1，7 个样本，取值分散，一致性仅 25%
