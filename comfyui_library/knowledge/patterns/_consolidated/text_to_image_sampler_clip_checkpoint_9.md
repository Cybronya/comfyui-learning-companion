---
name: text_to_image_sampler_clip_checkpoint_9
type: Text To Image
frequency: 10
level: moderate
coverage: 1
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/SD1.5使用wildcard随机更换画面元素_1955202232166727682.json, 图片生成/文生图/SD1.5官方文生图工作流_1989688004904185857.json, 图片生成/文生图/SD1.5文生图(教学用)_1955947044106108930.json, 图片生成/文生图/国画_2055308067151073282.json, 图片生成/文生图/字体设计_2069831680575238146.json, 图片生成/文生图/尘白禁区_二次元_2049892451862753282.json, 图片生成/文生图/御姐_2069833373064982529.json, 图片生成/文生图/手鞠_2106608817659277314.json, 图片生成/文生图/文字_2069832301265113090.json, 图片生成/文生图/文生图2_2001532648583491585.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_9

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/SD1.5使用wildcard随机更换画面元素_1955202232166727682.json、图片生成/文生图/SD1.5官方文生图工作流_1989688004904185857.json、图片生成/文生图/SD1.5文生图(教学用)_1955947044106108930.json、图片生成/文生图/国画_2055308067151073282.json、图片生成/文生图/字体设计_2069831680575238146.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 8/10 个有
- `easy cleanGpuUsed` —— 2/10 个有
- `ImpactWildcardProcessor` —— 1/10 个有
- `TT_img_enc` —— 1/10 个有
- `easy positive` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 10 | 92% |
| Prompt 约束强度(CFG) | 8 | 5 - 8 | 10 | 88% |
| 采样算法 | dpmpp_2m | - | 10 | 50% |
| 调度器 | karras | - | 10 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| LoRA 模型强度 | 0.31 | -0.12 - 0.9 | 8 | 17% |
| LoRA 文本强度 | 0.44 | 0.14 - 0.9 | 8 | 41% |
| 宽度 | 1156 | 512 - 1288 | 10 | 70% |
| 高度 | 720 | 512 - 1536 | 10 | 68% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，10 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 5 - 8，10 个样本，取值集中（一致性 88%）
- 采样算法 最常用 dpmpp_2m，10 个样本，一致性 50%
- 调度器 最常用 karras，10 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.31，观测区间 -0.12 - 0.9，8 个样本，取值分散，一致性仅 17%
- LoRA 文本强度 中位数 0.44，观测区间 0.14 - 0.9，8 个样本，取值分散，一致性仅 41%
- 宽度 中位数 1156，观测区间 512 - 1288，10 个样本
- 高度 中位数 720，观测区间 512 - 1536，10 个样本
