---
name: unknown_workflow_video_lora_sampler_997
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8005
common_nodes: [CLIPLoader, CLIPTextEncode, Compare, DepthAnything_V2, DiffusionModelLoaderKJ, DiffusionModelSelector, DownloadAndLoadDepthAnythingV2Model, ImageRemoveAlpha+, ImageResizeKJv2, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PreviewImage, Text, TrimVideoLatent, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVaceToVideo, easy ifElse, easy imageRemBg, easy showAnything]
problems: []
missing: []
members: [平台全量/电商服装展示 图片+视频生作品_2042053900110401537.json, 视频生成/图生视频/电商服装展示 图片参考视频生视频 wan2.2_1979016926770925569.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_997

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/电商服装展示 图片+视频生作品_2042053900110401537.json、视频生成/图生视频/电商服装展示 图片参考视频生视频 wan2.2_1979016926770925569.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Compare`
- `DepthAnything_V2`
- `DiffusionModelLoaderKJ`
- `DiffusionModelSelector`
- `DownloadAndLoadDepthAnythingV2Model`
- `ImageRemoveAlpha+`
- `ImageResizeKJv2`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PreviewImage`
- `Text`
- `TrimVideoLatent`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVaceToVideo`
- `easy ifElse`
- `easy imageRemBg`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 16 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | lcm | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 16，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 16，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
