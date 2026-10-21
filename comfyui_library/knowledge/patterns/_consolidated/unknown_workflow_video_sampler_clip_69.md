---
name: unknown_workflow_video_sampler_clip_69
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.52225
common_nodes: [CLIPLoader, CLIPTextEncode, Int, JoinStrings, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PainterI2V, PathchSageAttentionKJ, Qwen3_VQA, TextInput_, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1991521193536733186.json, 视频生成/图生视频/1992310906843623426.json, 视频生成/图生视频/2013170330788958209.json, 视频生成/图生视频/2008877214103769089.json, 视频生成/图生视频/2009248487199744001.json, 视频生成/图生视频/2063499906979033090.json, 视频生成/图生视频/2063503636654813185.json, 视频生成/图生视频/2009821052431503362.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_69

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/1991521193536733186.json、视频生成/图生视频/1992310906843623426.json、视频生成/图生视频/2013170330788958209.json、视频生成/图生视频/2008877214103769089.json、视频生成/图生视频/2009248487199744001.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：52%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Int`
- `JoinStrings`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PainterI2V`
- `PathchSageAttentionKJ`
- `Qwen3_VQA`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 7/8 个有
- `INTConstant` —— 6/8 个有
- `RIFE VFI` —— 6/8 个有
- `ShowText|pysssss` —— 5/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `RH_LLMAPI_NODE` —— 3/8 个有
- `DuckHideNode` —— 2/8 个有
- `GetImagesFromBatchIndexed` —— 2/8 个有
- `ImageResizeKJv2` —— 2/8 个有
- `Seed (rgthree)` —— 2/8 个有
- `preview_text` —— 2/8 个有
- `wanBlockSwap` —— 2/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 88% |
| Prompt 约束强度(CFG) | 4 | 4 - 6 | 8 | 81% |
| 采样算法 | 1 | 1 - 1.1 | 8 | 97% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | simple | - | 8 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 88%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 6，8 个样本，取值集中（一致性 81%）
- 采样算法 中位数 1，观测区间 1 - 1.1，8 个样本，取值集中（一致性 97%）
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 simple，8 个样本，一致性 75%
