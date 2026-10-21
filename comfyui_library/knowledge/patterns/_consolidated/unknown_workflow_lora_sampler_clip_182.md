---
name: unknown_workflow_lora_sampler_clip_182
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.535
common_nodes: [AILab_QwenVL, BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-Image+人像细节增强+美颜版本+全节点注释_2058872484786692098.json, 图片生成/文生图/Z-Image_写真写实+反推图片提示词生成+全节点注释_2057697011813675010.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_182

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-Image+人像细节增强+美颜版本+全节点注释_2058872484786692098.json、图片生成/文生图/Z-Image_写真写实+反推图片提示词生成+全节点注释_2057697011813675010.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：54%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConstrainImage|pysssss` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
