---
name: text_to_image_lora_sampler_clip_352
type: Text To Image
frequency: 2
level: weak
coverage: 0.904
common_nodes: [ApplyPulidFlux, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RH_Translator, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [ImageResize+]
members: [图片生成/文生图/1914135646209015810.json, 图片生成/文生图/1931578931458322433.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_352

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1914135646209015810.json、图片生成/文生图/1931578931458322433.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyPulidFlux`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RH_Translator`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowStringText` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PulidEvaClipLoader` —— 1/2 个有
- `PulidFluxEvaClipLoader` —— 1/2 个有
- `RandomPrompt` —— 1/2 个有
- `SUPIR_Upscale` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 964 | - | 2 | 94% |
| 高度 | 1112 | - | 2 | 92% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 964，样本不足，未给区间，2 个样本，取值集中（一致性 94%）
- 高度 中位数 1112，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- 这些节点还没有知识卡，系统对它们的理解有限：ImageResize+
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
