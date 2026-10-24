---
name: unknown_workflow_lora_sampler_unet_174
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.7065
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, GetNode, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SetNode, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2511图像扩展Outpaint_2065054917592702977.json, 图片生成/图生图/qwen-image-edit-2511 图像编辑多功能整合_2003617728734871554.json, 图片生成/图生图/qwen2511自由调整分镜镜头方向（自动提示词）_2009802431940530178.json, 图片生成/图生图/商用级图片编辑_2043847980528181249.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_174

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen2511图像扩展Outpaint_2065054917592702977.json、图片生成/图生图/qwen-image-edit-2511 图像编辑多功能整合_2003617728734871554.json、图片生成/图生图/qwen2511自由调整分镜镜头方向（自动提示词）_2009802431940530178.json、图片生成/图生图/商用级图片编辑_2043847980528181249.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `GetNode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `ImagePadForOutpaintMasked` —— 2/4 个有
- `MuyeTextEditOutput` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `ComfyMathExpression` —— 1/4 个有
- `DF_Get_image_size` —— 1/4 个有
- `DWPreprocessor` —— 1/4 个有
- `Int` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `QwenMultiangleCameraNode` —— 1/4 个有
- `easy promptLine` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
