---
name: unknown_workflow_inpaint_lora_sampler_26
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.7515
common_nodes: [CLIPLoader, ColorMatch, ConditioningZeroOut, EmptyLatentImage, ImageAndMaskPreview, ImageConcanate, InpaintCrop, InpaintStitch, KSampler, LayerMask: SegmentAnythingUltra V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, easy ifElse, easy imageSize, easy isMaskEmpty]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEdit2509自动修手方案_1976107106363420674.json, 图片生成/图生图/QwenEdit2509自动修手方案_1977327662769295361.json, 图片生成/图生图/QwenEdit2511自动修手方案V1_2004929724948377602.json, 数字人/数字人/QwenEdit2509修复烂脚丫子_1995737246269583362.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_26

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/QwenEdit2509自动修手方案_1976107106363420674.json、图片生成/图生图/QwenEdit2509自动修手方案_1977327662769295361.json、图片生成/图生图/QwenEdit2511自动修手方案V1_2004929724948377602.json、数字人/数字人/QwenEdit2509修复烂脚丫子_1995737246269583362.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageAndMaskPreview`
- `ImageConcanate`
- `InpaintCrop`
- `InpaintStitch`
- `KSampler`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy ifElse`
- `easy imageSize`
- `easy isMaskEmpty`

**可变部分**（部分 workflow 才有）：
- `RH_Jimeng4_Image2Image` —— 3/4 个有
- `RH_LLMAPI_NODE` —— 3/4 个有
- `Text Multiline` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `RH_Nano_Banana_Image2Image` —— 2/4 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/4 个有
- `RH_Nano_Banana2_Image2Image` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | beta57 | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 beta57，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
