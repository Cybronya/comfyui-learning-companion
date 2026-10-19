---
name: unknown_workflow_video_sampler_clip_12
type: Unknown Workflow
frequency: 22
level: moderate
coverage: 0.573727
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1981244475731337218.json, 视频生成/图生视频/1982712132548599809.json, 视频生成/图生视频/2038972688689008641.json, 视频生成/图生视频/2038989882521030658.json, 视频生成/图生视频/2009543545169907714.json, 视频生成/图生视频/2047592882332241922.json, 视频生成/图生视频/2051628991756419074.json, 视频生成/图生视频/2070382789744218114.json, 视频生成/图生视频/1987169484022681602.json, 视频生成/图生视频/2000107947743211522.json, 视频生成/图生视频/2014511689311461377.json, 视频生成/图生视频/1999730211526766594.json, 视频生成/图生视频/2005870552181080066.json, 视频生成/图生视频/1982684734805426178.json, 视频生成/图生视频/2076490092809637889.json, 视频生成/图生视频/1987069561856004097.json, 视频生成/图生视频/1987091319136956418.json, 视频生成/图生视频/1982359421470810113.json, 视频生成/图生视频/1982359410183946242.json, 视频生成/图生视频/2004446974457901057.json, 视频生成/图生视频/2003113307240374273.json, 视频生成/图生视频/2003436959081111553.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_12

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（视频生成/图生视频/1981244475731337218.json、视频生成/图生视频/1982712132548599809.json、视频生成/图生视频/2038972688689008641.json、视频生成/图生视频/2038989882521030658.json、视频生成/图生视频/2009543545169907714.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 21/22 个有
- `Int` —— 21/22 个有
- `PreviewImage` —— 21/22 个有
- `wanBlockSwap` —— 21/22 个有
- `ModelPatchTorchSettings` —— 19/22 个有
- `RIFE VFI` —— 18/22 个有
- `Fast Groups Bypasser (rgthree)` —— 16/22 个有
- `ImageResizeKJv2` —— 16/22 个有
- `ImageLoader` —— 15/22 个有
- `easy cleanGpuUsed` —— 14/22 个有
- `WanFirstLastFrameToVideo` —— 12/22 个有
- `MultiplePathsInput` —— 11/22 个有
- `Qwen3_VQA` —— 11/22 个有
- `easy showAnything` —— 11/22 个有
- `WanImageToVideo` —— 10/22 个有
- `LoraLoaderModelOnly` —— 9/22 个有
- `Any To Any` —— 7/22 个有
- `LoadImage` —— 7/22 个有
- `VHS_SelectFilename` —— 7/22 个有
- `HunyuanVideoFoley` —— 6/22 个有
- `LayerUtility: PurgeVRAM V2` —— 6/22 个有
- `easy float` —— 3/22 个有
- `CR Prompt Text` —— 2/22 个有
- `LayerUtility: PurgeVRAM` —— 2/22 个有
- `SaveLatent` —— 2/22 个有
- `VAEEncode` —— 2/22 个有
- `YC_textReplaceNode` —— 2/22 个有
- `Float` —— 1/22 个有
- `Label (rgthree)` —— 1/22 个有
- `RH_LLMAPI_Pro_Node` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 22 | 64% |
| Prompt 约束强度(CFG) | 4 | 4 - 20 | 22 | 29% |
| 采样算法 | 1 | 1 - 1 | 22 | 100% |
| 调度器 | euler | - | 22 | 100% |
| 重绘幅度 | normal | - | 22 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，22 个样本，一致性 64%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 20，22 个样本，取值分散，一致性仅 29%
- 采样算法 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，22 个样本，一致性 100%
- 重绘幅度 最常用 normal，22 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
