---
name: unknown_workflow_video_sampler_clip_189
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.974333
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, GetImageSize, HunyuanVideo15ImageToVideo, ImageConcanate, KSamplerSelect, ModelSamplingSD3, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/水豚视频编辑_2026094507036516353.json, 平台全量/水豚视频编辑_2028650231130234882.json, 平台全量/水豚视频编辑编辑_2025922518397227010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_189

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/水豚视频编辑_2026094507036516353.json、平台全量/水豚视频编辑_2028650231130234882.json、平台全量/水豚视频编辑编辑_2025922518397227010.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `GetImageSize`
- `HunyuanVideo15ImageToVideo`
- `ImageConcanate`
- `KSamplerSelect`
- `ModelSamplingSD3`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 2/3 个有
- `Int` —— 2/3 个有
- `JjkText` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
