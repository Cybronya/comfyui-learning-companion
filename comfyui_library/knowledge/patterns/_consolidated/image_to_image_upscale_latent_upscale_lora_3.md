---
name: image_to_image_upscale_latent_upscale_lora_3
type: Image To Image
frequency: 2
level: weak
coverage: 0.9695
common_nodes: [BooleanPrimitive, CLIPLoader, CLIPTextEncode, ComfyUI-Krea2T-Enhancer, ConditioningKrea2Rebalance, ConditioningZeroOut, DA3Inference, DA3Render, GetImageSizeAndCount, INTConstant, ImageScale, ImageUpscaleWithModel, KSampler, Krea2ControlApply, Krea2ControlImageEncode, Krea2ControlLoRALoader, LatentUpscale, LazySwitchKJ, LoadDA3Model, LoadImage, MathExpression|pysssss, PrimitiveStringMultiline, Qwen3VLProcessor, RH_LLMAPI_Pro_Node, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea 2 单图洗图_2080681456040501249.json, 图片生成/文生图/Krea 2单图洗图_2078868402176872450.json]
source: knowledge_consolidation
---

# image_to_image_upscale_latent_upscale_lora_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Krea 2 单图洗图_2080681456040501249.json、图片生成/文生图/Krea 2单图洗图_2078868402176872450.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
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
- `LoadImage`
- `MathExpression|pysssss`
- `PrimitiveStringMultiline`
- `Qwen3VLProcessor`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 1/2 个有
- `CFGGuider` —— 1/2 个有
- `JsonExtractString` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `RandomNoise` —— 1/2 个有
- `SamplerCustomAdvanced` —— 1/2 个有
- `SamplerEulerAncestral` —— 1/2 个有
- `SplitSigmas` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.275 | - | 2 | 91% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.275，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
