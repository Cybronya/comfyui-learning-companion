---
name: image_to_image_sampler_clip_checkpoint_3
type: Image To Image
frequency: 11
level: moderate
coverage: 0.933455
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSampler, LoadImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/图生图初代_1990402124561473537.json, 图片生成/图生图/图生图基础款_1818199756517605377.json, 图片生成/图生图/图生图基础款_1826544955593773057.json, 图片生成/图生图/图生图基础款_1892828128472174593.json, 图片生成/图生图/图生图多张输出_1777998877958410241.json, 图片生成/图生图/接力帧净化_SD图生图_3050低显存_2061824613121880066.json, 图片生成/图生图/洗图去AI感_2050522040632913922.json, 图片生成/图生图/清透水润写实图生图+LORA_1982124639554019330.json, 图片生成/图生图/高清画质特写_2049892403997364226.json, 图片生成/图生图/麦橘写实图生图基础版-shure_1982102747661123585.json, 视频生成/文生视频/国风女孩_2055307573456326657.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_checkpoint_3

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/图生图初代_1990402124561473537.json、图片生成/图生图/图生图基础款_1818199756517605377.json、图片生成/图生图/图生图基础款_1826544955593773057.json、图片生成/图生图/图生图基础款_1892828128472174593.json、图片生成/图生图/图生图多张输出_1777998877958410241.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/11 个有
- `LoraLoader` —— 3/11 个有
- `RepeatLatentBatch` —— 3/11 个有
- `ConditioningAverage` —— 2/11 个有
- `easy cleanGpuUsed` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 11 | 93% |
| Prompt 约束强度(CFG) | 8 | 7 - 8 | 11 | 96% |
| 采样算法 | euler_ancestral | - | 11 | 45% |
| 调度器 | normal | - | 11 | 45% |
| 重绘幅度 | 0.51 | 0.22 - 1 | 11 | 55% |
| LoRA 模型强度 | 0.25 | 0.25 - 0.5 | 3 | 65% |
| LoRA 文本强度 | 0.54 | 0.27 - 1 | 3 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，11 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 7 - 8，11 个样本，取值集中（一致性 96%）
- 采样算法 最常用 euler_ancestral，11 个样本，一致性 45%
- 调度器 最常用 normal，11 个样本，一致性 45%
- 重绘幅度 中位数 0.51，观测区间 0.22 - 1，11 个样本
- LoRA 模型强度 中位数 0.25，观测区间 0.25 - 0.5，3 个样本
- LoRA 文本强度 中位数 0.54，观测区间 0.27 - 1，3 个样本
