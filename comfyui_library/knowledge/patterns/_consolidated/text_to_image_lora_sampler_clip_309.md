---
name: text_to_image_lora_sampler_clip_309
type: Text To Image
frequency: 7
level: moderate
coverage: 0.956714
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen文生图-正负提示词_1989381394365378562.json, 图片生成/文生图/Qwen文生图_1975417957952172034.json, 图片生成/文生图/Qwen文生图_2058621505726144513.json, 图片生成/文生图/Qwen文生图基础工作流_1989984703535083522.json, 图片生成/文生图/Universal text to image_2057220020123561985.json, 图片生成/文生图/Z image lora批量测试工作流_1998391849226264577.json, 图片生成/文生图/最强书法字体_2086663263693131777.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_309

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen文生图-正负提示词_1989381394365378562.json、图片生成/文生图/Qwen文生图_1975417957952172034.json、图片生成/文生图/Qwen文生图_2058621505726144513.json、图片生成/文生图/Qwen文生图基础工作流_1989984703535083522.json、图片生成/文生图/Universal text to image_2057220020123561985.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 5/7 个有
- `PathchSageAttentionKJ` —— 4/7 个有
- `ConditioningZeroOut` —— 3/7 个有
- `Int` —— 3/7 个有
- `JjkText` —— 3/7 个有
- `CFGNorm` —— 1/7 个有
- `CR Seed` —— 1/7 个有
- `CR Text Concatenate` —— 1/7 个有
- `TextEncodeQwenImageEditPlus` —— 1/7 个有
- `ttN advPlot images` —— 1/7 个有
- `ttN advanced xyPlot` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 10 | 7 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 7 | 69% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 800 | 512 - 1024 | 7 | 69% |
| 高度 | 1024 | 512 - 1536 | 7 | 55% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 10，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 800，观测区间 512 - 1024，7 个样本
- 高度 中位数 1024，观测区间 512 - 1536，7 个样本
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足
