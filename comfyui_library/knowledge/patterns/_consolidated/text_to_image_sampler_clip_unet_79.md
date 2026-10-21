---
name: text_to_image_sampler_clip_unet_79
type: Text To Image
frequency: 6
level: strong
coverage: 0.930833
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea 2 反推生图 +LoRA_2080138987389411330.json, 图片生成/文生图/Krea 2 甜美人像_2082369312555356161.json, 图片生成/文生图/Krea-2 高真实感与卓越美学文生图_2069683043954151426.json, 图片生成/文生图/Krea2-Cc-MJ-影视柔光_2094377283531395074.json, 图片生成/文生图/Z-image文生图奇幻风格_1997646513021104130.json, 图片生成/文生图/丰盈美女_2094380168788922369.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_79

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Krea 2 反推生图 +LoRA_2080138987389411330.json、图片生成/文生图/Krea 2 甜美人像_2082369312555356161.json、图片生成/文生图/Krea-2 高真实感与卓越美学文生图_2069683043954151426.json、图片生成/文生图/Krea2-Cc-MJ-影视柔光_2094377283531395074.json、图片生成/文生图/Z-image文生图奇幻风格_1997646513021104130.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `LoadImage` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `ImpactInt` —— 2/6 个有
- `ResolutionSelector` —— 2/6 个有
- `DownloadAndLoadFlorence2Model` —— 1/6 个有
- `Florence2Run` —— 1/6 个有
- `String Literal` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 832 - 1920 | 6 | 70% |
| 高度 | 1024 | 720 - 1216 | 6 | 85% |
| 采样步数 | 8 | 8 - 10 | 6 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 832 - 1920，6 个样本
- 高度 中位数 1024，观测区间 720 - 1216，6 个样本，取值集中（一致性 85%）
- 采样步数 中位数 8，观测区间 8 - 10，6 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
