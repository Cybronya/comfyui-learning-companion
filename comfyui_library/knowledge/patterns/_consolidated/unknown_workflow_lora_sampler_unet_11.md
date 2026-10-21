---
name: unknown_workflow_lora_sampler_unet_11
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.978364
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1963214327899721729.json, 图片生成/文生图/1988774900942909442.json, 图片生成/文生图/1988927261430648834.json, 图片生成/文生图/1989171870014517249.json, 图片生成/文生图/1989311154684129281.json, 图片生成/文生图/1989695013087047682.json, 图片生成/文生图/2511 多角度_2019257618123984898.json, 图片生成/文生图/71.tonnie-2512基础_2010330338651803650.json, 图片生成/文生图/Qwen Edit 2509新旅游飞机_1991073540537524226.json, 图片生成/文生图/Qwen Edit 2509未来科技_1990647676465274881.json, 图片生成/文生图/文生图对比Z-Image VS Qwen_2019752105942196226.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_11

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/1963214327899721729.json、图片生成/文生图/1988774900942909442.json、图片生成/文生图/1988927261430648834.json、图片生成/文生图/1989171870014517249.json、图片生成/文生图/1989311154684129281.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImageEditPlus` —— 10/11 个有
- `EmptyLatentImage` —— 8/11 个有
- `EmptySD3LatentImage` —— 3/11 个有
- `LoadImage` —— 3/11 个有
- `TextEncodeQwenImageEdit` —— 3/11 个有
- `CLIPTextEncode` —— 2/11 个有
- `AILab_QwenVL` —— 1/11 个有
- `ImageScaleBy` —— 1/11 个有
- `LoraLoader` —— 1/11 个有
- `PreviewAny` —— 1/11 个有
- `VAEEncode` —— 1/11 个有
- `easy promptLine` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 11 | 62% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 82% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 1152 | 1024 - 1280 | 8 | 89% |
| 高度 | 1024 | 720 - 1280 | 8 | 76% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 82%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 1152，观测区间 1024 - 1280，8 个样本，取值集中（一致性 89%）
- 高度 中位数 1024，观测区间 720 - 1280，8 个样本
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
