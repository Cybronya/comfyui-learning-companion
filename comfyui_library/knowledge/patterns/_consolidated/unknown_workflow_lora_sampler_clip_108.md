---
name: unknown_workflow_lora_sampler_clip_108
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.747667
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoraLoaderModelOnly, PrimitiveStringMultiline, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_2512_360全景图一键生成_2084862528764604418.json, 图片生成/文生图/2030979258759258114.json, 图片生成/文生图/KREA2 TURBO 图图最强文生图工作流（提示词增强 + Krea2T 双增强）_2072516698963537921.json, 图片生成/文生图/MOSS-Image-SFT 加速一键开关版_2112030319821021185.json, 图片生成/文生图/黑丝的专属工作流_2090809889026306049.json, 平台全量/MOSS-CC街拍-加速一键开关版_2118708992510877698.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_108

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen_2512_360全景图一键生成_2084862528764604418.json、图片生成/文生图/2030979258759258114.json、图片生成/文生图/KREA2 TURBO 图图最强文生图工作流（提示词增强 + Krea2T 双增强）_2072516698963537921.json、图片生成/文生图/MOSS-Image-SFT 加速一键开关版_2112030319821021185.json、图片生成/文生图/黑丝的专属工作流_2090809889026306049.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 6 个 workflow 都包含：
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
- `ComfySwitchNode` —— 5/6 个有
- `PrimitiveBoolean` —— 5/6 个有
- `PrimitiveFloat` —— 5/6 个有
- `PrimitiveInt` —— 5/6 个有
- `StringConcatenate` —— 5/6 个有
- `EmptySD3LatentImage` —— 4/6 个有
- `ModelSamplingAuraFlow` —— 3/6 个有
- `ComfyUI-Krea2T-Enhancer` —— 2/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `EmptyFlux2LatentImage` —— 2/6 个有
- `EmptyImage` —— 2/6 个有
- `SkipLayerGuidanceDiTSimple` —— 2/6 个有
- `Switch image [Crystools]` —— 2/6 个有
- `TextGenerate` —— 2/6 个有
- `ClipLoaderGGUF` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `Seed Everywhere` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.5 | 8 - 50 | 6 | 14% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 6 | 34% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8.5，观测区间 8 - 50，6 个样本，取值分散，一致性仅 14%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，6 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（14/6 个样本）：Steps较低可能导致细节不足
