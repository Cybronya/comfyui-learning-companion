---
name: unknown_workflow_video_sampler_clip_16
type: Unknown Workflow
frequency: 19
level: strong
coverage: 0.535842
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, KSamplerAdvanced, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1981244475731337218.json, 视频生成/图生视频/1982712132548599809.json, 视频生成/图生视频/2038972688689008641.json, 视频生成/图生视频/2038989882521030658.json, 视频生成/图生视频/2009543545169907714.json, 视频生成/图生视频/2047592882332241922.json, 视频生成/图生视频/2051628991756419074.json, 视频生成/图生视频/2070382789744218114.json, 视频生成/图生视频/1987169484022681602.json, 视频生成/图生视频/2000107947743211522.json, 视频生成/图生视频/2014511689311461377.json, 视频生成/图生视频/1999730211526766594.json, 视频生成/图生视频/WAN2.2图生视频终极版_2083953699881316354.json, 视频生成/图生视频/1981254959582928897.json, 视频生成/图生视频/2001486989629288450.json, 视频生成/图生视频/1982359421470810113.json, 视频生成/图生视频/2001317113182777346.json, 视频生成/图生视频/2001269970967330818.json, 视频生成/图生视频/2022797713682735106.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_16

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/1981244475731337218.json、视频生成/图生视频/1982712132548599809.json、视频生成/图生视频/2038972688689008641.json、视频生成/图生视频/2038989882521030658.json、视频生成/图生视频/2009543545169907714.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：54%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `KSamplerAdvanced`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Int` —— 18/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 18/19 个有
- `easy cleanGpuUsed` —— 18/19 个有
- `RIFE VFI` —— 17/19 个有
- `Fast Groups Bypasser (rgthree)` —— 15/19 个有
- `wanBlockSwap` —— 14/19 个有
- `ImageLoader` —— 12/19 个有
- `WanImageToVideo` —— 11/19 个有
- `LoraLoaderModelOnly` —— 10/19 个有
- `ImageResizeKJv2` —— 9/19 个有
- `WanFirstLastFrameToVideo` —— 8/19 个有
- `LoadImage` —— 7/19 个有
- `Qwen3_VQA` —— 4/19 个有
- `easy showAnything` —— 4/19 个有
- `MultiplePathsInput` —— 3/19 个有
- `SetNode` —— 3/19 个有
- `CR Text` —— 2/19 个有
- `GetNode` —— 2/19 个有
- `easy seed` —— 2/19 个有
- `CompressImages` —— 1/19 个有
- `CreateVideo` —— 1/19 个有
- `MathExpression|pysssss` —— 1/19 个有
- `RHHiddenNodes` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 19 | 63% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 19 | 100% |
| 采样算法 | 1 | 1 - 1 | 19 | 100% |
| 调度器 | euler | - | 19 | 100% |
| 重绘幅度 | normal | - | 19 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，19 个样本，一致性 63%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，19 个样本，一致性 100%
- 重绘幅度 最常用 normal，19 个样本，一致性 100%
