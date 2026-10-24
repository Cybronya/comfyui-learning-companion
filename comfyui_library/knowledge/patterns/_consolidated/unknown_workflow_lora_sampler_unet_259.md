---
name: unknown_workflow_lora_sampler_unet_259
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.715
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, Fast Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, QwenEditConfigPreparer, ReferenceLatent, SaveImage, Seed (rgthree), TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_Edit_2511 人物一键三视图V2 （支持动漫和写实）_2045489953752227842.json, 图片生成/图生图/多角度控制生图+Qwen_Edit_2511_2073359929259413506.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_259

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen_Edit_2511 人物一键三视图V2 （支持动漫和写实）_2045489953752227842.json、图片生成/图生图/多角度控制生图+Qwen_Edit_2511_2073359929259413506.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `Fast Bypasser (rgthree)`
- `FluxKontextMultiReferenceLatentMethod`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `QwenEditConfigPreparer`
- `ReferenceLatent`
- `SaveImage`
- `Seed (rgthree)`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `LayerUtility: ImageReel` —— 1/2 个有
- `LayerUtility: ImageReelComposit` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `QwenMultiangleCameraNode` —— 1/2 个有
- `SDXLEmptyLatentSizePicker+` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy promptList` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768x1344 (0.57) | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | lcm | - | 2 | 50% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 lcm，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
