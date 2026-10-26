---
name: unknown_workflow_lora_sampler_clip_182
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.846
common_nodes: [ApplyPuLIDFlux2, BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, ImageScale, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PuLIDEVACLIPLoader, PuLIDInsightFaceLoader, PuLIDModelLoader, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Pulid脸部参考文生图V3_2038131436229763073.json, 图片生成/图生图/flux2klein 文生图身份一致_2078463797093822466.json, 图片生成/文生图/Flux2 Pulid脸部参考文生图V3_2036724647751852034.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_182

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux2 Pulid脸部参考文生图V3_2038131436229763073.json、图片生成/图生图/flux2klein 文生图身份一致_2078463797093822466.json、图片生成/文生图/Flux2 Pulid脸部参考文生图V3_2036724647751852034.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyPuLIDFlux2`
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxGuidance`
- `ImageScale`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PuLIDEVACLIPLoader`
- `PuLIDInsightFaceLoader`
- `PuLIDModelLoader`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 2/3 个有
- `Float` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `JWInteger` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `FaceAnalysisModels` —— 1/3 个有
- `FaceBoundingBox` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
