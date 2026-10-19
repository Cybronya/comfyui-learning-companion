---
name: unknown_workflow_video_sampler_clip_104
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.5666
common_nodes: [CLIPLoader, CLIPTextEncode, Fast Groups Bypasser (rgthree), ImageLoader, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, RIFE VFI, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/2006627267346173953.json, 视频生成/图生视频/1986365562794213377.json, 视频生成/图生视频/2032355101955858434.json, 视频生成/图生视频/1982960242092834818.json, 视频生成/图生视频/2006524559020789762.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_104

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2006627267346173953.json、视频生成/图生视频/1986365562794213377.json、视频生成/图生视频/2032355101955858434.json、视频生成/图生视频/1982960242092834818.json、视频生成/图生视频/2006524559020789762.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：57%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Fast Groups Bypasser (rgthree)`
- `ImageLoader`
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
- `INTConstant` —— 4/5 个有
- `ImageResizeKJv2` —— 4/5 个有
- `Int` —— 4/5 个有
- `WanFirstLastFrameToVideo` —— 4/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `Qwen3_VQA` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `DuckHideNode` —— 1/5 个有
- `Fast Bypasser (rgthree)` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `MultiplePathsInput` —— 1/5 个有
- `MultiplePathsInputPlus` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `WanImageToVideo` —— 1/5 个有
- `easy int` —— 1/5 个有
- `easy saveText` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 80% |
| Prompt 约束强度(CFG) | 4 | 4 - 6 | 5 | 82% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | normal | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 6，5 个样本，取值集中（一致性 82%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 normal，5 个样本，一致性 100%
