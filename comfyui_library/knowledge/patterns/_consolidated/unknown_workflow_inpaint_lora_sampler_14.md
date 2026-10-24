---
name: unknown_workflow_inpaint_lora_sampler_14
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.7105
common_nodes: [CheckpointLoaderSimple, DifferentialDiffusion, Float, InpaintModelConditioning, Int, KSampler, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskToSEGS, PreviewImage, RebatchLatents, RepeatLatentBatch, SaveImage, SegsToCombinedMask, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/002.Qwen编辑之王004.面部特征_2034492666024562690.json, 图片生成/图生图/Qwen Edit 一键换脸_2008380787414016001.json, 图片生成/图生图/Qwen Edit 极速换脸流_1997527977699262466.json, 图片生成/图生图/Qwen Edit 极速换脸流_1997537603048128514.json, 图片生成/图生图/Work Fisher_ Qwen Edit Rapid Face Swap-本地编码_2008457430597902338.json, 图片生成/图生图/千问AIO+F2P，单人_多人换脸工作流   —— 和风整理_2009067726576295938.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_14

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/002.Qwen编辑之王004.面部特征_2034492666024562690.json、图片生成/图生图/Qwen Edit 一键换脸_2008380787414016001.json、图片生成/图生图/Qwen Edit 极速换脸流_1997527977699262466.json、图片生成/图生图/Qwen Edit 极速换脸流_1997537603048128514.json、图片生成/图生图/Work Fisher_ Qwen Edit Rapid Face Swap-本地编码_2008457430597902338.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 6 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `DifferentialDiffusion`
- `Float`
- `InpaintModelConditioning`
- `Int`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToSEGS`
- `PreviewImage`
- `RebatchLatents`
- `RepeatLatentBatch`
- `SaveImage`
- `SegsToCombinedMask`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `LayerMask: PersonMaskUltra V2` —— 5/6 个有
- `Anything Everywhere3` —— 1/6 个有
- `DuckHideNode` —— 1/6 个有
- `LayerMask: DrawBBoxMaskV2` —— 1/6 个有
- `LayerMask: ObjectDetectorYOLO8` —— 1/6 个有
- `LayerUtility: CropByMask V2` —— 1/6 个有
- `PrimitiveBoolean` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `Qwen3_VQA` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `Text Concatenate` —— 1/6 个有
- `easy ifElse` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 8 | 6 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 0.72 | 0.72 - 0.72 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 8，6 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 0.72，观测区间 0.72 - 0.72，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
