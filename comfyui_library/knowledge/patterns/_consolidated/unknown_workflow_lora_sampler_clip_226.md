---
name: unknown_workflow_lora_sampler_clip_226
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.836
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, EmptyHunyuanLatentVideo, Image Comparer (rgthree), ImpactInt, KSamplerAdvanced, LoraLoaderModelOnly, RH_LLMAPI_NODE, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/wan2-2+seedvr高清放大超级真实质感文生图_2043161931514646530.json, 图片生成/文生图/wan2-2文生图 超级真实质感工作流_1964175572664467458.json, 图片生成/文生图/🏇wan2-2超级真实质感 文生图🏇_1961625719518511105.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_226

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/wan2-2+seedvr高清放大超级真实质感文生图_2043161931514646530.json、图片生成/文生图/wan2-2文生图 超级真实质感工作流_1964175572664467458.json、图片生成/文生图/🏇wan2-2超级真实质感 文生图🏇_1961625719518511105.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `EmptyHunyuanLatentVideo`
- `Image Comparer (rgthree)`
- `ImpactInt`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `SeedVR2BlockSwap` —— 2/3 个有
- `SeedVR2GGUF` —— 2/3 个有
- `INTConstant` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 10 | 10 - 10 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | res_2s | - | 3 | 100% |
| 重绘幅度 | bong_tangent | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 res_2s，3 个样本，一致性 100%
- 重绘幅度 最常用 bong_tangent，3 个样本，一致性 100%
