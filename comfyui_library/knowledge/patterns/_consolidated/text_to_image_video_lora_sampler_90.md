---
name: text_to_image_video_lora_sampler_90
type: Text To Image
frequency: 8
level: strong
coverage: 0.492375
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, DiffusionModelLoaderKJ, EmptyLatentImage, Fast Groups Bypasser (rgthree), ImageConcatMulti, ImageResizeKJv2, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, PrimitiveInt, SAM3_VideoTrack, SCAIL2ColoredMask, SingleBooleanTrigger, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo, easy imageRemBg, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/一键复刻爆款视频图生视频处理生成工作流工具_2101396084621926402.json, 数字人/数字人/一键复刻爆款视频｜数字人视频生视频 动作迁移照搬_2097579730450075650.json, 视频生成/图生视频/Scail2动作迁移For循环一键模仿图生视频处理工具_2101394038732709889.json, 视频生成/图生视频/Scail2多参动作迁移 官方节点无劣化工作流_2098311637685067777.json, 视频生成/图生视频/Scail2多参工作流｜图生视频角色动作驱动_2090932731508256770.json, 视频生成/图生视频/Scail2多参无劣化动作迁移 默认DPO Lora关闭按需开启_2098657872681979905.json, 视频生成/图生视频/多参动作迁移 Scail2 人物特效视频运镜图生视频_2094184722862796802.json, 视频生成/图生视频/运镜多参两不误｜Scail2人物特效视频生成_2096594560544759809.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_90

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/一键复刻爆款视频图生视频处理生成工作流工具_2101396084621926402.json、数字人/数字人/一键复刻爆款视频｜数字人视频生视频 动作迁移照搬_2097579730450075650.json、视频生成/图生视频/Scail2动作迁移For循环一键模仿图生视频处理工具_2101394038732709889.json、视频生成/图生视频/Scail2多参动作迁移 官方节点无劣化工作流_2098311637685067777.json、视频生成/图生视频/Scail2多参工作流｜图生视频角色动作驱动_2090932731508256770.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：49%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DiffusionModelLoaderKJ`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `PrimitiveInt`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SingleBooleanTrigger`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`
- `easy imageRemBg`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 7/8 个有
- `KSamplerSelect` —— 7/8 个有
- `SamplerCustom` —— 7/8 个有
- `ComfyMathExpression` —— 6/8 个有
- `Float` —— 6/8 个有
- `GetImageRangeFromBatch` —— 6/8 个有
- `easy batchAnything` —— 6/8 个有
- `easy forLoopEnd` —— 6/8 个有
- `easy forLoopStart` —— 6/8 个有
- `ComfySwitchNode` —— 5/8 个有
- `ImageBatchMultiple+` —— 5/8 个有
- `ImageFromBatch` —— 5/8 个有
- `SaveImage` —— 4/8 个有
- `Int` —— 2/8 个有
- `WanContextWindowsManual` —— 2/8 个有
- `Label (rgthree)` —— 1/8 个有
- `VAEDecodeTiled` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
