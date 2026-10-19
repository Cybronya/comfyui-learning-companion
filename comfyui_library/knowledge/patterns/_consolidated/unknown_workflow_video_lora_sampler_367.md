---
name: unknown_workflow_video_lora_sampler_367
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.709333
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, RIFE VFI, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2008144239636520961.json, 视频生成/图生视频/2008202129441296385.json, 视频生成/图生视频/2001276328982740993.json, 视频生成/图生视频/2033880906871611394.json, 视频生成/图生视频/2001269970967330818.json, 视频生成/图生视频/2015119585170690050.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_367

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2008144239636520961.json、视频生成/图生视频/2008202129441296385.json、视频生成/图生视频/2001276328982740993.json、视频生成/图生视频/2033880906871611394.json、视频生成/图生视频/2001269970967330818.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RIFE VFI`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/6 个有
- `Qwen3_VQA` —— 5/6 个有
- `easy showAnything` —— 5/6 个有
- `GetNode` —— 4/6 个有
- `JoinStrings` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `ShowText|pysssss` —— 4/6 个有
- `TextInput_` —— 4/6 个有
- `WanFirstLastFrameToVideo` —— 3/6 个有
- `CM_IntToFloat` —— 2/6 个有
- `ImageConcatMulti` —— 2/6 个有
- `PainterI2V` —— 2/6 个有
- `WanImageToVideo` —— 2/6 个有
- `CRTFirstLastFrameSelector` —— 1/6 个有
- `DuckHideNode` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `ImageLoader` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `MultiplyNode` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `ShellAgentPluginOutputText` —— 1/6 个有
- `easy float` —— 1/6 个有
- `easy int` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 67% |
| Prompt 约束强度(CFG) | 4 | 4 - 20 | 6 | 16% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler | - | 6 | 100% |
| 重绘幅度 | normal | - | 6 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 20，6 个样本，取值分散，一致性仅 16%
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，6 个样本，一致性 100%
- 重绘幅度 最常用 normal，6 个样本，一致性 83%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
