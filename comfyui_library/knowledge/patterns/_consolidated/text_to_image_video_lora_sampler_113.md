---
name: text_to_image_video_lora_sampler_113
type: Text To Image
frequency: 6
level: strong
coverage: 0.662667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3 Mask替换人物 视频人物替换进阶工具_2099906937986048002.json, 视频生成/图生视频/H3+Viggle动作迁移强化版｜免提示词 数字人动作跟随超自然_2105512132791066626.json, 视频生成/图生视频/H3加Viggle免提示词动作迁移 人物视频动态强化版_2110357557851287554.json, 视频生成/图生视频/H3加Viggle免提示词动作迁移强化版，数字人视频生视频图生视频工具_2105724742098571266.json, 视频生成/图生视频/H3加Viggle免提示词动作迁移画质强化版，视频生视频图生视频工具_2105771049332858882.json, 视频生成/图生视频/minimax-H3加Viggle动作迁移强化版，免提示词直接出片_2110451947428995074.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_113

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/H3 Mask替换人物 视频人物替换进阶工具_2099906937986048002.json、视频生成/图生视频/H3+Viggle动作迁移强化版｜免提示词 数字人动作跟随超自然_2105512132791066626.json、视频生成/图生视频/H3加Viggle免提示词动作迁移 人物视频动态强化版_2110357557851287554.json、视频生成/图生视频/H3加Viggle免提示词动作迁移强化版，数字人视频生视频图生视频工具_2105724742098571266.json、视频生成/图生视频/H3加Viggle免提示词动作迁移画质强化版，视频生视频图生视频工具_2105771049332858882.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `JWImageResizeToMegapixels` —— 5/6 个有
- `SaveImage` —— 5/6 个有
- `ViggleAnimateConditioning` —— 5/6 个有
- `ViggleTextCondLoader` —— 5/6 个有
- `CR Value` —— 3/6 个有
- `PrimitiveFloat` —— 3/6 个有
- `CheckpointLoaderSimple` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `ImageAndMaskPreview` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/6 个有
- `MiniMaxH3ReferenceToVideo` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `ResolutionSelector` —— 1/6 个有
- `SAM3_TrackPreview` —— 1/6 个有
- `SAM3_TrackToMask` —— 1/6 个有
- `SAM3_VideoTrack` —— 1/6 个有
- `VAEDecodeAudio` —— 1/6 个有
- `取色器_孤海` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
