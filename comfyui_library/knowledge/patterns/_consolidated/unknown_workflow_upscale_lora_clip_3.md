---
name: unknown_workflow_upscale_lora_clip_3
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.918429
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, Fast Groups Bypasser (rgthree), LayerUtility: PurgeVRAM, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader, easy getNode, easy setNode, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image Base & Turbo 双重采样文生图_2063288090013298690.json, 图片生成/文生图/Z-image-Turbo如梦似幻 加速lora文生图+高清放大_2079024122377629697.json, 图片生成/文生图/Z-image-Turbo如梦似幻 加速lora文生图+高清放大_2079402711237353473.json, 图片生成/文生图/Z-image-Turbo（如梦似幻+瑶光lora）文生图+高清放大_2063598346006253569.json, 图片生成/文生图/Z-image-base如梦似幻+加速Lora文生图+高清放大_2079025904818409473.json, 图片生成/文生图/Z-image-base如梦似幻+加速Lora文生图+高清放大_2079877016463171586.json, 图片生成/文生图/Z-image-base（如梦似幻+瑶光lora）文生图+高清放大_2063588760020930562.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_clip_3

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Z-image Base & Turbo 双重采样文生图_2063288090013298690.json、图片生成/文生图/Z-image-Turbo如梦似幻 加速lora文生图+高清放大_2079024122377629697.json、图片生成/文生图/Z-image-Turbo如梦似幻 加速lora文生图+高清放大_2079402711237353473.json、图片生成/文生图/Z-image-Turbo（如梦似幻+瑶光lora）文生图+高清放大_2063598346006253569.json、图片生成/文生图/Z-image-base如梦似幻+加速Lora文生图+高清放大_2079025904818409473.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy getNode`
- `easy setNode`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 6/7 个有
- `KSampler` —— 6/7 个有
- `ModelSamplingAuraFlow` —— 4/7 个有
- `EmptyLatentImage` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `KSamplerAdvanced` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 40 | 7 | 0% |
| 采样算法 | res_multistep | - | 7 | 86% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 864 | - | 1 | 100% |
| 高度 | 1536 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 40，7 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 res_multistep，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 40，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
