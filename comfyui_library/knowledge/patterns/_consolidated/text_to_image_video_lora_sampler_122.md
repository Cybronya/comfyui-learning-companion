---
name: text_to_image_video_lora_sampler_122
type: Text To Image
frequency: 5
level: strong
coverage: 0.755
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MiniMax H3快速动作一镜到底多图参考，文生图图生视频高效创作工具_2103959005801574402.json, 数字人/数字人/人物场景替换工作流｜数字人一键换背景搬家不穿帮_2097578172031258626.json, 视频生成/图生视频/H3 Mask替换人物 视频人物替换进阶工具_2099906937986048002.json, 视频生成/文生视频/Minimax-H3VDN-R2V三模式生成｜RH在线流直跑_2097156284557643777.json, 视频生成/文生视频/Minimax-H3VDN-R2V视频生成｜RH在线流工作流制作_2097073901951086594.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_122

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/MiniMax H3快速动作一镜到底多图参考，文生图图生视频高效创作工具_2103959005801574402.json、数字人/数字人/人物场景替换工作流｜数字人一键换背景搬家不穿帮_2097578172031258626.json、视频生成/图生视频/H3 Mask替换人物 视频人物替换进阶工具_2099906937986048002.json、视频生成/文生视频/Minimax-H3VDN-R2V三模式生成｜RH在线流直跑_2097156284557643777.json、视频生成/文生视频/Minimax-H3VDN-R2V视频生成｜RH在线流工作流制作_2097073901951086594.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 5 个 workflow 都包含：
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
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 4/5 个有
- `MiniMaxH3SigmaShift` —— 4/5 个有
- `ModelAttentionBackend` —— 4/5 个有
- `PathchSageAttentionKJ` —— 4/5 个有
- `MiniMaxChunkFeedForward` —— 3/5 个有
- `MiniMaxH3VDNRuntimeAuditT8Advanced` —— 3/5 个有
- `MiniMaxLowVRAMAttention` —— 3/5 个有
- `ModelPatchTorchSettings` —— 3/5 个有
- `SaveImage` —— 3/5 个有
- `SolAttnPatch` —— 3/5 个有
- `StringConcatenate` —— 3/5 个有
- `VHS_LoadVideo` —— 2/5 个有
- `CheckpointLoaderSimple` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ImageAndMaskPreview` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `LoadAudio` —— 1/5 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/5 个有
- `ModelPreviewOverrideKJ` —— 1/5 个有
- `SAM3_TrackPreview` —— 1/5 个有
- `SAM3_TrackToMask` —— 1/5 个有
- `SAM3_VideoTrack` —— 1/5 个有
- `取色器_孤海` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
