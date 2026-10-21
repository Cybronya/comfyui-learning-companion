---
name: text_to_image_video_lora_sampler_29
type: Text To Image
frequency: 16
level: strong
coverage: 0.726812
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax-H3数字人带货图生视频_2108450739797446658.json, 视频生成/图生视频/MiniMax-H3数字人带货视频｜模特产品展示图生视频_2108417540744638465.json, 视频生成/图生视频/MiniMax-H3数字人视频带货｜Digital Avatars模特产品展示_2108393078053756930.json, 视频生成/图生视频/MiniMax-H3数字人视频带货｜Digital Avatars电商好帮手_2111119123915821058.json, 视频生成/图生视频/MiniMaxH3 ref2va加速八步采样-图生视频工作流_2087367770194403330.json, 视频生成/图生视频/MiniMaxH3 ref2va四步加速V4版｜图生视频_2090101812916482049.json, 视频生成/图生视频/MiniMax_H3多参考7P3A2V生视频优化版｜图生视频_2100805403243278338.json, 视频生成/图生视频/MiniMax_H3多参考生视频优化版，文生视频视频生视频图生视频方案_2109447215457587202.json, 视频生成/图生视频/MiniMax_H3多参角色替换LoRA二采放大工作流，文生视频视频生视频图生视频_2109816691227185154.json, 视频生成/图生视频/MiniMax_H3多参角色替换LoRA二采放大，三种生视频模式_2110541129706987521.json, 视频生成/图生视频/MiniMax_H3多参角色替换LoRA二采放大，三种生视频模式_2110888174443655170.json, 视频生成/图生视频/ref2va四步加速v4｜MiniMaxH3图生视频极速版_2089456017561186306.json, 视频生成/图生视频/ref2va四步加速v4｜MiniMaxH3图生视频极速版_2091266588484923394.json, 视频生成/图生视频/ref2va四步加速v4｜MiniMaxH3图生视频极速直出_2089807243888914434.json, 视频生成/图生视频/ref2va超级加速版｜MiniMaxH3图生视频1.0分辨率极速出片_2093095662807248897.json, 视频生成/图生视频/ref2va超级加速版｜MiniMaxH3支持1.0分辨率图生视频_2093253169697611778.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_29

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3数字人带货图生视频_2108450739797446658.json、视频生成/图生视频/MiniMax-H3数字人带货视频｜模特产品展示图生视频_2108417540744638465.json、视频生成/图生视频/MiniMax-H3数字人视频带货｜Digital Avatars模特产品展示_2108393078053756930.json、视频生成/图生视频/MiniMax-H3数字人视频带货｜Digital Avatars电商好帮手_2111119123915821058.json、视频生成/图生视频/MiniMaxH3 ref2va加速八步采样-图生视频工作流_2087367770194403330.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 13/16 个有
- `SetNode` —— 13/16 个有
- `孤海注释` —— 12/16 个有
- `KSamplerSelect` —— 10/16 个有
- `LTXVConcatAVLatent` —— 9/16 个有
- `LTXVSeparateAVLatent` —— 9/16 个有
- `LoadAudio` —— 9/16 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/16 个有
- `MinimaxH3LatentUpscaler3D` —— 9/16 个有
- `ManualSigmas` —— 7/16 个有
- `ModelPatchTorchSettings` —— 7/16 个有
- `Text Multiline` —— 7/16 个有
- `ImageScale` —— 6/16 个有
- `MiniMaxH3TurboLoRA` —— 6/16 个有
- `MiniMaxH3TurboSampler` —— 6/16 个有
- `PrimitiveInt` —— 6/16 个有
- `easy compare` —— 6/16 个有
- `EmptyImage` —— 5/16 个有
- `PreviewImage` —— 5/16 个有
- `SplitSigmas` —— 5/16 个有
- `Text` —— 5/16 个有
- `VHS_LoadVideo` —— 5/16 个有
- `SaveImage` —— 4/16 个有
- `CreateVideo` —— 3/16 个有
- `ImageResizeKJv2` —— 3/16 个有
- `MiniMaxH3SigmaShift` —— 3/16 个有
- `ModelAttentionBackend` —— 3/16 个有
- `ModelPreviewOverrideKJ` —— 3/16 个有
- `SaveVideo` —— 3/16 个有
- `Label (rgthree)` —— 2/16 个有
- `easy float` —— 2/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（18/16 个样本）：Steps较低可能导致细节不足
