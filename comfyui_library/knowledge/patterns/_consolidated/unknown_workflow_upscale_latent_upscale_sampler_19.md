---
name: unknown_workflow_upscale_latent_upscale_sampler_19
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.85325
common_nodes: [CLIPLoader, CLIPTextEncode, ColorMatchV2, ConditioningZeroOut, EmptyLatentImage, KSamplerAdvanced, LatentUpscaleBy, PreviewImage, PrimitiveFloat, SaveImage, Seed (rgthree), UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/KREA2+3次采样+高清放大_2074736937302315010.json, 图片生成/文生图/Krea2二采文生图工作流_2076089896476954626.json, 图片生成/文生图/krea2 muse 二采高清生图、USD放大_2096529113921183746.json, 图片生成/文生图/▶▶Krea2-高清生图-人像_2078282360008826881.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_19

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/KREA2+3次采样+高清放大_2074736937302315010.json、图片生成/文生图/Krea2二采文生图工作流_2076089896476954626.json、图片生成/文生图/krea2 muse 二采高清生图、USD放大_2096529113921183746.json、图片生成/文生图/▶▶Krea2-高清生图-人像_2078282360008826881.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatchV2`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `LatentUpscaleBy`
- `PreviewImage`
- `PrimitiveFloat`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `GetImageSize+` —— 3/4 个有
- `Label (rgthree)` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `SimpleMathDual+` —— 3/4 个有
- `CR Prompt Text` —— 1/4 个有
- `CompressImages` —— 1/4 个有
- `ConditioningKrea2Rebalance` —— 1/4 个有
- `DuckHideNode` —— 1/4 个有
- `HAIGC_SaveImagesToZip` —— 1/4 个有
- `LoaderGGUF` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有
- `llama_cpp_instruct_adv` —— 1/4 个有
- `llama_cpp_model_loader` —— 1/4 个有
- `llama_cpp_parameters` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 720 - 1152 | 4 | 80% |
| 高度 | 1280 | 1080 - 1536 | 4 | 87% |
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 8.5 | 7 - 10 | 4 | 82% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 720 - 1152，4 个样本
- 高度 中位数 1280，观测区间 1080 - 1536，4 个样本，取值集中（一致性 87%）
- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8.5，观测区间 7 - 10，4 个样本，取值集中（一致性 82%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
