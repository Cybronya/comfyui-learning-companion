---
name: image_to_image_sampler_clip_unet_12
type: Image To Image
frequency: 18
level: strong
coverage: 0.918111
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/快速局部洗图_2064549413913194497.json, 图片生成/图生图/性感女讲师Flux2-Klein真实人像质感御姐美女_2040763565157654529.json, 图片生成/图生图/性感有韵味Flux2-Klein真实人像质感御姐美女_2040761141458116610.json, 图片生成/图生图/成熟有气质Flux2-Klein真实人像质感御姐美女_2040715025081438209.json, 图片生成/图生图/旗袍系列Flux2-Klein图生图真实人像质感御姐美女_2051608781892661250.json, 图片生成/图生图/昏暗灯光Flux2-Klein真实人像质感御姐美女_2040744156737310722.json, 图片生成/图生图/晚礼服Flux2-Klein真实人像质感御姐美女_2040741370549248002.json, 图片生成/图生图/欧式美女Flux2-Klein真实人像质感御姐美女_2040718407485628417.json, 图片生成/图生图/泳装系列Flux2-Klein真实人像质感御姐美女_2040441076468682754.json, 图片生成/图生图/现代客厅美女Flux2-Klein真实人像质感御姐美女_2040738759880216577.json, 图片生成/图生图/真实人像质感御姐美女_2040672256346562561.json, 图片生成/图生图/短裤Flux2-Klein真实人像质感御姐美女_2040682552553381889.json, 图片生成/图生图/立体立绘Flux2-Klein真实人像质感御姐美女_2040764640174542850.json, 图片生成/图生图/粉色长发Flux2-Klein真实人像质感御姐美女_2040766562637975553.json, 图片生成/图生图/系列Flux2-Klein真实人像质感御姐美女_2040668510103277570.json, 图片生成/图生图/美女写真图Flux2-Klein真实人像质感御姐美女_2040710445329289217.json, 图片生成/图生图/蕾丝内衣Flux2-Klein真实人像质感御姐美女_2040700533031309313.json, 图片生成/文生图/FLUX2-klein-水墨画油画2K出图_2013976365732728834.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_12

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/快速局部洗图_2064549413913194497.json、图片生成/图生图/性感女讲师Flux2-Klein真实人像质感御姐美女_2040763565157654529.json、图片生成/图生图/性感有韵味Flux2-Klein真实人像质感御姐美女_2040761141458116610.json、图片生成/图生图/成熟有气质Flux2-Klein真实人像质感御姐美女_2040715025081438209.json、图片生成/图生图/旗袍系列Flux2-Klein图生图真实人像质感御姐美女_2051608781892661250.json…）

- **类型**：Image To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 16/18 个有
- `scale` —— 16/18 个有
- `ImageResize+` —— 2/18 个有
- `ImageCompare` —— 1/18 个有
- `ImpactSwitch` —— 1/18 个有
- `LatentUpscaleBy` —— 1/18 个有
- `PrimitiveString` —— 1/18 个有
- `ReferenceLatent` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 18 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | beta | - | 18 | 89% |
| 重绘幅度 | 0.3 | 0.3 - 1 | 18 | 53% |
| LoRA 模型强度 | 0.8 | 0.8 - 0.8 | 16 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，18 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 89%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 1，18 个样本
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 0.8，16 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（18/18 个样本）：Steps较低可能导致细节不足
