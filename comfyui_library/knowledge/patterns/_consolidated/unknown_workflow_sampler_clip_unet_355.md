---
name: unknown_workflow_sampler_clip_unet_355
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.907
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-Image-Turbo + LORA，三秒定制个人3D卡通头像！_1997282565021188098.json, "图片生成/文生图/Z-Image+LLM反推洗图工作流,彻底解放_1993900840161312770.json", 图片生成/文生图/文生图大模型DeepSeek时刻！Z-Image宣判封顶！家用显卡就能运行！_1995826953766723586.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_355

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Z-Image-Turbo + LORA，三秒定制个人3D卡通头像！_1997282565021188098.json、图片生成/文生图/Z-Image+LLM反推洗图工作流,彻底解放_1993900840161312770.json、图片生成/文生图/文生图大模型DeepSeek时刻！Z-Image宣判封顶！家用显卡就能运行！_1995826953766723586.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `AILab_QwenVL` —— 1/3 个有
- `Qwen3_VQA` —— 1/3 个有
- `Text` —— 1/3 个有
- `easy indexAnything` —— 1/3 个有
- `string_util_StrConcat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 9 | 3 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_multistep | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 9，3 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
