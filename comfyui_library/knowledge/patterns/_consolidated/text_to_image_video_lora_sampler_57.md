---
name: text_to_image_video_lora_sampler_57
type: Text To Image
frequency: 12
level: strong
coverage: 0.717333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 I2V图生视频｜Fused ACC八步极速出片_2097147575894888449.json, 视频生成/图生视频/MiniMax H3 Ref2AV bf16 lightx2v八步加速V2工作流_2106095744552886273.json, 视频生成/图生视频/MiniMax H3全参官方指南自动扩展提示词T6工作流_角色一致性图生视频_2106097208906043393.json, 视频生成/图生视频/MiniMax H3全参官方指南自动扩展提示词，角色表演图生视频工作流_2103588976929099778.json, 视频生成/图生视频/MiniMax H3全参连续帧提示词自动优化工作流_图生视频高效创作方案_2106094286554099714.json, 视频生成/图生视频/MiniMaxH3 ref2va加速八步采样-图生视频工作流_2087367770194403330.json, 视频生成/图生视频/MiniMaxH3 ref2va四步加速V4版｜图生视频_2090101812916482049.json, 视频生成/图生视频/ref2va四步加速v4｜MiniMaxH3图生视频极速版_2089456017561186306.json, 视频生成/图生视频/ref2va四步加速v4｜MiniMaxH3图生视频极速版_2091266588484923394.json, 视频生成/图生视频/ref2va四步加速v4｜MiniMaxH3图生视频极速直出_2089807243888914434.json, 视频生成/图生视频/ref2va超级加速版｜MiniMaxH3图生视频1.0分辨率极速出片_2093095662807248897.json, 视频生成/图生视频/ref2va超级加速版｜MiniMaxH3支持1.0分辨率图生视频_2093253169697611778.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_57

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 I2V图生视频｜Fused ACC八步极速出片_2097147575894888449.json、视频生成/图生视频/MiniMax H3 Ref2AV bf16 lightx2v八步加速V2工作流_2106095744552886273.json、视频生成/图生视频/MiniMax H3全参官方指南自动扩展提示词T6工作流_角色一致性图生视频_2106097208906043393.json、视频生成/图生视频/MiniMax H3全参官方指南自动扩展提示词，角色表演图生视频工作流_2103588976929099778.json、视频生成/图生视频/MiniMax H3全参连续帧提示词自动优化工作流_图生视频高效创作方案_2106094286554099714.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 11/12 个有
- `PrimitiveFloat` —— 11/12 个有
- `GetNode` —— 8/12 个有
- `LoadAudio` —— 8/12 个有
- `SetNode` —— 8/12 个有
- `MiniMaxH3ReferenceToVideo` —— 7/12 个有
- `ModelPatchTorchSettings` —— 7/12 个有
- `Text Multiline` —— 7/12 个有
- `ImageScale` —— 6/12 个有
- `KSamplerSelect` —— 6/12 个有
- `MiniMaxH3TurboLoRA` —— 6/12 个有
- `MiniMaxH3TurboSampler` —— 6/12 个有
- `PrimitiveInt` —— 6/12 个有
- `easy compare` —— 6/12 个有
- `Text` —— 5/12 个有
- `RHHiddenNodes` —— 4/12 个有
- `SaveImage` —— 4/12 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 4/12 个有
- `ImageConcatenateMulti_UTK` —— 3/12 个有
- `PreviewImage` —— 3/12 个有
- `Label (rgthree)` —— 2/12 个有
- `EnhancedLoadDiffusionModel` —— 1/12 个有
- `LoraLoaderBypassModelOnly` —— 1/12 个有
- `MiniMaxH3ImageToVideo` —— 1/12 个有
- `easy imageSplitGrid` —— 1/12 个有
- `easy indexAnything` —— 1/12 个有
- `easy showAnything` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
