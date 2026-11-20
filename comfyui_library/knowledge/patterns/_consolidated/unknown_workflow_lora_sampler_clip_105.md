---
name: unknown_workflow_lora_sampler_clip_105
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.7712
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoraLoaderModelOnly, PrimitiveStringMultiline, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_2512_360全景图一键生成_2084862528764604418.json, 图片生成/文生图/2030979258759258114.json, 图片生成/文生图/KREA2 TURBO 图图最强文生图工作流（提示词增强 + Krea2T 双增强）_2072516698963537921.json, 图片生成/文生图/MOSS-Image-SFT 加速一键开关版_2112030319821021185.json, 图片生成/文生图/黑丝的专属工作流_2090809889026306049.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_105

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen_2512_360全景图一键生成_2084862528764604418.json、图片生成/文生图/2030979258759258114.json、图片生成/文生图/KREA2 TURBO 图图最强文生图工作流（提示词增强 + Krea2T 双增强）_2072516698963537921.json、图片生成/文生图/MOSS-Image-SFT 加速一键开关版_2112030319821021185.json、图片生成/文生图/黑丝的专属工作流_2090809889026306049.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 4/5 个有
- `EmptySD3LatentImage` —— 4/5 个有
- `PrimitiveBoolean` —— 4/5 个有
- `PrimitiveFloat` —— 4/5 个有
- `PrimitiveInt` —— 4/5 个有
- `StringConcatenate` —— 4/5 个有
- `ModelSamplingAuraFlow` —— 3/5 个有
- `ComfyUI-Krea2T-Enhancer` —— 2/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `EmptyImage` —— 2/5 个有
- `Switch image [Crystools]` —— 2/5 个有
- `TextGenerate` —— 2/5 个有
- `ClipLoaderGGUF` —— 1/5 个有
- `EmptyFlux2LatentImage` —— 1/5 个有
- `Seed Everywhere` —— 1/5 个有
- `SkipLayerGuidanceDiTSimple` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 5 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 5 | 25% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，5 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，5 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（13/5 个样本）：Steps较低可能导致细节不足
