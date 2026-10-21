---
name: unknown_workflow_video_lora_sampler_263
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.83625
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Apply LoRA Stack, CR Seed, CR Text, CheckpointLoaderSimple, ComfySwitchNode, ConditioningZeroOut, Convert Masks to Images, DiffusionModelLoaderKJ, INTConstant, Image Batch, ImageCompositeMasked, ImageScale, InvertMask, KSampler, LoadImage, ModelSamplingSD3, PrimitiveBoolean, SAM3_TrackPreview, SAM3_TrackToMask, SAM3_VideoTrack, SCAIL2ColoredMask, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanContextWindowsManual, WanSCAILToVideo, easy loraStack]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/SCAIL-2动作迁移&角色替换支持多参工作流_2086023874776489986.json, 视频生成/图生视频/SCAIL-2动作迁移&角色替换支持多参工作流_2111375323014189057.json, 视频生成/图生视频/SCAIL-2动作迁移&角色替换支持多参工作流_2111428969907179521.json, 视频生成/图生视频/SCAIL-2动作迁移&角色替换支持多参工作流小珠光同款_2104108308775915521.json, 视频生成/图生视频/2077936004870266882.json, 视频生成/图生视频/Scail2-长视频动作迁移_2093937361074872322.json, 视频生成/图生视频/Scail2-长视频角色替换_2093940597882179585.json, 视频生成/图生视频/🔪🔪终极效率版！SCAIL-2动作迁移&角色替换拆解工作流03集_2089247269597048834.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_263

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/SCAIL-2动作迁移&角色替换支持多参工作流_2086023874776489986.json、视频生成/图生视频/SCAIL-2动作迁移&角色替换支持多参工作流_2111375323014189057.json、视频生成/图生视频/SCAIL-2动作迁移&角色替换支持多参工作流_2111428969907179521.json、视频生成/图生视频/SCAIL-2动作迁移&角色替换支持多参工作流小珠光同款_2104108308775915521.json、视频生成/图生视频/2077936004870266882.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Apply LoRA Stack`
- `CR Seed`
- `CR Text`
- `CheckpointLoaderSimple`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `Convert Masks to Images`
- `DiffusionModelLoaderKJ`
- `INTConstant`
- `Image Batch`
- `ImageCompositeMasked`
- `ImageScale`
- `InvertMask`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `PrimitiveBoolean`
- `SAM3_TrackPreview`
- `SAM3_TrackToMask`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanContextWindowsManual`
- `WanSCAILToVideo`
- `easy loraStack`

**可变部分**（部分 workflow 才有）：
- `FastGroupsBypassSwitch` —— 7/8 个有
- `GetNode` —— 7/8 个有
- `SetNode` —— 7/8 个有
- `Text` —— 2/8 个有
- `Any Switch (rgthree)` —— 1/8 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/8 个有
- `Fast Groups Muter (rgthree)` —— 1/8 个有
- `Fast Muter (rgthree)` —— 1/8 个有
- `GIMMVFI_interpolate` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `LazySwitch2way` —— 1/8 个有
- `Seed (rgthree)` —— 1/8 个有
- `easy convertAnything` —— 1/8 个有
- `孤海注释` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 8 | 8 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | dpmpp_2m_sde_gpu | - | 8 | 88% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 8，8 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde_gpu，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
