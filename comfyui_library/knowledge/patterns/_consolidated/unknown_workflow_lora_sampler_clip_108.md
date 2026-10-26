---
name: unknown_workflow_lora_sampler_clip_108
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8182
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, Image Comparer (rgthree), ImpactSwitch, KSampler, LoadAndResizeImage, LoraLoader, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, RH_Translator, ReferenceLatent, RepeatLatentBatch, SaveImage, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/kontext+LLM超强人物一致性多角度可选_1948644635007692801.json, 图片生成/图生图/kontext之 一致性多角度生成_1943631912818933762.json, 图片生成/图生图/【最新】Flux 角色多角度生成_1956569197809684482.json, 图片生成/图生图/模特人物一致性｜多角度生成_1947258078280437761.json, 图片生成/文生图/一张图生成多角度姿势-Kontext人物一致性_1953657920561053698.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_108

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/kontext+LLM超强人物一致性多角度可选_1948644635007692801.json、图片生成/图生图/kontext之 一致性多角度生成_1943631912818933762.json、图片生成/图生图/【最新】Flux 角色多角度生成_1956569197809684482.json、图片生成/图生图/模特人物一致性｜多角度生成_1947258078280437761.json、图片生成/文生图/一张图生成多角度姿势-Kontext人物一致性_1953657920561053698.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `ImpactSwitch`
- `KSampler`
- `LoadAndResizeImage`
- `LoraLoader`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `RH_Translator`
- `ReferenceLatent`
- `RepeatLatentBatch`
- `SaveImage`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Primitive integer [Crystools]` —— 4/5 个有
- `TTP_text_mix` —— 4/5 个有
- `ImageConcanate` —— 3/5 个有
- `PreviewImage` —— 1/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有
- `TeaCache` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
