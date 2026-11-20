---
name: unknown_workflow_lora_sampler_unet_205
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.886
common_nodes: [CLIPLoader, CR Text, ConditioningZeroOut, DepthAnythingV2Preprocessor, DrawViTPose, KSampler, LayerUtility: ColorImage V2, LayerUtility: ImageBlend, LayerUtility: ImageMaskScaleAsV2, LoadImage, LoraLoaderModelOnly, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Eidt大动态姿态迁移，人物一致性套图生成工作流_1980900408317100033.json, 图片生成/图生图/人物一致性高难度Qwen-Eidt姿态迁移_1984224430169669633.json, 平台全量/人物+服装一致性复杂姿态迁移_1989537342681739265.json, 平台全量/大动态+构图视角迁移V2，一致性套图生成工作流_1987871524545826818.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_205

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-Eidt大动态姿态迁移，人物一致性套图生成工作流_1980900408317100033.json、图片生成/图生图/人物一致性高难度Qwen-Eidt姿态迁移_1984224430169669633.json、平台全量/人物+服装一致性复杂姿态迁移_1989537342681739265.json、平台全量/大动态+构图视角迁移V2，一致性套图生成工作流_1987871524545826818.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `ConditioningZeroOut`
- `DepthAnythingV2Preprocessor`
- `DrawViTPose`
- `KSampler`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageMaskScaleAsV2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `easy imageConcat` —— 3/4 个有
- `AILab_QwenVL` —— 2/4 个有
- `LayerMask: BiRefNetUltraV2` —— 2/4 个有
- `LayerMask: LoadBiRefNetModelV2` —— 2/4 个有
- `LayerUtility: ImageRemoveAlpha` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `easy imageSize` —— 2/4 个有
- `easy int` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `PIP_StringConcatenation` —— 1/4 个有
- `QwenEditConfigPreparer` —— 1/4 个有
- `RBGImageStitchPlus` —— 1/4 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6.5 | 5 - 8 | 4 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6.5，观测区间 5 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
