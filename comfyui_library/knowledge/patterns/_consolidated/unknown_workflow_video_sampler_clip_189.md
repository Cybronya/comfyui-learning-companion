---
name: unknown_workflow_video_sampler_clip_189
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.559667
common_nodes: [CLIPLoader, CLIPTextEncode, GetNode, JoinStrings, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, Primitive integer [Crystools], Qwen3_VQA, SetNode, ShowText|pysssss, SimpleMath+, TextInput_, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/2009841330003906561.json, 视频生成/图生视频/2008869399997980674.json, 视频生成/图生视频/2009276761355325442.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_189

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2009841330003906561.json、视频生成/图生视频/2008869399997980674.json、视频生成/图生视频/2009276761355325442.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：56%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `JoinStrings`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `Primitive integer [Crystools]`
- `Qwen3_VQA`
- `SetNode`
- `ShowText|pysssss`
- `SimpleMath+`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 2/3 个有
- `CLIPVisionLoader` —— 2/3 个有
- `CR Text` —— 2/3 个有
- `Float` —— 2/3 个有
- `ImpactSwitch` —— 2/3 个有
- `PainterI2V` —— 2/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `CR Text Replace` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `RH_LLMAPI_Pro_Node` —— 1/3 个有
- `RH_Nano_Banana2_Image2Image` —— 1/3 个有
- `SaveImage` —— 1/3 个有
- `WanFirstLastFrameToVideo` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
