---
name: image_to_image_lora_sampler_clip_132
type: Image To Image
frequency: 2
level: weak
coverage: 0.8525
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImageConcanate, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, RH_LLMAPI_NODE, ReferenceLatent, SaveImage, Text Concatenate, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageRemBg, easy imageSize, easy showAnything, workflow>遮罩图像2]
problems: []
missing: []
members: [图片生成/图生图/Kontext奇技淫巧之换装系列-换头拼图法_1941512409263796225.json, 图片生成/图生图/Kontext奇技淫巧之换装系列-遮罩串联一键换装_1941524232516091906.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_132

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Kontext奇技淫巧之换装系列-换头拼图法_1941512409263796225.json、图片生成/图生图/Kontext奇技淫巧之换装系列-遮罩串联一键换装_1941524232516091906.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageConcanate`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `ReferenceLatent`
- `SaveImage`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageRemBg`
- `easy imageSize`
- `easy showAnything`
- `workflow>遮罩图像2`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `FaceAnalysisModels` —— 1/2 个有
- `FaceBoundingBox` —— 1/2 个有
- `FastCanvas` —— 1/2 个有
- `FastCanvasTool` —— 1/2 个有
- `ImageAndMaskPreview` —— 1/2 个有
- `ImagePadForOutpaint` —— 1/2 个有
- `ImageStitch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
