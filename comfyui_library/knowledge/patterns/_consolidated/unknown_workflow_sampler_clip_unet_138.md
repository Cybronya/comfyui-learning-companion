---
name: unknown_workflow_sampler_clip_unet_138
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.9366
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/2030261410919354369.json, 图片生成/文生图/90后动漫风格-ZImage文生图_2018945323267268610.json, 图片生成/文生图/Flow-DPO LoRA工作流：AI人像终于不像塑料了！这个LoRA让光照秒变真实✨_2028104630768504833.json, 图片生成/文生图/Flow-DPO LoRA工作流：AI人像终于不像塑料了！这张照片太真实了_2028835652560756738.json, 图片生成/文生图/Qwen-Image-2512-Wuli_2007448165187854338.json, 图片生成/文生图/Qwen-Image-2512-lightx2v_2007448158065922050.json, 图片生成/文生图/Z-Image-Turbo文生图（OpenClaw远程控制版本）_2020379259021303809.json, 图片生成/文生图/【Z-Image-Turbo LoRA 一站式炼丹教程】手把手教你训练自己的猫咪LoRA，让自家猫咪“出现”在世界各地！_2004888505304182785.json, 图片生成/文生图/常用_图片_qwen2512文生图_2037710756266905602.json, 图片生成/文生图/文生图-qwen_image_2512-模板_2090689557934206978.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_138

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/2030261410919354369.json、图片生成/文生图/90后动漫风格-ZImage文生图_2018945323267268610.json、图片生成/文生图/Flow-DPO LoRA工作流：AI人像终于不像塑料了！这个LoRA让光照秒变真实✨_2028104630768504833.json、图片生成/文生图/Flow-DPO LoRA工作流：AI人像终于不像塑料了！这张照片太真实了_2028835652560756738.json、图片生成/文生图/Qwen-Image-2512-Wuli_2007448165187854338.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 9/10 个有
- `ConditioningZeroOut` —— 7/10 个有
- `Label (rgthree)` —— 4/10 个有
- `PrimitiveStringMultiline` —— 4/10 个有
- `easy seed` —— 3/10 个有
- `INTConstant` —— 1/10 个有
- `Image Comparer (rgthree)` —— 1/10 个有
- `MuyeTextEditOutput` —— 1/10 个有
- `StringFunction|pysssss` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 2 - 9 | 10 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 50% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 2 - 9，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 50%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（11/10 个样本）：Steps较低可能导致细节不足
