---
name: unknown_workflow_lora_sampler_clip_307
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.837
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, Image Comparer (rgthree), KSampler (Efficient), LoadImage, LoraLoaderModelOnly, RH_Translator, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/kontext-dev超强8步纠正场景背景透视角度匹配物体溶图重打光+可选4K高清出图_1994320561415323649.json, 平台全量/Kontext-DEV迄今超强8步出图言出法随，万物消失，背景修复超神工作流来袭✨_1942817532770496514.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_307

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/kontext-dev超强8步纠正场景背景透视角度匹配物体溶图重打光+可选4K高清出图_1994320561415323649.json、平台全量/Kontext-DEV迄今超强8步出图言出法随，万物消失，背景修复超神工作流来袭✨_1942817532770496514.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `KSampler (Efficient)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RH_Translator`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `ConstrainImage|pysssss` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `ImageColorMatch+` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `easy imageSize` —— 1/2 个有
- `workflow>高清放大` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 512 | - | 1 | 100% |
| 高度 | 512 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
