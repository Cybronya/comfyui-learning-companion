---
name: unknown_workflow_video_lora_sampler_503
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.86375
common_nodes: [CLIPLoader, CLIPTextEncode, ImageLoader, ImageResizeKJv2, Int, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/2042258477560631298.json, 视频生成/图生视频/2033421738389803009.json, 视频生成/图生视频/2009656283015684097.json, 视频生成/图生视频/2003358593732771842.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_503

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2042258477560631298.json、视频生成/图生视频/2033421738389803009.json、视频生成/图生视频/2009656283015684097.json、视频生成/图生视频/2003358593732771842.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageLoader`
- `ImageResizeKJv2`
- `Int`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `MultiplePathsInput` —— 3/4 个有
- `Qwen3_VQA` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `CR Text Replace` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `Pick From Batch (mtb)` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `RH_Nano_Banana2_Image2Image` —— 2/4 个有
- `SaveImage` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `ImageResize+` —— 1/4 个有
- `LoadVideo` —— 1/4 个有
- `TextInput_` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 75% |
| Prompt 约束强度(CFG) | 4 | 4 - 8 | 4 | 65% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | normal | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 8，4 个样本
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 normal，4 个样本，一致性 100%
