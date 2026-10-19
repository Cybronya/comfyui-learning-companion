---
name: unknown_workflow_video_sampler_clip_58
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.539222
common_nodes: [CLIPLoader, CLIPTextEncode, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1991521193536733186.json, 视频生成/图生视频/1992310906843623426.json, 视频生成/图生视频/1986747295184138242.json, 视频生成/图生视频/2013170330788958209.json, 视频生成/图生视频/2008877214103769089.json, 视频生成/图生视频/2009248487199744001.json, 视频生成/图生视频/2063499906979033090.json, 视频生成/图生视频/2063503636654813185.json, 视频生成/图生视频/2009821052431503362.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_58

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1991521193536733186.json、视频生成/图生视频/1992310906843623426.json、视频生成/图生视频/1986747295184138242.json、视频生成/图生视频/2013170330788958209.json、视频生成/图生视频/2008877214103769089.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：54%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `JoinStrings` —— 8/9 个有
- `PainterI2V` —— 8/9 个有
- `Qwen3_VQA` —— 8/9 个有
- `TextInput_` —— 8/9 个有
- `easy cleanGpuUsed` —— 8/9 个有
- `easy showAnything` —— 8/9 个有
- `RIFE VFI` —— 7/9 个有
- `INTConstant` —— 6/9 个有
- `PreviewImage` —— 5/9 个有
- `ShowText|pysssss` —— 5/9 个有
- `Fast Groups Bypasser (rgthree)` —— 4/9 个有
- `ImageResizeKJv2` —— 3/9 个有
- `RH_LLMAPI_NODE` —— 3/9 个有
- `wanBlockSwap` —— 3/9 个有
- `DuckHideNode` —— 2/9 个有
- `GetImagesFromBatchIndexed` —— 2/9 个有
- `Seed (rgthree)` —— 2/9 个有
- `preview_text` —— 2/9 个有
- `LoraLoaderModelOnly` —— 1/9 个有
- `WanImageToVideo` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 89% |
| Prompt 约束强度(CFG) | 4 | 4 - 6 | 9 | 80% |
| 采样算法 | 1 | 1 - 1.1 | 9 | 97% |
| 调度器 | euler | - | 9 | 100% |
| 重绘幅度 | simple | - | 9 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 89%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 6，9 个样本
- 采样算法 中位数 1，观测区间 1 - 1.1，9 个样本，取值集中（一致性 97%）
- 调度器 最常用 euler，9 个样本，一致性 100%
- 重绘幅度 最常用 simple，9 个样本，一致性 67%
