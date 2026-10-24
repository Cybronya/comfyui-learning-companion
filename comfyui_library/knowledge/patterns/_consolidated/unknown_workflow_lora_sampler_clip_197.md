---
name: unknown_workflow_lora_sampler_clip_197
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.744333
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2512 风格化 二次元_2006545169251831809.json, 图片生成/文生图/Qwen-Image-2512自动提示词优化版工作流_2006331950679724033.json, 图片生成/文生图/qwen悬疑小说推文（批量）_1967615082098286594.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_197

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2512 风格化 二次元_2006545169251831809.json、图片生成/文生图/Qwen-Image-2512自动提示词优化版工作流_2006331950679724033.json、图片生成/文生图/qwen悬疑小说推文（批量）_1967615082098286594.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 2/3 个有
- `EmptySD3LatentImage` —— 2/3 个有
- `ImpactSwitch` —— 2/3 个有
- `TextBox` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Image Filter Adjustments` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `QwenImageLatentAspectRatio` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `easy promptLine` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 5 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 5，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
