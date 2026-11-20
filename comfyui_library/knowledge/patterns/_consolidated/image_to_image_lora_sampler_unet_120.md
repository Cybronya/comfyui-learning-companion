---
name: image_to_image_lora_sampler_unet_120
type: Image To Image
frequency: 7
level: strong
coverage: 0.844857
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/👾怪獸-千问Edit万圣节合集👾_1983044701462888450.json, 图片生成/图生图/👾怪獸-自动丰胸👾_2014653557068271618.json, 图片生成/文生图/Qwen Image Edit 2511-三图编辑-圣诞节快乐_2003966404120461313.json, 图片生成/文生图/Qwen Image Edit 2511多图融合图像编辑+全节点注释_2058926060804329474.json, 平台全量/qwen-Edit-Plus_多图编辑工作流_1970504361166184449.json, 平台全量/阮旭东AIGC②：Qwen-Edit-Plus（Qwen_2509）_多图编辑工作流 （ABOUT）_1971021896789696514.json, 平台全量/阮旭东AIGC：Qwen-Edit-Plus（Qwen_2509）_多图编辑工作流 （ABOUT）_1970989153934577665.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_120

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/👾怪獸-千问Edit万圣节合集👾_1983044701462888450.json、图片生成/图生图/👾怪獸-自动丰胸👾_2014653557068271618.json、图片生成/文生图/Qwen Image Edit 2511-三图编辑-圣诞节快乐_2003966404120461313.json、图片生成/文生图/Qwen Image Edit 2511多图融合图像编辑+全节点注释_2058926060804329474.json、平台全量/qwen-Edit-Plus_多图编辑工作流_1970504361166184449.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 6/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `ConditioningZeroOut` —— 3/7 个有
- `ImageConcatMulti` —— 3/7 个有
- `SDXLEmptyLatentSizePicker+` —— 3/7 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/7 个有
- `ImpactSwitch` —— 2/7 个有
- `Int` —— 2/7 个有
- `RHHiddenNodes` —— 2/7 个有
- `Switch` —— 2/7 个有
- `Fast Groups Muter (rgthree)` —— 1/7 个有
- `ImageResize+` —— 1/7 个有
- `ImpactConditionalBranch` —— 1/7 个有
- `easy anythingIndexSwitch` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 7 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 832x1216 (0.68) | - | 3 | 67% |
| 高度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 最常用 832x1216 (0.68)，3 个样本，一致性 67%
- 高度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足
