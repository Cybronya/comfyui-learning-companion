---
name: unknown_workflow_inpaint_lora_sampler_11
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.922625
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/OneReward物体删除工作流_1988902210874519554.json, 图片生成/图生图/OneReward超强局部重绘_1988899762021732354.json, 图片生成/图生图/reward移除_2091215519079817218.json, 图片生成/图生图/修手丨成功率高_1895306650326794241.json, 图片生成/图生图/修手自用_1898609540873834498.json, 图片生成/图生图/局部重绘OneReward（ 加速版）_1966496761944682497.json, 图片生成/图生图/扩图 OneReward。超强（ 加速版）_1967942516572061697.json, 图片生成/图生图/扩图，裁图，方图，竖图，60秒一个_2037232059801935873.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_11

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/OneReward物体删除工作流_1988902210874519554.json、图片生成/图生图/OneReward超强局部重绘_1988899762021732354.json、图片生成/图生图/reward移除_2091215519079817218.json、图片生成/图生图/修手丨成功率高_1895306650326794241.json、图片生成/图生图/修手自用_1898609540873834498.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/8 个有
- `DifferentialDiffusion` —— 7/8 个有
- `PreviewImage` —— 5/8 个有
- `CR Latent Batch Size` —— 4/8 个有
- `GrowMaskWithBlur` —— 4/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/8 个有
- `Image Comparer (rgthree)` —— 3/8 个有
- `MaskPreview` —— 3/8 个有
- `Text` —— 3/8 个有
- `CR Prompt Text` —— 2/8 个有
- `DeepTranslatorTextNode` —— 2/8 个有
- `ImageAndMaskPreview` —— 2/8 个有
- `ImagePadForOutpaint` —— 2/8 个有
- `RH_Translator` —— 2/8 个有
- `ShowText|pysssss` —— 2/8 个有
- `ArgosTranslateTextNode` —— 1/8 个有
- `Bjornulf_WriteText` —— 1/8 个有
- `ImageScale` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 30 | 8 | 30% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 8 | 28% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 38% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 30，8 个样本，取值分散，一致性仅 30%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，8 个样本，取值分散，一致性仅 28%
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 38%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（5/8 个样本）：Steps较低可能导致细节不足
