---
name: unknown_workflow_sampler_clip_unet_326
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.673333
common_nodes: [AILab_QwenVL, BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Deepfacelab素材一键直出16宫格_2028777260731338753.json, 图片生成/文生图/Z-Image+人像细节增强+美颜版本+全节点注释_2058872484786692098.json, 图片生成/文生图/Z-Image_写真写实+反推图片提示词生成+全节点注释_2057697011813675010.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_326

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Deepfacelab素材一键直出16宫格_2028777260731338753.json、图片生成/文生图/Z-Image+人像细节增强+美颜版本+全节点注释_2058872484786692098.json、图片生成/文生图/Z-Image_写真写实+反推图片提示词生成+全节点注释_2057697011813675010.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_QwenVL`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `RHHiddenNodes` —— 2/3 个有
- `ConstrainImage|pysssss` —— 1/3 个有
- `DetailDaemonSamplerNode` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `MultiplySigmas` —— 1/3 个有
- `MuyeTextEditOutput` —— 1/3 个有
- `SeedVarianceEnhancer` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
