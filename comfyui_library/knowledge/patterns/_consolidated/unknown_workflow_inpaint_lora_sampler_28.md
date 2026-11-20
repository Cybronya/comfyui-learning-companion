---
name: unknown_workflow_inpaint_lora_sampler_28
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7584
common_nodes: [CLIPLoader, ColorMatch, ConditioningZeroOut, EmptyLatentImage, ImageAndMaskPreview, ImageConcanate, InpaintCrop, InpaintStitch, KSampler, LayerMask: SegmentAnythingUltra V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, easy ifElse, easy imageSize, easy isMaskEmpty]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEdit2509自动修手方案_1976107106363420674.json, 图片生成/图生图/QwenEdit2509自动修手方案_1977327662769295361.json, 图片生成/图生图/QwenEdit2511自动修手方案V1_2004929724948377602.json, 平台全量/【QwenEdit2509自动修手】千问-完美修手 手部修复 Qwen-lmage-Edit 千问模_1994325736379138049.json, 数字人/数字人/QwenEdit2509修复烂脚丫子_1995737246269583362.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_28

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/QwenEdit2509自动修手方案_1976107106363420674.json、图片生成/图生图/QwenEdit2509自动修手方案_1977327662769295361.json、图片生成/图生图/QwenEdit2511自动修手方案V1_2004929724948377602.json、平台全量/【QwenEdit2509自动修手】千问-完美修手 手部修复 Qwen-lmage-Edit 千问模_1994325736379138049.json、数字人/数字人/QwenEdit2509修复烂脚丫子_1995737246269583362.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 5 个 workflow 都包含：
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
- `RH_LLMAPI_NODE` —— 4/5 个有
- `Text Multiline` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `RH_Jimeng4_Image2Image` —— 3/5 个有
- `RH_Nano_Banana_Image2Image` —— 2/5 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/5 个有
- `RH_Nano_Banana2_Image2Image` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | beta57 | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 512 | 512 - 512 | 5 | 100% |
| 高度 | 512 | 512 - 512 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 beta57，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，5 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
