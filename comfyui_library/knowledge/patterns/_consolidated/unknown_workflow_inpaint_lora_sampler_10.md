---
name: unknown_workflow_inpaint_lora_sampler_10
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.74175
common_nodes: [CheckpointLoaderSimple, DifferentialDiffusion, InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerMask: PersonMaskUltra V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskToSEGS, PreviewImage, RepeatLatentBatch, SaveImage, SegsToCombinedMask, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/02huanlian(3gai)_2055179866324127746.json, 图片生成/反推提示词/02huanlian(3gai)_2059284763567026177.json, 图片生成/反推提示词/2qsazpmcbow_2059682144443789314.json, 图片生成/图生图/002.Qwen编辑之王004.面部特征_2034492666024562690.json, 图片生成/图生图/Qwen Edit 一键换脸_2008380787414016001.json, 图片生成/图生图/Qwen Edit 极速换脸流_1997527977699262466.json, 图片生成/图生图/Qwen Edit 极速换脸流_1997537603048128514.json, 图片生成/图生图/Work Fisher_ Qwen Edit Rapid Face Swap-本地编码_2008457430597902338.json, 平台全量/Qwen Edit 极速换脸流_1986228353298550785.json, 平台全量/Qwen 千问 换脸_1957463896011501569.json, 平台全量/Work-Fisher_Qwen Edit 极速换脸流_1983862598527582209.json, 平台全量/（牛逼换脸2）极速换脸流-魔改Work-Fisher，感谢原作者开源_2018747560051089409.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_10

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/反推提示词/02huanlian(3gai)_2055179866324127746.json、图片生成/反推提示词/02huanlian(3gai)_2059284763567026177.json、图片生成/反推提示词/2qsazpmcbow_2059682144443789314.json、图片生成/图生图/002.Qwen编辑之王004.面部特征_2034492666024562690.json、图片生成/图生图/Qwen Edit 一键换脸_2008380787414016001.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 12 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `DifferentialDiffusion`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToSEGS`
- `PreviewImage`
- `RepeatLatentBatch`
- `SaveImage`
- `SegsToCombinedMask`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 11/12 个有
- `Float` —— 11/12 个有
- `Int` —— 11/12 个有
- `RebatchLatents` —— 11/12 个有
- `RTXVideoSuperResolution` —— 3/12 个有
- `easy cleanGpuUsed` —— 3/12 个有
- `ColorMatch` —— 1/12 个有
- `DuckHideNode` —— 1/12 个有
- `Image Comparer (rgthree)` —— 1/12 个有
- `LayerUtility: CropByMask V2` —— 1/12 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/12 个有
- `LayerUtility: RestoreCropBox` —— 1/12 个有
- `ShellAgentPluginOutputText` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 12 | 12 | 79% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 0.72 | 0.72 - 0.75 | 12 | 99% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 12，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 0.72，观测区间 0.72 - 0.75，12 个样本，取值集中（一致性 99%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
