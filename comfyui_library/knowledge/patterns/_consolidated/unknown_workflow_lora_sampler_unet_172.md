---
name: unknown_workflow_lora_sampler_unet_172
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8918
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, QwenEditConfigPreparer, SaveImage, SolidMask, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader, easy ifElse, easy imageSize, easy isMaskEmpty]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEdit2509产品材质迁移_1989582060228669442.json, 图片生成/图生图/QwenEdit2509产品材质迁移_1991737590925701122.json, 图片生成/图生图/材质纹理迁移_Qwen edit_2005683154381926402.json, 平台全量/服装穿搭 _ Qwen-Image-Edit-2509_1890058904183906306.json, 平台全量/纹理迁移 _ Qwen-Image-Edit-2509_1890250628223082498.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_172

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/QwenEdit2509产品材质迁移_1989582060228669442.json、图片生成/图生图/QwenEdit2509产品材质迁移_1991737590925701122.json、图片生成/图生图/材质纹理迁移_Qwen edit_2005683154381926402.json、平台全量/服装穿搭 _ Qwen-Image-Edit-2509_1890058904183906306.json、平台全量/纹理迁移 _ Qwen-Image-Edit-2509_1890250628223082498.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `QwenEditConfigPreparer`
- `SaveImage`
- `SolidMask`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy ifElse`
- `easy imageSize`
- `easy isMaskEmpty`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `QwenEditOutputExtractor` —— 3/5 个有
- `Text Multiline` —— 3/5 个有
- `ImageConcanate` —— 2/5 个有
- `ImpactInt` —— 2/5 个有
- `LayerMask: MaskPreview` —— 2/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `ImageToPIL` —— 1/5 个有
- `MaskFillHoles` —— 1/5 个有
- `SaveText` —— 1/5 个有
- `easy imageToBase64` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
