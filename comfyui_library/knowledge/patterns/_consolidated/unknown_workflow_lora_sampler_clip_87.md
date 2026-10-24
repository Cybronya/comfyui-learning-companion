---
name: unknown_workflow_lora_sampler_clip_87
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.933167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TT_img_enc_v2, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-Image Turbo文生图_2016615447973601282.json, 图片生成/文生图/Z-Image 文生图（何君美女可灰度）_1998823040723079169.json, 图片生成/文生图/zimage base 文生图 工作流_2017488062816722946.json, 图片生成/文生图/夸张尺寸lora-Z-Image Turbo文生图_2017328560658194433.json, 图片生成/文生图/最新定制lora-Z-Image 文生图_2014062301778808834.json, 图片生成/文生图/重力下垂尺寸lora-Z-Image Turbo文生图_2018376234211741697.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_87

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Z-Image Turbo文生图_2016615447973601282.json、图片生成/文生图/Z-Image 文生图（何君美女可灰度）_1998823040723079169.json、图片生成/文生图/zimage base 文生图 工作流_2017488062816722946.json、图片生成/文生图/夸张尺寸lora-Z-Image Turbo文生图_2017328560658194433.json、图片生成/文生图/最新定制lora-Z-Image 文生图_2014062301778808834.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TT_img_enc_v2`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 5/6 个有
- `PathchSageAttentionKJ` —— 5/6 个有
- `Text` —— 5/6 个有
- `TwoWaySwitch` —— 5/6 个有
- `Float` —— 4/6 个有
- `VHS_Unbatch` —— 4/6 个有
- `CompressImages` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `EG_TSCDS_SRJK` —— 2/6 个有
- `Seed (rgthree)` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 36 | 6 | 32% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 6 | 25% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 36，6 个样本，取值分散，一致性仅 32%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，6 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
