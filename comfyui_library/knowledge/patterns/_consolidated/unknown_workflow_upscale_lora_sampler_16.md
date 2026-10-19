---
name: unknown_workflow_upscale_lora_sampler_16
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.882
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageBlend, ImageScale, ImageScaleBy, ImageUpscaleWithModel, KSamplerAdvanced, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, ResolutionSelector, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Krea2 文生图 双采_2104499569571749889.json, 图片生成/文生图/Krea2 文生图 双采_2104771231848423426.json, 数字人/数字人/krea2-UE5角色定妆照_2090840952448573441.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_16

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Krea2 文生图 双采_2104499569571749889.json、图片生成/文生图/Krea2 文生图 双采_2104771231848423426.json、数字人/数字人/krea2-UE5角色定妆照_2090840952448573441.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageBlend`
- `ImageScale`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ConditioningKrea2Rebalance` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `RH_Translator` —— 2/3 个有
- `easy clearCacheAll` —— 2/3 个有
- `easy seed` —— 2/3 个有
- `VAEDecodeTiled` —— 1/3 个有
- `easy mathInt` —— 1/3 个有
- `llama_cpp_instruct_adv` —— 1/3 个有
- `llama_cpp_model_loader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1536 | 3 | 80% |
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | sa_solver | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1536，3 个样本
- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 sa_solver，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
