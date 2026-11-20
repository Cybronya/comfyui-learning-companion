---
name: unknown_workflow_lora_sampler_clip_47
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9341
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSamplerAdvanced, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/HUI-KREA2双采-极_2116086018712629250.json, 图片生成/文生图/HUI-KREA2双采-极_2116353102835179521.json, 图片生成/文生图/Krea2 动画人物文生图_2090097765106933761.json, 图片生成/文生图/Krea2-turbo新模型真实人像_2071435896448184322.json, 图片生成/文生图/VividMuse Krea2真实人像V1_2071177424569720833.json, 图片生成/文生图/VividMuse Z-Image-Turbo-全能图片G2-Style_2057436016042139650.json, 图片生成/文生图/VividMuse Z-Image-turbo-SDA 完美破解随机性_2037532958734688257.json, 图片生成/文生图/VividMuse Z-Image家族模型大对比(2)_2034289450481623041.json, 图片生成/文生图/VividMuse Z-Image家族模型大对比_2021580062834827265.json, 图片生成/文生图/Z-Image-turbo Qwen3 4B Engineer V4和Flow-DPO比对_2028451786385793026.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_47

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/HUI-KREA2双采-极_2116086018712629250.json、图片生成/文生图/HUI-KREA2双采-极_2116353102835179521.json、图片生成/文生图/Krea2 动画人物文生图_2090097765106933761.json、图片生成/文生图/Krea2-turbo新模型真实人像_2071435896448184322.json、图片生成/文生图/VividMuse Krea2真实人像V1_2071177424569720833.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 7/10 个有
- `easy promptList` —— 7/10 个有
- `Seed (rgthree)` —— 6/10 个有
- `LayerUtility: ImageReel` —— 4/10 个有
- `LayerUtility: ImageReelComposit` —— 4/10 个有
- `PrimitiveStringMultiline` —— 4/10 个有
- `ResolutionSelector` —— 4/10 个有
- `DF_Text_Box` —— 3/10 个有
- `PrimitiveInt` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `LatentUpscaleBy` —— 2/10 个有
- `PathchSageAttentionKJ` —— 2/10 个有
- `CLIPLoaderGGUF` —— 1/10 个有
- `CheckpointLoaderSimple` —— 1/10 个有
- `Saturation` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 512 - 1536 | 10 | 61% |
| 高度 | 1536 | 512 - 2048 | 10 | 55% |
| 采样步数 | fixed | - | 10 | 60% |
| Prompt 约束强度(CFG) | 8 | 8 - 12 | 10 | 82% |
| 采样算法 | 1 | 1 - 1 | 10 | 100% |
| 调度器 | euler | - | 10 | 60% |
| 重绘幅度 | simple | - | 10 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1280，观测区间 512 - 1536，10 个样本
- 高度 中位数 1536，观测区间 512 - 2048，10 个样本
- 采样步数 最常用 fixed，10 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 12，10 个样本，取值集中（一致性 82%）
- 采样算法 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，10 个样本，一致性 60%
- 重绘幅度 最常用 simple，10 个样本，一致性 50%
