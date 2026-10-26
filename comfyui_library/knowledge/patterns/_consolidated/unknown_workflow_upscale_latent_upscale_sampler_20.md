---
name: unknown_workflow_upscale_latent_upscale_sampler_20
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.824
common_nodes: [CLIPLoader, CLIPTextEncode, ColorMatchV2, ConditioningZeroOut, EmptyLatentImage, KSamplerAdvanced, LatentUpscaleBy, PreviewImage, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/krea2 muse 二采高清生图_2096540586579939330.json, 图片生成/文生图/▶▷Krea2-高清生图优化流_2077777851994165250.json, 图片生成/文生图/梦中情人-Krea2Turbo  固定角色 自用流_2081083885131223041.json, 图片生成/文生图/泠月luna-Krea2Turbo  固定角色 自用流_2080837616429260802.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_20

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/krea2 muse 二采高清生图_2096540586579939330.json、图片生成/文生图/▶▷Krea2-高清生图优化流_2077777851994165250.json、图片生成/文生图/梦中情人-Krea2Turbo  固定角色 自用流_2081083885131223041.json、图片生成/文生图/泠月luna-Krea2Turbo  固定角色 自用流_2080837616429260802.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：82%

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
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `GetImageSize+` —— 3/4 个有
- `PrimitiveFloat` —— 3/4 个有
- `SimpleMathDual+` —— 3/4 个有
- `UltimateSDUpscale` —— 3/4 个有
- `UpscaleModelLoader` —— 3/4 个有
- `CR Text Concatenate` —— 2/4 个有
- `Label (rgthree)` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `MuyeTextEditOutput` —— 2/4 个有
- `ResolutionStdSelector` —— 2/4 个有
- `孤海注释` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `CompressImages` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 7 | 7 - 10 | 4 | 83% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |
| 宽度 | 720 | 720 - 1152 | 4 | 77% |
| 高度 | 1280 | 1280 - 1536 | 4 | 92% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 7，观测区间 7 - 10，4 个样本，取值集中（一致性 83%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
- 宽度 中位数 720，观测区间 720 - 1152，4 个样本
- 高度 中位数 1280，观测区间 1280 - 1536，4 个样本，取值集中（一致性 92%）
