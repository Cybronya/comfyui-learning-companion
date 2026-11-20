---
name: unknown_workflow_controlnet_video_upscale_2
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.921857
common_nodes: [ADE_AnimateDiffLoaderWithContext, ADE_AnimateDiffUniformContextOptions, CLIPSetLastLayer, CLIPTextEncode, CR VAE Input Switch, CheckpointLoaderSimpleWithNoiseSelect, ControlNetApplyAdvanced, ControlNetLoaderAdvanced, DWPreprocessor, FreeU, ImageResize+, ImageUpscaleWithModel, KSamplerAdvanced, ModelSamplingDiscrete, PreviewImage, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/真人视频转动漫_1809295841103900674.json, 平台全量/真人视频转动漫_1818483064082202626.json, 平台全量/真人视频转动漫_1821024195198234626.json, 平台全量/真人视频转动漫_1821410414272884738.json, 平台全量/真人视频转动漫_1989167162130575362.json, 平台全量/真人视频转动漫_1994786196167569410.json, 平台全量/真人视频风格转动漫风格_1899137614862270465.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_upscale_2

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/真人视频转动漫_1809295841103900674.json、平台全量/真人视频转动漫_1818483064082202626.json、平台全量/真人视频转动漫_1821024195198234626.json、平台全量/真人视频转动漫_1821410414272884738.json、平台全量/真人视频转动漫_1989167162130575362.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `ADE_AnimateDiffLoaderWithContext`
- `ADE_AnimateDiffUniformContextOptions`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CR VAE Input Switch`
- `CheckpointLoaderSimpleWithNoiseSelect`
- `ControlNetApplyAdvanced`
- `ControlNetLoaderAdvanced`
- `DWPreprocessor`
- `FreeU`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `KSamplerAdvanced`
- `ModelSamplingDiscrete`
- `PreviewImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 6/7 个有
- `ImageScale` —— 4/7 个有
- `RHHiddenNodes` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |
| 采样步数 | fixed | - | 7 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 7 | 100% |
| 采样算法 | 2 | 1 - 2 | 7 | 81% |
| 调度器 | lcm | - | 7 | 100% |
| 重绘幅度 | normal | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样步数 最常用 fixed，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 2，观测区间 1 - 2，7 个样本，取值集中（一致性 81%）
- 调度器 最常用 lcm，7 个样本，一致性 100%
- 重绘幅度 最常用 normal，7 个样本，一致性 100%
