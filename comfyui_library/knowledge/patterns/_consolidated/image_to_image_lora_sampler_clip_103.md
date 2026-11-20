---
name: image_to_image_lora_sampler_clip_103
type: Image To Image
frequency: 3
level: strong
coverage: 0.938667
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImageStitch, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, TeaCache, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/三图融合言出法随Kontext Dev+SeedVR2超分+LLM扩词_1938998105222078466.json, 图片生成/图生图/产品首饰手链精修工作流_1953486548664766465.json, 图片生成/图生图/新Kontext-青铜雕塑风格转绘+TEACACHE加速_1946480965322436610.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_103

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/三图融合言出法随Kontext Dev+SeedVR2超分+LLM扩词_1938998105222078466.json、图片生成/图生图/产品首饰手链精修工作流_1953486548664766465.json、图片生成/图生图/新Kontext-青铜雕塑风格转绘+TEACACHE加速_1946480965322436610.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `TeaCache`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `EmptySD3LatentImage` —— 2/3 个有
- `LoadImageOutput` —— 2/3 个有
- `easy imageRemBg` —— 2/3 个有
- `ImageResizeKJ` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `SeedVR2` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy imageColorMatch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
