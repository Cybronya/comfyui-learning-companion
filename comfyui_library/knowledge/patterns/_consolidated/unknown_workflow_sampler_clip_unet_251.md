---
name: unknown_workflow_sampler_clip_unet_251
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9874
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, SaveLatent, SimpleMath+, TT_img_enc, TextInput_, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/三图自用输出latent_2035338730898198529.json, 视频生成/图生视频/三图自用输出latent_2016685027785969665.json, 视频生成/图生视频/三图自用输出latent_2035339153382055937.json, 视频生成/图生视频/自用单图latent1_2018705139464413185.json, 视频生成/图生视频/自用单图latent1_2018711525216751618.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_251

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/三图自用输出latent_2035338730898198529.json、视频生成/图生视频/三图自用输出latent_2016685027785969665.json、视频生成/图生视频/三图自用输出latent_2035339153382055937.json、视频生成/图生视频/自用单图latent1_2018705139464413185.json、视频生成/图生视频/自用单图latent1_2018711525216751618.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 5 个 workflow 都包含：
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
- `GetImage` —— 3/5 个有
- `ImageBatchMultiple+` —— 3/5 个有
- `ImageResizeKJv2` —— 3/5 个有
- `SaveImage` —— 3/5 个有
- `WanMultiFrameRefToVideo` —— 3/5 个有
- `ModelSamplingSD3` —— 2/5 个有
- `PainterI2V` —— 2/5 个有
- `RIFE VFI` —— 2/5 个有
- `VHS_VideoCombine` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `GetImageSize_` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 100% |
| Prompt 约束强度(CFG) | 6 | 4 - 6 | 5 | 81% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 6，5 个样本，取值集中（一致性 81%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
