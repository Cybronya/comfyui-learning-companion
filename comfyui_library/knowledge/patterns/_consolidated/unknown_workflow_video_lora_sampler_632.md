---
name: unknown_workflow_video_lora_sampler_632
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.978333
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, WanVideoNAG]
problems: []
missing: []
members: [视频生成/图生视频/2022215823229718529.json, 视频生成/图生视频/1955942871625027585.json, 视频生成/图生视频/1957122488750759938.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_632

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2022215823229718529.json、视频生成/图生视频/1955942871625027585.json、视频生成/图生视频/1957122488750759938.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 2/3 个有
- `GetImageSizeAndCount` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `ImageColorMatch+` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImageResizeKJ` —— 1/3 个有
- `ImageSmartSharpen+` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `SaveImage` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `easy imageRemBg` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | lcm | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
