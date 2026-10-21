---
name: unknown_workflow_lora_sampler_clip_184
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.83
common_nodes: [Anything Everywhere, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize, ImageScaleToTotalPixels, ImageSharpen, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, ShowText|pysssss, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy clearCacheAll, workflow>LLama-ccp提示词反推, workflow>自定义采样器]
problems: []
missing: []
members: [图片生成/文生图/Zimage+生图+洗图+双采样+Klein放大_2070378304154193922.json, 图片生成/文生图/生图_洗图_Zimage双采样+Klein放大_2020509073417969666.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_184

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Zimage+生图+洗图+双采样+Klein放大_2070378304154193922.json、图片生成/文生图/生图_洗图_Zimage双采样+Klein放大_2020509073417969666.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `ImageSharpen`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `ShowText|pysssss`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `workflow>LLama-ccp提示词反推`
- `workflow>自定义采样器`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 12 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | res_multistep | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1536 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 12，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 res_multistep，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
