---
name: text_to_image_sampler_clip_checkpoint_4
type: Text To Image
frequency: 19
level: moderate
coverage: 0.988158
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: [easy cleanGpuUsed, easy positive]
members: [图片生成/文生图/1955202232166727682.json, 图片生成/文生图/1955947044106108930.json, 图片生成/文生图/black_2069832138584842241.json, 图片生成/文生图/cat_2069832508115607553.json, 图片生成/文生图/girl_2069831968304488450.json, 图片生成/文生图/grass_2069806965517283330.json, 图片生成/文生图/ground_2069833349966942209.json, 图片生成/文生图/ip形象_2064388541148385281.json, 图片生成/文生图/创新艺术_2064382794180161538.json, 图片生成/文生图/创新艺术_2069077816934748161.json, 图片生成/文生图/文生图2_2001532648583491585.json, 图片生成/文生图/星河_2064389839939792898.json, 图片生成/文生图/水墨_2064375871598845954.json, 图片生成/文生图/白绿插画_2064386951142268930.json, 图片生成/文生图/白色新式水墨_2064384907228573697.json, 图片生成/文生图/白金炫彩_2064380939660259329.json, 图片生成/文生图/红色_2064377423529074690.json, 图片生成/文生图/绿色_2064378897935978498.json, 视频生成/文生视频/幽蓝_2064370709702467586.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_4

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/文生图/1955202232166727682.json、图片生成/文生图/1955947044106108930.json、图片生成/文生图/black_2069832138584842241.json、图片生成/文生图/cat_2069832508115607553.json、图片生成/文生图/girl_2069831968304488450.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 18/19 个有
- `LoraLoader|pysssss` —— 11/19 个有
- `easy cleanGpuUsed` —— 2/19 个有
- `ImpactWildcardProcessor` —— 1/19 个有
- `TT_img_enc` —— 1/19 个有
- `easy positive` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 19 | 94% |
| Prompt 约束强度(CFG) | 8 | 7 - 8 | 19 | 97% |
| 采样算法 | dpmpp_2m | - | 19 | 84% |
| 调度器 | karras | - | 19 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |
| LoRA 模型强度 | 0.155 | 0.09 - 0.9 | 18 | 13% |
| LoRA 文本强度 | 0.155 | 0.07 - 0.9 | 18 | 3% |
| 宽度 | 1288 | 512 - 1288 | 19 | 83% |
| 高度 | 720 | 720 - 1024 | 19 | 88% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，19 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 7 - 8，19 个样本，取值集中（一致性 97%）
- 采样算法 最常用 dpmpp_2m，19 个样本，一致性 84%
- 调度器 最常用 karras，19 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.155，观测区间 0.09 - 0.9，18 个样本，取值分散，一致性仅 13%
- LoRA 文本强度 中位数 0.155，观测区间 0.07 - 0.9，18 个样本，取值分散，一致性仅 3%
- 宽度 中位数 1288，观测区间 512 - 1288，19 个样本，取值集中（一致性 83%）
- 高度 中位数 720，观测区间 720 - 1024，19 个样本，取值集中（一致性 88%）
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed、easy positive
