---
name: unknown_workflow_sampler_clip_vae
type: Unknown Workflow
frequency: 24
level: moderate
coverage: 0.915917
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/nunchaku-qwen-image_1959414093880963073.json, 图片生成/文生图/nunchaku-qwen-image_2073056140971298817.json, 图片生成/文生图/nunchaku_Qwen_image_1959965300433301506.json, 图片生成/文生图/nunkucha-qwen-image_1960520624663949314.json, 图片生成/文生图/ovis-image-文生图工作流_1997464079977627649.json, 图片生成/文生图/qwen Image2512-文生图片生成视觉海报平面设计-封装优化版_2092630964051734530.json, 图片生成/文生图/qwen image nunchaku加速_1963054435381522434.json, 图片生成/文生图/qwen-Image -nunchaku+lora_1963114884189884418.json, 图片生成/文生图/qwen-image_1959137346446897153.json, 图片生成/文生图/qwen-image文生图工笔画关羽_1953057914565103617.json, 图片生成/文生图/qwen-image文生图珐琅彩孙悟空_1953757506445213698.json, 图片生成/文生图/qwen-image文生图青花瓷黛玉_1953758140024147969.json, 图片生成/文生图/qwen文生图片（加速）_2003133550327209985.json, 图片生成/文生图/z_image-文生图_2018374992529985537.json, 图片生成/文生图/z_image_base_2016450301691174913.json, 图片生成/文生图/z_image_base_2019688358565384194.json, 图片生成/文生图/z_image_turbo_1994152061438722050.json, 图片生成/文生图/z_image_turbo_1994983879373152258.json, 图片生成/文生图/z_image_turbo_gap_focus_2015970628842557442.json, 图片生成/文生图/z_image_turbo_ultra_fast_1994239876770054145.json, 图片生成/文生图/z_image文生图工作流（内部教学）_2033253705268596738.json, 图片生成/文生图/z_image文生图工作流（真人直播间）_2046779750718377985.json, 图片生成/文生图/zimage 文生图工作流 Z-image_2037728300130377730.json, 图片生成/文生图/zimage+base+文生图+工作流_2074064661959503874.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/文生图/nunchaku-qwen-image_1959414093880963073.json、图片生成/文生图/nunchaku-qwen-image_2073056140971298817.json、图片生成/文生图/nunchaku_Qwen_image_1959965300433301506.json、图片生成/文生图/nunkucha-qwen-image_1960520624663949314.json、图片生成/文生图/ovis-image-文生图工作流_1997464079977627649.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 24 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 17/24 个有
- `NunchakuQwenImageDiTLoader` —— 7/24 个有
- `PathchSageAttentionKJ` —— 3/24 个有
- `NunchakuQwenImageLoraLoader1` —— 1/24 个有
- `PrimitiveStringMultiline` —— 1/24 个有
- `ResizeAndPadImage` —— 1/24 个有
- `Seed (rgthree)` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 50 | 24 | 38% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 5 | 24 | 50% |
| 采样算法 | euler | - | 24 | 79% |
| 调度器 | simple | - | 24 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 50，24 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 5，24 个样本
- 采样算法 最常用 euler，24 个样本，一致性 79%
- 调度器 最常用 simple，24 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
