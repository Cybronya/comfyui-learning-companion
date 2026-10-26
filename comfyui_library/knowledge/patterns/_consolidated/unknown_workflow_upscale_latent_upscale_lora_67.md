---
name: unknown_workflow_upscale_latent_upscale_lora_67
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.908
common_nodes: [BooleanPrimitive, CLIPLoader, CLIPTextEncode, ComfyUI-Krea2T-Enhancer, ConditioningKrea2Rebalance, ConditioningZeroOut, DA3Inference, DA3Render, GetImageSizeAndCount, INTConstant, ImageScale, ImageUpscaleWithModel, KSampler, Krea2ControlApply, Krea2ControlImageEncode, Krea2ControlLoRALoader, LatentUpscale, LazySwitchKJ, LoadDA3Model, MathExpression|pysssss, PreviewImage, PrimitiveStringMultiline, Qwen3VLProcessor, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy batchAnything, easy forLoopEnd, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea 2 本地批量洗图_2080681468573085697.json, 图片生成/文生图/Krea 2 线上批量洗图_2080681462248071170.json, 图片生成/文生图/Krea 2线上批量洗图_2078868414222913537.json, 图片生成/文生图/Krea+2本地批量洗图 (仅本地使用)_2079244095242981378.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_67

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Krea 2 本地批量洗图_2080681468573085697.json、图片生成/文生图/Krea 2 线上批量洗图_2080681462248071170.json、图片生成/文生图/Krea 2线上批量洗图_2078868414222913537.json、图片生成/文生图/Krea+2本地批量洗图 (仅本地使用)_2079244095242981378.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `BooleanPrimitive`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyUI-Krea2T-Enhancer`
- `ConditioningKrea2Rebalance`
- `ConditioningZeroOut`
- `DA3Inference`
- `DA3Render`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageScale`
- `ImageUpscaleWithModel`
- `KSampler`
- `Krea2ControlApply`
- `Krea2ControlImageEncode`
- `Krea2ControlLoRALoader`
- `LatentUpscale`
- `LazySwitchKJ`
- `LoadDA3Model`
- `MathExpression|pysssss`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `Qwen3VLProcessor`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RH_LLMAPI_Pro_Node` —— 3/4 个有
- `BasicScheduler` —— 2/4 个有
- `CFGGuider` —— 2/4 个有
- `IntToText` —— 2/4 个有
- `JWInteger` —— 2/4 个有
- `JWStringConcat` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `JsonExtractString` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `RHBatchImages:` —— 2/4 个有
- `RHUploadZip` —— 2/4 个有
- `RH_ExtractImage` —— 2/4 个有
- `RandomNoise` —— 2/4 个有
- `SamplerCustomAdvanced` —— 2/4 个有
- `SamplerEulerAncestral` —— 2/4 个有
- `SplitSigmas` —— 2/4 个有
- `easy forLoopStart` —— 2/4 个有
- `easy loadImagesForLoop` —— 2/4 个有
- `easy mathInt` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.95 | 0.92 - 0.95 | 4 | 99% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.95，观测区间 0.92 - 0.95，4 个样本，取值集中（一致性 99%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
