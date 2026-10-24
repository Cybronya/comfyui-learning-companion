---
name: unknown_workflow_lora_sampler_unet_217
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.927333
common_nodes: [CLIPLoader, FluxKontextImageScale, FluxKontextMultiReferenceLatentMethod, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【🛫书墨】qwen-2511-单图、双图、三图任意切换工作流_2003710742723477505.json, 图片生成/图生图/扩图_2004013721959735298.json, 图片生成/文生图/qwen-2511-edit工作流_2011999736877813762.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_217

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/【🛫书墨】qwen-2511-单图、双图、三图任意切换工作流_2003710742723477505.json、图片生成/图生图/扩图_2004013721959735298.json、图片生成/文生图/qwen-2511-edit工作流_2011999736877813762.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `FluxKontextImageScale`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 2/3 个有
- `CFGNorm` —— 1/3 个有
- `EmptyLatentImage` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `ImagePadForOutpaint` —— 1/3 个有
- `LayerUtility: ColorImage` —— 1/3 个有
- `LayerUtility: ImageBlend` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 512 | - | 1 | 100% |
| 高度 | 512 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
