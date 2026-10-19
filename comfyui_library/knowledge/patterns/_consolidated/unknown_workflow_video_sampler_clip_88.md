---
name: unknown_workflow_video_sampler_clip_88
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.537833
common_nodes: [CLIPLoader, CLIPTextEncode, FloatConstant, GetNode, INTConstant, ImageFromBatch+, JjkShowText, KSamplerAdvanced, ModelSamplingSD3, PathchSageAttentionKJ, Primitive string multiline [Crystools], SetNode, SimpleCondition+, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy clearCacheAll, easy seed]
problems: []
missing: [ImageFromBatch+, Primitive string multiline [Crystools], SimpleCondition+, SimpleMath+, easy cleanGpuUsed, easy clearCacheAll, easy seed]
members: [图片生成/文生图/1980468292714455042.json, 视频生成/图生视频/1981975406876213250.json, 视频生成/图生视频/1981981430689472513.json, 视频生成/图生视频/1980163388754006018.json, 视频生成/图生视频/1981942632731557889.json, 视频生成/文生视频/Wan2.2 Smooth Mix文生视频_1980468292714455042.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_88

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1980468292714455042.json、视频生成/图生视频/1981975406876213250.json、视频生成/图生视频/1981981430689472513.json、视频生成/图生视频/1980163388754006018.json、视频生成/图生视频/1981942632731557889.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：54%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `FloatConstant`
- `GetNode`
- `INTConstant`
- `ImageFromBatch+`
- `JjkShowText`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `Primitive string multiline [Crystools]`
- `SetNode`
- `SimpleCondition+`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 5/6 个有
- `GIMMVFI_interpolate` —— 5/6 个有
- `CLIPVisionEncode` —— 4/6 个有
- `CLIPVisionLoader` —— 4/6 个有
- `ImageResizeKJv2` —— 4/6 个有
- `Int` —— 4/6 个有
- `LoadImage` —— 4/6 个有
- `RH_LLMAPI_NODE` —— 4/6 个有
- `WanImageToVideo` —— 4/6 个有
- `AILab_MiniCPM_4_V_Advanced` —— 2/6 个有
- `ImageBatchMultiple+` —— 2/6 个有
- `ModelPatchTorchSettings` —— 2/6 个有
- `Power Lora Loader (rgthree)` —— 2/6 个有
- `WanFirstLastFrameToVideo` —— 2/6 个有
- `wanBlockSwap` —— 2/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有
- `easy int` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 6 | 100% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler_ancestral | - | 6 | 100% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，6 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，6 个样本，一致性 100%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
- 这些节点还没有知识卡，系统对它们的理解有限：ImageFromBatch+、Primitive string multiline [Crystools]、SimpleCondition+、SimpleMath+、easy cleanGpuUsed
