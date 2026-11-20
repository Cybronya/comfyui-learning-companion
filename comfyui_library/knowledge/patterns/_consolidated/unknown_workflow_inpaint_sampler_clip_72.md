---
name: unknown_workflow_inpaint_sampler_clip_72
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8235
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler (Efficient), LayerFilter: HDREffects, LoadImage, PreviewImage, SaveImage, VAELoader]
problems: []
missing: []
members: [平台全量/FLUX  万物消除术_1936622650091540482.json, 平台全量/一键运行：FLUX OneReward 一键换背景，图像修改_1968496146467434498.json, 平台全量/一键运行：FLUX OneReward 扩图，图像修复_1968492247048171522.json, 平台全量/一键运行：Nunchaku 完美扩图 修复_1937040303381712898.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_72

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/FLUX  万物消除术_1936622650091540482.json、平台全量/一键运行：FLUX OneReward 一键换背景，图像修改_1968496146467434498.json、平台全量/一键运行：FLUX OneReward 扩图，图像修复_1968492247048171522.json、平台全量/一键运行：Nunchaku 完美扩图 修复_1937040303381712898.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler (Efficient)`
- `LayerFilter: HDREffects`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ApplyFBCacheOnModel` —— 2/4 个有
- `DeepTranslatorTextNode` —— 2/4 个有
- `ImagePadForOutpaint` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `NunchakuFluxDiTLoader` —— 2/4 个有
- `NunchakuFluxLoraLoader` —— 2/4 个有
- `Seed Everywhere` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `UNETLoader` —— 2/4 个有
- `BiRefNet_Hugo` —— 1/4 个有
- `ImageStitch` —— 1/4 个有
- `InvertMask` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
