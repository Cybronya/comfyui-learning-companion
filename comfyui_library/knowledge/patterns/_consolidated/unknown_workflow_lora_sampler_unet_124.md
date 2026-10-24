---
name: unknown_workflow_lora_sampler_unet_124
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.898
common_nodes: [CLIPLoader, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/image_qwen_image_2512_with_2steps_lora.json, 图片生成/图生图/002.Qwen编辑之王030.三视图-Qwen2511-高度一致性_2043365337059561474.json, 图片生成/图生图/18A_2035893292444950529.json, 图片生成/图生图/Qwen 2512海报洗图工作流（图中文字都能直出）_2021063722009108481.json, 图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑(换装)_2032084048595656705.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_124

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（comfyui-workflow-templates-json/image_qwen_image_2512_with_2steps_lora.json、图片生成/图生图/002.Qwen编辑之王030.三视图-Qwen2511-高度一致性_2043365337059561474.json、图片生成/图生图/18A_2035893292444950529.json、图片生成/图生图/Qwen 2512海报洗图工作流（图中文字都能直出）_2021063722009108481.json、图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑(换装)_2032084048595656705.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `ModelSamplingAuraFlow` —— 4/5 个有
- `CFGNorm` —— 3/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `EmptySD3LatentImage` —— 3/5 个有
- `CLIPTextEncode` —— 2/5 个有
- `FluxKontextImageScale` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `AILab_QwenVL` —— 1/5 个有
- `Display Any (rgthree)` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `TextEncodeQwenImageEditPlusPro_lrzjason` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 2 - 8 | 5 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 2 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
