---
name: unknown_workflow_controlnet_inpaint_lora_17
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.581
common_nodes: [CLIPLoader, CLIPTextEncode, DifferentialDiffusion, GetNode, Image Comparer (rgthree), InpaintModelConditioning, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ModelSamplingAuraFlow, QwenImageDiffsynthControlnet, RebatchLatents, RepeatLatentBatch, SaveImage, SetNode, Text, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/🈚️QWEN 图生图-局部重绘_1959606125010300929.json, 平台全量/✅Qwen-Edit 参考到局部重绘_参考迁移_万物迁移_换装-手动版_1959517851717677057.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_lora_17

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/🈚️QWEN 图生图-局部重绘_1959606125010300929.json、平台全量/✅Qwen-Edit 参考到局部重绘_参考迁移_万物迁移_换装-手动版_1959517851717677057.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：58%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `GetNode`
- `Image Comparer (rgthree)`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `QwenImageDiffsynthControlnet`
- `RebatchLatents`
- `RepeatLatentBatch`
- `SaveImage`
- `SetNode`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `Anything Everywhere3` —— 1/2 个有
- `CFGNorm` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `ImageAndMaskPreview` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `ImageSmartSharpen+` —— 1/2 个有
- `LayerMask: MaskGrow` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `Qwen2.5VL` —— 1/2 个有
- `TextEncodeQwenImageEdit` —— 1/2 个有
- `easy seed` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
