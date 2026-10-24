---
name: text_to_image_lora_sampler_clip_157
type: Text To Image
frequency: 10
level: strong
coverage: 0.8792
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MiniMax H3 V4 加速版｜8步便宜高分辨率 Lightx2v 新版_2096848305606184962.json, 图片生成/图生图/V4加速8步Lightx2v新版｜MiniMax H3便宜高分辨率图生图_2096688541081366530.json, 视频生成/图生视频/8步增速最新版｜Minimax H3 图生视频_2089273029355466753.json, 视频生成/图生视频/MiniMax H3图生视频官方版｜高质量视频生成_2095962744792113153.json, 视频生成/图生视频/MiniMax H3图生视频工作流，图生视频高质量视频生成方案_2107902631598444546.json, 视频生成/图生视频/MiniMax H3图生视频｜官方加速版工作流生成_2096335585295290369.json, 视频生成/图生视频/MiniMax H3开源版首尾帧8步加速工作流，数字人图生视频处理工具_2106532091839205378.json, 视频生成/图生视频/MiniMax H3开源版首尾帧8步加速工作流，数字人图生视频处理工具_2106879845912371201.json, 视频生成/图生视频/MiniMax H3首尾帧生视频｜官方加速版工作流制作_2096332861723996162.json, 视频生成/文生视频/多合一加速修复｜MiniMax H3热门IP模糊视频高清处理_2090232166843240449.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_157

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/MiniMax H3 V4 加速版｜8步便宜高分辨率 Lightx2v 新版_2096848305606184962.json、图片生成/图生图/V4加速8步Lightx2v新版｜MiniMax H3便宜高分辨率图生图_2096688541081366530.json、视频生成/图生视频/8步增速最新版｜Minimax H3 图生视频_2089273029355466753.json、视频生成/图生视频/MiniMax H3图生视频官方版｜高质量视频生成_2095962744792113153.json、视频生成/图生视频/MiniMax H3图生视频工作流，图生视频高质量视频生成方案_2107902631598444546.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/10 个有
- `BasicScheduler` —— 7/10 个有
- `CreateVideo` —— 7/10 个有
- `KSamplerSelect` —— 7/10 个有
- `SaveVideo` —— 7/10 个有
- `GetImageSize` —— 5/10 个有
- `ImageScaleToTotalPixels` —— 5/10 个有
- `Seed (rgthree)` —— 5/10 个有
- `ComfySwitchNode` —— 4/10 个有
- `Fast Groups Bypasser (rgthree)` —— 4/10 个有
- `MiniMaxH3DualClockSamplerT8` —— 4/10 个有
- `PrimitiveBoolean` —— 4/10 个有
- `Any Switch (rgthree)` —— 3/10 个有
- `ImpactConditionalBranch` —— 3/10 个有
- `SaveImage` —— 3/10 个有
- `VHS_VideoCombine` —— 3/10 个有
- `Fast Bypasser (rgthree)` —— 2/10 个有
- `ImageResizeKJv2` —— 2/10 个有
- `PrimitiveInt` —— 2/10 个有
- `easy cleanGpuUsed` —— 2/10 个有
- `LoraLoaderBypassModelOnly` —— 1/10 个有
- `QwenTE_ImageInfer` —— 1/10 个有
- `QwenTE_ModelLoader` —— 1/10 个有
- `TE_H3_Prompt_Enhancer` —— 1/10 个有
- `TE_prompt_text` —— 1/10 个有
- `TE_text_display` —— 1/10 个有
- `easy boolean` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（11/10 个样本）：Steps较低可能导致细节不足
