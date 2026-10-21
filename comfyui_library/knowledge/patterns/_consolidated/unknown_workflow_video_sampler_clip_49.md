---
name: unknown_workflow_video_sampler_clip_49
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7998
common_nodes: [CLIPLoader, CLIPTextEncode, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2010412985205923842.json, 视频生成/图生视频/2010413439973330946.json, 视频生成/图生视频/2010348801411780609.json, 视频生成/图生视频/2010386931812667393.json, 视频生成/图生视频/2013251284761059330.json, 视频生成/图生视频/2023419797345669121.json, 视频生成/图生视频/2023632584692994049.json, 视频生成/图生视频/2080553179648978945.json, 视频生成/图生视频/2025278485094211586.json, 视频生成/图生视频/2008918546440523778.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_49

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2010412985205923842.json、视频生成/图生视频/2010413439973330946.json、视频生成/图生视频/2010348801411780609.json、视频生成/图生视频/2010386931812667393.json、视频生成/图生视频/2013251284761059330.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ModelPatchTorchSettings` —— 9/10 个有
- `PathchSageAttentionKJ` —— 9/10 个有
- `SimpleMath+` —— 8/10 个有
- `PainterI2V` —— 7/10 个有
- `INTConstant` —— 6/10 个有
- `JoinStrings` —— 6/10 个有
- `Qwen3_VQA` —— 6/10 个有
- `RIFE VFI` —— 6/10 个有
- `ShowText|pysssss` —— 6/10 个有
- `TextInput_` —— 6/10 个有
- `ImageConcatMulti` —— 5/10 个有
- `CR Text` —— 4/10 个有
- `PrimitiveString` —— 4/10 个有
- `RHHiddenNodes` —— 4/10 个有
- `WanFirstLastFrameToVideo` —— 3/10 个有
- `CustomAddLabel` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `GetImagesFromBatchIndexed` —— 1/10 个有
- `LoraLoaderModelOnly` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 10 | 80% |
| Prompt 约束强度(CFG) | 4 | 4 - 6 | 10 | 80% |
| 采样算法 | 1 | 1 - 1 | 10 | 100% |
| 调度器 | euler | - | 10 | 100% |
| 重绘幅度 | simple | - | 10 | 70% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，10 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 6，10 个样本
- 采样算法 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，10 个样本，一致性 100%
- 重绘幅度 最常用 simple，10 个样本，一致性 70%
