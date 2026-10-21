---
name: unknown_workflow_video_sampler_clip_66
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.54025
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, RIFE VFI, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/2006627267346173953.json, 视频生成/图生视频/1986365562794213377.json, 视频生成/图生视频/2032355101955858434.json, 视频生成/图生视频/1999623009306636290.json, 视频生成/图生视频/1988509206477234177.json, 视频生成/图生视频/2044709107302670338.json, 视频生成/图生视频/1982960242092834818.json, 视频生成/图生视频/2006524559020789762.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_66

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2006627267346173953.json、视频生成/图生视频/1986365562794213377.json、视频生成/图生视频/2032355101955858434.json、视频生成/图生视频/1999623009306636290.json、视频生成/图生视频/1988509206477234177.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：54%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RIFE VFI`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 7/8 个有
- `ImageLoader` —— 7/8 个有
- `ImageResizeKJv2` —— 7/8 个有
- `Int` —— 7/8 个有
- `INTConstant` —— 6/8 个有
- `WanFirstLastFrameToVideo` —— 6/8 个有
- `WanImageToVideo` —— 4/8 个有
- `LoadImage` —— 3/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `Qwen3_VQA` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `DuckHideNode` —— 1/8 个有
- `Fast Bypasser (rgthree)` —— 1/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `MultiplePathsInput` —— 1/8 个有
- `MultiplePathsInputPlus` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `easy int` —— 1/8 个有
- `easy saveText` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 50% |
| Prompt 约束强度(CFG) | 4 | 4 - 6 | 8 | 81% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | normal | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 6，8 个样本，取值集中（一致性 81%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 normal，8 个样本，一致性 100%
