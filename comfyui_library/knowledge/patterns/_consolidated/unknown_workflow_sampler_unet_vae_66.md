---
name: unknown_workflow_sampler_unet_vae_66
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.772
common_nodes: [CLIPLoader, KSampler, PreviewAny, PrimitiveStringMultiline, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Fibo2文生图_2116522251024691202.json, 图片生成/文生图/Fibo2智能文生图_2115437162157137922.json, 图片生成/文生图/Flux3-Klein智能文生图_2114904139665854466.json, 图片生成/文生图/Flux3-Klein智能文生图_2116355959416246273.json, 图片生成/文生图/Flux3-Klein智能文生图_2116367707561091073.json, 图片生成/文生图/Flux3-klein文生图PUP增强_2111479315035676674.json, 图片生成/文生图/MOSS Image Base + SFT 融合版文生图_2115444235745980418.json, 图片生成/文生图/Moss Image智能文生图_2114917051671343106.json, 图片生成/文生图/Moss 文生图高质量版_2114973070078341122.json, 图片生成/文生图/Moss 文生图高质量版_2116405423283724290.json, 图片生成/文生图/Moss 模型融合工作流_2114890474770227202.json, 图片生成/文生图/Moss 模型融合工作流_2114947721344929794.json, 图片生成/文生图/Moss 模型融合工作流_2115700533108502530.json, 平台全量/Moss Image文生图_2117862760578109441.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_66

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Fibo2文生图_2116522251024691202.json、图片生成/文生图/Fibo2智能文生图_2115437162157137922.json、图片生成/文生图/Flux3-Klein智能文生图_2114904139665854466.json、图片生成/文生图/Flux3-Klein智能文生图_2116355959416246273.json、图片生成/文生图/Flux3-Klein智能文生图_2116367707561091073.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 13/14 个有
- `CLIPTextEncode` —— 12/14 个有
- `EmptyFlux2LatentImage` —— 12/14 个有
- `SkipLayerGuidanceDiTSimple` —— 8/14 个有
- `Display Int (rgthree)` —— 7/14 个有
- `GoohaiUniversalSlider` —— 7/14 个有
- `MOSSMergePreset` —— 7/14 个有
- `孤海注释` —— 7/14 个有
- `Text Prompt (JPS)` —— 6/14 个有
- `TextEncodeFibo2` —— 2/14 个有
- `Switch any [Crystools]` —— 1/14 个有
- `Text` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 37.5 | 16 - 50 | 14 | 62% |
| Prompt 约束强度(CFG) | 3 | 1 - 3.5 | 14 | 61% |
| 采样算法 | euler | - | 14 | 86% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 37.5，观测区间 16 - 50，14 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3.5，14 个样本
- 采样算法 最常用 euler，14 个样本，一致性 86%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
