---
name: unknown_workflow_sampler_clip_unet_172
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.98425
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, SaveLatent, SimpleMath+, TT_img_enc, TextInput_, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2016685027785969665.json, 视频生成/图生视频/2035339153382055937.json, 视频生成/图生视频/2018705139464413185.json, 视频生成/图生视频/2018711525216751618.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_172

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2016685027785969665.json、视频生成/图生视频/2035339153382055937.json、视频生成/图生视频/2018705139464413185.json、视频生成/图生视频/2018711525216751618.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `SaveLatent`
- `SimpleMath+`
- `TT_img_enc`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImage` —— 2/4 个有
- `ImageBatchMultiple+` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `ModelSamplingSD3` —— 2/4 个有
- `PainterI2V` —— 2/4 个有
- `RIFE VFI` —— 2/4 个有
- `SaveImage` —— 2/4 个有
- `VHS_VideoCombine` —— 2/4 个有
- `WanMultiFrameRefToVideo` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `GetImageSize_` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 5 | 4 - 6 | 4 | 80% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 5，观测区间 4 - 6，4 个样本，取值集中（一致性 80%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
